# Document data model

from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from datetime import datetime

class DocumentMetadata(BaseModel):
    title: str
    description: Optional[str]
    author: Optional[str]
    created_date: datetime
    modified_date: datetime
    page_count: Optional[int]
    language: Optional[str]
    keywords: List[str] = Field(default_factory=list)
    custom_metadata: Dict[str, any] = Field(default_factory=dict)

class DocumentVersion(BaseModel):
    version_id: str
    storage_path: str
    created_at: datetime
    created_by: str
    size: int
    hash: str
    comment: Optional[str]
    metadata: DocumentMetadata

class Document(BaseModel):
    id: str
    filename: str
    content_type: str
    size: int
    storage_path: str
    metadata: DocumentMetadata
    versions: List[DocumentVersion]
    current_version: str
    processing_status: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str
    tags: List[str]
    classification: List[str]
    permissions: Dict[str, List[str]]
    encryption_info: Optional[EncryptionInfo]
    retention_policy: Optional[RetentionPolicy]
    audit_trail: List[AuditEvent]