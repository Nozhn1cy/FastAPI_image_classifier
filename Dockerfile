FROM python:3.9

WORKDIR /fastapi_app

COPY requirements.txt /fastapi_app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /fastapi_app

WORKDIR /fastapi_app/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]