# src/application/tasks/celery_app.py
from celery import Celery

celery_app = Celery(
    "clm_worker",
    broker="redis://localhost:6379/0",   # Redis reçoit les tâches
    backend="redis://localhost:6379/0",  # Redis stocke les résultats
    include=["src.application.tasks.contrat_tasks"]  # modules contenant les tâches
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Europe/Paris",
    enable_utc=True,
)