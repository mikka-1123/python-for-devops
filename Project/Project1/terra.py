import subprocess

def terraform_run(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
    print(process.stdout.decode())
#    return process.stderr.decode()

directory = "/workspaces/python-for-devops/Project/Project1/Terraform"
command = f"terraform -chdir={directory} destroy -auto-approve"
#command = f"terraform -chdir={directory} validate"

terraform_run(command)