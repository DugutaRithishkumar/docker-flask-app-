# Use a lightweight Python 3.9 image as the base
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from your computer to the container
COPY requirements.txt /app/

# Install all Python packages listed in requirements.txt
# --no-cache-dir keeps the image smaller by not storing pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Tell Docker that the container will use port 5000
EXPOSE 5000

# Command to run when the container starts
# It runs your Python app
CMD ["python", "app.py"]
