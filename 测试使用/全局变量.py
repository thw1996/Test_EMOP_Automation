import time

class Asadada():
    day = time.strftime("%Y-%m-%d_%H_%M_%S_", time.localtime(time.time()))
    print(day)
    def day_ii(self):
        time.sleep(5)
        global day
        day = time.strftime("%Y-%m-%d_%H_%M_%S_", time.localtime(time.time()))
        print(day+"ssss")
    def day2(self):
        print(day)
    print(day)
if __name__ == '__main__':
    Asadada().day_ii()
    Asadada().day2()