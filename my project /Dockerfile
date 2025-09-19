# Use a lightweight Python 3.9 image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Create a non-root user and switch to it
# This is a security best practice
RUN useradd --create-home appuser
USER appuser

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python packages
# --no-cache-dir keeps the image smaller
# --user installs packages in the user's home directory
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the rest of your application code
COPY . .

# Tell Docker that the container will use port 8000
EXPOSE 8000

# Command to run when the container starts
# The path needs to be updated to the user's local bin
CMD ["/home/appuser/.local/bin/python", "app.py"]
