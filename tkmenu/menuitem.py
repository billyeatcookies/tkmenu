import tkinter as tk


class MenuItem(tk.Menubutton):
    def __init__(self, master, text, command, bg, fg, font, padx=20, pady=2, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.command = command
        
        self.config(text=text, anchor=tk.W, font=font,
            padx=padx, pady=pady, bg=bg, fg=fg
        )
        self.bind("<Button-1>", self.onclick)
    
    def onclick(self, *_):
        self.master.hide()
        self.command()
