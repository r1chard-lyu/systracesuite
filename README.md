# Tracium
Tracium is a Model Context Protocol (MCP) server designed to expose Linux tracing and debugging capabilities such as eBPF, bpftrace, perf, ftrace, and syscall tracing to LLMs and autonomous agents.

It provides a unified observability interface that enables AI systems to inspect, profile, and debug Linux kernel and user-space behavior through safe, structured MCP tools.


# Python MCP Server (via stdio)

This project contains a simple implementation of a "fastmcp" style server that communicates over STDIO using JSON-RPC.

## Files

- `mcp_server/main.py`: The main server executable.
- `requirements.txt`: Contains the required Python packages.
- `setup.sh`: Setup Tracium's whitelisted tools so they can run with passwordless sudo. The MCP Server cannot trigger the Gemini CLI interactive shell to prompt the user for privilege escalation.

## Installation

This server relies on the `fastmcp` library. Install all dependencies using pip and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage
Quick start

1. Clone the repository and change into the project directory:
    ```bash
    git clone git@github.com:r1chard-lyu/tracium.git
    cd tracium
    ```

2. Create a virtual environment and install Python dependencies:
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

3. Allow passwordless sudo for bpftrace so the server can run tools without interactive prompts. Note: use only in development — do not enable in production.
    ```bash
    sudo ./setup.sh
    ```

4. Register Tracium as an MCP server with your Gemini CLI. Replace `<ABS_PATH_TO_TRACIUM>` with the absolute path to this repository on your machine:
    ```bash
    gemini mcp add tracium \
        --scope user \
        uv run --with fastmcp \
        fastmcp run <ABS_PATH_TO_TRACIUM>/mcp_server/main.py
    ```

5. Verify the MCP registration:
    ```bash
    gemini mcp list
    ```

    If registration succeeded you should see an entry like:
    ```text
    Configured MCP servers:

    ✓ tracium: uv run --with fastmcp fastmcp run <ABS_PATH_TO_TRACIUM>/mcp_server/main.py (stdio) - Connected
    ```

# Contributing
Contributions, features, issues, and discussions are all welcome.