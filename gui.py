import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        self.quiz_data = [
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                "correct_answer": 0
            },
            {
                "question": "Who wrote the novel 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Emily Bronte", "Charlotte Bronte", "Louisa May Alcott"],
                "correct_answer": 0
            },
            {
                "question": "What is the chemical symbol for the element Gold?",
                "options": ["Ag", "Au", "Cu", "Fe"],
                "correct_answer": 1
            }
        ]
        self.current_question_index = 0
        self.score = 0
        self.time_left = 60  # Initial time for each question (in seconds)
        
        self.window = tk.Tk()
        self.window.title("Quiz App")
        
        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()
        
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", width=30, command=lambda idx=i: self.check_answer(idx))
            button.pack()
            self.option_buttons.append(button)
        
        self.timer_label = tk.Label(self.window, text="Time left: 60 seconds")
        self.timer_label.pack()
        
        self.load_question()
        self.update_timer()
        
    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])
    
    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        correct_answer_index = question_data["correct_answer"]
        
        if selected_option == correct_answer_index:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect!")
        
        self.current_question_index += 1
        if self.current_question_index < len(self.quiz_data):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Over", f"Quiz finished. Your score: {self.score}/{len(self.quiz_data)}")
            self.window.quit()
    
    def update_timer(self):
        self.time_left -= 1
        self.timer_label.config(text=f"Time left: {self.time_left} seconds")
        if self.time_left > 0:
            self.window.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's up!", "You ran out of time!")
            self.current_question_index += 1
            if self.current_question_index < len(self.quiz_data):
                self.load_question()
                self.time_left = 60  # Reset time for the next question
                self.update_timer()
            else:
                messagebox.showinfo("Quiz Over", f"Quiz finished. Your score: {self.score}/{len(self.quiz_data)}")
                self.window.quit()

z_app = QuizApp()
z_app.window.mainloop()
