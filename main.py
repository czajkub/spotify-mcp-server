import subprocess
import sys

from app import project_dir

def main():
    print("Hello from spotify-mcp-server!")

    cmd = [
        # "export",
        # f"PYTHONPATH={project_dir}"
        # "&"
        "uv",
        "run",
        "--directory",
        str(project_dir),
        "fastmcp",
        "run",
        "app/mcp/mcp.py",
    ]

    sys.exit(subprocess.run(cmd))

if __name__ == "__main__":
    main()
