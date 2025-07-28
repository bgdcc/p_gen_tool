import typer
from .password_generator import get_password

app = typer.Typer()
app.command()(get_password)

if __name__ == "__main__":
    app()