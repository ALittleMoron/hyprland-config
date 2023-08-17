#!/usr/bin/env bash

sh -c '(sleep 0.2s; pkill wofi || wofi -c ~/.config/wofi/config-lmenu)' & disown

printf "Application manager\n"
