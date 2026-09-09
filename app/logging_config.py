import logging

class SuppressHealthLiveAccess(logging.Filter):
    def filter(self, record):
        try:
            return "/health/live" not in record.getMessage()
        except Exception:
            return True

def configure_logging():
    logging.getLogger("uvicorn.access").addFilter(SuppressHealthLiveAccess())
