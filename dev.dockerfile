FROM python:3.8-slim

RUN apt-get update > /dev/null && \
    apt-get upgrade --yes > /dev/null && \
    apt-get clean > /dev/null && \
    rm -rf /var/lib/apt/lists/* > /dev/null && \
    pip install --no-cache-dir -U pip setuptools wheel > /dev/null 

WORKDIR /code

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -U -r requirements.txt

COPY ./src ./src

EXPOSE 8080

# ENTRYPOINT ["gunicorn", "main:app", "--chdir", "./src", "--workers", "4", \
#             "--worker-class", "uvicorn.workers.UvicornWorker", "-b", ":8080"]
ENTRYPOINT ["uvicorn", "main:app", "--port", "8080", "--reload", "--app-dir", "./src", "--host", "0.0.0.0"]
