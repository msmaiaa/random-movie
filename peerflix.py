import os

#pasted from https://github.com/AnthonyBloomer/ezflix/blob/master/ezflix/utils.py
def peerflix(magnet_link, media_player, remove):

    remove = "--remove" if remove else ""
    cmd = 'peerflix "%s" --%s %s' % (magnet_link, media_player, remove)
    print("Executing " + cmd)
    #subprocess.Popen(["/bin/bash", "-c", cmd], shell=True)
    os.system(f'cmd /k {cmd}')