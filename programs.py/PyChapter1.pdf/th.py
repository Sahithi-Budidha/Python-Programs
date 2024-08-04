import threading

def print_numbers():
    for i in range(10):
        print(i)

# Create a new thread
t = threading.thread(target=print_numbers)

# Start the thread
t.start()

# Wait for the thread to finish
t.join()

# Print a message indicating that the program has finished
print("All done!")
