"""  """
import tkinter as tk
from PIL import Image, ImageTk
import password
import random
import pickle
from pprint import pprint

# websites_data = {'example.com': {'abc@gmail.com': 'incorrect123',
#                                 'Guido': 'q1w2e3r4t5',
#                                 'somebody': 'topsecret',         
#                                 },
#                 'google.com': {'guido_van_rossum@python.org': 'letmein',
#                                'somebody': '123456789'
#                               },
#                }

def resize_img(img: Image, width, height) -> Image:
    """ resize img (PIL.Image) """
    img_width, img_height = img.size
    min_delta = min(width - img_width, height - img_height)
    img_width += min_delta
    img_height += min_delta
    img_resized = img.resize((img_width, img_height))
    return img_resized

def get_data_from_file(filename : str='data.pickle') -> dict:
    """ load data_base from file """
    try:
        with open(filename, 'rb') as datafile:
            data = pickle.load(datafile)
            return data
    except:
        print('something went wrong')
        return {}
    
def save_data_to_file(data_object: object, filename: str='data.pickle'):
    """ save object to file """
    with open(filename, 'wb') as datafile:
        pickle.dump(data_object, datafile, protocol=pickle.HIGHEST_PROTOCOL)
        print('data was saved')

class PasswordManager(tk.Tk):
    """ password dialog """
    def __init__(self) -> None:
        super().__init__()
        self.data_base = get_data_from_file()
        self.current_website = 'example.org'
        self.current_user = 'guido_van_rossum@python.org'
        self.current_password = 'letmein'
        self.title('Password Manager')
        self._width = 500
        self._height = 500        
        self.geometry(f'{self._width}x{self._height}+100+100')

        self.add_canvas()
        self.add_dialog()

    def add_canvas(self):
        """ add main canvas """
        self.canvas = tk.Canvas(master=self, bg="green")
        self.canvas.pack(fill='both', expand=True)
        self.add_canvas_bg_img()

    def add_canvas_bg_img(self):
        """add canvas bg img"""
        self.canvas.update()
        self.canvas.pil_bg_img = Image.open('safe_lock.png')
        img_resized = resize_img(self.canvas.pil_bg_img, self.canvas.winfo_width(), self.canvas.winfo_height())
        self.canvas.bg_photo_img = ImageTk.PhotoImage(img_resized)
        self.canvas.bg_image = self.canvas.create_image(0, 0, anchor='nw', image=self.canvas.bg_photo_img)
        self.canvas.bind("<Configure>", self.resizer_canvas_bg_img)

    def resizer_canvas_bg_img(self, event):
        """ resize canvas bg image """
        img_resized = resize_img(self.canvas.pil_bg_img, event.width, event.height)
        self.canvas.bg_photo_img = ImageTk.PhotoImage(img_resized)        
        self.canvas.itemconfig(self.canvas.bg_image, image=self.canvas.bg_photo_img)    

    def get_new_password(self):
        """ generate new password """
        self.current_password = password.generate_password(random.randint(10,15))
        self.password_field.delete(0, last='end')
        self.password_field.insert(0, self.current_password)

    def save_password(self):
        """ save current password """
        self.current_website = self.website_field.get()
        self.current_user = self.username_field.get()
        self.current_password = self.password_field.get()

        if password.is_correct(self.current_password):
            print('Saving current password:', self.current_password)
            website_users = self.data_base.setdefault(self.current_website, {})
            website_users[self.current_user] = self.current_password
            pprint(self.data_base)
            save_data_to_file(self.data_base)     
        else:
            print('Password:', self.current_password, 'is not correct. Try another')
            self.password_field.focus()

    def check_user_in_database(self):
        """ check if current user has password in data_base """
        self.password_field.delete(0, last='end')
        self.current_website = self.website_field.get()
        self.current_user = self.username_field.get()
        website_users = self.data_base.get(self.current_website, {})
        self.current_password = website_users.get(self.current_user, '')
        self.password_field.insert(0, self.current_password)
        if self.current_password:
            print(f'{self.current_user} has already registered on {self.current_website} with {self.current_password=}')

    def add_dialog(self):
        """ add dialog """
        frame_pady = 3
        bg_color = self.canvas.cget('background')
        font_color = 'white'
        x_pos = self._width // 2
        y_pos = self._height // 2
        self.dialog_frame = tk.Frame(master=self.canvas, borderwidth=1, bg=bg_color)
        # frame.pack()
        self.canvas.create_window(x_pos, y_pos, window=self.dialog_frame)

#-------------------------------------------------------------------
        self.website_label = tk.Label(master=self.dialog_frame, text='Website:', bg=bg_color, fg=font_color)
        self.website_label.grid(column=0, row=0, sticky='e', pady=frame_pady)
        self.website_field = tk.Entry(master=self.dialog_frame, width=30)
        self.website_field.insert(0, self.current_website)
        self.website_field.grid(column=1, row=0, pady=frame_pady)
#-------------------------------------------------------------------        
        self.username_label = tk.Label(master=self.dialog_frame, text='Email/Username:', bg=bg_color, fg=font_color)
        self.username_label.grid(column=0, row=1, sticky='e', pady=frame_pady)
        self.username_field = tk.Entry(master=self.dialog_frame, width=30)
        self.username_field.insert(0, self.current_user)
        self.username_field.grid(column=1, row=1, pady=frame_pady)
        self.check_btn = tk.Button(master=self.dialog_frame, text='Check', command=self.check_user_in_database)
        self.check_btn.grid(column=2, row=1, sticky='W', pady=frame_pady)
#-------------------------------------------------------------------    
        self.password_label = tk.Label(master=self.dialog_frame, text='Password:', bg=bg_color, fg=font_color)
        self.password_label.grid(column=0, row=2, sticky='e', pady=frame_pady)
        self.password_field = tk.Entry(master=self.dialog_frame, width=30)
        self.password_field.insert(0, self.current_password)
        self.password_field.grid(column=1, row=2, pady=frame_pady)
        self.btn_generate = tk.Button(master=self.dialog_frame, text='Generate', command=self.get_new_password)
        self.btn_generate.grid(column=2, row=2, pady=frame_pady)
#-------------------------------------------------------------------
        self.btn_save = tk.Button(master=self.dialog_frame, text='Save', command=self.save_password)
        self.btn_save.grid(column=1, row=3)



def main():
    """ main function """
    password_manager = PasswordManager()
    password_manager.mainloop()

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
