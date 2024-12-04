import paramiko


def restart_nginx(host, username, password, directory):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print(f"Connecting to {host}...")
        ssh.connect(hostname=host, username=username, password=password)

        if directory:
            print(f"Navigating to {directory}...")
            command = f"cd {directory} && pwd"
            stdin, stdout, stderr = ssh.exec_command(command)

            result = stdout.read().decode().strip()
            print(f"Current directory: {result}")

            if result != directory:
                print("Directory navigation failed.")
                return

        print("Pulling latest changes from Git...")
        git_command = f"cd {directory} && php git pull"
        stdin, stdout, stderr = ssh.exec_command(git_command)

        git_output = stdout.read().decode()
        git_error = stderr.read().decode()

        if git_error:
            print(f"Failed to pull latest changes: {git_error}")
        else:
            print(f"Git pull output: {git_output}")

        print("Restarting Nginx service...")
        stdin, stdout, stderr = ssh.exec_command(
            "sudo systemctl restart nginx")

        nginx_error = stderr.read().decode()

        if nginx_error:
            print(f"Failed to restart Nginx: {nginx_error}")
        else:
            print("Nginx restarted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
        print("SSH connection closed.")
