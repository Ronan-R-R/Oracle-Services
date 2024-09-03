import subprocess
import os
import ctypes
import time

# List of services to manage
services = [
    "SQLAgent$MSSQLSERVER01",
    "SQLBrowser",
    "SQLSERVERAGENT",
    "SQLTELEMETRY",
    "SQLTELEMETRY$MSSQLSERVER01",
    "SQLWriter",
    "OracleJobSchedulerORCL",
    "OracleOraDB19Home1MTSRecoveryService",
    "OracleOraDB19Home1TNSListener",
    "OracleRemExecServiceV2",
    "OracleServiceORCL",
    "OracleVssWriterORCL"
]


def is_admin():
    """Check if the script is being run with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def manage_services(action):
    if action not in ["start", "stop"]:
        print(f"Invalid action: {action}. Use 'start' or 'stop'.")
        return

    for service_name in services:
        try:
            print(f"Attempting to {action} {service_name}...")
            subprocess.run(["sc", action, service_name], check=True)
            print(f"Successfully {action}ed {service_name}.")
            time.sleep(0.5)  # Brief pause between commands to ensure proper execution
        except subprocess.CalledProcessError as e:
            print(f"Failed to {action} {service_name}. Error: {e}")
        except Exception as ex:
            print(f"An unexpected error occurred while trying to {action} {service_name}: {ex}")


def main():
    action = input("Enter 'start' to start all services or 'stop' to stop all services: ").lower()
    manage_services(action)


if __name__ == "__main__":
    if is_admin():
        main()
    else:
        print("Please run this script with administrative privileges.")
        # You can also add a prompt to elevate the script to admin rights if necessary.
