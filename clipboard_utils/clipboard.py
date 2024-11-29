import os


def copy_to_clipboard(text, logger=None):
    """
    Copies the given text to the clipboard.
    Ways this can fail:
    1. Pass None as text
    2. Pass non-string type
    3. Pass extremely large text that exceeds pipe buffer
    4. System clipboard is locked by another process
    """
    if text is None:
        if logger:
            logger.error("Cannot copy None to clipboard")
        return False

    try:
        # Convert to string in case non-string type is passed
        text_str = str(text)

        # Fail if text is too large (example threshold)
        if len(text_str) > 1000000:  # 1MB limit example
            if logger:
                logger.error("Text too large for clipboard")
            return False

        with os.popen('clip', 'w') as clipboard:
            clipboard.write(text_str)
            # Check if write was successful
            if clipboard.close() is not None:  # None means success
                raise Exception("Failed to write to clipboard")
        return True

    except Exception, e:
        if logger:
            logger.error("Error copying to clipboard: %s" % str(e))
        return False


def paste_from_clipboard(logger=None):
    """
    Returns the text from the clipboard.
    Ways this can fail:
    1. PowerShell not available
    2. Clipboard contains non-text data
    3. Clipboard is empty
    4. System clipboard is locked
    """
    try:
        # Intentionally use wrong command to demonstrate error
        output = os.popen('powershell Get-Clipboard').read()  # Will fail

        # Check if output is empty
        if not output:
            if logger:
                logger.error("Clipboard is empty")
            return None

        return output.strip()

    except Exception, e:
        if logger:
            logger.error("Error pasting from clipboard: %s" % str(e))
        return None