import tkinter as tk
import random

# List of jumbled words
words = ['PYTHON', 'JAVA', 'JAVASCRIPT', 'RUBY', 'PHP', 'HTML', 'CSS', 'SQL', 'KOTLIN']

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to jumble the chosen word
def jumble_word(word):
    jumbled = ''.join(random.sample(word, len(word)))
    return jumbled

# Function to check if the answer is correct
def check_answer(word, answer):
    return word == answer.upper()

# Function to display the jumbled word
def display_word():
    global word, jumbled_word
    word = choose_word()
    jumbled_word = jumble_word(word)
    word_label.config(text=jumbled_word)

# Function to check the answer
def submit_answer():
    global word, jumbled_word
    answer = answer_entry.get()
    if check_answer(word, answer):
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect!")
    display_word()
    answer_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Jumble Word Game")

# Create the widgets
word_label = tk.Label(root, text="", font=("Arial", 36), fg="blue")
word_label.pack(pady=10)

answer_label = tk.Label(root, text="Enter your answer:", font=("Arial", 24), fg="green")
answer_label.pack()

answer_entry = tk.Entry(root, font=("Arial", 24))
answer_entry.pack()

submit_button = tk.Button(root, text="Submit", font=("Arial", 18), fg="red", command=submit_answer)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 24), fg="purple")
result_label.pack(pady=10)

new_word_button = tk.Button(root, text="New Word", font=("Arial", 18), fg="orange", command=display_word)
new_word_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", font=("Arial", 18), fg="brown", command=root.destroy)
quit_button.pack(pady=10)

# Display the first word
display_word()

# Start the main loop
root.mainloop()
