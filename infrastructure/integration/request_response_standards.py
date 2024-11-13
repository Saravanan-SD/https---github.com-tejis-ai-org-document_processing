class APIStandards:
    class Headers:
        required = {
            "Authorization": "Bearer {token}",
            "X-Correlation-ID": "UUID v4",
            "X-Client-Version": "Semver",
            "Content-Type": "application/json"
        }
        
        optional = {
            "X-Request-Priority": "high|medium|low",
            "X-Callback-URL": "URL",
            "X-Idempotency-Key": "UUID v4"
        }

    class ResponseCodes:
        success_codes = {
            200: "OK - Request successful",
            201: "Created - Resource created",
            202: "Accepted - Processing initiated",
            204: "No Content - Operation successful"
        }
        
        error_codes = {
            400: "Bad Request - Invalid parameters",
            401: "Unauthorized - Invalid credentials",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Resource not found",
            409: "Conflict - Resource conflict",
            422: "Unprocessable Entity - Validation failed",
            429: "Too Many Requests - Rate limit exceeded",
            500: "Internal Server Error",
            503: "Service Unavailable"
        }