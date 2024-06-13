FROM python:3.12

WORKDIR /app

COPY rrr.txt .

RUN pip install --no-cache-dir -r rrr.txt

COPY . .

CMD ["python", "main.py"]
