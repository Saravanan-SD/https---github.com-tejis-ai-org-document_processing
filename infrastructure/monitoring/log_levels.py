class LogConfig:
    class Levels:
        ERROR = {
            "level": 40,
            "description": "System failures and critical errors"
        }
        WARN = {
            "level": 30,
            "description": "Potential issues and degraded performance"
        }
        INFO = {
            "level": 20,
            "description": "Normal operation events"
        }
        DEBUG = {
            "level": 10,
            "description": "Detailed debugging information"
        }
        TRACE = {
            "level": 5,
            "description": "Very detailed debugging information"
        }

    class Categories:
        SECURITY = "security"
        PERFORMANCE = "performance"
        PROCESSING = "processing"
        STORAGE = "storage"
        API = "api"
        INTEGRATION = "integration"