from libqtile.lazy import lazy
from libqtile.config import Key
from modules.variables import mod, terminal


keys = [
    Key([mod], "d", lazy.spawn("sh -c ~/.config/qtile/rofi/launcher/launcher_d.sh")),
    Key([mod], "h", lazy.layout.left(), ),
    Key([mod], "l", lazy.layout.right(), ),
    Key([mod], "j", lazy.layout.down(), ),
    Key([mod], "k", lazy.layout.up(), ),
    Key([mod], "q", lazy.window.kill(), ),
    Key([mod], "f", lazy.window.toggle_fullscreen(), ),
    Key([mod], "n", lazy.layout.normalize(), ),
    Key([mod], "r", lazy.spawncmd(), ),
    Key([mod], "t", lazy.window.toggle_floating(), ),

    Key([mod], "Tab", lazy.next_layout(), ),
    Key([mod], "space", lazy.layout.next(), ),
    Key([mod], "Return", lazy.spawn(terminal), ),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), ),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), ),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), ),
    Key([mod, "shift"], "f", lazy.layout.flip()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), ),

    Key([mod, "control"], "h", lazy.layout.grow_left(), ),
    Key([mod, "control"], "l", lazy.layout.grow_right(), ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), ),
    Key([mod, "control"], "k", lazy.layout.grow_up(), ),
    Key([mod, "control"], "r", lazy.reload_config(), ),
    Key([mod, "control"], "q", lazy.shutdown(), ),

    ]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod, "shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod, "shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])
