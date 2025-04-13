"""Service layer."""

from app.internal.services.tasks import TaskService
from dependency_injector import containers, providers

from app.internal.repository import Repositories, postgresql




class Services(containers.DeclarativeContainer):
    """Containers with services."""

    repositories: postgresql.Repositories = providers.Container(
        Repositories.postgres,
    )
    
    task_service = providers.Factory(
        TaskService,
        task_repository = repositories.task_repository,
        
    )

