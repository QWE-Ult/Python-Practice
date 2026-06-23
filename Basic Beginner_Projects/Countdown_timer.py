import time
import winsound

def alarm():

    for _ in range(5):
        winsound.Beep(1000, 200)
        time.sleep(0.1)


def timer(ts):

    for i in range(ts, 0, -1):

        h = i // 3600
        m = (i % 3600) // 60
        s = i % 60

        print(f"{h:02}:{m:02}:{s:02}")

        time.sleep(1)

    print("Time's Up!")

    alarm()


seconds = int(input("Enter seconds: "))
timer(seconds)