fixdisplays
===========

Control which screens are used.

::

   Usage:
       fixdisplays [options]
       fixdisplays [options] l|laptop
       fixdisplays [options] d|desktop
       fixdisplays [options] p|projector

   Options:
       -s, --swap       swap the displays
       -n, --narrate    narrate the changes
       -q, --quiet      suppress all messages except for error messages

   The three available configurations are:
       l, laptop        enable built-in screen, disable all others.
       d, desktop       enable external monitors, disable all others.
       p, projector     enable external VGA projector along with built-in screen.


This script allows you to quickly reconfigure the screens you are using based on 
which monitors are available.  It must be set up by modifying the script itself 
so that it knows which screens you want to use when you are in the various 
modes.

Also configures the default audio sink when you switch the displays.

The following things can be configured by modifying the script:

LAPTOP_PREFIX, DESKTOP_PREFIX, PROJECTOR_PREFIX:

    This script assumes that each type of display has a different xrandr prefix, 
    which are specified in these three settings.

SOUND_SINKS:

    A dictionary that give the string that is used to identify the *internal* 
    and *external* sound sinks.  The information may be anything produced by 
    *pacmd list-sinks* that uniquely identifies the sink.

RESET_KEYBOARD:

    Command used to reset the keyboard. By default this is 'reset', but can be 
    set to None to eliminate resetting of the keyboard.

VOL_CONTROL_CMD:

    Normally *fixdisplays* tries to create a command that controls the volume of 
    the active sound sink. This would be the path for the command. If set to 
    None, the command is not created.

