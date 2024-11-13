# Processing APIs

@router.prefix("/api/v1/processing")
class ProcessingController:
    @post("/convert")
    async def convert_document(
        self,
        document_id: str,
        options: ConversionOptions,
    ) -> JobResponse:
        """
        Initialize document conversion job
        """
        pass

    @post("/ocr")
    async def perform_ocr(
        self,
        document_id: str,
        options: OCROptions,
    ) -> JobResponse:
        """
        Start OCR processing job
        """
        pass

    @post("/analyze")
    async def analyze_document(
        self,
        document_id: str,
        analysis_types: List[AnalysisType],
        options: AnalysisOptions,
    ) -> JobResponse:
        """
        Begin document analysis job
        """
        pass

    @get("/jobs/{job_id}")
    async def get_job_status(
        self,
        job_id: str,
        include_results: bool = Query(False),
    ) -> JobStatusResponse:
        """
        Get processing job status and results
        """
        pass

    @post("/batch")
    async def batch_process(
        self,
        document_ids: List[str],
        operations: List[ProcessingOperation],
    ) -> BatchJobResponse:
        """
        Start batch processing job
        """
        pass