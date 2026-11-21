FROM python:3.11-slim

# Install system dependencies, Chromium, and Indian fonts for flawless Devanagari & Gujarati rendering
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    fonts-noto \
    fonts-noto-cjk \
    fonts-deva \
    fonts-gujr \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn vedic_server:app --host 0.0.0.0 --port ${PORT:-8000}"]
