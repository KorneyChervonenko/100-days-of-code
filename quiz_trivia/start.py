""" Trivia Question API Challenge https://www.udemy.com/course/100-days-of-code/ """
import tkinter as tk

import requests

import quiz
import quiz_data

# from pprint import pprint

def get_categories() -> dict:
    """ return dict with categories """
    response = requests.get(url='https://opentdb.com/api_category.php')
    response.raise_for_status()
    data = response.json().get('trivia_categories')
    data = sorted(data, key=lambda category: category['name'])
    categories = {'Any Category' : 999}
    categories.update({category['name']: category['id'] for category in data})
    return categories

class RequestCreator(tk.Tk):
    """ dialog class """
    def __init__(self) -> None:
        super().__init__()
        self.title('Quiz setter')
        self.width = 350
        self.height = 550        
        self.geometry(f'{self.width}x{self.height}+100+100')
        self.config(background='green')
        # self.grid_columnconfigure(0, weight=1)
        self.config(padx=10, pady=10)
        self.categories = get_categories()
        self.add_num_of_questions_dialog()
        self.add_category_dialog()
        self.add_difficulty_dialog()
        self.add_type_dialog()
        self.add_start_button()

    def add_num_of_questions_dialog(self):
        """ add num of questions dialog """

        def update_num_of_questions(value):
            """ get num_of_questions from num_of_questions_scale and store it in self.num_of_questions """
            self.num_of_questions = value
            print(self.num_of_questions)

        self.num_of_questions_frame = tk.Frame(master=self)
        self.num_of_questions_frame.config(highlightthickness=1, highlightbackground = 'gray')
        self.num_of_questions_frame.grid_columnconfigure(0, weight=1)
        self.num_of_questions_frame.grid(column=0, row=0, sticky='ew')
        # self.num_of_questions_frame.pack(expand=True, fill=tk.X)

        self.num_of_questions = 10
        self.num_of_questions_label = tk.Label(master=self.num_of_questions_frame, text='Number of Questions')
        self.num_of_questions_label.grid(column=0, row=0, sticky='ew')
        # self.num_of_questions_label.pack(expand=True, fill=tk.X)
        self.num_of_questions_scale = tk.Scale(master=self.num_of_questions_frame,
                                               from_=1, to=50,
                                               orient='horizontal',
                                               command=update_num_of_questions)
        self.num_of_questions_scale.set(self.num_of_questions)
        self.num_of_questions_scale.grid(column=0, row=1, sticky='ew')
        # self.num_of_questions_scale.pack(expand=True, fill=tk.X)

    def add_category_dialog(self):
        """ select category """

        def update_category(event):
            """ get current selection from listbox """
            selected_category_index = self.categories_listbox.curselection()
            selected_category = self.categories_listbox.get(selected_category_index)
            self.category = selected_category
            print(self.category)

        self.category = 'Any Category'

        self.categories_frame = tk.Frame(master=self)
        self.categories_frame.config(highlightthickness=1, highlightbackground = 'gray')
        self.categories_frame.grid_columnconfigure(0, weight=1)
        self.categories_frame.grid(column=0, row=1, sticky='ew')
        # self.categories_frame.pack(expand=True, fill=tk.X)

        self.categories_label = tk.Label(master=self.categories_frame, text='Category')
        self.categories_label.grid(column=0, row=0)

        self.categories_listbox = tk.Listbox(master=self.categories_frame, height=4, width=38, exportselection=False)
        self.categories_listbox.grid(column=0, row=1)
        for name, id in self.categories.items():
            self.categories_listbox.insert(id, name)
        self.categories_listbox.bind("<<ListboxSelect>>", update_category)

        self.categories_scrollbar = tk.Scrollbar(master=self.categories_frame, orient='vertical')
        self.categories_scrollbar.grid(column=1, row=1, sticky='ns')

        self.categories_listbox.config(yscrollcommand=self.categories_scrollbar.set)
        self.categories_scrollbar.config(command=self.categories_listbox.yview)

    def add_difficulty_dialog(self):
        """ select difficulty """

        def get_difficulty_value():
            """ get difficulty from difficulty_state and store it in difficulty_level """
            selected_index = self.difficulty_state.get()
            self.difficulty_level = levels[selected_index]
            # print(self.difficulty_state.get())
            print(self.difficulty_level)

        
        self.levels_frame = tk.Frame(master=self)
        self.levels_frame.config(highlightthickness=1, highlightbackground = 'gray')
        self.levels_frame.grid_columnconfigure(0, weight=1)
        self.levels_frame.grid(column=0, row=2, sticky='ew')
        # self.levels_frame.pack(expand=True, fill=tk.X)

        self.difficulty_level = 'Any Difficulty'
        levels = (self.difficulty_level, 'Easy', 'Medium', 'Hard')
        self.difficulty_state = tk.IntVar(master=self.levels_frame)
        self.difficulty_state.set(0)

        self.difficulty_label = tk.Label(master=self.levels_frame, text='Difficulty')
        self.difficulty_label.grid(column=0, row=0)

        for indx, level in enumerate(levels):
            tk.Radiobutton(master=self.levels_frame,
                           text=level,
                           value=indx,
                           variable=self.difficulty_state,
                           command=get_difficulty_value).grid(column=0, row=indx+1, sticky='w')

    def add_type_dialog(self):
        """ select type """

        def get_type_value():
            """ get type  """
            selected_index = self.type_state.get()
            self.quiz_type = types[selected_index]
            print(self.quiz_type)

        
        self.type_frame = tk.Frame(master=self)
        self.type_frame.config(highlightthickness=1, highlightbackground = 'gray')
        self.type_frame.grid_columnconfigure(0, weight=1)
        self.type_frame.grid(column=0, row=3, sticky='ew')
        # self.type_frame.pack(expand=True, fill=tk.X)

        self.type_label = tk.Label(master=self.type_frame, text='Type')
        self.type_label.grid(column=0, row=0)        

        self.quiz_type = 'Any Type'
        types = (self.quiz_type, 'Multiple Choice', 'True\False',)
        self.type_state = tk.IntVar(master=self.type_frame)
        self.type_state.set(0)

        for indx, quiz_type in enumerate(types):
            tk.Radiobutton(master=self.type_frame,
                           text=quiz_type,
                           value=indx,
                           variable=self.type_state,
                           command=get_type_value).grid(column=0, row=indx+1, sticky='w')

    def add_start_button(self):
        def create_api_link():
            link = 'https://opentdb.com/api.php?'
            link += f'amount={self.num_of_questions}'
            if self.category != 'Any Category':
                category_index = self.categories.get(self.category)
                link += f'&category={category_index}'
                print(self.category, category_index)
            if self.difficulty_level != 'Any Difficulty':
                link += f'&difficulty={self.difficulty_level.lower()}'
            if self.quiz_type != 'Any Type':
                quiz_type  = {'Multiple Choice': 'multiple', 'True\False': 'boolean'}.get(self.quiz_type)
                link += f'&type={quiz_type}'
            print(link)

            quiz_questions = quiz_data.get_quiz_data(link)
            quiz_dialog = quiz.Quiz(quiz_questions)
            quiz_dialog.mainloop()


        self.start_btn = tk.Button(master=self, text='Start quiz', command=create_api_link)
        self.start_btn.grid(column=0, row=4)
        self.grid_rowconfigure(4, weight=1)

def main():
    """ main function """
    dialog = RequestCreator()
    dialog.mainloop()

if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
