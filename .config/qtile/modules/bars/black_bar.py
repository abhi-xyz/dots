import colors
from libqtile import bar, qtile, widget
from libqtile.config import Screen

# from libqtile.lazy import lazy

colors = colors.DoomOne

base_color01 = "#363636"
base_color02 = "#282828"
font_color01 = "#FFFFFF"


widget_defaults = dict(
    font="Maple Mono Bold",
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
                    filename="~/.config/qtile/assets/bar/black/6.png",
                    background=base_color02,
                ),
                widget.GroupBox(
                    padding=0,
                    font="Maple Mono Bold",
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
                    filename="~/.config/qtile/assets/bar/black/1.png",
                    background=base_color02,
                ),
                widget.TextBox(
                    fmt=' ',
                    font="Maple Mono Bold",
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.CurrentLayout(
                    font="Maple Mono Bold",
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/5.png",
                    background=base_color01,
                ),
                widget.Prompt(),
                widget.TextBox(
                    fmt='󰎇',
                    background=base_color02,
                    foreground=font_color01,
                ),
                widget.Mpris2(
                    background=base_color02,
                    foreground=font_color01,
                    font="Maple Mono Bold",
                    max_chars=70,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/4.png",
                    background=base_color01,
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background="#363636",
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/3.png",
                    background=base_color02,
                ),
                widget.Clock(
                    fontsize=12,
                    font="Maple Mono Bold",
                    background=base_color02,
                    foreground=font_color01,
                    format="%Y-%m-%d %a %I:%M %p",
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/4.png",
                    background=base_color02,
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=base_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/3.png",
                    background=base_color02,
                ),
                widget.Clipboard(
                    font="Maple Mono Bold",
                    background=base_color02,
                    foreground=font_color01,
                    max_width=20,
                ),
                widget.Systray(
                    background=base_color02,
                    foreground=font_color01,
                ),
                widget.Net(
                    font="Maple Mono Bold",
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
                    type='line',
                    line_width=1,
                    bandwidth_type='down',
                    border_width=0,
                ),
                widget.Net(
                    font="Maple Mono Bold",
                    background=base_color02,
                    foreground=font_color01,
                    fontsize=12,
                    padding=0,
                    #  prefix="M",
                    format="-> {down:.0f}{down_suffix}",
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/6.png",
                    background=base_color02,
                ),
                widget.Volume(
                    fmt="Vol: {}",
                    font="Maple Mono Bold",
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/2.png",
                    background=base_color02,
                ),
                widget.Memory(
                    format="Mem: {MemUsed: .0f}{mm}",
                    font="Maple Mono Bold",
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/2.png",
                    background=base_color02,
                ),
                widget.Memory(
                    format="Swap: {SwapUsed: .0f}{ms}",
                    font="Maple Mono Bold",
                    background=base_color01,
                    foreground=font_color01,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/black/5.png",
                    background=base_color02,
                ),
                widget.Net(
                    font="Maple Mono Bold",
                    background=base_color02,
                    foreground=font_color01,
                    fontsize=12,
                    padding=0,
                    prefix="M",
                    format="WiFi: {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix} ",
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
