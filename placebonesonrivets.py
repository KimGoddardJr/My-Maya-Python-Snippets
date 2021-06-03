import maya.cmds as cmds

rivet_group = cmds.ls('rivets', dag=1)
cmds.group( em=True,n='eyelash_joints' )

print(rivet_group)


for locator in rivet_group:
    if 'Shape' not in locator:
        print(locator)
        cmds.select(locator)
        locator_pos = cmds.xform(locator,q=1,ws=1,rp=1)
        cmds.select(clear=True)
        new_joint = cmds.joint(p=(locator_pos[0],locator_pos[1],locator_pos[2]))
        cmds.select(new_joint)
        cmds.parent( new_joint, 'eyelash_joints' )
        cmds.select(clear=True)
        cmds.parentConstraint(locator,new_joint , maintainOffset=True)
        
     
        #new_joint = cmds.joint(p=(0,0,0))
        #cmds.select(locator)
        #cmds.select(new_joint)f
        #cmds.parent(new_joint,locator,r=True)
        #cmds.select(new_joint)
