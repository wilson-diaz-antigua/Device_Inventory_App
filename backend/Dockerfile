FROM python:latest
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV PYTHONPATH=/app
EXPOSE 8080

CMD [ "python","-m","run" ]
