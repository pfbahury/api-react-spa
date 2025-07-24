FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt install -y libpq-dev 

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "8000"]