#!/usr/bin/env python3
import subprocess

from script_helpers import (
    ToolDirectoryService,
    ToolInfoService,
    configure_logging,
)
from txt_to_image import DallEWrapper

configure_logging()

directory_service = ToolDirectoryService()
tool_service = ToolInfoService(
    "generate_img",
    {
        "dall_e": DallEWrapper().get_info(),
    },
)

tool = tool_service.select_tool_prompt()
prompt = input("Prompt: ")

parameters = {}
args_str = ""
is_docker = "generate" not in tool

if "command" in tool:
    args_str += f"{tool['command']} "

if is_docker:
    if "format" in tool["input_prompt_arg"]:
        prompt = tool["input_prompt_arg"]["format"].format(value=prompt)
    args_str += f"{tool['input_prompt_arg']['flag']} {prompt} "

for key, parameter in tool.get("parameters", {}).items():
    parameters[key] = input(
        f"{parameter['description']} ({parameter.get('default')}): "
    )
    if parameters[key] == "":
        if "default" in parameter:
            parameters[key] = parameter["default"]
        else:
            continue
    if "format" in parameter:
        parameters[key] = parameter["format"].format(value=parameters[key])
    if is_docker:
        args_str += f"{parameter['flag']} {parameters[key]} "

if is_docker:
    subprocess.run(
        f"docker-compose run ml {args_str}",
        cwd=f"{directory_service.tools_dir}/{tool['name']}",
        shell=True,
    )
else:
    tool["generate"](
        prompt,
        directory_service.working_volume_dir,
        parameters["count"],
        parameters["size"],
    )
