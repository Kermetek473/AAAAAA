import requests

def getAnimeFacts(anime_name: str) -> str:
    """
    Get facts about an anime.
    """
    url = f"https://anime-facts-rest-api.onrender.com/api/v1/{anime_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            facts = [fact['fact'] for fact in data['data']]
            return "\n".join(facts)
        else:
            return "No facts found."
    else:
        return "Anime not found or API error."
