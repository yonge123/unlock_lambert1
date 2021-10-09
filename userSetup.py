import maya.cmds as cmds

# Unlock Lambert1 after SceneOpened
cmds.scriptJob(event=["SceneOpened", "import time;time.sleep(0.3);unLockInitialShaders()"], protected=True)

# Unlock Lambert1 Before SceneSaved
cmds.scriptJob(event=["idle", "beforeSaveCallback()"], runOnce=True)

