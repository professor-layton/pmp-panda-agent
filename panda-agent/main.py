from fastapi import APIRouter, Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from utils import BaseParentModel

app = FastAPI(
    title="PMP-Panda",
    description="",
    version="0.1.0",
    root_path_in_servers=False,
    docs_url="/docs",
    openapi_url="/openapi.json",
    dependencies=[Depends()],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/copilot")

class HealthCheckResponse(BaseParentModel):
    message: str

@router.get("/copilot/health", status_code=200)
def health() -> HealthCheckResponse:
    return HealthCheckResponse(message="OK")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
