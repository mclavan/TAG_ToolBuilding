'''

Building Hierarchies
mec_hierarchy.py


How To Run:

import hierarchy
import importlib
importlib.reload(mec_hierarchy)
mec_hierarchy.create_hiearchy()

'''

import maya.cmds as cmds

print('Hierarchy Tool Active.')

def create_hiearchy():

	print('Hierarchy Created')

	# Get three selected joints.
	selected = cmds.ls(sl=True)

	print('Currently Selected: ', selected)


	for current_joint in selected:
		# Name system
		local_pad_name = current_joint.replace('_bind', '_local')
		icon_name = current_joint.replace('_bind', '_icon')

		# Create first control system
		# Create the control and group
		# Create nurbs circle
		# circle -c 0 0 0 -nr 1 0 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; 
		icon = cmds.circle(nr=[1, 0, 0], radius=.6, ch=False, name=icon_name)[0]

		# Group created nurbs circle
		# group -empty;
		local_pad = cmds.group(name=local_pad_name)
		print('First Group: ', local_pad, ' -- First Icon Created:', icon)

		# Move pad and control system over to the target joint.
		# Which we got in the previous section through selected.
		# constraint method
		# parentConstraint -weight 1;
		kenny = cmds.parentConstraint(current_joint, local_pad, weight=1)
		cmds.delete(kenny)


def create_parent_hiearchy():

	print('Hierarchy Created')

	# Get three selected joints.
	selected = cmds.ls(sl=True)

	print('Currently Selected: ', selected)

	previous_parent = None

	for current_joint in selected:
		# Name system
		local_pad_name = current_joint.replace('_bind', '_local')
		icon_name = current_joint.replace('_bind', '_icon')

		# Create first control system
		# Create the control and group
		# Create nurbs circle
		# circle -c 0 0 0 -nr 1 0 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; 
		icon = cmds.circle(nr=[1, 0, 0], radius=.6, ch=False, name=icon_name)[0]

		# Group created nurbs circle
		# group -empty;
		local_pad = cmds.group(name=local_pad_name)
		print('First Group: ', local_pad, ' -- First Icon Created:', icon)

		# Move pad and control system over to the target joint.
		# Which we got in the previous section through selected.
		# constraint method
		# parentConstraint -weight 1;
		kenny = cmds.parentConstraint(current_joint, local_pad, weight=1)
		cmds.delete(kenny)

		if(previous_parent):
			cmds.parent(local_pad, previous_parent)

		previous_parent = icon

