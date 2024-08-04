import tkinter as tk
import random

# List of words to be jumbled
WORDS = ['PYTHON', 'PROGRAMMING', 'COMPUTER', 'ENGINEERING', 'INFORMATION', 'TECHNOLOGY']

class JumbleGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Jumble Word Game")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Generate a random word from the list
        self.word = random.choice(WORDS)
        self.jumbled_word = self.jumble_word(self.word)

        # Create widgets
        self.title_label = tk.Label(self, text="Unscramble the word:")
        self.title_label.config(font=("Helvetica", 20))
        self.title_label.pack(side="top", pady=10)

        self.jumbled_label = tk.Label(self, text=self.jumbled_word)
        self.jumbled_label.config(font=("Helvetica", 30), fg="blue")
        self.jumbled_label.pack(side="top", pady=20)

        self.guess_entry = tk.Entry(self)
        self.guess_entry.config(font=("Helvetica", 20))
        self.guess_entry.pack(side="top", pady=10)
        self.guess_entry.focus_set()

        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.config(font=("Helvetica", 20), bg="green", fg="white")
        self.submit_button.pack(side="top", pady=20)

        self.message_label = tk.Label(self)
        self.message_label.config(font=("Helvetica", 20))
        self.message_label.pack(side="top", pady=20)

    def jumble_word(self, word):
        # Shuffle the characters of the word
        shuffled_word = random.sample(word, len(word))
        return ''.join(shuffled_word)

    def check_guess(self):
        guess = self.guess_entry.get().upper()
        if guess == self.word:
            self.message_label.config(text="Correct! You Win!", fg="green")
        else:
            self.message_label.config(text="Sorry, Try Again!", fg="red")

# Main function to start the game
def main():
    root = tk.Tk()
    root.geometry("500x500")
    app = JumbleGame(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
