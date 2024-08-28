import subprocess
import sys

def run_command(command):
    """Run a command and exit if it fails."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

def uninstall_package(package_name):
    """Uninstall a package if it exists."""
    result = subprocess.run(f"pip show {package_name}", shell=True, stdout=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Uninstalling {package_name}...")
        run_command(f"pip uninstall -y {package_name}")
    else:
        print(f"{package_name} is not installed.")

def install_requirements():
    """Install the dependencies from requirements.txt."""
    print("Installing dependencies from requirements.txt...")
    run_command("pip install -r requirements.txt")

def install_package():
    """Install the current package in editable mode."""
    print("Installing the current package in editable mode...")
    run_command("pip install -e .")

if __name__ == "__main__":
    package_name = "codesentry"
    uninstall_package(package_name)
    install_requirements()
    install_package()
    print("Setup completed successfully.")