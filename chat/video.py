


import requests

key = "enter_your_api_key_here"  # Remplacez par votre clé API YouTube Data v3

def search_youtube_videos(query, max_results=3):
    """
    Recherche des vidéos YouTube en fonction d'une requête.
    
    """
    url = "https://www.googleapis.com/youtube/v3/search"
    
    params = {
        "part": "snippet",
        "q": query,
        "key": key,
        "maxResults": max_results,
        "type": "video"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    results = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        link = f"https://www.youtube.com/watch?v={video_id}"
        results.append(link)
    
    return results


# Exemple d’utilisation
if __name__ == "__main__":
    videos = search_youtube_videos("exercice bras fauteuil roulant")
    for v in videos:
        print(f"{v['title']} → {v['url']}")
