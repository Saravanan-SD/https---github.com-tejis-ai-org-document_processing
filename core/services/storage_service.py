# Processing and analysis service 

class StorageService:
    async def store_document(
        self,
        file_data: bytes,
        metadata: StorageMetadata,
        encryption: Optional[EncryptionOptions] = None,
    ) -> StorageResponse:
        """
        Store document in MinIO with optional encryption
        """
        pass

    async def retrieve_document(
        self,
        storage_path: str,
        options: RetrievalOptions,
    ) -> bytes:
        """
        Retrieve document from storage
        """
        pass

    async def generate_presigned_url(
        self,
        storage_path: str,
        expiration: int,
        permissions: str = "read",
    ) -> str:
        """
        Generate presigned URL for document access
        """
        pass