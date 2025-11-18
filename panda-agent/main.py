from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from utils import BaseParentModel
from agents.deploy import deploy_router

app = FastAPI(
    title="PMP-Panda",
    description="",
    version="0.1.0",
    root_path_in_servers=False,
    docs_url="/docs",
    openapi_url="/openapi.json",
    dependencies=[],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

top_router = APIRouter(prefix="/copilot")

class HealthCheckResponse(BaseParentModel):
    message: str

@top_router.get("/health", status_code=200)
def health() -> HealthCheckResponse:
    return HealthCheckResponse(message="OK")

app.include_router(top_router)
app.include_router(deploy_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
