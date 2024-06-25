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

def gui():

	win_width = 300
	win_name = cmds.window()
	cmds.columnLayout()
	cmds.button(label='Create Hierarchy', w=win_width, command=create_controls_on_selected)
	cmds.rowColumnLayout(nc=2, cw=[[1, win_width * .75], [2, win_width * .25]])
	cmds.button(w=win_width * .75, label='Create Controls', c=create_controls_on_selected)
	cmds.button(w=win_width * .25, label='Next', command=finish_system)
	cmds.showWindow(win_name)


def create_controls_on_selected(*args):
	global arm_system, selected_joints
	# Get three selected joints.
	selected_joints = cmds.ls(sl=True, dag=True)

	print('Currently Selected: ', selected_joints)


	arm_system = create_local_icon(selected_joints[0:-1])
	print('Created:', arm_system)



def finish_system(*args):
	print('System Finished.')
	# [0][0]
	# # Result: [['rt_arm_01_local', 'rt_arm_01_icon'], ['rt_arm_02_local', 'rt_arm_02_icon']]
	
	previous_parent = None
	
	for current_system in arm_system:
		pad = current_system[0]
		icon = current_system[1]
		print('pad: ', pad, ' - Icon:', icon)
		cmds.makeIdentity(icon, apply=True, t=1, r=1, s=1, n=0, pn=1)
		cmds.matchTransform(icon, pad, pos=False, rot=False, scl=False, piv=True)

		if(previous_parent):
			cmds.parent(pad, previous_parent)

		previous_parent = icon


	# icon = arm_system[1][1]
	# cmds.makeIdentity(icon, apply=True, t=1, r=1, s=1, n=0, pn=1)


	# cmds.matchTransform(icon, where_to_go, pivot=True)
	# cmds.matchTransform(control, target_object, pivot=True)	

def create_local_icon(joints):

	# [['local_pad_1', 'icon_1'], ['local_pad_2', 'icon_2']]
	control_systems = []

	for current_joint in joints:

		# Name system
		local_pad_name = current_joint.replace('_bind', '_local')
		icon_name = current_joint.replace('_bind', '_icon')

		# Create first control system
		# Create the control and group
		# Create nurbs circle
		# circle -c 0 0 0 -nr 1 0 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; 
		icon = cmds.circle(nr=[1, 0, 0], radius=3, ch=False, name=icon_name)[0]

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

		# ['local_pad', 'icon']
		control_system = [local_pad, icon]
		control_systems.append(control_system)

	return control_systems


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


def create_parent_hiearchy(*args):

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

