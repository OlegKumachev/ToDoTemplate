from typing import List

from app.internal.repository.postgresql.tasks import TaskRepository
from app.pkg import models
from app.pkg.models.exceptions.repository import EmptyResult, UniqueViolation
from app.pkg.models.exceptions.task import TasksAlreadyExists, TasksNotFound

__all__ = ["TaskService"]

class TaskService:
    """Service for managing tasks."""

    repository: TaskRepository

    def __init__(self, task_repository: TaskRepository):
        self.repository = task_repository

    async def create_task(self, cmd: models.CreateTaskCommand) -> models.Task:
        try:
            return await self.repository.create(cmd=cmd)
        except UniqueViolation as e:
            raise TasksAlreadyExists from e

    async def read_task(self, query: models.ReadTaskQuery) -> models.Task:
        try:
            return await self.repository.read(query=query)
        except EmptyResult as e:
            raise TasksNotFound from e

    async def read_all_tasks(self) -> List[models.Task]:
        try:
            return await self.repository.read_all()
        except EmptyResult as e:
            raise TasksNotFound from e

    async def update_task(self, task_id: int, cmd: models.UpdateTaskCommand) -> models.Task:
        
        try:

            cmd.id = task_id
            updated_task = await self.repository.update(cmd=cmd)

            return updated_task
        except UniqueViolation as e:
            raise TasksAlreadyExists from e
        except TasksNotFound as e:
            raise e


    async def delete_task(self, cmd: models.DeleteTaskCommand) -> models.Task:
        
        return await self.repository.delete(cmd=cmd)
