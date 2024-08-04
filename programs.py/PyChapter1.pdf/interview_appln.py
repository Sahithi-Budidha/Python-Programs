import tkinter as tk

class InterviewSessionWindow:
    def _init_(self, master):
        self.master = master
        master.title("Interview Session")

        # Question label
        self.question_label = tk.Label(master, text="Please answer the following questions:")
        self.question_label.pack()

        # First question
        self.question1_label = tk.Label(master, text="What is your name?")
        self.question1_label.pack()
        self.question1_entry = tk.Entry(master)
        self.question1_entry.pack()

        # Second question
        self.question2_label = tk.Label(master, text="What is your age?")
        self.question2_label.pack()
        self.question2_entry = tk.Entry(master)
        self.question2_entry.pack()

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        # Get answers
        name = self.question1_entry.get()
        age = self.question2_entry.get()

        # Print answers to console
        print("Name: ", name)
        print("Age: ", age)

        # Clear entry fields
        self.question1_entry.delete(0, tk.END)
        self.question2_entry.delete(0, tk.END)

# Create window
root = tk.Tk()
interview_session_window = InterviewSessionWindow(root)
root.mainloop()