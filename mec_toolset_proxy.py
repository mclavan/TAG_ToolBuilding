'''
Rigging Toolset - Proxy
mecProxy.py

Description:

How to run:


import mecProxy
import importlib
importlib.reload(mecProxy)
mecProxy.gui()

'''

print('Rigging Toolset Active')

import pymel.core as pm 

win_width = 200

def gui():

    win_obj = pm.window(w=win_width, h=300, title='Proxy Toolset')
    pm.columnLayout()
    pm.button(label='Rigging Vison', w=win_width, c=rigging_vision_toggle)

    pm.rowColumnLayout(nc=2, cw=[[1,win_width/2], [2, win_width/2]])
    pm.button(label='Joint On', c=joint_sel_on)
    pm.button(label='Joint Off', c=joint_sel_off)
    pm.button(label='Geometry On', c=geometry_sel_on)
    pm.button(label='Gomeetry Off', c=geometry_sel_off)
    pm.setParent('..')
    pm.separator(h=5)

    pm.rowColumnLayout(nc=2, cw=[[1,win_width/2], [2, win_width/2]])
    pm.button(label='Detach', w=win_width/2, c=detach_poly)
    pm.button(label='Separate', w=win_width/2, c=separate_poly)
    pm.setParent('..')
    pm.button(label="Full Separate", w=win_width, c=poly_separate_full)
    pm.separator(h=5)

    pm.button(label='MultiCUT', w=win_width, c=multicut_tool)
    pm.button(label='Extract', w=win_width, c=extract_face)
    pm.button(label='Duplicate', w=win_width, c=duplicate_face)
    pm.button(label='Combine', w=win_width, c=combine_poly)

    pm.separator(h=5)
    pm.rowColumnLayout(nc=3, cw=[[1, win_width/3],[2, win_width/3], [3, win_width/3]])
    pm.button(label='Freeze', c=freeze_transforms)
    pm.button(label='History', c=delete_history)
    pm.button(label='Center', c=center_pivot)
    pm.button(label='NUKE', w=win_width, c=nuke)
    pm.setParent('..')
    pm.separator(h=5)

    pm.button(label='Rename Proxy', w=win_width, c=rename_proxy, ann='Select the joint then the proxy geometry.')
    pm.button(label='Rename & Constrain', w=win_width, c=rename_and_constrain)
    pm.button(label='**Rename & Bind', w=win_width, c=rename_and_bind)

    pm.separator(h=5)
    pm.button(label='**Remove Bind', w=win_width)
    pm.button(label='**Remove Constraint', w=win_width)
    win_obj.show()

def detach_poly(*args):
    pm.mel.DetachComponent()

def separate_poly(*args):
    pm.mel.SeparatePolygon()

def combine_poly(*args):
    pm.mel.CombinePolygons()

def duplicate_face(*args):
    pm.mel.DuplicateFace()

def extract_face(*args):
    pm.mel.ExtractFace()

def poly_separate_full(*args):
    pm.mel.DetachComponent()
    pm.mel.toggleSelMode()
    pm.mel.eval('selectMode -object;')
    pm.mel.SeparatePolygon()

def multicut_tool(*args):
    pm.mel.MultiCutTool()

def delete_history(*args):
    pm.delete(ch=True)

def freeze_transforms(*args):
    pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

def center_pivot(*args):
    pm.xform(cpc=True)

def nuke(*args):
    delete_history()
    freeze_transforms()
    center_pivot()

# setObjectPickMask "Joint" true;
# setObjectPickMask "Surface" true; # Geometry

def joint_sel_on(*args):
    pm.mel.eval('setObjectPickMask "Joint" true;')

def joint_sel_off(*args):
    pm.mel.eval('setObjectPickMask "Joint" false;')

def geometry_sel_on(*args):
    pm.mel.eval('setObjectPickMask "Surface" true;')

def geometry_sel_off(*args):
    pm.mel.eval('setObjectPickMask "Surface" false;')

toggle_state = False
def rigging_vision_toggle(*args):
    global toggle_state

    panel_cameras = ['modelPanel1', 'modelPanel2', 'modelPanel3', 'modelPanel4']

    for current_camera in panel_cameras:
        pm.modelEditor(current_camera, e=True, jointXray=toggle_state)
        pm.modelEditor(current_camera, e=True, wireframeOnShaded=toggle_state)

    if(toggle_state):
        toggle_state = False
    else:
        toggle_state = True

def rename_proxy(*args):
    joint, proxy_piece = pm.ls(sl=True)

    new_name = joint.replace('_bind', '_proxy')
    proxy_piece.rename(new_name)

    pm.select(proxy_piece, r=True)

def rename_and_constrain(*args):
    pm.parentConstraint(mo=1)
    rename_proxy()

def rename_and_bind(*args):
    pass

import maya.cmds as cmds
wire_toggle_state = False
joint_toggle_state = False
def rigging_joint_toggle():
    global joint_toggle_state

    panel_cameras = ['modelPanel1', 'modelPanel2', 'modelPanel3', 'modelPanel4']

    for current_camera in panel_cameras:
        cmds.modelEditor(current_camera, e=True, jointXray=joint_toggle_state)

    if(joint_toggle_state):
        joint_toggle_state = False
    else:
        joint_toggle_state = True

def rigging_wire_toggle():
    global wire_toggle_state

    panel_cameras = ['modelPanel1', 'modelPanel2', 'modelPanel3', 'modelPanel4']

    for current_camera in panel_cameras:
        cmds.modelEditor(current_camera, e=True, wireframeOnShaded=wire_toggle_state)

    if(wire_toggle_state):
        wire_toggle_state = False
    else:
        wire_toggle_state = True