FROM python:3.9

COPY . /code
WORKDIR /code

RUN apt-get update && apt-get install -y libsasl2-dev
RUN apt-get install -y libsasl2-modules
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

CMD ["uvicorn", "src.main:app", "--reload", "--port",  "8081", "--host", "0.0.0.0"]
