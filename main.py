import blinkt
import time
import psutil
import multigraph

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

colors = [[0, 0, 0]] * blinkt.NUM_PIXELS

cpu_color = (0, 0, 100)
mem_color = (100, 0, 0)

while True:
    cpu_perc = psutil.cpu_percent() / 100.0
    mem_perc = psutil.virtual_memory().percent / 100.0

    multigraph.show(cpu_perc, mem_perc, cpu_color, mem_color)

    time.sleep(1)
