# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# No additional packages needed for this script
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run parse_fixed_width.py when the container launches
CMD ["python", "parse_fixed_width.py", "spec.txt", "input.txt", "output.csv"]
