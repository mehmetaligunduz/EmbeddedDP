import time
import schedule

class CyclicExecutivePattern:

    def __init__(self, *code):
        self.code = code
        for i in range(0, len(code), 2):
            schedule.every(code[i+1]).seconds.do(code[i])

    def exec(self):
        while True:
            schedule.run_pending()
