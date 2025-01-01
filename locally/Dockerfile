# Use the latest available Python 3.13 image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Notebook and IPython (if not included in requirements.txt)
RUN pip install jupyter ipython nbconvert

# Copy the Python script into the container
COPY script.py . 

# Copy the CSV files into the container
COPY *.csv /app/

# Set the default command to run IPython with the script
CMD ["python", "script.py"]
