FROM python:3.10-slim

# Set the application working directory
WORKDIR /code

# Install the system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y curl

# Install the Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY requirements.dev.txt .
RUN pip install -r requirements.dev.txt

# Copy the application files
COPY . .

# Set the web server command
CMD ["gunicorn", "-c", "gunicorn.conf.py"]
