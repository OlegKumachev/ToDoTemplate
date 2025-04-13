"""Global point for collected routers. __routes__ is a :class:`.Routes`
instance that contains all routers in your application.

Examples:
    After declaring all routers, you need to register them in your application::

        >>> from fastapi import FastAPI
        >>> app = FastAPI()
        >>> __routes__.register_routes(app=app)
"""

from fastapi import APIRouter
from app.internal.routes.tasks import task_router
from app.pkg.models.core.routes import Routes

from app.pkg.models.exceptions import (
    task,


)

__all__ = [
    "__routes__",
    "task",
]

tasks_router = APIRouter(
    prefix = "/tasks",
    tags = ["Tasks"],
    responses={
        **task.TasksNotFound.generate_openapi(),
    },
    
)
tasks_router.include_router(task_router) 

__routes__ = Routes(
    routers=(
        tasks_router,
    ),
)
