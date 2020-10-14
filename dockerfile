FROM python:3.8

ENV SRC_DIR /usr/bin/src/webapp/src
ENV PYTHONUNBUFFERED=1

COPY server/* ${SRC_DIR}/

WORKDIR ${SRC_DIR}

CMD ["python", "server.py"]
