# Dockerfile

# Stage 1: Build Stage
FROM python:3.13-slim as builder

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
# It's good practice to upgrade pip, setuptools, and wheel first,
# as some packages might require their latest versions for proper installation.
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r /app/requirements.txt

# Stage 2: Production Stage
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# >>> NEW LINE HERE: Explicitly set PATH to include /usr/local/bin <<<
# This ensures that executables installed in /usr/local/bin (like uvicorn) are found.
ENV PATH="/usr/local/bin:${PATH}"

# Copy the installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# Explicitly copy the uvicorn executable from the builder stage
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
# Ensure it's executable (it should be, but doesn't hurt to explicitly set)
RUN chmod +x /usr/local/bin/uvicorn

# Copy all project files from the build context into /app in the container
COPY . /app

# Expose the port that Uvicorn will listen on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "ecore.main:app", "--host", "0.0.0.0", "--port", "8000"]