# Use an official lightweight Python image
FROM python:3.12-slim-bullseye as base

# Environment settings
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=true \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    QR_CODE_DIR=/myapp/qr_codes

# Set the working directory
WORKDIR /myapp

# Install required system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY ./requirements.txt .

# 🚨 Important: Force reinstall to guarantee update
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --force-reinstall -r requirements.txt

# Add a non-root user and switch
RUN useradd -m myuser
USER myuser

# Now copy all the app code (AFTER requirements to keep cache intact)
COPY --chown=myuser:myuser . .

# Expose the service port
EXPOSE 8000

# Entry point
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
