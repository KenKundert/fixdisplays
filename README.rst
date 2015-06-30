Fixdisplays
===========

Control which screens are used.

Usage:
    fixdisplays [options]

Options:
    -l, --laptop     enable built-in screen, disable all others.
    -d, --desktop    enable external monitors, disable all others.
    -p, --projector  enable external VGA projector along with built-in screen.
    -t, --trialrun   describe what would be done rather than doing it

This script allow you to quickly reconfigure the screens you are using based on 
which monitors are available.  It must be set up by modifying the script itself 
so that it knows which screens you want to use when you are in the various 
modes.
