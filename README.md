# Oracle and SQL Server Services Manager

## Overview

This Python script controls the Oracle SQL Developer and SQL Server services on a Windows PC. The script allows you to start and stop many services with a single command. This is especially critical when services, like Oracle SQL Developer, are always running and using a large amount of RAM, causing performance issues on lower-end computers. It is important to note that if you have not completely disabled the services from the start-up, not via Task Manager, they will continue to run during boot.

## Purpose

The primary purpose of this script is to:
- **Stop services** that may not be in use, freeing up system resources.
- **Start services** when they are needed again.

This script is especially helpful for those who find that Oracle SQL Developer services are taking up significant RAM even when not in active use.

## Features

- Start or stop all relevant Oracle and SQL Server services with a single command.
- Easy to use, command-line interface.
- Includes a standalone executable for users who may not have Python installed.

## Affected Services

This script will manage the following services:

- **Oracle SQL Developer Services:**
  - OracleJobSchedulerORCL
  - OracleOraDB19Home1MTSRecoveryService
  - OracleOraDB19Home1TNSListener
  - OracleRemExecServiceV2
  - OracleServiceORCL
  - OracleVssWriterORCL

- **SQL Server Services:**
  - SQL Server Agent (MSSQLSERVER)
  - SQL Server Browser
  - SQL Server Agent (MSSQLSERVER01)
  - SQL Server CEIP service (MSSQLSERVER)
  - SQL Server CEIP service (MSSQLSERVER01)
  - SQL Server VSS Writer

## Prerequisites

- **Windows 10**: This script is specifically designed for Windows 10.
- **Administrator Privileges**: The script must be run with administrative privileges to control services.

## How to Run

### Running from Python Script

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Ronan-R-R/service-manager.git
    cd service-manager
    ```

2. **Run the script**:
    ```bash
    python manage_services.py
    ```

3. **Choose an action**:
    - Enter `start` to start all listed services.
    - Enter `stop` to stop all listed services.

### Running the Executable

1. **Locate the executable**:
    After building the executable (or using the pre-built one), locate `manage_services.exe` in the `dist/` directory.

2. **Run the executable as an administrator**:
    - Right-click the `.exe` file and select "Run as administrator".
    - Follow the prompts to start or stop the services.

## Warnings

- **Administrative Rights Required**: You must run the script or executable with administrative privileges. Failure to do so will result in errors when attempting to start or stop services.
- **Service Dependencies**: Be aware that stopping some services may affect dependent applications or services. Ensure that you understand which services you are stopping.
- **System Performance**: Stopping critical services may improve system performance but could also impact functionality. Use this script carefully and make sure to restart necessary services when required.

## License

This project is free to use and modify. However, the author is not liable for any damage or issues that may arise from the use of this script. Use it at your own risk.
