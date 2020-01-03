#!/usr/bin/python3
from fabric.api import put, run, local, env
from shlex import split
from datetime import datetime

env.hosts = ["34.73.4.188", "35.237.83.22"]

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


"""do_deploy - deploy the archive with the servers
"""


def do_deploy(archive_path):
    if not archive_path:
        return False

    # Create the name dict for backup
    my_split = archive_path.split("/")
    file_tar = my_split[1]
    new_dict = my_split[1][:-4])

    # Upload .targz in the machine
    put(archive_path, "/tmp/")
    # Create the new directory
    run("mkdir -p /data/web_static/releases/{}/".format(new_dict))
    # Umcompress the file in /data/web_static/releases/ and remove
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_tar, new_dict))
    run("rm /tmp/{}".format(file_tar))
    run("mv /data/web_static/releases/{}/web_static/*
        /data/web_static/releases/{}/".format(new_dict, new_dict))
    # Remove the symlink and create the new symblink
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(new_dict))
