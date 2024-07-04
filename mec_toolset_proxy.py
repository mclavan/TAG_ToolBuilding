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

import maya.cmds as cmds
import maya.mel as mel 

win_width = 200


def gui():
    
    win_obj = cmds.window(w=win_width, h=300, title='Proxy Toolset')
    cmds.columnLayout()

    cmds.button(label='Rigging Vison', w=win_width, c=rigging_vision_toggle)

    cmds.rowColumnLayout(nc=2, cw=[[1,win_width/2], [2, win_width/2]])
    cmds.button(label='Joint On', c=joint_sel_on)
    cmds.button(label='Joint Off', c=joint_sel_off)
    cmds.button(label='Geometry On', c=geometry_sel_on)
    cmds.button(label='Gomeetry Off', c=geometry_sel_off)
    cmds.setParent('..')
    cmds.separator(h=5)

    cmds.rowColumnLayout(nc=2, cw=[[1,win_width/2], [2, win_width/2]])
    cmds.button(label='Detach', w=win_width/2, c=detach_poly)
    cmds.button(label='Separate', w=win_width/2, c=separate_poly)
    cmds.setParent('..')
    cmds.button(label="Full Separate", w=win_width, c=poly_separate_full)
    cmds.separator(h=5)
    
    cmds.button(label='MultiCUT', w=win_width, c=multicut_tool)
    cmds.button(label='Extract', w=win_width, c=extract_face)
    cmds.button(label='Duplicate', w=win_width, c=duplicate_face)
    cmds.button(label='Combine', w=win_width, c=combine_poly)

    cmds.separator(h=5)
    cmds.rowColumnLayout(nc=3, cw=[[1, win_width/3],[2, win_width/3], [3, win_width/3]])
    cmds.button(label='Freeze', c=freeze_transforms)
    cmds.button(label='History', c=delete_history)
    cmds.button(label='Center', c=center_pivot)
    cmds.button(label='NUKE', w=win_width, c=nuke)
    cmds.setParent('..')
    cmds.separator(h=5)

    cmds.button(label='Rename Proxy', w=win_width, c=rename_proxy, ann='Select the joint then the proxy geometry.')
    cmds.button(label='Rename & Constrain', w=win_width, c=rename_and_constrain)

    cmds.separator(h=5)
    cmds.button(label='**Rename & Bind', w=win_width, c=rename_and_bind)
    cmds.button(label='**Remove Bind', w=win_width)
    cmds.button(label='**Remove Constraint', w=win_width)
    cmds.showWindow(win_obj)
    


def detach_poly(*args):
    '''
    mel_line = ''
    mel.eval(mel_line)
    '''
    mel_line = 'DetachComponent()'
    mel.eval(mel_line)

def separate_poly(*args):
    # pm.mel.SeparatePolygon()
    mel_line = 'SeparatePolygon'
    mel.eval(mel_line)


def combine_poly(*args):
    # pm.mel.CombinePolygons()
    mel_line = 'CombinePolygons'
    mel.eval(mel_line)

def duplicate_face(*args):
    # pm.mel.DuplicateFace()
    mel_line = 'DuplicateFace'
    mel.eval(mel_line)

def extract_face(*args):
    # pm.mel.ExtractFace()
    mel_line = 'ExtractFace'
    mel.eval(mel_line)
    
def poly_separate_full(*args):
    # pm.mel.DetachComponent()
    # pm.mel.toggleSelMode()
    # pm.mel.eval('selectMode -object;')
    # pm.mel.SeparatePolygon()

    mel.eval('DetachComponent')
    mel.eval('toggleSelMode')
    cmds.selectMode(object=True)
    # mel.eval('selectMode -object;')
    mel.eval('SeparatePolygon')


def multicut_tool(*args):
    mel.eval('MultiCutTool')

def delete_history(*args):
    cmds.delete(ch=True)

def freeze_transforms(*args):
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

def center_pivot(*args):
    cmds.xform(cpc=True)

def nuke(*args):
    delete_history()
    freeze_transforms()
    center_pivot()

# setObjectPickMask "Joint" true;
# setObjectPickMask "Surface" true; # Geometry

def joint_sel_on(*args):
    mel.eval('setObjectPickMask "Joint" true;')

def joint_sel_off(*args):
    mel.eval('setObjectPickMask "Joint" false;')

def geometry_sel_on(*args):
    mel.eval('setObjectPickMask "Surface" true;')

def geometry_sel_off(*args):
    mel.eval('setObjectPickMask "Surface" false;')

toggle_state = False
def rigging_vision_toggle(*args):
    global toggle_state

    panel_cameras = ['modelPanel1', 'modelPanel2', 'modelPanel3', 'modelPanel4']

    for current_camera in panel_cameras:
        cmds.modelEditor(current_camera, e=True, jointXray=toggle_state)
        cmds.modelEditor(current_camera, e=True, wireframeOnShaded=toggle_state)

    if(toggle_state):
        toggle_state = False
    else:
        toggle_state = True

def rename_proxy(*args):
    joint, proxy_piece = cmds.ls(sl=True)

    new_name = joint.replace('_bind', '_proxy')
    cmds.rename(proxy_piece, new_name)
    # proxy_piece.rename(new_name)

    cmds.select(proxy_piece, r=True)

def rename_and_constrain(*args):
    cmds.parentConstraint(mo=1)
    rename_proxy()

def rename_and_bind(*args):
    pass

# import maya.cmds as cmds
# wire_toggle_state = False
# joint_toggle_state = False
# def rigging_joint_toggle():
#     global joint_toggle_state

#     panel_cameras = ['modelPanel1', 'modelPanel2', 'modelPanel3', 'modelPanel4']

#     for current_camera in panel_cameras:
#         cmds.modelEditor(current_camera, e=True, jointXray=joint_toggle_state)

#     if(joint_toggle_state):
#         joint_toggle_state = False
#     else:
#         joint_toggle_state = True

# def rigging_wire_toggle():
#     global wire_toggle_state

#     panel_cameras = ['modelPanel1', 'modelPanel2', 'modelPanel3', 'modelPanel4']

#     for current_camera in panel_cameras:
#         cmds.modelEditor(current_camera, e=True, wireframeOnShaded=wire_toggle_state)

#     if(wire_toggle_state):
#         wire_toggle_state = False
#     else:
#         wire_toggle_state = True

    