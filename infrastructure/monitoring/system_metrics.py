class SystemMetrics:
    class APIMetrics:
        # Request metrics
        requests_total: Counter = {
            "labels": ["endpoint", "method", "status_code"],
            "help": "Total number of API requests"
        }
        request_duration_seconds: Histogram = {
            "labels": ["endpoint", "method"],
            "buckets": [0.1, 0.5, 1.0, 2.0, 5.0]
        }
        request_size_bytes: Histogram = {
            "labels": ["endpoint"],
            "buckets": [1000, 10000, 100000, 1000000]
        }
        
        # Error metrics
        error_total: Counter = {
            "labels": ["endpoint", "error_type"],
            "help": "Total number of API errors"
        }
        
        # Rate limiting metrics
        rate_limit_hits: Counter = {
            "labels": ["endpoint", "client_id"]
        }

    class ProcessingMetrics:
        # Job metrics
        jobs_total: Counter = {
            "labels": ["job_type", "status"],
            "help": "Total number of processing jobs"
        }
        job_duration_seconds: Histogram = {
            "labels": ["job_type"],
            "buckets": [1, 5, 10, 30, 60, 120, 300]
        }
        job_queue_length: Gauge = {
            "labels": ["job_type"],
            "help": "Current length of processing queues"
        }
        
        # OCR metrics
        ocr_confidence_score: Histogram = {
            "labels": ["language"],
            "buckets": [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
        }
        
        # Classification metrics
        classification_confidence: Histogram = {
            "labels": ["model"],
            "buckets": [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
        }

    class StorageMetrics:
        # Storage usage metrics
        storage_usage_bytes: Gauge = {
            "labels": ["bucket"],
            "help": "Current storage usage in bytes"
        }
        document_count: Gauge = {
            "labels": ["document_type"],
            "help": "Total number of stored documents"
        }
        
        # Operation metrics
        storage_operations_total: Counter = {
            "labels": ["operation", "status"],
            "help": "Total number of storage operations"
        }