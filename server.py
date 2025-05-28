from mcp.server.fastmcp import FastMCP
from app import get_random_quote

# Initialize MCP server
mcp = FastMCP("animequote-mcp")

@mcp.tool()
async def random_anime_quote() -> str:
    """
    Get a random anime quote.
    """
    return get_random_quote()

if __name__ == "__main__":
    mcp.run(transport="stdio")
