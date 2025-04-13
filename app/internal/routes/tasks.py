from typing import List
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from app.internal.services import Services
from app.internal.services.tasks import TaskService
from app.pkg import models


task_router = APIRouter()


@task_router.get(
    "/",
    response_model=List[models.Task],
    status_code=status.HTTP_200_OK,
    description="Get all tasks",
)

@inject
async def read_all_tasks(
    task_service: TaskService = Depends(Provide[Services.task_service]),
):
    return await task_service.read_all_tasks()


@task_router.get(
    "/{task_id:int}/",
    response_model=models.Task,
    status_code=status.HTTP_200_OK,
    description="Read specific task",
)

@inject
async def read_task(
    task_id: int,
    task_service: TaskService = Depends(Provide[Services.task_service]),
):
    return await task_service.read_task(
        query=models.ReadTaskQuery(id=task_id),
    )
    

@task_router.post(
    "/",
    response_model=models.Task,
    status_code=status.HTTP_201_CREATED,
    description="Create task",
)

@inject
async def create_task(
    cmd: models.CreateTaskCommand,
    task_service: TaskService = Depends(Provide[Services.task_service]),
):
    return await task_service.create_task(cmd=cmd)


@task_router.put(
    "/{task_id:int}/",
    response_model=models.Task,
    status_code=status.HTTP_200_OK,
    description="Update task",
)

@inject
async def update_task(
    task_id: int,
    cmd: models.UpdateTaskCommand,
    task_service: TaskService = Depends(Provide[Services.task_service]),
):
    
    return await task_service.update_task(task_id=task_id, cmd=cmd)


@task_router.delete(
    "/{task_id:int}/",
    response_model=models.Task,
    status_code=status.HTTP_200_OK,
    description="Delete task",
)

@inject
async def delete_task(
    task_id: int,
    task_service: TaskService = Depends(Provide[Services.task_service]),
):
    return await task_service.delete_task(cmd=models.DeleteTaskCommand(id=task_id))
