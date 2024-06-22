import colors
from custom_brightness import CustomBacklight
from libqtile import bar, qtile, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

# from libqtile.lazy import lazy

colors = colors.DoomOne

base_color01 = "#2f1629"
base_color02 = "#10091b"
font_color01 = "#FFFFFF"

my_font = "Maple Mono Bold"

widget_defaults = dict(
    font=my_font,
    foreground="#f4b8e4",
    background=base_color01,
    fontsize=10,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=7,
                    background=base_color02,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/icons/archlinux.svg",
                    margin=2,
                    background=base_color02,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty")},
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/6.png",
                    background=base_color02,
                ),
                widget.GroupBox(
                    padding=0,
                    font=my_font,
                    scroll=False,
                    hide_unused=True,
                    highlight_method="line",
                    background=base_color01,
                    inactive="#404040",
                    block_highlight_text_color=font_color01,
                    this_current_screen_border=font_color01,
                    highlight_color=[base_color01, "#282828"],
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/1.png",
                    background=base_color02,
                ),
                widget.TextBox(
                    fmt=" ",
                    font=my_font,
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.CurrentLayout(
                    font=my_font,
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/5.png",
                    background=base_color01,
                ),
                widget.Prompt(),
                widget.TextBox(
                    fmt="󰎇",
                    background=base_color02,
                    foreground=font_color01,
                ),
                widget.Mpris2(
                    background=base_color02,
                    foreground=font_color01,
                    font=my_font,
                    max_chars=70,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/4.png",
                    background=base_color01,
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=base_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/3.png",
                    background=base_color02,
                ),
                widget.Clock(
                    fontsize=12,
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    format="%Y-%m-%d %a %I:%M %p",
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/4.png",
                    background=base_color02,
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=base_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/3.png",
                    background=base_color02,
                ),
                widget.Clipboard(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    max_width=20,
                ),
                widget.Systray(
                    background=base_color02,
                    foreground=font_color01,
                ),
                widget.Spacer(
                    length=7,
                    background=base_color02,
                ),
                widget.Net(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    fontsize=12,
                    padding=0,
                    #  prefix="M",
                    format="WiFi:",
                ),
                widget.NetGraph(
                    background=base_color02,
                    graph_color=font_color01,
                    samples=100,
                    type="line",
                    line_width=1,
                    bandwidth_type="down",
                    border_width=0,
                ),
                widget.Net(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    fontsize=12,
                    padding=0,
                    #  prefix="M",
                    format="-> {down:.0f}{down_suffix}",
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/6.png",
                    background=base_color02,
                ),
                widget.Volume(
                    fmt="Vol: {}",
                    font=my_font,
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/2.png",
                    background=base_color02,
                ),
                widget.Memory(
                    format="Mem: {MemUsed: .0f}{mm}",
                    font=my_font,
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/2.png",
                    background=base_color02,
                ),
                widget.Memory(
                    format="Swap: {SwapUsed: .0f}{ms}",
                    font=my_font,
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/pink/5.png",
                    background=base_color02,
                ),
                widget.GenPollCommand(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    fontsize=12,
                    padding=0,
                    cmd="./.config/qtile/scripts/brightness --get",
                    mouse_callbacks={
                        "Button5": lazy.spawn("./.config/qtile/scripts/brightness +5"),
                        "Button6": lazy.spawn("./.config/qtile/scripts/brightness -5"),
                    },
                    fmt="brightness: {}",
                    shell=True,
                    update_interval=0.1,
                ),
                widget.Spacer(
                    length=4,
                    background=base_color02,
                ),
                widget.TextBox(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    fontsize=12,
                    padding=0,
                    mouse_callbacks={
                        "Button1": lazy.spawn("redshift -O 5000k"),
                        "Button3": lazy.spawn("redshift -x"),
                    },
                    fmt="RedShift",
                ),
                widget.Spacer(
                    length=4,
                    background=base_color02,
                ),
            ],
            26,
        ),
    ),
]
