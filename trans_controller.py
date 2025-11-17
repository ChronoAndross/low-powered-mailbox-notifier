# This script provides functions to enable/disable UART, WiFi, and Bluetooth LE functionality.
# Note that these functions will only work when using sudo.

import subprocess
import os

def run_command(command):
    """Helper function to run shell commands as superuser."""
    try:
        subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully ran: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def block_rf():
    run_command("sudo rfkill block all")

def unblock_rf():
    run_command("sudo rfkill unblock all")
