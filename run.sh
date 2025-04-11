sudo python3 kindle-build-env1.py
distrobox create -i archlinux -n kindle-build-env -volume $(pwd)
dir=$(pwd)/kindle-build-env2.py
echo "sudo pacman -S python3" > python.sh
echo "python3 $dir" >> python.sh
distrobox enter kindle-build-env -- bash $(pwd)/python.sh
