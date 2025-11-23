import click
import platform
import subprocess
import os
import json

@click.group()
def cli():
    """RHEL AI Toolkit - system helper utilities."""
    pass

@cli.command()
def sysinfo():
    """Print system information."""
    print(json.dumps({
        "os" : platform.platform(),
        "python" : platform.python_version(),
        "machine" : platform.machine()
    }, indent=2))

@cli.command()
def check_selinux():
    """Check SELinux enforcement status."""
    try:
        output=subprocess.check_output(["getenforce"], text=True).strip()
        print("SELinux:", output)
    except Exception:
        print("SELinux: Unable to query (Likely macOS or missing getenforce)")

@cli.command()
@click.option("--path", default="/", help="path to check disk usage of.")
def disk(path):
    """Check disk usage for a path."""
    stat = os.statvfs(path)
    total = stat.f_blocks * stat.f_frsize
    free = stat.f_bfree * stat.f_frsize
    print(f"Total: {total/1e9:.2f} GB")
    print(f"Free:  {free/1e9:.2f} B")
            
if __name__ == "__main__":
    cli()