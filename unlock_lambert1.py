import maya.cmds as cmds
import maya.OpenMaya as om

_INITIAL_SHADERS = ['initialShadingGroup', 'initialParticleSE', 'lambert1']


def iterLockedInitialShaders():
    nodes = cmds.ls(_INITIAL_SHADERS, r=True)
    if nodes:
        for node in nodes:
            locked = cmds.lockNode(node, q=True, lu=True)
            if locked[0]:
                yield node


def unLockInitialShaders():
    for node in iterLockedInitialShaders():
        print('unlock node -> "{}"'.format(node))
        cmds.lockNode(node, l=False, lu=False)


def beforeSaveCallback():
    # Unlock Lambert1 before SceneSaved
    om.MSceneMessage.addCallback(om.MSceneMessage.kBeforeSave, unLockInitialShaders)


