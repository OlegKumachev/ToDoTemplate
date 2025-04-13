from app.internal.repository.postgresql.tasks import TaskRepository
from dependency_injector import containers, providers




class Repositories(containers.DeclarativeContainer):
    """Container for postgresql repositories."""
    task_repository = providers.Factory(TaskRepository)
