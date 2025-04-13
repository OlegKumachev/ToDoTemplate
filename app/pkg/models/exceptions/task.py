from starlette import status

from app.pkg.models.base import BaseAPIException


__all__ = [
    "TasksNotFound",
    "DuplicateTaskTitle",
    "TasksAlreadyExists",
    "TasksIncomplete",
]


class TasksNotFound(BaseAPIException):
    message = "Task not found."
    status_code = status.HTTP_404_NOT_FOUND


class DuplicateTaskTitle(BaseAPIException):
    message = "Task with this title already exists."
    status_code = status.HTTP_409_CONFLICT


class TasksAlreadyExists(BaseAPIException):
    message = "This task already exists."
    status_code = status.HTTP_409_CONFLICT


class TasksIncomplete(BaseAPIException):
    message = "Task is incomplete or invalid."
    status_code = status.HTTP_400_BAD_REQUEST

__constrains__ = {
    "tasks_title_key": DuplicateTaskTitle,
    "tasks_unique_key": TasksAlreadyExists,
}
