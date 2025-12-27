# ---------- Base Python Image ----------
FROM python:3.10-slim

# ---------- Environment Config ----------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---------- Working Directory ----------
WORKDIR /app

# ---------- System Dependencies (needed for LightGBM / sklearn) ----------
RUN apt-get update && apt-get install -y \
    gcc \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# ---------- Copy requirements ----------
COPY requirements.txt .

# ---------- Install Python dependencies ----------
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy project files ----------
COPY . .

# ---------- Expose Flask Port ----------
EXPOSE 5000

# ---------- Run Flask ----------
CMD ["python", "app.py"]
