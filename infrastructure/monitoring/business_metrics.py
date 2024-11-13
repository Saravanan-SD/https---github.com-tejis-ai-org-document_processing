class BusinessMetrics:
    # Document metrics
    document_processing_success_rate: Gauge = {
        "labels": ["document_type"],
        "help": "Success rate of document processing"
    }
    average_processing_time: Gauge = {
        "labels": ["document_type", "operation"],
        "help": "Average processing time in seconds"
    }
    
    # Usage metrics
    active_users: Gauge = {
        "labels": ["user_type"],
        "help": "Number of active users"
    }
    document_uploads: Counter = {
        "labels": ["user_type", "document_type"],
        "help": "Total number of document uploads"
    }