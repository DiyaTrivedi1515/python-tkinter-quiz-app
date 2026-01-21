import tkinter as tk
from tkinter import messagebox

# 20 questions divided by category
core_python_questions = [
    {"question": "Which keyword defines a function?", "options": ["func", "define", "def", "function"], "answer": 2},
    {"question": "Which data type is immutable?", "options": ["list", "tuple", "dict", "set"], "answer": 1},
    {"question": "What does 'len([1,2,3])' return?", "options": ["3", "2", "Error", "0"], "answer": 0},
    {"question": "Which loop runs at least once?", "options": ["for", "while", "do-while", "None"], "answer": 3},
    {"question": "How to add comment in Python?", "options": ["// comment", "# comment", "/* comment */", "<!-- comment -->"], "answer": 1},
    {"question": "What is the output of '3 * 2 ** 2'?", "options": ["36", "12", "8", "None"], "answer": 2},
    {"question": "Which of these is NOT a Python keyword?", "options": ["lambda", "eval", "pass", "global"], "answer": 1},
    {"question": "What is the correct way to create a dictionary?", "options": ["{}", "[]", "()", "<>"], "answer": 0},
    {"question": "Which operator is used for floor division?", "options": ["/", "//", "%", "**"], "answer": 1},
    {"question": "How do you declare a global variable inside a function?", "options": ["global x", "var x", "let x", "x = global"], "answer": 0},
]

library_questions = [
    {"question": "Which library is used for GUI?", "options": ["numpy", "pygame", "tkinter", "matplotlib"], "answer": 2},
    {"question": "Which library is used for random numbers?", "options": ["random", "math", "sys", "os"], "answer": 0},
    {"question": "Which library is used for data visualization?", "options": ["math", "os", "matplotlib", "sys"], "answer": 2},
    {"question": "Which library helps to handle dates?", "options": ["datetime", "calendar", "time", "All"], "answer": 3},
    {"question": "Which library is used for JSON handling?", "options": ["json", "pickle", "csv", "requests"], "answer": 0},
    {"question": "Which library is used to interact with the OS?", "options": ["os", "sys", "platform", "shutil"], "answer": 0},
    {"question": "Which library helps in making HTTP requests?", "options": ["requests", "urllib", "http", "All"], "answer": 3},
    {"question": "Which library is used for math functions?", "options": ["math", "cmath", "numpy", "All"], "answer": 3},
    {"question": "Which library is used for game development?", "options": ["pygame", "tkinter", "matplotlib", "numpy"], "answer": 0},
    {"question": "Which library is used for file handling?", "options": ["os", "io", "shutil", "All"], "answer": 3},
]

# Initialize variables
score = 0
current_q = 0
questions = []

# --- Functions ---
def start_quiz(category):
    global questions, current_q, score
    current_q = 0
    score = 0
    selected_option = tk.IntVar()
    if category == "Core Python":
        questions = core_python_questions
    else:
        questions = library_questions
    category_frame.pack_forget()
    quiz_frame.pack(pady=20)
    load_question()

def load_question():
    question_label.config(text=f"Q{current_q+1}: {questions[current_q]['question']}")
    for i, option in enumerate(options):
        option.config(text=questions[current_q]["options"][i])
    selected_option.set(-1)
    question_counter.config(text=f"Question {current_q+1} of {len(questions)}")

def next_question():
    global current_q, score, answered

    # If user hasn't selected anything
    if selected_option.get() == -1:
        messagebox.showerror("Invalid", "Please select an option")
        return

    # First click: check answer
    if not answered:
        if selected_option.get() == questions[current_q]["answer"]:
            score += 1
            question_label.config(bg="lightgreen")  # correct = green
        else:
            question_label.config(bg="red")  # wrong = red
        answered = True  # mark this question as answered
        return  # wait for next click to move on

    # Second click: move to next question
    answered = False
    question_label.config(bg="#f0f8ff")  # reset color
    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Finished", f"Your score: {score}/{len(questions)}")
        root.destroy()


# --- UI ---
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("600x400")
root.configure(bg="#f0f8ff")  # Light background

selected_option = tk.IntVar()
selected_option.set(-1)

answered = False

# Category selection
category_frame = tk.Frame(root, bg="#f0f8ff")
tk.Label(category_frame, text="Choose Quiz Category", font=("Arial", 18), bg="#f0f8ff").pack(pady=20)
tk.Button(category_frame, text="Core Python", width=20, command=lambda: start_quiz("Core Python")).pack(pady=10)
tk.Button(category_frame, text="Python Libraries", width=20, command=lambda: start_quiz("Python Libraries")).pack(pady=10)
category_frame.pack(pady=50)

# Quiz frame
quiz_frame = tk.Frame(root, bg="#f0f8ff")
question_label = tk.Label(quiz_frame, text="", font=("Arial", 14), wraplength=500, bg="#f0f8ff")
question_label.pack(pady=20)

selected_option = tk.IntVar()
options = []
for i in range(4):
    rb = tk.Radiobutton(quiz_frame, text="", variable=selected_option, value=i, font=("Arial", 12), bg="#f0f8ff")
    rb.pack(anchor="w", pady=2)
    options.append(rb)

next_btn = tk.Button(quiz_frame, text="Next", command=next_question, bg="#87ceeb", font=("Arial", 12))
next_btn.pack(pady=15)

question_counter = tk.Label(quiz_frame, text="", font=("Arial", 10), bg="#f0f8ff")
question_counter.pack()

root.mainloop()
