# Copywrite (C) 2025 Kieran Gilpin <kgilpin2022@gmail.com>
# This file is covered by the GNU General Public License.
#import required dependancies
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

#define the global plugin
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	#Flag that shows the user has pressed alt+space and opened the window navigation menu
	In_Nav_Menu = False
	#Flag that shows the user has pressed 'm' after alt+space and entered teh window navigation mode.
	In_Nav_Mode = False

	#Script that exits navigation mode and sets flags to false when user presses enter (sets window position)
	@scriptHandler.script(gesture="kb:enter")
	def script_exitNavMode(self, gesture):
		gesture.send()
		if self.In_Nav_Mode:
			ui.message("You are exiting nav mode.")
			self.In_Nav_Menu = False
			self.In_Nav_Mode = False

	#detect alt+space command and change flag
	@scriptHandler.script(gesture="kb:alt+space")
	def script_detectNavMenu(self, gesture):
		#sends the gesture(command) to the operating system to perform normal windows action
		gesture.send()
		self.In_Nav_Mode = True
		

	@scriptHandler.script(gesture="kb:m")
	def script_navModeEnabled(self, gesture):
		gesture.send()
		#make sure alt+space has been pressed already
		if self.In_Nav_Mode:
			obj = api.getFocusObject()
			#When pressing alt+space, windows automatically focuses a popup menu. This checks to make sure that has happened.
			if (obj.role == controlTypes.Role.MENUITEM) or (obj.role == controlTypes.Role.POPUPMENU):
				self.In_Nav_Menu = True
			#When pressing alt+space and not focusing a window, set the alt+space flag to false.
			else:
				self.In_Nav_Mode = False

	@scriptHandler.script(gestures =["kb:leftArrow", "kb:rightArrow"])
	def script_moveHorizontal(self, gesture):
		gesture.send()
		#make sure alt+space, m have been pressed already
		if self.In_Nav_Menu:
			#get the main window of the current application, that is what we want the location of
			ancestors = api.getFocusAncestors()
			#ancestors[0] is always the desktop itself
			if ancestors[1]:
				obj = ancestors[1]
			else:
				obj = api.getFocusObject()
			#make sure a window is focused
			if (obj.role == controlTypes.Role.WINDOW) and (obj != api.getDesktopObject()):
				text = obj._get_locationText()
				ui.message(f"Horizontal movement, press enter to exit nav mode {text}")
			#set flags to false if no window is focused
			else:
				self.In_Nav_Menu = False
				self.In_Nav_Mode = False

	@scriptHandler.script(gestures=["kb:upArrow", "kb:downArrow"])
	def script_moveVertical(self, gesture):
		gesture.send()
		#make sure alt+space, m have been pressed already
		if self.In_Nav_Menu:
			#get the main window of the current application, that is what we want the location of
			ancestors = api.getFocusAncestors()
			#ancestors[0] is always the desktop itself
			if ancestors[1]:
				obj = ancestors[1]
			else:
				obj = api.getFocusObject()
			#make sure a window is focused
			if (obj.role == controlTypes.Role.WINDOW) and (obj != api.getDesktopObject()):
				text = obj._get_locationText()
				ui.message(f"Vertical movement, press enter to exit nav mode {text}")
			#set flags to false if no window is focused
			else:
				self.In_Nav_Menu = False
				self.In_Nav_Mode = False

#create a script that reads the location every time an arrow key is pressed
# use gesture.send() to pass the arrow key to the window
