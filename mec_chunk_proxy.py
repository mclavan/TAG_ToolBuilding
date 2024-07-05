'''

Basic Tools
mec_basicTools.py


How To Run:

import mec_chunk_proxy.py
import importlib
importlib.reload(mec_chunk_proxy.py)
mec_chunk_proxy.py.gui()

'''


import maya.cmds as cmds

print('Basic Rigging Tools')

def gui():

	win_width = 300
	win_name = cmds.window()
	cmds.columnLayout()
	cmds.button(label='Detach', w=win_width, c=detach_poly)
	cmds.button(label='Separate', w=win_width, c=separate_poly)


	cmds.showWindow(win_name)


def press_me(*args):
	print('Button has been pressed.')

def detach_poly(*args):
	print('Button has been pressed.')

def separate_poly(*args):
	print('Button has been pressed.')