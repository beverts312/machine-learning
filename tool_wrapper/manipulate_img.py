#!/usr/bin/env python3
import logging
import shutil
import subprocess
from script_helpers import configure_logging, ToolDirectoryService, ToolInfoService


configure_logging()

tool_directory_service = ToolDirectoryService()
tool_info_service = ToolInfoService("manipulate_img")

tool_directory_service.prepare_directories()

tool = tool_info_service.select_tool_prompt()
tool_args = ""

input_file = input("Input file path: ")
input_dir = tool_directory_service.add_working_dir(tool.get("input_dir", ""))
try:
    shutil.copy(input_file, input_dir)
except shutil.Error:
    logging.warn(f"File already exists in {input_dir}")

if "input_file_arg" in tool:
    if tool["input_file_arg"]["type"] == "positional":
        tool_args += f"{input_file.split('/')[-1]} "

for key, param in tool.get("parameters", {}).items():
    value = input(f"{param['description']} ({param['default']}): ")
    if value == "":
        value = param["default"]
    tool_args += f"{param['flag']} {value} "

subprocess.run(
    f"docker-compose run ml {tool_args}",
    cwd=f"{tool_directory_service.tools_dir}/{tool['name']}",
    shell=True,
)
