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
COPY start.sh .
COPY start.py .
COPY init_schema.py .

EXPOSE 8080

# Command to run
CMD ["/bin/bash", "start.sh"]