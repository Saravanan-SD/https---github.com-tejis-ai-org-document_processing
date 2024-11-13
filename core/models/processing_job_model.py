# Processing job model

class ProcessingJob(BaseModel):
    id: str
    document_id: str
    job_type: str
    status: str
    priority: int
    progress: float
    started_at: datetime
    estimated_completion: Optional[datetime]
    completed_at: Optional[datetime]
    results: Optional[Dict[str, any]]
    error: Optional[ErrorInfo]
    retry_count: int
    worker_id: Optional[str]
    callback_url: Optional[str]
    dependencies: List[str]
    resources: ResourceRequirements