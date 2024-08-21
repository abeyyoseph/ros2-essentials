import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
current_dir = os.path.dirname(os.path.realpath(__file__))
repo_dir = os.path.realpath(f"{current_dir}/..")

logging.info("Checking if `master` branch is accidentally used in github workflows...")
for filename in glob.glob(f"{repo_dir}/.github/workflows/*.yaml", recursive=True):
    logging.debug(f"Checking: '{filename[len(repo_dir)+1:]}'...")
    with open(filename, "r") as f:
        content = f.read()
        if "master" in content:
            # Ref: https://github.com/j3soon/ros2-essentials/pull/44#pullrequestreview-2251404984
            raise ValueError(f"`master` should not exist since it's obsolete: '{filename}'")
