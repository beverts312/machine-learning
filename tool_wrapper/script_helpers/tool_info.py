from glob import glob
import logging
import yaml
from .tool_directory_service import ToolDirectoryService


class ToolInfoService:
    def __init__(self, tool_type=None):
        self.directory_service = ToolDirectoryService()
        self.tools = {}
        self._load_info(tool_type)

    def _load_info(self, tool_type):
        for info_file in glob(f"{self.directory_service.tools_dir}/*/info.yml"):
            logging.debug(f"Loading info from {info_file}")
            with open(info_file) as f:
                info = yaml.safe_load(f)
                if tool_type is None or info["type"] == tool_type:
                    self.tools[info["name"]] = info

    def select_tool_prompt(self):
        print("Select a tool to run:")
        tool_by_index = []
        for i, tool in enumerate(self.tools.keys()):
            print(f"{i}: {tool}")
            tool_by_index.append(tool)
        tool_index = int(input("Tool: "))
        return self.tools[tool_by_index[tool_index]]
