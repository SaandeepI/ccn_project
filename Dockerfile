FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y libgl1 && \
    rm -rf /var/lib/apt/lists/*
    pip install --no-cache-dir --upgrade pip && \
   

RUN pip install --no-cache-dir streamlit opencv-python-headless

WORKDIR /app

COPY . .

CMD ["streamlit", "run", "excercise_tracker.py"]
