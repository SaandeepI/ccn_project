FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir streamlit opencv-python-headless mediapipe 

WORKDIR /app

COPY . .

CMD ["streamlit", "run", "excercise_tracker.py"]
