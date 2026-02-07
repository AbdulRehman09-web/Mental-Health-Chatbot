# -----------------------------
# Base image
# -----------------------------
FROM python:3.11-slim

# -----------------------------
# Set workdir
# -----------------------------
WORKDIR /app

# -----------------------------
# Copy requirements
# -----------------------------
COPY requirements.txt .

# -----------------------------
# Install dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy all project files
# -----------------------------
COPY . .

# -----------------------------
# Expose port
# -----------------------------
EXPOSE 10000

# -----------------------------
# Start command
# -----------------------------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
