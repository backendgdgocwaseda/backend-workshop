# Backend Workshop: Intro to FastAPI

## Prerequisites

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

### macOS/Linux: 
1. **Copy and paste this command into your terminal:**

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    or if you have Homebrew:

    ```bash
    brew install uv
    ```

2. **Restart your terminal.**

3. **Check if your installation succeeded:**
    ```bash
    uv --version
    ```

### Windows:
1. **Copy and paste this command into your PowerShell:**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
2. **Restart your terminal.**
3. **Check if your installation succeeded:**
    ```powershell
    uv --version
    ```

## Setup

Clone the repository and install the exact locked dependencies from `uv.lock`:

```bash
git clone https://github.com/backendgdgocwaseda/backend-workshop.git
cd backend-workshop/
uv sync --locked
```

## Running the Application

### Development Server (with auto-reload)

```bash
uv run fastapi dev main.py

```

Once running, the interactive API documentation is available at:

* **API Endpoint:** http://localhost:8000
* **Swagger UI:** http://localhost:8000/docs