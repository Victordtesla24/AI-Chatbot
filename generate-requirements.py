
import subprocess
import pkg_resources

def generate_requirements():
    """Generate a requirements.txt file with explicit 
    versions."""
    installed_packages = pkg_resources.working_set
    requirements = []

    for package in installed_packages:
        requirements.append(f"{package.key}=={package.version}")

    with open("requirements.txt", "w") as f:
        f.write("\n".join(sorted(requirements)))

    print("requirements.txt has been generated.")

if __name__ == "__main__":
    generate_requirements()


