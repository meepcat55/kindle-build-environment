# kindle-build-environment
A script that automatically sets up a distrobox with the tools needed for kindle homebrew development
## This only supports linux systems WSL is untested
## All information was sourced from the good folks at the kindle modding wiki https://kindlemodding.org/kindle-dev/gtk-tutorial/
## Requirements
- A Distro with distrobox in the repo
- Probably an x86-64 computer no guaranties about any other architecture
# Usage
`git clone https://github.com/meepcat55/kindle-build-environment.git && cd kindle-build-environment && bash run.sh`
- The SDK is currently probably unsuported with it giving the error mount: mnt: failed to setup loop device for /var/home/meepcat/Downloads/kindle-build-environment-main/koxtoolchain/kindle-sdk/cache/arm-kindlehf-linux-gnueabihf/firmware/rootfs.img
- Probably related to using distrobox, if anyone knows how to fix it please make a pull request.
