# Informacje dla posiadaczy „zwykłego” Arduino

W programie wykorzystano moduł pymata_aio (https://github.com/MrYsLab/pymata-aio) autorstwa Alan'a Yorinks'a (MrYsLab) oraz oprogramowanie firmowe do Arduino tego autora (https://github.com/MrYsLab/pymata-aio/tree/master/FirmataPlus).

---
## Układ PINów:

    # buttons
    self.button_left = 12
    self.button_middle = 11
    self.button_right = 10
   
    # service_led
    self.service_led = 13

    # pwm_diode
    self.pwm_diode = 9

    # signal_rgb_3_leds
    self.red_diode = 8  # red
    self.yellow_diode = 7  # yellow
    self.green_diode = 2  # green

    # rgb_color - diode
    self.rgb_red = 5
    self.rgb_green = 3
    self.rgb_blue = 6

    # buzzer
    self.buzzer = 4

    # analog sensors ...
    # empty -           = 0
    # empty -           = 1
    self.fotoresistor = 2
    self.volume_sensor = 3
    self.temp_sensor = 4
    self.potentiometer = 5

---
## Minimalny kod:

```python
print("This is sample of using PyTechBrain module.")
print("===========================================")

# creating board object with default debugging with no output
test_board = PyTechBrain()

# the same, but with full debugging during using module
# test_board = PyTechBrain(debug=True)

if test_board.board_init():
    print("Super!")
    test_board.set_buzzer("beep")  # demo, on, off
else:
    print("Something went wrong... check output.")

test_board.full_debug_output()

```