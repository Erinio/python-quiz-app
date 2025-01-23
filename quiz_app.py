import tkinter as tk
from tkinter import messagebox

# Predefined list of questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 1  # Position in the options array
    },
    {
        "topic": "Lists",
        "question": "What is the output of the following code?",
        "code": "my_list = [1, 2, 3]\nprint(len(my_list))",
        "options": ["1", "2", "3", "4"],
        "answer": 3
    },
    {
        "topic": "Strings",
        "question": "What does the following code output?",
        "code": "print('hello'.upper())",
        "options": ["HELLO", "hello", "Hello", "Error"],
        "answer": 1
    }
]

# Functionality
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")
        self.root.geometry("600x400")  # Set the default window size to 600x400
        self.current_question = None

        # GUI elements
        self.topic_label = tk.Label(root, text="Enter Python Topic:")
        self.topic_label.pack()

        self.topic_entry = tk.Entry(root)
        self.topic_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Python Question", command=self.generate_question)
        self.generate_button.pack()

        self.question_frame = tk.Frame(root)
        self.question_frame.pack(pady=10)

        self.radio_var = tk.IntVar()

        # Submit button starts disabled
        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer, state=tk.DISABLED)
        self.submit_button.pack()

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

    def generate_question(self):
        topic = self.topic_entry.get().strip()
        filtered_questions = [q for q in questions if q["topic"].lower() == topic.lower()]

        if not filtered_questions:
            messagebox.showerror("Error", "No questions available for the given topic.")
            return

        self.current_question = filtered_questions[0]
        self.display_question()

        # Enable the submit button after generating a question
        self.submit_button.config(state=tk.NORMAL)

    def display_question(self):
        # Clear the question frame
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        question = self.current_question

        topic_label = tk.Label(self.question_frame, text=f"Topic: {question['topic']}")
        topic_label.pack()

        question_label = tk.Label(self.question_frame, text=f"Question: {question['question']}")
        question_label.pack()

        if "code" in question:
            code_label = tk.Label(self.question_frame, text=f"Code:\n{question['code']}", justify="left", bg="#f0f0f0", anchor="w")
            code_label.pack(fill="x", padx=5, pady=5)

        for idx, option in enumerate(question["options"], 1):
            radio = tk.Radiobutton(self.question_frame, text=option, variable=self.radio_var, value=idx)
            radio.pack(anchor="w")

        self.radio_var.set(0)

    def check_answer(self):
        selected_option = self.radio_var.get()
        if selected_option == 0:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        if selected_option == self.current_question["answer"]:
            self.feedback_label.config(text="Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
