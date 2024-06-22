import os
import shlex
from functools import partial, wraps
from time import time

from libqtile.command.base import expose_command
from libqtile.log_utils import logger
from libqtile.widget import base


def debounce(wait):
    """Decorator that will postpone a function's execution until after `wait` seconds
    have elapsed since the last time it was invoked.
    """

    def decorator(fn):
        @wraps(fn)
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
                debounced._timer = None

            if debounced._timer is not None:
                debounced._timer.cancel()

            debounced._timer = Timer(wait, call_it)
            debounced._timer.start()

        debounced._timer = None
        return debounced

    return decorator


class CustomBacklight(base.InLoopPollText):
    """A custom widget to show and manage the current brightness using a custom script."""

    defaults = [
        ("update_interval", 0.2, "The delay in seconds between updates"),
        ("step", 1, "Percent of backlight change on scroll"),
        ("format", "{percent:2.0%}", "Display format"),
        ("min_brightness", 0, "Minimum brightness percentage"),
        (
            "brightness_script",
            "~/.config/qtile/scripts/brightness",
            "Path to the brightness script",
        ),
        (
            "scroll_delay",
            0.5,
            "Delay in seconds before applying brightness change after scroll",
        ),
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(CustomBacklight.defaults)
        self._future = None
        self._brightness_change_time = time()

        self.brightness_script = os.path.expanduser(self.brightness_script)

        self.add_callbacks(
            {
                "Button4": partial(self._scroll_brightness, "up"),
                "Button5": partial(self._scroll_brightness, "down"),
            }
        )

    def finalize(self):
        if self._future and not self._future.done():
            self._future.cancel()
        base.InLoopPollText.finalize(self)

    def _run_command(self, command):
        """Run the command and return the output."""
        try:
            result = self.call_process(shlex.split(command))
            return result.strip()
        except Exception as e:
            logger.error("Error running command '%s': %s", command, e)
            return None

    def _get_brightness(self):
        """Get the current brightness as a percentage."""
        output = self._run_command(f"{self.brightness_script} --get")
        try:
            brightness = float(output)
            return brightness / 100
        except (TypeError, ValueError):
            logger.error("Error parsing brightness value: %s", output)
            return None

    def poll(self):
        """Poll the current brightness."""
        percent = self._get_brightness()
        if percent is None:
            return "Error"
        return self.format.format(percent=percent)

    @expose_command()
    def change_backlight(self, direction, step=None):
        """Change the brightness in the specified direction by the step amount."""
        if not step:
            step = self.step

        if direction == "up":
            command = f"{self.brightness_script} +{step}"
        elif direction == "down":
            command = f"{self.brightness_script} -{step}"
        else:
            logger.error("Invalid direction: %s", direction)
            return

        self._future = self.qtile.run_in_executor(self._run_command, command)

    def _scroll_brightness(self, direction):
        """Handle mouse scroll to change brightness smoothly."""
        self._brightness_change_time = time()
        self.qtile.call_later(
            self.scroll_delay, self._apply_brightness_change, direction
        )

    def _apply_brightness_change(self, direction):
        """Apply brightness change if the scroll action is finished."""
        if time() - self._brightness_change_time >= self.scroll_delay:
            self.change_backlight(direction)
