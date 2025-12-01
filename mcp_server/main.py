from fastmcp import FastMCP
import subprocess
import os

# Initialize the server
mcp = FastMCP(name="Tracium MCP Server")

@mcp.tool
def status():
    """Checks if the server is running."""
    return "Server is running and ready."

@mcp.tool
def echo(message: str = None, value: int = None):
    """The server will echo back any content you send in the payload. This is useful for testing the connection."""
    payload = {}
    if message is not None:
        payload["message"] = message
    if value is not None:
        payload["value"] = value
    return payload

@mcp.tool
def stop():
    """Shuts down the server."""
    # In a real application, you might want a more graceful shutdown
    # For this example, we'll return a message and rely on the process to be terminated externally or by FastMCP itself.
    # For local execution, FastMCP.run() handles exiting when a 'stop' command is received.
    return "Server shutting down."

@mcp.tool
def top():
    """Executes `top -b -n 1` to get a single snapshot of the current processes."""
    try:
        result = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing top command: {e.stderr}"

@mcp.tool
def perf(args: list[str]):
    """Executes the `perf` tool with the specified arguments."""
    try:
        full_command = ["perf"] + args
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return result.stdout
    except FileNotFoundError:
        return "Error: 'perf' command not found. Please ensure perf is installed and in your PATH."
    except subprocess.CalledProcessError as e:
        return f"Error executing perf command: {e.stderr}"

if __name__ == "__main__":
    mcp.run()