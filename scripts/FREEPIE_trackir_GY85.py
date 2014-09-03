# Important! Activate and configure AHRS IMU and
# trackIR plugins in FreePIE
# Testes in FreePIE 1.5.475.0 for Windows

import math

def update():
   global yaw
   global roll
   global pitch
   
   yaw = ahrsImu.yaw -cyaw
   roll = ahrsImu.roll - croll
   pitch = ahrsImu.pitch - cpitch
   
if starting:
   cyaw=0
   croll=0
   cpitch=0
   yaw=0
   pitch=0
   roll=0
   ahrsImu.update += update
   
# set pitch, yaw and roll for the three axis
# in trackIR emulator
trackIR.yaw = yaw
trackIR.roll = roll
trackIR.pitch = pitch

diagnostics.watch(trackIR.yaw)
diagnostics.watch(trackIR.pitch)
diagnostics.watch(trackIR.roll)

center = keyboard.getPressed(Key.Z)

# set new 'zero' in the current position for the three axis
if center:
   cyaw = trackIR.yaw
   croll = trackIR.roll
   cpitch = trackIR.pitch