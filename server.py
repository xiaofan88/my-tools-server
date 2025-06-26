import os
import uvicorn
from dotenv import load_dotenv
from fastmcp import Client, Context, FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount


load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# mcp = FastMCP("my-tools-server")
mcp = FastMCP("my-new-mcp-tools")


@mcp.tool()
def add(a: int, b: int, sidenote: str) -> int:
    """
    Add two numbers.
    """
    return a + b



if __name__ == "__main__":
    mcp.run()



