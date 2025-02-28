from fastapi import APIRouter, BackgroundTasks
from sse_starlette.sse import EventSourceResponse
from ...migrator.orchestrator import MigrationOrchestrator

router = APIRouter()
migration_tasks = {}

@router.post("/migrations")
async def create_migration(config: dict, bg_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    orchestrator = MigrationOrchestrator(config)
    migration_tasks[task_id] = {"status": "pending", "progress": 0}
    
    bg_tasks.add_task(run_migration_task, task_id, orchestrator)
    return {"task_id": task_id}

@router.get("/migrations/{task_id}/progress")
async def migration_progress(task_id: str):
    async def event_generator():
        while True:
            status = migration_tasks.get(task_id, {})
            yield {
                "event": "progress",
                "data": {
                    "status": status.get("status"),
                    "progress": status.get("progress"),
                    "details": status.get("details")
                }
            }
            if status.get("status") in ["completed", "failed"]:
                break
            await asyncio.sleep(1)
    
    return EventSourceResponse(event_generator())

async def run_migration_task(task_id, orchestrator):
    try:
        migration_tasks[task_id]["status"] = "running"
        await orchestrator.run(lambda p, d: update_progress(task_id, p, d))
        migration_tasks[task_id].update({
            "status": "completed",
            "progress": 100
        })
    except Exception as e:
        migration_tasks[task_id].update({
            "status": "failed",
            "error": str(e)
        })

def update_progress(task_id, progress, details):
    migration_tasks[task_id].update({
        "progress": progress,
        "details": details
    })
