import click

import sys
import os
import pathlib
import glob
import json

import jarvis.constats as constats


def find_config_file(execution_location):
    end_of_search = pathlib.PurePosixPath(os.path.expanduser('~'))
    while execution_location != end_of_search:

        for file_name in os.listdir(execution_location):
            if file_name == '.jarvis':
                return execution_location / file_name

        execution_location = execution_location.parent

    return None


def open_config(path):
    with open(path, 'r') as conf:
        config_value = conf.read()

    return config_value


def open_and_find_config(execution_location):
    path = find_config_file(execution_location)

    config = open_config(path)

    os.environ[constats.SAVED_PATH] = str(path)
    return (config, str(path.parent))


def get_saved_path():
    raw_saved_path = os.environ.get(constats.SAVED_PATH)

    if raw_saved_path:
        return pathlib.PurePosixPath(os.environ.get(constats.SAVED_PATH))

    return None


def get_config():
    saved_path = get_saved_path()
    execution_location = pathlib.PurePosixPath(os.getcwd())

    if saved_path and str(saved_path.parent) in str(execution_location):
        try:
            return (open_config(saved_path), str(saved_path.parent))
        except Exception:
            return open_and_find_config(execution_location)
    else:
        return open_and_find_config(execution_location)


def get_project_info():
    config, root_path = get_config()
    return (json.loads(config), root_path)
