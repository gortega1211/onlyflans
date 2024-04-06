# Use a lightweight base image
FROM python:3.10.10-slim


# Set up environment variable for the application directory
ENV APP_HOME=/app
ARG PROJECT_FOLDER
ENV PROJECT=$PROJECT_FOLDER

# Create the application directory
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy only the requirements file
COPY requirements.txt .

# # Create and activate virtual environment
# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire local project into the container
COPY . .

EXPOSE 8000

WORKDIR $PROJECT_FOLDER

# Start the server
CMD ["python3", "manage.py", "runserver"]
