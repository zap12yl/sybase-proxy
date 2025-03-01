from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordBearer
from ..models import MigrationTask
from migration.src.migrator import DatabaseMigrator

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

tasks = {}

@router.post("/start", response_model=MigrationTask)
async def start_migration(background_tasks: BackgroundTasks):
    migrator = DatabaseMigrator()
    task_id = id(migrator)
    tasks[task_id] = {"status": "running", "progress": 0}
    
    def run_migration():
        try:
            migrator.full_migration()
            tasks[task_id]["status"] = "completed"
        except Exception as e:
            tasks[task_id]["status"] = f"failed: {str(e)}"
    
    background_tasks.add_task(run_migration)
    return {"task_id": task_id, "status": "started"}

@router.get("/status/{task_id}", response_model=MigrationTask)
async def get_status(task_id: int):
    return tasks.get(task_id, {"status": "unknown"})