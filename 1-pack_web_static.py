#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
"""do_pack - create a pack for web_static
"""


def do_pack():
    folder = "web_static"
    time = datetime.now()
    version_file = "{}_{}{}{}{}{}{}.tgz".format(folder, time.year,
                                time.month, time.day,
                                time.hour, time.minute,
                                time.second)

    local("mkdir -p versions")
    local("tar cavf versions/{} {}".format(version_file, folder))
