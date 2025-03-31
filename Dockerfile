FROM python:3.9-slim

RUN apt-get update && apt-get install -y libgomp1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED=1

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]