import globalPluginHandler
import ui
import api
import platform
import sys
import winreg
from fileUtils import getFileVersionInfo
from versionInfo import version as nvda_version


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    def get_windows_info(self):
        arch = platform.architecture()[0]
        release = platform.release()
        build = sys.getwindowsversion().build
        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"
            )
            display_version, _ = winreg.QueryValueEx(key, "DisplayVersion")
            ubr, _ = winreg.QueryValueEx(key, "UBR")
            winreg.CloseKey(key)
        except Exception:
            display_version, ubr = "Unknown", 0
        return f"Windows {release} ({arch}) Version: {display_version}, Build: {build}.{ubr}"

    def get_focused_app_info(self):
        fg = api.getForegroundObject()
        app_name = fg.appModule.appName
        process_path = fg.appModule.appPath
        try:
            info = getFileVersionInfo(process_path, 'ProductVersion')
            # ms = info['FileVersionMS']
            # ls = info['FileVersionLS']
            # version = f"{ms >> 16}.{ms & 0xFFFF}.{ls >> 16}.{ls & 0xFFFF}"
            version = info["ProductVersion"]
        except Exception:
            version = "Unknown"
        return app_name, version

    def copy_debug_info(self):
        windows = self.get_windows_info()
        app_name, app_version = self.get_focused_app_info()

        text = (
            f"NVDA version: {nvda_version}\n"
            f"{windows}\n"
            f"Focused App: {app_name} ({app_version})\n"
        )

        api.copyToClip(text)
        ui.message("Debug info copied to clipboard.")
        return text

    def script_copyDebugInfo(self, gesture):
        """Copies system and app debug info to the clipboard."""
        self.copy_debug_info()

    __gestures = {
        "kb:NVDA+shift+k": "copyDebugInfo"
    }
