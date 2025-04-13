from datetime import date, datetime
from typing import Optional
from pydantic.fields import Field
from pydantic.types import PositiveInt
from app.pkg.models.base import BaseModel


__all__ = [
    "Task",
    "CreateTaskCommand",
    "UpdateTaskCommand",
    "DeleteTaskCommand",
    "ReadTaskQuery",
]


class BaseTask(BaseModel):
    """Base model for tasks."""


class TaskFields:
    id: PositiveInt = Field(description="Internal task id.", example=1)
    title: str = Field(description="Task title.", example="Finish report")
    description: str = Field(description="Task description.", example="Complete the monthly report for review")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Task creation date.")
    due_date: Optional[date] = Field(description="Task due date.")
    is_completed: Optional[bool] = Field(default=False, description="Task status.")

   
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S'),
            date: lambda v: v.strftime('%Y-%m-%d')
        }


class _Task(BaseTask):
    title: str = TaskFields.title
    description: str = TaskFields.description
    created_at: Optional[datetime] = TaskFields.created_at
    due_date: Optional[date] = TaskFields.due_date
    is_completed: Optional[bool] = TaskFields.is_completed

    
    class Config:
        json_encoders = TaskFields.Config.json_encoders


class Task(_Task):
    id: PositiveInt = TaskFields.id


class CreateTaskCommand(_Task):
    title: str
    description: str
    due_date: Optional[date] 


class UpdateTaskCommand(_Task):
    id: PositiveInt = TaskFields.id


class DeleteTaskCommand(BaseTask):
    id: PositiveInt = TaskFields.id


class ReadTaskQuery(BaseTask):
    id: PositiveInt = TaskFields.id
