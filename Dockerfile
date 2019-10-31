FROM python:3.7

RUN mkdir -p /work
WORKDIR /work

COPY /requirements.txt /work
RUN pip3 install -r requirements.txt

ADD k8s_registry/ /work

CMD "bash -c 'PYTHONPATH=/work python3 -m k8s_registry'"
