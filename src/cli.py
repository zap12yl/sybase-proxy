import typer
from migrator.orchestrator import MigrationOrchestrator

app = typer.Typer()

@app.command()
def migrate(config: str):
    """Run full database migration"""
    orchestrator = MigrationOrchestrator(config)
    orchestrator.run()

@app.command()
def adduser(username: str, password: str):
    """Add new user to authentication system"""
    auth = AuthHandler()
    auth.add_user(username, password)
    print(f"User {username} created")

if __name__ == "__main__":
    app()
