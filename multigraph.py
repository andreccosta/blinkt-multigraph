import blinkt


def _clamp(v, floor=0.0, ceiling=1.0):
    return max(min(v, ceiling), floor)


def _render_graph(v1, v2, color1, color2):
    v1 *= blinkt.NUM_PIXELS
    v2 *= blinkt.NUM_PIXELS

    for x, y in zip(
            range(blinkt.NUM_PIXELS), reversed(range(blinkt.NUM_PIXELS))):
        blinkt.set_pixel(
            x,
            *(z + w
              for z, w in zip([int(_clamp(v1 - x) * c) for c in color1],
                              [int(_clamp(v2 - y) * c) for c in color2])))


def show(v1, v2, color1, color2):
    _render_graph(v1, v2, color1, color2)

    blinkt.show()