# FastAPI Model Server Classifier
Сервер на фреймворке FastAPI, с помощью которого можно классифицировать изображения. 

В качестве базовой модели машинного обучения использована EfficientNetB0.
## Methods
Сервис поддерживает 3 метода:
* GET запрос, позволяющий получить статус сервера.
  
  Пример запроса:
 ```bash
 http://localhost:8000/status
 ``` 
* POST запрос, позволяющий классифицировать изображение и получить вероятности популярных классов. Для этого нужно указать в num_predicts число классов в ответе.
  
  Пример запроса:

``` bash
url = 'http://localhost:8000/predict_image'
with open ("image_for_classificaion.jpg", 'rb') as f:
    data = f.read()
    data = base64.b64encode(data).decode("utf-8")
    data = {'base64Image': data, 'num_predicts': 2}
y = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
``` 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Пример ответа:
``` bash
{"top_classes":["borzoi","Saluki"],"top_probs":[0.98,0.0]}
``` 
* Классификация изображения непосредственно с главной страницы браузера.

## Requirements
Python 3.9+

## Installation
описание как запустить git clone + docker compose up

## Run it
1. Выполнить команду в терминале:
```bash
uvicorn main:app
```
2. Перейти в браузере http://localhost:8000/.