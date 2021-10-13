FROM python:3.9

# RUN apt-get -y install openssh-client
# RUN ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa

# RUN eval "$(ssh-agent -s)" && \
#     ssh-add /root/.ssh/id_rsa && \

# WORKDIR ~/.ssh
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN apt-get update && apt-get install libsasl2-dev
RUN pip install --upgrade -r /code/requirements.txt
COPY ./src /code/src
# WORKDIR /home
CMD ["uvicorn", "src.main:app", "--reload"]