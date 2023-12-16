FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the FastAPI application source code into the container
COPY . .

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "simple_restful_api:app", "--host", "0.0.0.0", "--port", "8000"]