"""  https://www.udemy.com/course/100-days-of-code/ """
import html
import os
import sys
import tkinter as tk
import tkinter.messagebox as msg
from pprint import pprint

# from quiz_data import questions as quiz_questions
import quiz_data


class Quiz(tk.Tk):
    """ dialog class """
    def __init__(self, questions: dict) -> None:
        super().__init__()
        self.title('Quiz')
        self.width = 450
        self.height = 250        
        self.geometry(f'{self.width}x{self.height}+500+500')
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.config(background='green')
        self.config(padx=10, pady=10)
        self.questions = questions
        self.score = 0
        self.maxscore = len(self.questions)
        self.current_question = self.get_next_question()
        self.answer = None
        self.show_question()
        self.add_answer_frame()
        self.show_answer_dialog()

    def add_answer_frame(self):
        self.answer_frame = tk.Frame(master=self)
        self.answer_frame.grid(row=2, column=0, sticky='ew')

    def get_next_question(self):
        """ get question from questions """
        if len(self.questions) == 0:
            # print('You have already answered all question. Reset ? ')
            answer = msg.showinfo(message=f'You have already answered all question. Your score is {self.score}/{self.maxscore}')
            self.destroy()
            sys.exit()
        else:    
            return self.questions.pop()

    def show_question(self):
        self.question_title = tk.Label(master=self, text=f'Question from category "{self.current_question.category}":')
        self.question_title.grid(row=0, column=0, sticky='ew')

        self.question_text = tk.Label(master=self, text=html.unescape(self.current_question.question), wraplength=350)
        self.question_text.grid(row=1, column=0, sticky='ew')

    def show_answer_dialog(self):

        def get_answer_index():
            selected_index = self.answer_index.get()
            self.answer = answers[selected_index]
            # print(self.answer)

        def submit_answer():
            if self.answer == self.current_question.correct_answer:
                print('answer is correct')
                self.score += 1
            else:
                print('answer is NOT correct')

            self.current_question = self.get_next_question()
            self.question_title.destroy()
            self.question_text.destroy()            
            self.show_question()
            self.show_answer_dialog()            

        self.answer_frame.destroy()
        self.add_answer_frame()
        # self.answer_frame.configure(background='green')

        if self.current_question.type == 'multiple':
            answers = self.current_question.incorrect_answers + [self.current_question.correct_answer,]
        if self.current_question.type == 'boolean':
            answers = ['True', 'False']
        print(answers)

        self.update()
        width, height, posx, posy = map(int, self.geometry().replace('+', ' ').replace('x', ' ').split())
        new_height = 110 + len(answers) * 40
        self.geometry(f'{width}x{new_height}+{posx}+{posy}')

        for i in (0,1,2): self.answer_frame.grid_columnconfigure(i, weight=1)
        self.multiple_choice_frame = tk.Frame(master=self.answer_frame)
        self.multiple_choice_frame.grid(row=0, column=1, sticky='ew')
        
        self.answer_index = tk.IntVar(master=self.multiple_choice_frame)
        self.answer_index.set(0)            
        for indx, answer in enumerate(answers):
            tk.Radiobutton(master=self.multiple_choice_frame,
                        text=html.unescape(answer),
                        value=indx,
                        variable=self.answer_index,
                        command=get_answer_index).grid(row=indx+1, column=1, sticky='w')
        
        self.submit_btn = tk.Button(master=self.answer_frame, text='Submit', command=submit_answer)
        self.submit_btn.grid(row=1, column=1)

def main():
    """ main function """
    quiz_questions = quiz_data.get_quiz_data()
    pprint(quiz_questions)
    quiz = Quiz(quiz_questions)
    quiz.mainloop()

if __name__ == "__main__":
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
