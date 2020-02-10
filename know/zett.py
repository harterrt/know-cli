import datetime as dt
from subprocess import call
import os

def new_note(settings):
    call(['vim', os.path.join(
        settings['ROOT'],
        'raw/zett',
        dt.datetime.now().isoformat() + '.md'
    )])
