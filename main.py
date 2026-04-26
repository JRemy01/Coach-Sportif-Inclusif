
from chat.ChatBot import generate_response
from chat.video import search_youtube_videos
from chat.fill_video import fill_videos

def chatbot():
    print("Coach Sportif Inclusif")
    print("'exit' pour quitter.\n")
    
    while True:

        #  Message utilisateur
        user_message = input("👤 Toi : ")
        
        if user_message.lower() in ["exit", "quit", "stop"]:
            print("Merci d'avoir utilisé le Coach Sportif Inclusif. À bientôt !")
            break
        
        # Génération de la réponse  {vid1}, {vid2}, {vid3}
        raw_response = generate_response(user_message)
        if not raw_response:
            print(" Erreur lors de la génération de la réponse.")
            continue
        
        #  vidéos  YouTube
        videos = search_youtube_videos(user_message, max_results=3)
        if not videos:
            print("Aucune vidéo trouvée, la réponse sera affichée sans liens.")
            final_response = raw_response
        else:
            # Remplacement par les ù liens
            final_response = fill_videos(raw_response, videos)
        
        # 5. Affichage final
        print("\n🤖 Coach :\n", final_response, "\n")


if __name__ == "__main__":
    chatbot()
