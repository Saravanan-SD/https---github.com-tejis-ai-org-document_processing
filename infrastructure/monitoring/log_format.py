class LogFormat:
    required_fields = {
        "timestamp": "ISO8601 UTC",
        "level": "ERROR|WARN|INFO|DEBUG|TRACE",
        "category": "Category from LogConfig.Categories",
        "correlation_id": "UUID v4",
        "service": "service-name",
        "instance": "instance-id",
        "message": "Event description"
    }
    
    contextual_fields = {
        "user_id": "User identifier if available",
        "document_id": "Document identifier if applicable",
        "job_id": "Processing job identifier if applicable",
        "duration_ms": "Operation duration if applicable",
        "endpoint": "API endpoint if applicable"
    }
    
    error_fields = {
        "error_code": "Standardized error code",
        "error_message": "Human-readable error message",
        "stack_trace": "Stack trace for ERROR level",
        "exception_type": "Exception class name"
    }