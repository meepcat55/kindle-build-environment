import os
pm="NA"
distrobox=0
if os.path.isfile("/usr/bin/distrobox") or os.path.isfile("/bin/distrobox"):
    print("Distrobox detected")
    distrobox=1
else:
    print("distrobox not found, trying to detect package manager")
    if os.path.isfile("/usr/bin/apt-get") or os.path.isfile("/bin/apt-get"):
        print("apt-get detected, trying to install distrobox")
        os.system("sudo apt-get install distrobox podman -y")
        if os.path.isfile("/usr/bin/distrobox") or os.path.isfile("/bin/distrobox"):
            print("distrobox installed!")
            distrobox=1
        else:
            print("Distrobox is not installed!, trying other package managers")
    if os.path.isfile("/usr/bin/dnf") or os.path.isfile("/bin/dnf"):
        print("dnf detected trying to install distrobox")
        os.system("sudo dnf install distrobox podman -y")
        if os.path.isfile("/usr/bin/distrobox") or os.path.isfile("/bin/distrobox"):
            print("distrobox installed!")
            distrobox = 1
        else:
            print("Distrobox is not installed!, trying other package managers")
    if os.path.isfile("/usr/bin/pacman") or os.path.isfile("/bin/pacman"):
        print("pacman detected trying to install distrobox")
        os.system("sudo pacman -S distrobox podman")
        if os.path.isfile("/usr/bin/distrobox") or os.path.isfile("/bin/distrobox"):
            print("distrobox installed!")
            distrobox = 1
        else:
            print("Distrobox is not installed!, trying other package managers")
    if os.path.isfile("/usr/bin/zypper") or os.path.isfile("/bin/zypper"):
        print("zypper detected trying to install distrobox")
        os.system("sudo zypper install distrobox podman")
        if os.path.isfile("/usr/bin/distrobox") or os.path.isfile("/bin/distrobox"):
            print("distrobox installed!")
            distrobox = 1
        else:
            print("Distrobox is not installed!, trying other package managers")
    if os.path.isfile("/usr/bin/apk") or os.path.isfile("/bin/apk"):
        print("apk detected, never thought anyone would actually use alpine but here we are, trying to install distrobox")
        os.system("doas apk add distrobox podman")
        if os.path.isfile("/usr/bin/distrobox") or os.path.isfile("/bin/distrobox"):
            print("distrobox installed!")
            distrobox = 1
        else:
            print("Distrobox is not installed! all out of package managers")
if distrobox == 0:
    print("Alright bro ima keep it real, your either using windows, mac os, or some super obscure linux distro, if its the ladder go read the distrobox github and figure out how to install it")
    quit()