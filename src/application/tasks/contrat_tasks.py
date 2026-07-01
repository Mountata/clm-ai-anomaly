# src/application/tasks/contrat_tasks.py
import time
from src.application.tasks.celery_app import celery_app


@celery_app.task(bind=True, name="analyser_contrat")
def analyser_contrat_task(self, contrat_reference: str) -> dict:
    """
    Simule une analyse longue d'un contrat (OCR + extraction IA).
    Pour l'instant : juste une attente de 5 secondes.
    
    """
    print(f"[Worker] Début analyse du contrat {contrat_reference}")

    # Simule un traitement long (OCR, appel LLM...)
    for i in range(60):
        time.sleep(1)
        # Met à jour la progression (visible via l'API)
        self.update_state(state="PROGRESS", meta={"progression": f"{(i+1)*20}%"})
        print(f"[Worker] Progression : {(i+1)*20}%")

    print(f"[Worker] Analyse terminée pour {contrat_reference}")
    return {
        "reference": contrat_reference,
        "statut": "analysé",
        "resume": f"Contrat {contrat_reference} analysé avec succès (simulé)",
        "risque": "faible"
    }