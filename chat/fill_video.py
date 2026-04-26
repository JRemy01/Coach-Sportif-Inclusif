def fill_videos(responses, vid_links):
    """
    Args:
        template_response (str): La réponse avec placeholders {vidX}
        video_links (list[str]): Liste des liens vidéos à injecter
    """
    response_filled = responses
    for i, link in enumerate(vid_links, start=1):
        response_filled = response_filled.replace(f"{{vid{i}}}", link)
    return response_filled