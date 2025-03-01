from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from ..models import MigrationTask
from fastapi.responses import JSONResponse
from migration import DatabaseMigrator, DatabaseNotAvailableError, DatabaseConnectionError

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

tasks = {}

@router.post("/start", response_model=MigrationTask)
async def start_migration():
    try:
        migrator = DatabaseMigrator()
        migrator.full_migration()
        task_id = id(migrator)
        tasks[task_id] = {"status": "running", "progress": 0}
        return {"status": "success", "message": "Migration completed"}
        
    except DatabaseNotAvailableError as e:
        return JSONResponse(
            status_code=get_status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "error",
                "message": "Target database unavailable",
                "detail": str(e)
            }
        )
    
    except DatabaseConnectionError as e:
        return JSONResponse(
            status_code=get_status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "Database connection failed",
                "detail": str(e)
            }
        )
    
    except Exception as e:
        return JSONResponse(
            status_code=get_status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "Migration failed",
                "detail": str(e)
            }
        )

    
@router.get("/status/{task_id}", response_model=MigrationTask)
async def get_status(task_id: int):
    return tasks.get(task_id, {"status": "unknown"})