FROM python:3.8-slim


WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


RUN pip install gdown

RUN gdown 1suRXkUCw6-e7dDrzip0aKPRkbgXbUefF

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]