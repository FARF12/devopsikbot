FROM python:3.10-slim

WORKDIR /app


COPY requirements.txt ./
COPY bot.py ./
COPY .env ./

RUN pip install --no-cache-dir -r requirements.txt

ENV $(cat .env | xargs)

CMD ["python", "bot.py"]

