import globalPluginHandler
import tones
import ui
import api
import controlTypes
import scriptHandler
from logHandler import log
import core
from NVDAObjects import NVDAObject
import eventHandler

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	In_Nav_Menu = False
	In_Nav_Mode = False


	@scriptHandler.script(gesture="kb:enter")
	def script_exitNavMode(self, gesture):
		gesture.send()
		if self.In_Nav_Mode:
			ui.message("You are exiting nav mode.")
			self.In_Nav_Menu = False
			self.In_Nav_Mode = False

	@scriptHandler.script(gesture="kb:alt+space")
	def script_detectNavMenu(self, gesture):
		gesture.send()
		self.In_Nav_Mode = True
		

	@scriptHandler.script(gesture="kb:m")
	def script_navModeEnabled(self, gesture):
		gesture.send()
		if self.In_Nav_Mode:
			obj = api.getFocusObject()
			if (obj.role == controlTypes.Role.MENUITEM) or (obj.role == controlTypes.Role.POPUPMENU):
				self.In_Nav_Menu = True
			else:
				self.In_Nav_Mode = False

	@scriptHandler.script(gestures =["kb:leftArrow", "kb:rightArrow"])
	def script_moveHorizontal(self, gesture):
		gesture.send()
		if self.In_Nav_Menu:
			ancestors = api.getFocusAncestors()
			if ancestors[1]:
				obj = ancestors[1]
			else:
				obj = api.getFocusObject()
			if (obj.role == controlTypes.Role.WINDOW) and (obj != api.getDesktopObject()):
				text = obj._get_locationText()
				ui.message(f"Horizontal movement, press enter to exit nav mode {text}")
			else:
				self.In_Nav_Menu = False
				self.In_Nav_Mode = False

	@scriptHandler.script(gestures=["kb:upArrow", "kb:downArrow"])
	def script_moveVertical(self, gesture):
		gesture.send()
		if self.In_Nav_Menu:
			ancestors = api.getFocusAncestors()
			if ancestors[1]:
				obj = ancestors[1]
			else:
				obj = api.getFocusObject()
			if (obj.role == controlTypes.Role.WINDOW) and (obj != api.getDesktopObject()):
				text = obj._get_locationText()
				ui.message(f"Vertical movement, press enter to exit nav mode {text}")
			else:
				self.In_Nav_Menu = False
				self.In_Nav_Mode = False

#create a script that reads the location every time an arrow key is pressed
# use gesture.send() to pass the arrow key to the window
