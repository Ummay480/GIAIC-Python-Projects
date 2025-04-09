import time

def countdown(seconds):
    while seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's Up!")

if __name__ == "__main__":
    countdown(10)  # Change the number to set how many seconds to count down
