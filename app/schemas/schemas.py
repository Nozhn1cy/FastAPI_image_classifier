from pydantic import BaseModel


class ImageClassificationInputDataSchema(BaseModel):
    """Input data for image classification

    :param base64Image: base64 image
    :param num_predicts: integer number of top classes
    """

    base64Image: str
    num_predicts: int = 1


class ImageClassificationOutputDataSchema(BaseModel):
    """Output prediction

    :param top_classes: top classes from model
    :param top_probs: top probabilities from model
    """

    top_classes: list
    top_probs: list

    def to_dict(cls) -> dict:
        """convert to dict

        :returns: dict with keywords: top_classes and top_probs
        """
        return {"top_classes": cls.top_classes, "top_probs": cls.top_probs}
