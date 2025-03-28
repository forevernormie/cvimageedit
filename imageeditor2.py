from tkinter import ttk, Tk, PhotoImage, Canvas, filedialog, colorchooser, RIDGE, GROOVE
from PIL import Image, ImageTk, ImageDraw, ImageEnhance, ImageFilter
import cv2
import numpy as np

class FrontEnd:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x700+250+10')
        self.master.title('Arcade Image Editor')
        self.master.config(bg='black')

        self.frame_header = ttk.Frame(self.master, style='Header.TFrame')
        self.frame_header.pack()

        ttk.Label(self.frame_header, text='Arcade Image Editor', style='Header.TLabel').grid(row=0, column=2, columnspan=1)
        ttk.Label(self.frame_header, text='An Image Editor Just For You!', style='SubHeader.TLabel').grid(row=1, column=1, columnspan=3)

        self.frame_menu = ttk.Frame(self.master, style='Menu.TFrame')
        self.frame_menu.pack(pady=20)
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))

        buttons = [
            ("Upload An Image", self.upload_action),
            ("Crop Image", self.crop_action),
            ("Add Text", self.text_action_1),
            ("Draw Over Image", self.draw_action),
            ("Apply Filters", self.filter_action),
            ("Blur/Smoothening", self.blur_action),
            ("Adjust Levels", self.adjust_action),
            ("Rotate", self.rotate_action),
            ("Flip", self.flip_action),
            ("Save As", self.save_action)
        ]

        for i, (text, command) in enumerate(buttons):
            ttk.Button(self.frame_menu, text=text, command=command, style='Arcade.TButton').grid(row=i, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        self.canvas = Canvas(self.frame_menu, bg="gray", width=400, height=400, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=3, rowspan=10, padx=10)

        self.apply_and_cancel = ttk.Frame(self.master, style='ApplyCancel.TFrame')
        self.apply_and_cancel.pack(pady=10)
        ttk.Button(self.apply_and_cancel, text="Apply", command=self.apply_action, style='Arcade.TButton').grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky='sw')
        ttk.Button(self.apply_and_cancel, text="Cancel", command=self.cancel_action, style='Arcade.TButton').grid(row=0, column=1, columnspan=1, padx=5, pady=5, sticky='sw')
        ttk.Button(self.apply_and_cancel, text="Revert All Changes", command=self.revert_action, style='Arcade.TButton').grid(row=0, column=2, columnspan=1, padx=5, pady=5, sticky='sw')

        self.image = None
        self.tk_image = None
        self.image_path = None

    def upload_action(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def crop_action(self):
        pass

    def text_action_1(self):
        pass

    def draw_action(self):
        pass

    def filter_action(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.display_image(self.image)

    def blur_action(self):
        self.image = self.image.filter(ImageFilter.GaussianBlur(5))
        self.display_image(self.image)

    def adjust_action(self):
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(1.5)
        self.display_image(self.image)

    def rotate_action(self):
        self.image = self.image.rotate(90, expand=True)
        self.display_image(self.image)

    def flip_action(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.display_image(self.image)

    def save_action(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.image.save(file_path)

    def apply_action(self):
        pass

    def cancel_action(self):
        pass

    def revert_action(self):
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.display_image(self.image)

    def display_image(self, image=None):
        if image:
            self.tk_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)

if __name__ == "__main__":
    root = Tk()

    # Style configuration for arcade look
    style = ttk.Style()
    style.configure('Header.TFrame', background='black')
    style.configure('Header.TLabel', background='black', foreground='lime', font=('Courier', 24, 'bold'))
    style.configure('SubHeader.TLabel', background='black', foreground='cyan', font=('Courier', 14, 'bold'))
    style.configure('Menu.TFrame', background='black')
    style.configure('Arcade.TButton', background='black', foreground='cyan', font=('Courier', 12, 'bold'), padding=10)
    style.configure('ApplyCancel.TFrame', background='black')

    app = FrontEnd(root)
    root.mainloop()
