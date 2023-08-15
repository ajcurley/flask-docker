FROM python:3.10-slim

# Set the application working directory
WORKDIR /code

# Install the Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY requirements.dev.txt .
RUN pip install -r requirements.dev.txt

# Copy the application files
COPY . .

# TODO: Set the web server command
CMD ["tail", "-f", "/dev/null"]
