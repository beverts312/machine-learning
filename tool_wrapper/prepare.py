#!/usr/bin/env python3
import logging
import requests
from script_helpers import configure_logging, ToolDirectoryService, ToolInfoService


configure_logging()

tool_directory_service = ToolDirectoryService()
tool_info_service = ToolInfoService()

tool_directory_service.prepare_directories()

tool = tool_info_service.select_tool_prompt()

checkpoints = tool.get("checkpoints", [])
if len(checkpoints) == 0:
    logging.info(f"No checkpoints for {tool['name']}")
    exit(0)

for checkpoint in checkpoints:
    download_checkpoint = input(
        f"Download checkpoint {checkpoint['name']} for {tool['name']}? [y/N] "
    )
    if download_checkpoint.lower() == "y":
        logging.info(f"Downloading checkpoint {checkpoint['name']} for {tool['name']}")
        res = requests.get(checkpoint["url"], stream=True)
        with open(
            f"{tool_directory_service.checkpoint_volume_dir}/{checkpoint['name']}", "wb"
        ) as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
