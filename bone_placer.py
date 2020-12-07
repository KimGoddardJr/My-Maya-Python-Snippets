
import maya.cmds as cmds
import pymel.core as pm
import re
import json

cur_file_dir = cmds.workspace( q=True, dir=True )

json_name ='sl_vertex.json'

json_template = os.path.join(cur_file_dir,json_name)

with open('{}'.format(json_template)) as template_file:
    template = json.load(template_file)

type(template)

cmds.selectPref(tso = True)
obj = cmds.ls(sl=True, fl=True)[0]
vertices = cmds.ls(obj+'.vtx[*]', fl=True)

ids = [re.findall(r"[\w]+", i)[-1] for i in vertices]

mjoints = [b for b in cmds.ls(type='joint', l=True) if 'boner_' in b]

joint_vertices = []

for v in vertices:
    for index in template:
        if v.split('.')[-1] in index:
            joint_vertices.append(v)

for j in mjoints:
    bone_name = j.split('|')[-1]
    for jv in joint_vertices:
        jv_id = re.findall(r"[\w]+", jv)[-1]
        if bone_name.split('_')[-1] == jv_id:             
            cmds.xform(j, ws=True, t=cmds.xform(jv, q=True, ws=True, t=True))