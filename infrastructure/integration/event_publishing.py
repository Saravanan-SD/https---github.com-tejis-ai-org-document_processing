class DocumentEventPublisher:
    async def publish_document_created(
        self,
        document_id: str,
        metadata: DocumentMetadata,
        user_id: str
    ) -> None:
        pass

    async def publish_processing_completed(
        self,
        document_id: str,
        processing_results: ProcessingResults,
        status: str
    ) -> None:
        pass

    async def publish_document_deleted(
        self,
        document_id: str,
        deletion_type: str,
        user_id: str
    ) -> None:
        pass