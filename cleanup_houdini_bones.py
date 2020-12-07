import maya.cmds as cmds

# list all the joints from the scene
mjoints = cmds.ls(type='joint', l=True)
for joint in mjoints:
	if 'effector' in joint:
		cmds.delete(joint)