import maya.cmds as cmds

# Unlock Lambert1 after SceneOpened
cmds.scriptJob(event=["SceneOpened", "import time;time.sleep(0.3);import unlock_lambert1;unlock_lambert1.unLockInitialShaders()"], protected=True)

# Unlock Lambert1 Before SceneSaved
cmds.scriptJob(event=["idle", "import unlock_lambert1;unlock_lambert1.beforeSaveCallback()"], runOnce=True)

