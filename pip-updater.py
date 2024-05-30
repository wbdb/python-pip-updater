import subprocess
import json

def upgrade_pip():
    # Display the current version of pip
    result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
    if result.returncode == 0:
        current_version = result.stdout.strip().split()[1]
        print(f"Current pip version: {current_version}")
    else:
        print(f"Error retrieving current pip version:\n{result.stderr}")
        return

    # Execute 'pip install --upgrade pip' to upgrade pip
    upgrade_result = subprocess.run(['pip', 'install', '--upgrade', 'pip'], capture_output=True, text=True)
    if upgrade_result.returncode != 0:
        print(f"Error upgrading pip:\n{upgrade_result.stderr}")
        return

    # Display the new version of pip
    new_result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
    if new_result.returncode == 0:
        new_version = new_result.stdout.strip().split()[1]
        print(f"New pip version: {new_version}")
        if current_version != new_version:
            print(f"pip successfully upgraded from version {current_version} to {new_version}")
        else:
            print("pip is already up-to-date.")
    else:
        print(f"Error retrieving new pip version:\n{new_result.stderr}")

def get_outdated_packages():
    # Execute 'pip list --outdated --format=json'
    result = subprocess.run(['pip', 'list', '--outdated', '--format=json'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error retrieving outdated packages")
        return []
    
    # Convert the JSON output to a Python object
    outdated_packages = json.loads(result.stdout)
    return outdated_packages

def update_package(package_name):
    # Execute 'pip install --upgrade <package_name>'
    result = subprocess.run(['pip', 'install', '--upgrade', package_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully updated: {package_name}")
    else:
        print(f"Error updating {package_name}:\n{result.stderr}")

def main():
    # Upgrade pip
    upgrade_pip()

    # Get the list of outdated packages
    outdated_packages = get_outdated_packages()
    
    if not outdated_packages:
        print("All packages are up-to-date.")
    else:
        # Update each outdated package
        for package in outdated_packages:
            update_package(package['name'])
    
    # Wait for user confirmation to exit
    input("Process completed. Press Enter to exit the program.")

if __name__ == "__main__":
    main()
