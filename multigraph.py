import blinkt


def _render_graph(colors, v, color, rev=False):
    r, g, b = color
    v *= blinkt.NUM_PIXELS

    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        index = x if not rev else blinkt.NUM_PIXELS - 1 - x
        colors[index] = [
            255 if y + z > 255 else y + z
            for y, z in zip(colors[index], [r, g, b])
        ]
        v -= 1


def show(v1, v2, color1, color2):
    colors = [[0, 0, 0]] * blinkt.NUM_PIXELS

    _render_graph(colors, v1, color1, True)
    _render_graph(colors, v2, color2, False)

    for i, x in enumerate(colors):
        blinkt.set_pixel(i, *x)

    blinkt.show()
