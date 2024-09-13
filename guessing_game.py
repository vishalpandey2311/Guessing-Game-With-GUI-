import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.attributes('-fullscreen', True)

        # Create a canvas for background with linear gradient color
        self.canvas = tk.Canvas(self.master, width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight(), bg='#4e54c8', highlightthickness=0)
        self.canvas.pack()

        # Heading with red color and increased font size
        self.create_heading_with_shadow()

        # Question
        self.question = tk.Label(self.canvas, text="Guess a number between 1 to 100", font=("Helvetica", 18), fg="white", bg='#4e54c8')
        self.question.place(relx=0.5, rely=0.3, anchor="center")

        # Entry for user input
        self.user_input = tk.Entry(self.canvas, font=("Helvetica", 16))
        self.user_input.place(relx=0.5, rely=0.4, anchor="center")

        # Button to submit the guess
        self.submit_button = tk.Button(self.canvas, text="Submit", command=self.check_guess, font=("Helvetica", 16), bg='#ff7675', fg="white")
        self.submit_button.place(relx=0.5, rely=0.5, anchor="center")

        # Initialize the target number
        self.target_number = random.randint(1, 100)

        # Initialize attempts
        self.attempts = 0
    def create_heading_with_shadow(self):
        # Heading with red color and increased font size
        main_heading = tk.Label(self.canvas, text="Guessing Game", font=("Helvetica", 48, "bold"), fg="#e74c3c", bg='#4e54c8')
        main_heading.place(relx=0.5, rely=0.1, anchor="center")

        # Create a shadow by creating additional labels with slightly shifted positions and different colors
        for offset in range(1, 4):
            shadow_heading = tk.Label(self.canvas, text="Guessing Game", font=("Helvetica", 48, "bold"), fg="#2c3e50", bg='#4e54c8')
            shadow_heading.place(relx=0.5 - offset, rely=0.1 + offset / 10, anchor="center")

    def check_guess(self):
        # Increment attempts
        self.attempts += 1

        # Get user's guess
        user_guess = int(self.user_input.get())

        # Check if the guess is correct
        if user_guess == self.target_number:
            self.show_congratulations()
        else:
            # Provide feedback on the guess
            if user_guess < self.target_number:
                feedback = "Try higher!"
            else:
                feedback = "Try lower!"

            # Show feedback
            messagebox.showinfo("Feedback", feedback)

    def show_congratulations(self):
        # Destroy all widgets
        for widget in self.canvas.winfo_children():
            widget.destroy()

        # Display congratulations message
        congrats_label = tk.Label(self.canvas, text="Congratulations!", font=("Helvetica", 24, "bold"), fg="white", bg='#4e54c8')
        congrats_label.place(relx=0.5, rely=0.5, anchor="center")

        # Display attempts
        attempts_label = tk.Label(self.canvas, text=f"Attempts: {self.attempts}", font=("Helvetica", 18), fg="white", bg='#4e54c8')
        attempts_label.place(relx=0.5, rely=0.6, anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Guessing Game")
    app = GuessingGame(root)
    root.mainloop()
