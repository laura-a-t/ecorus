FROM python:3.8-slim-buster

# Create root directory
WORKDIR api
# Install PIP dependencies
COPY requirements.txt .
RUN pip3.8 install --upgrade pip
RUN pip3.8 install --upgrade -r requirements.txt

# Copy files
COPY api ./api
COPY dev_config.yml .
COPY start.py .

EXPOSE 8080

# Command to run
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8080", "start:app"]