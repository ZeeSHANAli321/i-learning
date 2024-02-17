import openai
from googletrans import Translator
import os
import random
import pygame
""" from youtubesearchpython import VideosSearch, VideoSortOrder  # Import the necessary classes """

apikey = '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'

# Initialize the speech recognition engine


class ChatBot:
    def __init__(self):
        self.current_language = "en"  # Default language is English
        self.openai_api_key = apikey
        self.setup_openai()
        self.chat_history = []  # Store chat history as (query, response) pairs
        self.music_directory = r"C:\Users\madde\OneDrive\Desktop\song"
        self.setup_music_player()

    def setup_openai(self):
        openai.api_key = self.openai_api_key

    def setup_music_player(self):
        pygame.mixer.init()

    def change_language(self, new_language):
        self.current_language = new_language
        return f"Language changed to {new_language}."

    def ai_response(self, prompt):
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # Use a supported model name, e.g., "text-davinci-003"
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["text"]

    def play_random_song(self):
        music_files = [f for f in os.listdir(self.music_directory) if f.endswith(".mp3")]
        if music_files:
            random_song = random.choice(music_files)
            pygame.mixer.music.load(os.path.join(self.music_directory, random_song))
            pygame.mixer.music.play()
            return f"Now playing: {random_song}"
        else:
            return "No music files found in the directory."

    """ def search_youtube_video(self, query):
        videos_search = VideosSearch(query, limit=10)
        results = videos_search.result()
        if results:
            first_video = results['result'][0]
            video_title = first_video['title']
            video_url = first_video['link']
            return f"Here's the link to the video '{video_title}':\n{video_url}"
        else:
            return "No matching videos found on YouTube."

    def search_related_videos(self, query):
        videos_search = VideosSearch(query, limit=5, order=VideoSortOrder.Relevance)  # Limit the search to 5 videos
        results = videos_search.result()
        if results:
            related_videos = results['result']
            response = "Here are some related videos on YouTube:\n"
            for video in related_videos:
                video_title = video['title']
                video_url = video['link']
                response += f"- {video_title}: {video_url}\n"
            return response
        else:
            return "No related videos found on YouTube."
 """
    def chat(self, query):
        if "change your language" in query.lower():
            print("Available languages: 'en' (English), 'hi' (Hindi)")
            language_choice = input("Enter the language code you want to switch to: ").lower()
            if language_choice in ["en", "hi"]:
                return self.change_language(language_choice)
            else:
                return "Invalid language choice. Language remains unchanged."

        elif "play a song" in query.lower():
            return self.play_random_song()

        elif "search on youtube for" in query.lower():
            # Extract the query for YouTube search
            search_query = query.lower().replace("search on youtube for", "").strip()
            return self.search_youtube_video(search_query)

        elif "related videos" in query.lower():
            # Extract the query for related videos search
            related_query = query.lower().replace("related videos", "").strip()
            return self.search_related_videos(related_query)

        else:
            # Translate the user's query to the current language
            translator = Translator()
            translated_query = translator.translate(query, src='en', dest=self.current_language).text

            # Check if the current query relates to a previous question
            for prev_query, prev_response in reversed(self.chat_history):
                if prev_query.lower() in translated_query.lower():
                    prompt = f"gaurav: {translated_query}\n gaurav: {prev_response}"
                    response = self.ai_response(prompt)
                    # Translate the response back to the source language
                    translated_response = translator.translate(response, src='en', dest=self.current_language).text
                    return translated_response

            # If not related to a previous question, generate a new response
            response = self.ai_response(f"gaurav: {translated_query}\n gaurav: ")
            # Translate the response back to the source language
            translated_response = translator.translate(response, src='en', dest=self.current_language).text

            # Add the current query and response to chat history
            self.chat_history.append((translated_query, translated_response))
            return translated_response

    def get_response(self, user_input):
        return self.chat(user_input)

    def run(self):
        print('Welcome to gaurav AI')
        while True:
            print("Enter your query:")
            user_input = input("You: ")
            if "quit" in user_input.lower():
                break
            elif "reset chat" in user_input.lower():
                self.setup_openai()
            else:
                print("Chatting...")
                response = self.get_response(user_input)
                print(response)  # Display the response as text


if __name__ == '__main__':
    chatbot = ChatBot()
    chatbot.run()
