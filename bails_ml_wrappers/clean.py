#!/usr/bin/env python3
import logging
import subprocess
from script_helpers import configure_logging, ToolDirectoryService

configure_logging()

tool_directory_service = ToolDirectoryService()

confirm = input("Are you sure you want to clean the working directory? (y/n): ")
if confirm == "y":
    logging.info(f"Cleaning {tool_directory_service.working_volume_dir}")
    subprocess.run(f"rm -r {tool_directory_service.working_volume_dir}/*", shell=True)
else:
    logging.info("Aborting clean")
