import gui

def doInstall(
	createDesktopShortcut=True,
	startOnLogon=True,
	isUpdate=False,
	copyPortableConfig=False,
	silent=False,
	startAfterInstall=True,
):
	
	if not silent:
		msg = (
			# Translators: The message displayed when NVDA has been successfully installed.
			_("Successfully installed NVDA. ")
			if not isUpdate
			# Translators: The message displayed when NVDA has been successfully updated.
			else _("Successfully updated your installation of NVDA. ")
		)
		updateContents = ""
		with open('../../user_docs/en/changes.md', 'r', encoding='utf-8') as f:
			for line in f:
				if line.startswith('###'):
					break
				updateContents += line
		gui.messageBox(
			# Translators: The message displayed to the user after NVDA is installed
			# and the installed copy is about to be started.
			msg + _("Please press OK to start the installed copy.") + updateContents,
			# Translators: The title of a dialog presented to indicate a successful operation.
			_("Success"),
		)

# '/user_docs/en/changes.md'
# '../../user_docs/en/changes.md'
