FROM python:3.9

COPY . /code
RUN mkdir /root/.ssh
COPY config /root/.ssh/
WORKDIR /code

RUN apt-get update && apt-get install libsasl2-dev
RUN apt-get install libsasl2-modules
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]
