# Document management APIs

from fastapi import APIRouter, UploadFile, File, Form, Query, Path
from typing import List, Optional

@router.prefix("/api/v1/documents")
class DocumentController:
    @post("/upload")
    async def upload_document(
        self,
        file: UploadFile = File(...),
        metadata: DocumentMetadata = Form(...),
        processing_options: ProcessingOptions = Form(...),
        chunk_number: int = Form(...),
        total_chunks: int = Form(...),
    ) -> UploadResponse:
        """
        Handle chunked document upload with metadata
        """
        pass

    @get("/{document_id}")
    async def get_document(
        self,
        document_id: str = Path(...),
        include_metadata: bool = Query(True),
        version: Optional[str] = Query(None),
    ) -> DocumentResponse:
        """
        Retrieve document details with optional version
        """
        pass

    @put("/{document_id}/metadata")
    async def update_metadata(
        self,
        document_id: str,
        metadata: DocumentMetadata,
    ) -> DocumentResponse:
        """
        Update document metadata
        """
        pass

    @delete("/{document_id}")
    async def delete_document(
        self,
        document_id: str,
        permanent: bool = Query(False),
    ) -> None:
        """
        Delete or archive document
        """
        pass

    @get("/search")
    async def search_documents(
        self,
        query: str = Query(None),
        file_types: List[str] = Query([]),
        date_range: DateRange = Query(None),
        tags: List[str] = Query([]),
        page: int = Query(1),
        page_size: int = Query(20),
        sort_by: str = Query("created_at"),
        sort_order: str = Query("desc"),
    ) -> DocumentSearchResponse:
        """
        Search documents with filtering and pagination
        """
        pass