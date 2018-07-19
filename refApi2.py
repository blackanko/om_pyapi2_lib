import sys

import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as omanim
import maya.api.OpenMayaRender as omrender

'''
recursion function to search all child node

parameter:
    root: MFnDagNode
    meshList: output list

'''
def recursionGetMeshObj(root, meshList):
    childCount = root.childCount()
    if childCount == 0:
        if root.getPath().hasFn(om.MFn.kMesh):
            meshList.append(root)
    else:
        for i in range(childCount):
            childObj = root.child(i)
            childNode = om.MFnDagNode(childObj)
            recursionGetMeshObj(childNode, meshList)

'''
get all child mesh node from selected node

return:
    meshList: list(MFnDagNode)

'''
def getAllMeshNode():
    sel = om.MGlobal.getActiveSelectionList()
    if sel.isEmpty():
        return
    node = om.MFnDagNode(sel.getDependNode(0))
    meshList = []
    recursionGetMeshObj(node, meshList)
    return meshList

#getAllMeshNode()

'''
get selected mesh's all vertex info

parameter:
    mesh: MFnDagNode

return:
    vtxList: list -> {id: vtx_id, pos: vtx_postion}
    vtxIter: MItMsehVertex

'''
def getAllVertex(mesh):
    fnMesh = om.MFnMesh(mesh.getPath())
    vtxIter = om.MItMeshVertex(mesh.getPath())
    vtxList = []
    while not vtxIter.isDone():
        id = vtxIter.index()
        pos = vtxIter.position()
        vtxList.append({"id":id, "pos":pos})
        vtxIter.next()
    vtxIter.reset()
    return vtxList

#mesh = getAllMeshNode()[0]
#print getAllVertex(mesh)
