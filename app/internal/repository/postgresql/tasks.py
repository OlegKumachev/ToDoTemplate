from typing import List
from app.internal.repository.postgresql.connection import get_connection
from app.internal.repository.postgresql.handlers.collect_response import collect_response
from app.internal.repository.repository import Repository
from app.pkg import models
from app.pkg.models.exceptions.task import TasksNotFound

__all__ = ["TaskRepository"]

class TaskRepository(Repository):
    """Repository for tasks."""

    @collect_response
    async def create(self, cmd: models.CreateTaskCommand) -> models.Task:
        q = """
            insert into tasks(
                title,
                description,
                due_date
            ) values (
                %(title)s,
                %(description)s,
                %(due_date)s
            )
            returning id, title, description, due_date
        """
        
        data = cmd.dict()
        async with get_connection() as cur:
            await cur.execute(q, data)
            result = await cur.fetchone()
            return result

    @collect_response
    async def read(self, query: models.ReadTaskQuery) -> models.Task:
        q = """
            select
                id, title, description, due_date, is_completed, created_at
            from tasks
            where id = %(id)s
        """
        async with get_connection() as cur:
            await cur.execute(q, query.to_dict())
            return await cur.fetchone()

    @collect_response
    async def read_all(self) -> List[models.Task]:
        q = """
            select
                id, title, description, due_date, is_completed, created_at
            from tasks
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()

    async def update(self, cmd: models.UpdateTaskCommand) -> models.Task:
        q = """
            UPDATE tasks
            SET
                title = %(title)s,
                description = %(description)s,
                due_date = %(due_date)s,
                is_completed = %(is_completed)s
            WHERE id = %(id)s
            RETURNING id, title, description, due_date, is_completed, created_at
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.dict())
            result = await cur.fetchone()
            return result if result else None 

    @collect_response
    async def delete(self, cmd: models.DeleteTaskCommand) -> models.Task:
        q = """
            delete from tasks
            where id = %(id)s
            returning id, title, description, due_date
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()
