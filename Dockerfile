# Use Python 3.9 image
FROM python:3.9

# Set working directory
WORKDIR /

# Copy files
COPY requirements.txt .
COPY app.py .
COPY models/my_model.pkl ./models/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
