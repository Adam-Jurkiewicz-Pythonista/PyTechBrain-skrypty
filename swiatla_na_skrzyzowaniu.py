# Kod źródłowy dla lekcji: Światła na skrzyżowaniu
# Autor: Adam Jurkiewicz, ABIX Edukacja https://pytechbrain.edu.pl
#

from PyTechBrain import *
from time import sleep
from sys import exit as exit_application

# create object
my_board = PyTechBrain()

if my_board.board_init():  # initializing connection
    print("Super! Initialization complete.")
    my_board.set_buzzer("beep")  # demo, on, off
else:
    print("Something was wrong!")
    my_board.full_debug_output()
    my_board.usage_info()
    exit_application(2)

# now we do the rest....

# we set off all outputs
if not my_board.set_off_outputs():
    print("Something was wrong!")
    my_board.full_debug_output()
    exit_application(2)

while True:
    my_board.set_signal_red("on")
    sleep(1.7)
    my_board.set_signal_yellow("on")
    sleep(1.3)
    my_board.set_signal_red("off")
    my_board.set_signal_yellow("off")
    my_board.set_signal_green("on")
    sleep(2.5)
    my_board.set_signal_green("off")
    my_board.set_signal_yellow("on")
    sleep(1.4)
    my_board.set_signal_yellow("off")
