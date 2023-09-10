""" flash card from https://www.udemy.com/course/100-days-of-code/ """
import pickle
import random
import tkinter as tk
import tkinter.messagebox as msg
from collections import namedtuple
from pprint import pprint

Word = namedtuple('Word', ('Index', 'EN', 'RU', 'Count'))

def get_data_from_file(filename : str='data.pickle') -> dict:
    """ load data_base from file """
    try:
        with open(filename, 'rb') as datafile:
            data = pickle.load(datafile)
            return data
    except Exception as ex:
        # print('something went wrong')
        # print(ex)
        return [Word(0, 'word', 'слово', 0),]
    
def save_data_to_file(data_object: object, filename: str='data.pickle'):
    """ save object to file """
    with open(filename, 'wb') as datafile:
        pickle.dump(data_object, datafile, protocol=pickle.HIGHEST_PROTOCOL)
        # print('data was saved')

class Dialog(tk.Tk):
    """ main dialog """    
    def __init__(self) -> None:
        super().__init__()
        self.title('Flashy')
        self.geometry('800x500+100+100')
        self.configure(background = 'olive drab')

        self.data = get_data_from_file()
        self.max_yes_answers = 3
        self.current_word = self.get_next_word()

        self.add_widgets()

    @property
    def unknown_words(self):
        return [word for word in self.data if word.Count < self.max_yes_answers]

    def add_widgets(self):
        """ add canvas """
        for i in (0, 1, 2, 3, 4): self.grid_columnconfigure(i, weight=1)
        for i in (0, 1, 2, 3, 4): self.grid_rowconfigure(i, weight=1)

        self.english_label = tk.Label(master=self, text=self.current_word.EN, font=("Courier", 30))
        self.english_label.grid(row=1, column=1, columnspan=3, sticky='news')
        self.russian_label = tk.Label(master=self, text='', font=("Courier", 30))
        self.russian_label.grid(row=2, column=1, columnspan=3, sticky='news')

        self.no_btn_image = tk.PhotoImage(file="cross-mark-button.png").subsample(4, 4)
        self.no_btn = tk.Button(master=self, image=self.no_btn_image, 
                                 background='olive drab',
                                 activebackground='olive drab',
                                 bd=0,
                                 command=self.no_btn_pressed)
        # self.no_btn = tk.Button(master=self, bd=5, text='No', font=("Courier", 50), bg='red', command=self.no_btn_pressed)
        self.no_btn.grid(row=3, column=1)
        
        self.yes_btn_image = tk.PhotoImage(file="check-mark-button.png").subsample(4, 4)
        self.yes_btn = tk.Button(master=self, image=self.yes_btn_image, 
                                 background='olive drab',
                                 activebackground='olive drab',
                                 bd=0,
                                 command=self.yes_btn_pressed)
        # self.yes_btn = tk.Button(master=self, bd=5, text='Yes', font=("Courier", 50), bg='green', command=self.yes_btn_pressed)
        self.yes_btn.grid(row=3, column=3)

        self.next_btn = tk.Button(master=self, bd=5, text='Next', font=("Courier", 30), command=self.display_next_word)
        self.next_btn.grid(row=3, column=2)
        
    def get_next_word(self):
        """ get random word from words """
        if len(self.unknown_words) == 0:
            print('You have already studied all words. Reset ? ')
            answer = msg.showinfo(message='You have already studied all words. Dictionary will be reset')
            self.data = [Word(word.Index, word.EN, word.RU, 0) for word in self.data]
            save_data_to_file(self.data)
        return random.choice(self.unknown_words)

    def display_next_word(self):
        """ NEXT button pressed scenario """
        next_word = self.get_next_word() # select new word from database
        while next_word == self.current_word and len(self.unknown_words) > 1:
            next_word = self.get_next_word()
        self.current_word = next_word
        
        self.english_label.config(text=self.current_word.EN) # display source word
        self.russian_label.config(text='') # clean translation
        self.no_btn.config(state='normal')
        self.yes_btn.config(state='normal')

    def no_btn_pressed(self):
        """ NO button pressed scenario """
        self.current_word = Word(self.current_word.Index,
                                 self.current_word.EN,
                                 self.current_word.RU,
                                 max(0, self.current_word.Count-1))
        self.data[self.current_word.Index] = self.current_word
        save_data_to_file(self.data)

        self.russian_label.config(text=self.current_word.RU)
        self.no_btn.config(state='disabled')
        self.yes_btn.config(state='disabled')

    def yes_btn_pressed(self):
        """ YES button pressed scenario """
        self.current_word = Word(self.current_word.Index,
                                 self.current_word.EN,
                                 self.current_word.RU,
                                 self.current_word.Count+1)
        self.data[self.current_word.Index] = self.current_word
        save_data_to_file(self.data)
        
        self.russian_label.config(text=self.current_word.RU)
        # self.no_btn.config(state='disabled')
        self.yes_btn.config(state='disabled')

def main():
    """ main function """
    dialog = Dialog()
    dialog.mainloop()

if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
