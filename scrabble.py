"""Scrabble game"""

import tkinter as tk
from tkinter import messagebox
import random
from input_handler import InputHandler
from score_calculator import ScoreCalculator


class Scrabble: #  pylint: disable = possibly-used-before-assignment too-many-instance-attributes
    """Python Scrabble class"""

    input_handler = InputHandler()
    score_calculator = ScoreCalculator()
    time_left = 15
    playing_game = False
    score = 0
    amount_characters = 0
    round = 0
    timer_running = False

    def __init__(self, root):
        self.root = root
        self.root.title("Scrabble score")

        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        # Start button
        self.start_button = tk.Button(button_frame, text='Start game',
                                      command=self.start_game)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Quit button
        self.quit_button = tk.Button(button_frame, text='Quit game',
                                     command=self.quit_game)
        self.quit_button.pack(side=tk.LEFT, padx=10)

        # Timer label
        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}")
        self.timer_label.pack(pady=20)

        # Score label
        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.score_label.pack(pady=20)

        # Promt label
        self.promt_label = tk.Label(root, text="Welcome to Scrabble score")
        self.promt_label.pack(pady=20)

        # Text entry widget
        self.entry = tk.Entry(root)
        self.entry.pack(pady=20)

        # Submit button
        self.submit_button = tk.Button(root, text='submit',
                                       command=self.check_word, state="disabled")
        self.submit_button.pack(pady=10)

    def update_score(self, points):
        """Updates score with given points"""

        self.score += points
        self.score_label.config(text=f"Score: {self.score}")

    def update_timer(self):
        """If playing starts a self contained timer"""
        if self.playing_game:
            if self.time_left > 0:  # Checks that time hasn't run out
                self.time_left -= 1
                self.timer_label.config(text=f"Time left: {self.time_left}")
                self.root.after(1000, self.update_timer)
            else:  # If time has run out
                messagebox.showinfo(message="You answered too slow")
                self.timer_running = False
                self.play_round()

    def reset_timer(self):
        """Resets timer"""
        self.time_left = 15
        self.timer_label.config(text=f"Time left: {self.time_left}")
        if self.timer_running is False:
            self.update_timer()
            self.timer_running = True

    def check_word(self):
        """Gets word from inputfield"""
        word = self.entry.get()
        if self.input_handler.is_correct_input(word, self.amount_characters):
            self.update_score(self.score_calculator.calculate(word))
            self.entry.delete(0, tk.END)
            self.play_round()
        else:
            messagebox.showwarning(message="Enter a word only using letters")

    def play_round(self):
        """Starts a new round"""
        self.round += 1
        if self.round > 10:
            self.finish_game()
        else:
            self.reset_timer()
            self.amount_characters = random.randrange(2, 8)
            self.promt_label.config(text=f"Write a {self.amount_characters} character long word")

    def finish_game(self):
        """Resets the game and shows score"""
        messagebox.showinfo("GAME OVER", f"Your total score is {self.score}")
        self.score = 0
        self.round = 0
        self.reset_timer()
        self.playing_game = False
        self.score_label.config(text=f"Score: {self.score}")
        self.promt_label.config(text="Welcome to Scrabble score")
        self.submit_button.config(state="disabled")
        self.start_button.config(state="active")

    def start_game(self):
        """Initiates new game"""
        self.round = 0
        self.score = 0
        self.playing_game = True
        self.submit_button.config(state="active")
        self.start_button.config(state="disabled")
        self.update_timer()
        self.timer_running = True
        self.play_round()

    def quit_game(self):
        """Quits game and closes application"""
        response = messagebox.askokcancel("Exit", f"Your score is {self.score}. \nPress ok to exit")
        if response:
            app.destroy()


if __name__ == "__main__":
    app = tk.Tk()
    game = Scrabble(app)
    app.mainloop()
