FROM python:3.8-slim


WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install gdown

RUN gdown 1suRXkUCw6-e7dDrzip0aKPRkbgXbUefF

RUN gdown 1SVdndqvn59f9dZNya5-8CGQbRtybYlMh

RUN gdown 1aom0L-tJLmkpuN4sutCYFQ9sgVEnSMZr

RUN gdown 15sOHdzTwyXEDHRLoEJlH10GtWpw_pxKC

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]


