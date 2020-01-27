import inspect
import os

settings_path = os.path.expanduser('~/.config/know/settings.py')
settings = {
    'ROOT': os.path.expanduser('~/know/'),
}


def get_settings_from_module(module):
    '''https://github.com/getpelican/pelican/blob/master/pelican/settings.py'''

    if module is not None:
        settings.update(
                (k, v) for k, v in inspect.getmembers(module) if k.isupper()
        )

    return settings

