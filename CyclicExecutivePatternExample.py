from CyclicExecutive import CyclicExecutivePattern

def task_1():
    print("t_1")

def task_2():
    print("t_2")

p1 = CyclicExecutivePattern(task_1, 2, task_2, 4)

try:
    x = p1.exec()
except Exception as e:
    print(e)