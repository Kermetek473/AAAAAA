import requests

def get_random_quote() -> str:
    """
    Get a random anime quote.
    """
    url = "https://animechan.xyz/api/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quote = data.get("quote", "No quote found.")
        character = data.get("character", "Unknown character")
        anime = data.get("anime", "Unknown anime")
        return f'"{quote}"\n- {character} ({anime})'
    else:
        return "Could not fetch quote."
