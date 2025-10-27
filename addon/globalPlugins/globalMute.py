from comtypes import CLSCTX_ALL
from ctypes import POINTER, cast, c_bool
import subprocess
import sys
import globalPluginHandler
import os
from logHandler import log
from pycaw import utils
from scriptHandler import script

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Get the default audio capture (microphone) device
	log.debug("RUNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNn")
	devices = utils.AudioUtilities.GetMicrophone()
	interface = devices.Activate(utils.IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(utils.IAudioEndpointVolume))
	mute = False
	volume.SetMute(0, None)
	@script(gesture='kb:NVDA+g')
	def script_muteMic(self, gesture):
		# Mute the mic
		log.debug("BUTTON PRESSEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
		if GlobalPlugin.mute == False:
			GlobalPlugin.mute = True
			GlobalPlugin.volume.SetMute(1, None)
			log.debug("Muting Microphone")
		# Unmute
		else:
			GlobalPlugin.mute = False
			GlobalPlugin.volume.SetMute(0, None)
			log.debug("Unmuting Microphone")
