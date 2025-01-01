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

# Copy the notebook file into the container
COPY DuckDB.ipynb .

# Copy the CSV files into the container
COPY *.csv /app/

# Convert the notebook to a Python script
RUN jupyter nbconvert --to script DuckDB.ipynb

# Set the default command to run IPython with the generated Python script
CMD ["ipython", "DuckDB.py"]
