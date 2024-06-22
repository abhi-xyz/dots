# ------------------------ importing modules ------------------------ #

from modules.bars.pink_bar import screens
from modules.groups import groups
from modules.hooks import *
from modules.keys import keys
from modules.layouts import floating_layout, layouts
from modules.mouse import mouse
#from modules.bar import screens
from modules.variables import home, mod, terminal

# ------------------------------------------------------------------- #


dgroups_key_binder = None
dgroups_app_rules = []
main = None
floating_types = ["notification", "toolbar", "splash", "dialog"]
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"
wmname = "LG3D"
