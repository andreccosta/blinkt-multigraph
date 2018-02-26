import blinkt
import time
import psutil
import multigraph

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

cpu_color = (0, 0, 200)
mem_color = (200, 0, 0)

ceiling = 100
floor = step = v = 1

while True:
    v += step
    if v == ceiling or v == floor:
        step = -step

    cpu_perc = mem_perc = v / 100.0

    multigraph.show(cpu_perc, mem_perc, cpu_color, mem_color)

    time.sleep(0.01)
