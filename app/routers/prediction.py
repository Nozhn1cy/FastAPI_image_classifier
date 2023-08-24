from fastapi import APIRouter
from fastapi import File, UploadFile, Request
from starlette.templating import Jinja2Templates
import base64
from schemas.schemas import ImageClassificationInputDataSchema
from services.model import Classifier

model = Classifier()

router = APIRouter()

templates = Jinja2Templates(directory="../templates")


@router.post("/predict_image")
def predict_image(data: ImageClassificationInputDataSchema) -> dict:
    """Predict top classes on a image

    :param data: input data containing base64image and num_predicts
    :returns: dict with keywords: top_classes and top_probabilies
    """
    img = base64.b64decode(data.base64Image)
    prediction = model.predict(img, data.num_predicts).to_dict()

    return prediction


@router.get("/")
async def classifier(request: Request):
    """Home page

    :param request: request
    :returns: page
    """
    return templates.TemplateResponse("classifier.html", {"request": request})


@router.post("/")
async def upload(request: Request, file: UploadFile = File(...)):
    """Predict top classes on a image

    :param request: request
    :param file: upload file
    :returns: page with uploaded photo, popular class and probability of that class
    """
    try:
        img = file.file.read()
        prediction = model.predict(img)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    top_class, top_prob = prediction.top_classes[0], prediction.top_probs[0]
    encoded_image = base64.b64encode(img).decode("utf-8")

    return templates.TemplateResponse(
        "classifier.html",
        {
            "request": request,
            "picture": encoded_image,
            "probability": (top_class, top_prob),
        },
    )
