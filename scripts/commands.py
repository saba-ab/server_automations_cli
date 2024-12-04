import paramiko
from rich.console import Console

console = Console()


def execute_ssh_command(command: str, host: str, username: str, password: str) -> str:
    """Executes a command over SSH and returns output."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        _, stdout, stderr = ssh.exec_command(command)
        return stdout.read().decode().strip(), stderr.read().decode().strip()
    finally:
        ssh.close()


def git_branch(host, username, password, directory):
    command = f"cd {directory} && git branch --show-current"
    console.print("[cyan]Checking current branch ...[/cyan]")
    output, error = execute_ssh_command(command, host, username, password)
    if error:
        console.print(f"[red]Failed to check current branch: {error} [/red]\n")
    else:
        console.print(f"[green]current branch: {output} [/green]\n")


def git_pull(host, username, password, directory):
    command = f"cd {directory} && git pull"
    console.print("[cyan]Pulling latest changes from Git...[/cyan]")
    output, error = execute_ssh_command(command, host, username, password)
    if error:
        console.print(f"[red]Git pull failed: {error}[/red]\n")
    else:
        console.print(f"[green]Git pull successful: {output}[/green]\n")


def php_artisan_migrate(host, username, password, directory):
    command = f"cd {directory} && php artisan migrate --force"
    console.print("[cyan]Running migrations...[/cyan]")
    output, error = execute_ssh_command(command, host, username, password)
    if error:
        console.print(f"[red]Migrations failed: {error}[/red]\n")
    else:
        console.print(f"[green]Migrations successful: {output}[/green]\n")


def php_artisan_migrate_status(host, username, password, directory):
    command = f"cd {directory} && php artisan migrate:status"
    console.print("[cyan]Checking migration status...[/cyan]")
    output, error = execute_ssh_command(command, host, username, password)
    if error:
        console.print(f"[red]Migration status failed: {error}[/red]\n")
    else:
        console.print(f"[green]Migration Status:\n{output}[/green]\n")


def restart_nginx_service(host, username, password):
    command = f"systemctl restart nginx"
    console.print("[cyan]Restarting nginx service ...[/cyan]")
    output, error = execute_ssh_command(command, host, username, password)
    if error:
        console.print(
            f"[red]Restarting nginx service failed: {error} [/red]\n")
    else:
        console.print(
            f"[green]Restarted nginx service successfully {output} [/green]\n")
