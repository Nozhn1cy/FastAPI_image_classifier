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
* Классификация изображения непосредственно с главной страницы в браузере.

## Requirements
Python 3.9+

## Installation
Скопировать репозиторий в папку *name_dir*
```bash
git clone https://github.com/Nozhn1cy/FastAPI_image_classifier name_dir
```
Перейти в папку *name_dir* и установить библиотеки
```bash
pip install -r requirements.txt
```

## Run it
1. Перейти в папку *app* и выполнить команду в терминале:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
2. Перейти в браузере http://localhost:8000/.

Также сервер можно запустить из папки *name_dir* с помощью команды
```bash
docker compose up
```