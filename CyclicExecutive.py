import time

class CyclicExecutivePattern:

    def __init__(self, code, code2):
        self.code = code
        self.code2 = code2

    def exec(self):
        while True:
            print(self.code() + "\t" +  time.ctime())
            print(str(self.code2()) + "\t" +  time.ctime())
            time.sleep(1)