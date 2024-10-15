# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the entire project to the container, including .env and source code
COPY . /app

# Install python-dotenv for loading .env file
RUN pip install python-dotenv

# Set the working directory to src (where your app.py is located)
WORKDIR /app/src

# Expose the port that Streamlit will run on
EXPOSE 8000

# Command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
