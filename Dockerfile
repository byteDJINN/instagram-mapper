# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]