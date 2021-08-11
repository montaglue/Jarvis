import os
import pathlib

import click

from jarvis.project_info import get_project_info
import jarvis.constats as constats
import jarvis.cargo_wrapper as cargo_wrapper
from jarvis.init_proj import raw_init


@click.command()
@click.option('--release', is_flag=True)
@click.option('--dev', is_flag=True)
@click.option('--no_proj', is_flag=True)
@click.argument('command')
def main2(release, dev, no_proj, command):
    if command != constats.INIT_COMMAND and command != constats.NEW_COMMAND:
        (proj_info, root_path) = get_project_info()

    if proj_info['type'] == constats.RUST:
        arguments = {
            'config': proj_info,
            'root path': root_path,
            'release': release,
            'dev': dev
        }
        cargo_wrapper.exec(command, arguments)
    elif proj_info['type'] == constats.TYPESCRIPT:
        pass


@click.group()
def main():
    pass


@main.command()
@click.option('--release', is_flag=True)
def build(release):
    (proj_info, root_path) = get_project_info()

    if proj_info['type'] == constats.RUST:
        if release:
            os.system('cargo build --release')
        else:
            os.system('cargo build --release')
    elif proj_info['type'] == constats.TYPESCRIPT:
        if release:
            os.system('yarn build')
        else:
            os.system('yarn build-dev')


@main.command()
def doc():
    (proj_info, root_path) = get_project_info()

    if proj_info['type'] == constats.RUST:
        os.system('cargo doc')


@main.command()
@click.argument('name')
@click.argument('typ')
def new(name, typ):
    path = os.path.normpath(pathlib.PurePosixPath(os.getcwd()) / name)
    os.system(f'mkdir {name}')

    raw_init(name, typ)


@main.command()
@click.argument('raw_path', type=click.Path())
@click.argument('typ')
def init(raw_path, typ):
    path = os.path.normpath(pathlib.PurePosixPath(os.getcwd()) / raw_path)

    raw_init(path, typ)


@main.command()
@click.option('--release', is_flag=True)
def run():
    print('run')


@main.command()
def test():
    print('test')


@main.command()
def upgrade():
    print('upgrade')


@main.command()
@click.option('--dev', is_flag=True)
def add(dev):
    print('add')


@main.command()
def commit():
    print('commit')


@main.command()
@click.argument('dir')
def checkout(dir):
    print('checkout')


@main.command()
def map():
    print('map')
