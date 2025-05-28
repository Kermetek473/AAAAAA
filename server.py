from mcp.server.fastmcp import FastMCP
from app import getForecast

# Initialize MCP server
mcp = FastMCP("weather-mcp")

@mcp.tool()
async def get_forecast(lat: float, lon: float) -> str:
    """
    Get weather forecast for a given latitude and longitude.
    """
    return getForecast(lat, lon)

if __name__ == "__main__":
    mcp.run(transport="stdio")
