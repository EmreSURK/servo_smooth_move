import RPi.GPIO as GPIO
import time
import math
from threading import Thread

# servo connected pin.
servoPIN = 15

# movement data.
start_pos = 0
end_pos = 60


GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(0)


def duty(target_degree):
    duty_value = (float(target_degree) / 18.0 + 2)
    return duty_value


p.ChangeDutyCycle(duty(start_pos))
time.sleep(2)


def cos_value(value):
    return math.cos(value)


def current_pos(step_y_value):
    new_end_pos = 0
    dif = end_pos - start_pos
    if start_pos < end_pos:
        new_end_pos = int(end_pos - (dif * step_y_value))
    else:
        new_end_pos = int(start_pos + (dif * step_y_value))
    # print("new end pos : ", new_end_pos)
    # empty_line = ""
    # for x in range(new_end_pos):
    #     empty_line += " "
    # print(empty_line + ".")
    return new_end_pos


def move():
    start = math.pi
    end = math.pi * 2

    step = start
    while step < end:
        step = step + 0.08
        y_value = cos_value(step)
        # print(y_value)
        new_end_pos = current_pos(y_value)
        duty_value = duty(new_end_pos)
        p.ChangeDutyCycle(duty_value)
        time.sleep(0.02)


# move()
Thread(target=move, args=()).start()
