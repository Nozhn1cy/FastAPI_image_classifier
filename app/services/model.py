import torch
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
from schemas.schemas import ImageClassificationOutputDataSchema
import io


class Classifier:
    """Image classification model"""

    def __init__(self, path: str = "../model/model"):
        """
        Constructor for the classifier object

        :param path: path to load model
        :returns: None
        """
        self.path = path
        self.model = torch.load(self.path)
        self.model.eval()
        self.config = resolve_data_config({}, model=self.model)
        self.transform = create_transform(**self.config)
        with open("../imagenet_classes.txt", "r") as f:
            self.categories = [s.strip() for s in f.readlines()]

    def preprocess(self, image: bytes) -> torch.tensor:
        """Preprocessing input image

        :param image: binary data
        :returns: tensor
        """
        image = io.BytesIO(image)
        img = Image.open(image).convert("RGB")
        tensor = self.transform(img).unsqueeze(0)

        return tensor

    def postprocess(
        self, logits: torch.tensor, num_predicts: int = 1
    ) -> ImageClassificationOutputDataSchema:
        """Postprocessing logits

        :param logits: output of model
        :param num_predicts: integer number of top classes
        :returns: prediction with top_classes and top_probabilities
        """
        probabilities = torch.nn.functional.softmax(logits[0], dim=0)
        top_prob, top_catid = torch.topk(probabilities, num_predicts)

        top_classes = list(self.categories[i] for i in top_catid)
        top_probabilities = list(round(i, 2) for i in top_prob.tolist())

        prediction = ImageClassificationOutputDataSchema(
            top_classes=top_classes, top_probs=top_probabilities
        )

        return prediction

    def predict(
        self, image: bytes, num_predicts: int = 1
    ) -> ImageClassificationOutputDataSchema:
        """Predict class on image

        :param image: binary data
        :param num_predicts: integer number of popular classes
        :returns: prediction with top_classes and top_probabilities
        """
        tensor = self.preprocess(image)
        logits = self.model(tensor)
        prediction = self.postprocess(logits, num_predicts)

        return prediction
