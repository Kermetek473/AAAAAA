from mcp.server.fastmcp import FastMCP
from app import getAnimeFacts

# Initialize MCP server
mcp = FastMCP("anime-facts-mcp")

@mcp.tool()
async def get_anime_facts(anime_name: str) -> str:
    """
    Get facts about an anime.
    """
    facts = getAnimeFacts(anime_name)
    if not facts:
        return "No facts found."

    return facts

if __name__ == "__main__":
    mcp.run(transport="stdio")
