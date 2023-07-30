#TODO convert menu items to frames
#TODO checkbox items
#TODO optional icons

import tkinter as tk
from tkinter.font import Font

from .menuitem import MenuItem
from .separator import Separator
from .menubar import Menubar


class Menu(tk.Toplevel):
    """
    Better Menus for Tkinter

    Typical usage example:
        menu = Menu(button, )

    Attributes
    ----------
    master
        parent tkinter widget
    name : str
        menu id (required when using `tkmenu.Menubar`)
    bg : str
        background color of menu
    fg : str
        foreground color of menu
    border : str
        border color of menu 
    bd : int
        border width of menu (defaults to 1)
    font : str|tuple|Font
        font used in menu (Segoi UI by default)
    itempadx : int
        menu items horizontal padding from border (defaults to 20)
    itempady : int
        menu items vertical padding from border (defaults to 2)
    """
    def __init__(self, master, 
                 name: str=None, bg: str=None, fg: str=None, border: str=None, bd=1,
                 font: str|tuple|Font=("Segoe UI", 10), itempadx: int=20, itempady: int=2, 
                 *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.name = name
        self.bg = bg
        self.fg = fg
        self.border = border
        self.font = font
        self.itempadx = itempadx
        self.itempady = itempady

        self.active = False
        self.config(bg=border)
        self.withdraw()
        self.overrideredirect(True)

        self.container = tk.Frame(self, padx=5, pady=5)
        self.container.pack(fill=tk.BOTH, expand=True, padx=1, pady=1, bg=bg)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.hide = self.hide

        self.menu_items = []
        self.row = 0

        self._config_bindings()

    def add_item(self, text: str, callback: function=lambda *_:...) -> MenuItem:
        """Add a normal menu item to menu

        Parameters
        ----------
        text : str
            text shown in menu item
        callback : function
            the callback function when menu item is clicked
        
        Returns
        -------
        MenuItem
            the menu item instance added to menu
        """

        new_item = MenuItem(self.container, text, callback, self.bg, self.fg, self.font, self.itempadx, self.itempady)
        new_item.grid(row=self.row, sticky=tk.EW, pady=0)
        self.menu_items.append(new_item)

        self.row += 1
        return new_item

    def add_separator(self, length: int=18) -> None:
        """Add a separator to menu

        Parameters
        ----------
        length : int
            length of separator (defaults to 18)
        """

        new_sep = Separator(self.container, length)
        new_sep.grid(row=self.row, sticky=tk.EW, pady=0)
        self.menu_items.append(new_sep)

        self.row += 1
    
    def get_coords(self, e: object=None) -> tuple[int, int]:
        """Defines where the menu will appear when show() is called, to be overwritten if needs to be changed.
        `e.widget.winfo...` and `self.master.winfo...`, `self.winfo...` functions can be used to determine value.
        
        Parameters
        ----------
        event
            The mouse click event (only when show() is bound to mouse clicks)
        
        Returns
        -------
        tuple
            position as (x, y) tuple.
        """

        return self.master.winfo_rootx(), self.master.winfo_rooty() + self.master.winfo_height()

    def show(self, *e) -> None:
        """Show the menu. 
        If bound to mouse clicks, get_coords() can use the event to calculate the position. 
        """
        self.active = True
        self.update_idletasks()

        x, y = self.get_coords(*e)
        self.wm_geometry(f"+{x}+{y}")
        
        self.deiconify()
        self.focus_set()
    
    def hide(self, *args) -> None:        
        "Hide the menu"
        self.active = False
        self.withdraw()

    def _config_bindings(self) -> None:
        self.bind("<FocusOut>" , self.hide)
        self.bind("<Escape>", self.hide)
