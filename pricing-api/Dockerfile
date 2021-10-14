FROM python:3.9

COPY . /code
RUN mkdir /root/.ssh
COPY config /root/.ssh/
WORKDIR /code

RUN apt-get update && apt-get install libsasl2-dev
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

CMD ["ssh", "mpmg", "-At", "-L", "0.0.0.0:10000:hadoopmn-gsi-prod03.mpmg.mp.br:10000"]

# CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]
