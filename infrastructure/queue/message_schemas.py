class DocumentUploadMessage(BaseModel):
    message_id: str
    document_id: str
    chunk_info: ChunkInfo
    storage_location: str
    processing_options: ProcessingOptions
    metadata: DocumentMetadata
    timestamp: datetime
    trace_id: str

class ProcessingMessage(BaseModel):
    message_id: str
    document_id: str
    operation: str
    parameters: Dict[str, any]
    priority: int
    callback_url: Optional[str]
    timestamp: datetime
    trace_id: str

class DocumentEventMessage(BaseModel):
    message_id: str
    event_type: str
    document_id: str
    user_id: str
    details: Dict[str, any]
    timestamp: datetime
    trace_id: str