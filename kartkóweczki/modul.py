import time
def czas1():
    print("Data:")
    print(time.strftime("%Y", time.localtime()))
    print(time.strftime("%m", time.localtime()))
    print(time.strftime("%d", time.localtime()))

def czas():
    x=int(input("Jaka sekunda UNIX_TIME: "))
    print("Data:")
    print(time.strftime("%Y", time.localtime(x)))
    print(time.strftime("%m", time.localtime(x)))
    print(time.strftime("%d", time.localtime(x)))
if __name__ == "__main__":
    czas1()
