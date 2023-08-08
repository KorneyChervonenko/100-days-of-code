"""  https://en.wikipedia.org/wiki/Pomodoro_Technique from https://www.udemy.com/course/100-days-of-code/  """
import tkinter as tk
import datetime

class Clock(tk.Tk):
    """ on screen clock """
    def __init__(self) -> None:
        super().__init__()
        self.counter_max = 1500
        self.counter = self.counter_max
        self.is_activated = True
        self._width = 800
        self._height = 800
        self.title('Pomodoro')
        self.geometry(f'{self._width}x{self._height}+100+100')
        self.canvas = tk.Canvas(master=self, bg="green", width=self._width, height=self._height)
        self.canvas.pack()
        self.photo_image = tk.PhotoImage(file='tomato.png')
        self.canvas.create_image(self._width//2, self._height//2, image=self.photo_image)
        self.center_text = self.canvas.create_text(self._width//2, self._height//2,
                                                   text = self.seconds2time(self.counter),
                                                   font=('Courier New', 24, 'bold'),
                                                   fill='SpringGreen')
        self.add_ctrl_buttons()

    def add_ctrl_buttons(self):
        """ add ctrl buttons """
        x_pos = self._width // 2
        y_pos = self._height - 50
        self.frame = tk.Frame(master=self, borderwidth=1, bg='gray')
        # frame.pack()
        self.canvas.create_window(x_pos, y_pos, window=self.frame)

        quit_btn = tk.Button(master=self.frame, text='Quit', command=self.destroy)
        quit_btn.grid(column=2,row=0)

        reset_btn = tk.Button(master=self.frame, text='Reset', command=self.reset)
        reset_btn.grid(column=1, row=0)

        start_btn = tk.Button(master=self.frame, text='Start', command=self.activate)
        start_btn.grid(column=0, row=0)

    def print_center_text(self, message: str):
        """" print some text in center of the window """
        self.canvas.itemconfigure(self.center_text, text=message)

    def update_counter(self):
        """ update timer """
        if self.counter == 0:
            self.reset()
        if self.is_activated:
            self.counter -= 1
            self.print_center_text(self.seconds2time(self.counter))
            self.after(1000, self.update_counter)

    def activate(self):
        """ activate counter """
        self.canvas.configure(bg = 'green')
        self.is_activated = True
        self.update_counter()

    def reset(self):
        """ reset counter """
        self.canvas.configure(bg = 'red')
        self.is_activated = False
        self.counter = self.counter_max
        self.print_center_text(self.seconds2time(self.counter))

    @staticmethod
    def seconds2time(counter: int) -> str:
        """ convert seconds to time string """
        return str(datetime.timedelta(seconds=counter))

def main():
    """ main function """
    clock = Clock()
    clock.mainloop()

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
