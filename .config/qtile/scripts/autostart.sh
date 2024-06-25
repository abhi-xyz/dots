#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}


feh --bg-scale ~/.config/qtile/assets/wallpapers/wallp-pink.png &
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &
playerctld &
kdeconnect-indicator &
setxkbmap -option caps:swapescape &
#setxkbmap -option grp:lalt_lshift_toggle &

run variety &
run nm-applet &
#run pamac-tray &
run xfce4-power-manager &
numlockx on &
run volumeicon &
blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# /usr/lib/xfce4/notifyd/xfce4-notifyd &

#starting user applications at boot time
#run discord &
#nitrogen --restore &
#run caffeine -a &
#run spotify &
#run telegram-desktop &
#run /usr/bin/octopi-notifier &


#start the conky to learn the shortcuts
(conky -c $HOME/.config/qtile/scripts/system-overview) &


#Set your native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

#Find out your monitor name with xrandr or arandr (save and you get this line)
#xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#xrandr --output DP2 --primary --mode 1920x1080 --rate 60.00 --output LVDS1 --off &
#xrandr --output LVDS1 --mode 1366x768 --output DP3 --mode 1920x1080 --right-of LVDS1
#xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off
#autorandr horizontal

##changed via give-me-azerty-qtile
#setxkbmap be

