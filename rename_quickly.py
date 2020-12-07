import pymel.core as pm
import maya.cmds as cmds

sel=pm.ls(selection=True)

for each in all_joints:
    newname=each.nodeName().replace(":", "_")
    each.rename(newname)