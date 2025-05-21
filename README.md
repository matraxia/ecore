# 🚀 Ecore FastAPI Backend Service

## 1. Prerequisites

To set up and run this project, you'll need the following software installed on your system:

* **Python 3.13:** Download it from [python.org](https://www.python.org/downloads/). Make sure `pip` (Python's package installer) is also available.
    * **Verify installation:**
        ```bash
        python3.13 --version
        ```
* **Docker Desktop (or Docker Engine):** Essential for containerizing and running the application. Get it from [docker.com](https://www.docker.com/products/docker-desktop/).
    * **Verify installation:**
        ```bash
        docker --version
        ```

---

## 2. Getting Started: Local Environment Setup

Follow these steps to prepare your local development environment and install the necessary dependencies.

### 2.1. Repository Setup

1.  **Clone the repository** (if you're using Git) or extract your project archive:
    ```bash
    git clone [repository-url]
    ```
2.  **Navigate into your project's root directory:**
    ```bash
    cd /path/to/your/ecore_project_root/ecore
    ```
    (Ensure you're in the directory where your `Dockerfile` and `requirements.txt` are located.)

### 2.2. Python Virtual Environment Setup

Using a **virtual environment** is a best practice to keep your project's dependencies isolated from other Python projects.

1.  **Create a virtual environment:**
    ```bash
    python3.13 -m venv .venv
    ```
2.  **Activate the virtual environment:**
    * **macOS / Linux:**
        ```bash
        source .venv/bin/activate
        ```
    * **Windows (Command Prompt):**
        ```bash
        .venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

### 2.3. Install Project Dependencies

With your virtual environment active, install all required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2.4. Run the Application Locally with Uvicorn
Once all dependencies are installed and your virtual environment is active, you can start the FastAPI application directly using Uvicorn:

```bash
uvicorn ecore.main:app --reload --host 0.0.0.0 --port 8000
```

ecore.main:app: This specifies the Python module (ecore.main) where your FastAPI application instance (app) is located.
--reload: Enables live-reloading, which is very useful during development as it automatically restarts the server when code changes are detected. (Do not use in production!)
--host 0.0.0.0: Binds the server to all available network interfaces, making it accessible from your browser.
--port 8000: Sets the port on which the server will listen for incoming requests.
You should see output indicating that the server has started, typically including a line like Uvicorn running on http://0.0.0.0:8000.


# 3. Docker Deployment:

Starting the ContainerDocker lets you package your application and its environment into a container, ensuring it runs consistently anywhere.

### 3.1. Build the Docker Image

Make sure you're in your project's root directory (ecore/) where the Dockerfile is located.
```bash
docker build -t ecore-fastapi-service .
```

This command tells Docker to build an image named ecore-fastapi-service.The . indicates that the Dockerfile for the build is in your current directory.

### 3.2. Run the Docker Container

Once the image is built, you can start a container from it:

```bash
docker run -d --name ecore-app-container -p 8000:8000 ecore-fastapi-service
```
-d: Runs the container in detached mode (in the background).--name ecore-app-container: Gives your running container a friendly name.-p 8000:8000: This is crucial! It maps port 8000 on your computer to port 8000 inside the container.ecore-fastapi-service: The name of the Docker image you want to run.

### 3.3. Verify Container Status

To check if your container is running:

```bash
docker ps
```

You should see ecore-app-container listed in the output.

### 3.4. Stop and Remove the Container

When you're done, you can manage your running container:

```bash
Stop the container:docker stop ecore-app-container
```

Remove the container (after it's stopped):

```bash
docker rm ecore-app-container
```
