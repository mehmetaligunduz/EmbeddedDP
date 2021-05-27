import random
from CyclicExecutive import CyclicExecutivePattern

def fasten_seat_belt_buzzer():
    randx = random.randint(0,2)
    if randx == 0:
        return "True"
    return "False"

def speedometer():
    return random.randint(0,120)

p1 = CyclicExecutivePattern(fasten_seat_belt_buzzer, speedometer)

try:
    x = p1.exec()
except Exception as e:
    print(e)
else:
    print(x)