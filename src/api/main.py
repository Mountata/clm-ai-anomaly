from fastapi import FastAPI

print("🔍 1. Début de l'import du routeur...")
from src.api.routes import contracts
print("🔍 2. Import réussi !")

print("🔍 3. Contenu de contracts :", contracts)
print("🔍 4. Contenu de contracts.router :", contracts.router)
print("🔍 5. Routes dans le router :", contracts.router.routes)

app = FastAPI(
    title="AI-Enhanced CLM Platform",
    description="platforme de gestion de contrats augmentée pour l'IA",
    version="0.1.0"
)

print("🔍 6. Inclusion du routeur dans l'application...")
app.include_router(contracts.router)
print("🔍 7. Routeur inclus !")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API CLM opérationnelle"}

print("🔍 8. Application prête !")