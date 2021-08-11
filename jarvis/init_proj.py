import os
import jarvis.constats as constats


def raw_init(path, project_type):
    default_project = os.path.expanduser(
        '~/.config/jarvis/') + project_type + '/*'

    os.system(f'cp -r {default_project} {path}')
