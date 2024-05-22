FROM python:latest
WORKDIR /app
EXPOSE 5000
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
COPY . .
CMD python3 -m flask run --host=0.0.0.0
