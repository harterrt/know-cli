import datetime as dt
from subprocess import call
import os

def new_note(settings):
    call(['vim', os.path.join(
        settings['ROOT'],
        'raw/zeit',
        dt.datetime.now().isoformat() + '.md'
    )])
