# Fix the hidpi scaling issues
xrandr --output eDP-1 --scale 1.5x1.5
xrandr --output eDP-1 --panning 3840x2160

# Fix the Lenovo TrackPoint (default is very slow)
echo 200 | sudo tee /sys/devices/platform/i8042/serio1/serio2/sensitivity
echo 255 | sudo tee /sys/devices/platform/i8042/serio1/serio2/speed
sudo udevadm control --reload-rules
sudo udevadm trigger
