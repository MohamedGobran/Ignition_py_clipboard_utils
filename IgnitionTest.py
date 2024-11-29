from clipboard_utils import copy_to_clipboard
from clipboard_utils import paste_from_clipboard
_logger_=system.util.getLogger("clipboard")
copy_to_clipboard(event.source.parent.getComponent('Text Field').text,_logger_)
event.source.parent.getComponent('dest_label').text=paste_from_clipboard(_logger_)