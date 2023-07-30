"""Better and more customizable menus for tkinter applications"""

__version__ = '0.1.0'
__author__ = 'billyeatcookies'
__version_info__ = tuple([ int(num) for num in __version__.split('.')])

__all__ = ["Menu", "Menubar"]

from .menu import Menu
from .menubar import Menubar
