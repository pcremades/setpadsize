try:
    from .plugin import SetPadSizePlugin
    plugin = SetPadSizePlugin()
    plugin.register()
except Exception as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))
