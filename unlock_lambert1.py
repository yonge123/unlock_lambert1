# !/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.OpenMaya as om
import locale

_LOCALE, _ = locale.getdefaultlocale()

if _LOCALE == 'ko_KR':
    _UNLOCK_MSG = u" lambert1 이 lock 되어있는 문제를 수정하였습니다.\n 수정한 scene 을 저장하십시오."
else:
    _UNLOCK_MSG = u' The lambert1 locking issue has been solving.\n Save the scene file, please.'

_INITIAL_SHADERS = ['initialShadingGroup', 'initialParticleSE', 'lambert1']


def iterLockedInitialShaders():
    nodes = cmds.ls(_INITIAL_SHADERS, r=True)
    if nodes:
        for node in nodes:
            locked = cmds.lockNode(node, q=True, lu=True)
            if locked[0]:
                yield node


def unLockInitialShaders(*args):
    lockShaders = list(iterLockedInitialShaders())
    if lockShaders:
        for node in lockShaders:
            print('unlock node -> "{}"'.format(node))
            cmds.lockNode(node, l=False, lu=False)

        cmds.inViewMessage(bkc=0x09e2e2e, msg=_UNLOCK_MSG, fst=3200, fade=6, fts=14, font='Arial', pos='midCenterTop')


def beforeSaveCallback():
    # Unlock Lambert1 before SceneSaved
    om.MSceneMessage.addCallback(om.MSceneMessage.kBeforeSave, unLockInitialShaders)
