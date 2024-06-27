import colors
from custom_brightness import CustomBacklight
from libqtile import bar, qtile, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

colors = colors.DoomOne

base_color01 = "#150619"
base_color02 = "#10091b"
hl_color01 = "#f1bee0"
font_color01 = "#FFFFFF"
font_color02 = "#000000"

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
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("alacritty")},
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
                widget.Prompt(),
                widget.WindowName(
                    background=base_color01,
                    foreground=font_color01,
                    font=my_font,
                    fmt="[] - {}"
                ),
                widget.Clipboard(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    max_width=20,
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
                    format="[ WiFi:",
                ),
                widget.NetGraph(
                    background=base_color02,
                    graph_color=font_color01,
                    margin_x=0,
                    margin_y=13,
                    samples=100,
                    type="line",
                    padding=0,
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
                    prefix="k",
                    # prefix="M",
                    format="-> {down:.0f}{down_suffix} ]",
                ),
                widget.OpenWeather(
                    location='Ponkunnam', format='[ temp: {main_temp}°{units_temperature} - {weather_details} ]',
                    font=my_font,
                ),
                widget.Volume(
                    fmt="[ Vol: {} ]",
                    font=my_font,
                    background=base_color01,
                    foreground=font_color01,
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
                    fmt="[ bri: {} ]",
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
                    padding=0,
                    mouse_callbacks={
                        "Button1": lazy.spawn("redshift -O 5000k"),
                        "Button3": lazy.spawn("redshift -x"),
                    },
                    fmt="[ red: ",
                ),
                widget.TextBox(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    padding=0,
                    fontsize=16,
                    mouse_callbacks={
                        "Button1": lazy.spawn("redshift -O 5000k"),
                        "Button3": lazy.spawn("redshift -x"),
                    },
                    fmt="󱩌",
                ),
                widget.TextBox(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    padding=0,
                    mouse_callbacks={
                        "Button1": lazy.spawn("redshift -O 5000k"),
                        "Button3": lazy.spawn("redshift -x"),
                    },
                    fmt=" ]",
                ),
                widget.Memory(
                    format="[ Mem:{MemUsed: .0f}{mm} ]",
                    font=my_font,
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.CPU(
                    format="[ Cpu: {freq_current}GHz - {load_percent}% ]",
                    font=my_font,
                ),
                widget.Clock(
                    fontsize=12,
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    format="[ %Y-%m-%d %a %I:%M %p ]",
                ),
                widget.Spacer(
                    length=4,
                    background=base_color02,
                ),
                widget.TextBox(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    padding=0,
                    fmt="[ ",
                ),
                widget.WidgetBox(
                    close_button_location='right',
                    fontsize=28,
                    text_closed="",
                    text_open="",
                    widgets=[
                        widget.Systray(
                            background=base_color02,
                            foreground=font_color01,
                        ),
                    ]
                ),
                widget.TextBox(
                    font=my_font,
                    background=base_color02,
                    foreground=font_color01,
                    padding=0,
                    fmt=" ]",
                ),
            ],
            30,
        ),
    ),
]
