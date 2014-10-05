def update():
   global yaw
   global roll
   global pitch
   yaw = ahrsImu.yaw
   if (yaw<0):
      yaw = 360 + yaw
   roll = ahrsImu.roll
   pitch = ahrsImu.pitch

if starting:
   pyaw=0
   proll=04
   ppitch=0
   yaw = 0
   roll = 0
   pitch = 0
   enabled = False
   ahrsImu.update += update

diagnostics.watch(yaw)
diagnostics.watch(roll)
diagnostics.watch(pitch)

deltaYaw = filters.delta(yaw)

if (deltaYaw>150):
   deltaYaw = deltaYaw - 360
if (deltaYaw<(-150)):
   deltaYaw = deltaYaw + 360

deltaPitch = filters.delta(pitch)
deltaRoll = filters.delta(roll)
   
if (enabled):
   mouse.deltaX = deltaYaw*5
   mouse.deltaY = -deltaPitch*5
   diagnostics.watch(deltaYaw)
   diagnostics.watch(-deltaPitch)

toggle = keyboard.getPressed(Key.Z)

if toggle:
   enabled = not enabled