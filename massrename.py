import maya.cmds as cmds

rig = cmds.ls('RIG', dag=1)


for joint in rig:
    cmds.select(joint)
    new_name = joint.replace('pasted__','')
    cmds.rename(new_name)
    cmds.select(clear=True)