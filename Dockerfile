FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    apt-get install -y libgl1-mesa-dri && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "excercise_tracker.py"]
