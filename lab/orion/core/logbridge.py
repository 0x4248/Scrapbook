import logging

class logBridge(logging.Handler):
    def __init__(self, orionLoggerBridge):
        super().__init__()
        self.orionLoggerBridge = orionLoggerBridge

    def emit(self, record: logging.LogRecord):
        try:
            msg = self.format(record)
            self.orionLoggerBridge.log(
                f"BRIDGE -> {record.name}.{record.funcName}()",
                msg,
                record.levelname,
            )
        except Exception:
            self.handleError(record)
