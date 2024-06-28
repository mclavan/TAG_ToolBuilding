'''

Basic Tools
mec_basicTools.py


How To Run:

import mec_basicTools
import importlib
importlib.reload(mec_basicTools)
mec_basicTools.gui()

'''


import maya.cmds as cmds

print('Basic Rigging Tools')

def gui():

	win_width = 300
	win_name = cmds.window()
	cmds.columnLayout()
	cmds.button(label='Button Example', w=win_width, c=press_me)

	cmds.showWindow(win_name)


def press_me(*args):
	print('Button has been pressed.')