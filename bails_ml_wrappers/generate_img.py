#!/usr/bin/env python3
from saas import dall_e
from script_helpers import ToolDirectoryService, configure_logging

configure_logging()

saas_generators = {
    "dall_e": dall_e.generate_image,
}

directory_service = ToolDirectoryService()

prompt = input("Prompt: ")
count = input("Count (per generator if using multiple): ")

for generator_name, generator in saas_generators.items():
    use_generator = input(f"Use {generator_name}? (y/n): ")
    if use_generator == "y":
        generator(prompt, directory_service.working_volume_dir, count)
