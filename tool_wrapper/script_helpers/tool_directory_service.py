import os
import logging


class ToolDirectoryService:
    def __init__(self):
        self.base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        )
        self.volumes_dir = os.path.join(self.base_dir, "volumes")
        self.working_volume_dir = os.path.join(self.volumes_dir, "working")
        self.checkpoint_volume_dir = os.path.join(self.volumes_dir, "checkpoints")
        self.tools_dir = os.path.join(self.base_dir, "tools")

    def prepare_directories(self):
        logging.info("Preparing directories")
        os.makedirs(self.working_volume_dir, exist_ok=True)
        os.makedirs(self.checkpoint_volume_dir, exist_ok=True)
        os.makedirs(self.tools_dir, exist_ok=True)

    def add_working_dir(self, dir_name):
        logging.info(f"Adding working directory {dir_name}")
        dir_path = os.path.join(self.working_volume_dir, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
