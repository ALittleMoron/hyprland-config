#!/usr/bin/env bash

if [ ! -f /etc/arch-release ]; then
    exit 0
fi

AUR=$(yay -Qua | wc -l)
OFFICIAL=$(checkupdates | wc -l)
COUNT=$((OFFICIAL+AUR))

case $1 in
    aur) echo " $AUR";;
    official) echo " $OFFICIAL";;
esac

if [[ "$COUNT" = "0" ]]
then
    echo ""
    printf "No packages to update"
else
    echo " $COUNT"
    printf "Need to update $COUNT packages ($AUR aur and $OFFICIAL official)"
fi
exit 0
