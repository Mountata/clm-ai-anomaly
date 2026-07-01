from fastapi import FastAPI


from src.api.routes import contracts



app = FastAPI(
    title="AI-Enhanced CLM Platform",
    description="platforme de gestion de contrats augmentée pour l'IA",
    version="0.1.0"
)


app.include_router(contracts.router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "API CLM opérationnelle"}

