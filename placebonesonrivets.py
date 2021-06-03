import maya.cmds as cmds

rivet_group = cmds.ls('rivets', dag=1)
print(rivet_group)

#TODO:Fix placing
for locator in rivet_group:
    if 'Shape' not in locator:
        print(locator)
        new_joint = cmds.joint(p=(0,0,0))
        cmds.select(locator)
        #cmds.select(new_joint)f
        cmds.parent(new_joint,locator,r=True)
        cmds.select(new_joint)