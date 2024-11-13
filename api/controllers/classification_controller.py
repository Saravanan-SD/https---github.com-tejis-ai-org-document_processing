# Classification APIs

@router.prefix("/api/v1/classification")
class ClassificationController:
    @post("/classify")
    async def classify_document(
        self,
        document_id: str,
        models: List[str] = Query(["default"]),
        confidence_threshold: float = Query(0.7),
    ) -> ClassificationResponse:
        """
        Classify document using specified models
        """
        pass

    @get("/models")
    async def list_models(
        self,
        status: str = Query("active"),
    ) -> List[ModelInfo]:
        """
        List available classification models
        """
        pass

    @post("/models/train")
    async def train_model(
        self,
        training_config: TrainingConfig,
        dataset_id: str,
    ) -> TrainingJobResponse:
        """
        Initialize model training job
        """
        pass

    @post("/feedback")
    async def submit_feedback(
        self,
        document_id: str,
        classification_id: str,
        feedback: ClassificationFeedback,
    ) -> None:
        """
        Submit classification feedback for model improvement
        """
        pass