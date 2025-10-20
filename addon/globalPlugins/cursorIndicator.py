# Copywrite (C) 2025 
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
from source import mouseHandler
import ui


# defining plugin
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    On = False
    @scriptHandler.script(gesture="kb:alt+g")
    def script_indOn(self, gesture):
        if On == False:
            speech.speak(["Feature on"], None, priorities.Spri.NOW)
            log.debug("Feature onnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
            (MaxW, MaxH, (X,Y)) = getTotalWidthAndHeightAndMinimumPosition(displays)
            try:
                eventHandler.executeEvent("mouseMove", mouseObject, x=x, y=y)
                if x == X and y == Y:
                    speech.speak(["Mouse at bottom left corner"], None, priorities.Spri.NOW)
                elif x == X and y == MaxY:
                    speech.speak(["Mouse at top left corner"], None, priorities.Spri.NOW)
                elif x == MaxW and y == Y:
                    speech.speak(["Mouse at bottom right corner"], None, priorities.Spri.NOW)
                elif x == MaxW and y == MaxH:
                    speech.speak(["Mouse at top right corner"], None, priorities.Spri.NOW)
                elif x == X:
                    speech.speak(["Mouse at left border"], None, priorities.Spri.NOW)
                elif y == Y:
                    speech.speak(["Mouse at bottom border"], None, priorities.Spri.NOW)
                elif x == MaxW:
                    speech.speak(["Mouse at right border"], None, priorities.Spri.NOW)
                elif y == MaxH:
                    speech.speak(["Mouse at bottom border"], None, priorities.Spri.NOW)
                On = True
            except:
                return
        else:
            speech.speak(["Feature off"], None, priorities.Spri.NOW)
            log.debug("Feature offffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
            On = False
