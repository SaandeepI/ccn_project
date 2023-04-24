FROM python:3.9

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app files
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Start the app
CMD ["streamlit", "run", "excercise_tracker.py"]
