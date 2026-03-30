FROM python:3.10-slim

WORKDIR /app

# Copy semua file
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port streamlit
EXPOSE 8501

# Run app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]