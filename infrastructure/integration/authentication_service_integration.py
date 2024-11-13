class AuthenticationConfig:
    auth_service_url: str = "<http://auth-service/api/v1>"
    token_validation_endpoint: str = "/validate-token"
    timeout_ms: int = 2000
    cache_ttl_seconds: int = 300
    retry_attempts: int = 3

class AuthenticationIntegration:
    async def validate_token(self, token: str) -> TokenValidation:
        pass
    
    async def get_user_permissions(self, user_id: str) -> UserPermissions:
        pass