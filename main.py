from config.casino import HOST, USERNAME, PASSWORD, DIRECTORY
import typer
import questionary
from scripts.commands import git_pull, php_artisan_migrate, php_artisan_migrate_status, restart_nginx_service, git_branch

app = typer.Typer()


@app.command()
def git():
    """Run Git Pull."""
    git_pull(HOST, USERNAME, PASSWORD, DIRECTORY)


@app.command()
def migrate():
    """Run PHP Artisan Migrate."""
    php_artisan_migrate(HOST, USERNAME, PASSWORD, DIRECTORY)


@app.command()
def status():
    """Check PHP Artisan Migration Status."""
    php_artisan_migrate_status(HOST, USERNAME, PASSWORD, DIRECTORY)


@app.command()
def interactive():
    """Interactive CLI."""
    while True:
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Git Branch",
                "Git Pull",
                "PHP Artisan Migrate",
                "PHP Artisan Migration Status",
                "Restart nginx service",
                "Exit",
            ]
        ).ask()

        if action == "Git Branch":
            git_branch(HOST, USERNAME, PASSWORD, DIRECTORY)
        elif action == "Git Pull":
            git_pull(HOST, USERNAME, PASSWORD, DIRECTORY)
        elif action == "PHP Artisan Migrate":
            php_artisan_migrate(HOST, USERNAME, PASSWORD, DIRECTORY)
        elif action == "PHP Artisan Migration Status":
            php_artisan_migrate_status(HOST, USERNAME, PASSWORD, DIRECTORY)
        elif action == "Restart nginx service":
            restart_nginx_service(HOST, USERNAME, PASSWORD)
        else:
            typer.Exit()
            break


if __name__ == "__main__":
    app()
