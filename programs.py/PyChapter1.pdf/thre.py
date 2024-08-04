import threading
import time

def worker(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} exiting")

def main():
    print("Main thread starting")

    # Create a new thread
    t = threading.Thread(target=worker, args=("Worker",))

    # Start the thread
    t.start()

    # Wait for the thread to finish
    t.join()

    print("Main thread exiting")

if __name__ == "__main__":
    main()
