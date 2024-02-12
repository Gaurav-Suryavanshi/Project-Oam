import os
import speech_recognition as sr
from win32com.client import Dispatch
import webbrowser
import datetime
import subprocess
from openai import OpenAI
import random
import cv2
import requests

TMDB_API_KEY = 'e46699161f0b7dd8356b06b96aa874f9'
def get_movie_rating(movie_title):
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': TMDB_API_KEY,
        'query': movie_title
    }
    response = requests.get(search_url, params=params)
    data = response.json()

    if response.status_code == 200 and data['results']:
        movie_id = data['results'][0]['id']
        movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            'api_key': TMDB_API_KEY,
        }
        movie_response = requests.get(movie_details_url, params=params)
        movie_data = movie_response.json()
        if movie_response.status_code == 200:
            rating = movie_data.get('vote_average')
            return f"The rating of {movie_title} is {rating} out of 10."
        else:
            return f"Sorry, I couldn't fetch the rating for {movie_title}."
    else:
        return f"Sorry, I couldn't find information about the movie {movie_title}."


NEWS_API_KEY = "31f1932d9f094afe9fc40ec9953ddafa"
def get_news():
    news_url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(news_url)
    news_data = response.json()

    if response.status_code == 200:
        articles = news_data.get('articles', [])
        if articles:
            for i, article in enumerate(articles[:10]):
                title = article.get('title', '')
                print(f"{i + 1}. {title}")
                speaker.speak(f"News {i + 1}. {title}")
        else:
            print("No news articles found.")
            speaker.speak("Sorry, no news articles found.")
    else:
        print(f"Error fetching news: {news_data.get('message', 'Unknown error')}")
        speaker.speak("Sorry, there was an error fetching news.")

OPENWEATHERMAP_API_KEY = '1e3ea8d22f2e6d4a68d9eaada1d5909f'
OWM_API_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
def get_weather(city):
    params = {
        'q': city,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric'  # Change to 'imperial' for Fahrenheit
    }

    response = requests.get(OWM_API_ENDPOINT, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        return f"The weather in {city} is {description}. The temperature is {temperature} degrees Celsius."
    else:
        return f"Sorry, I couldn't fetch the weather information for {city}."

chatStr = ""
def chat(query):
    global chatStr
    client = OpenAI(api_key="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")
    chatStr += f"Gaurav: {query}\n Oam:"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speaker.speak(response.choices[0].text)
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text
    print(chatStr)
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", 'w') as f:
        f.write(text)

def open_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow("Camera", frame)

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()

def ai(prompt):
    client = OpenAI(api_key = "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")
    text = f"OpenAI response for Prompt: {prompt} \n *********************** \n\n"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].text)
    text += response.choices[0].text
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", 'w') as f:
       f.write(text)

speaker = Dispatch("SAPI.SpVoice")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error Occurred. Sorry from Oam"

if __name__ == '__main__':
    s = "Jai SHREE RAAM, I am Oam"
    print(s)
    speaker.speak(s)

    while True:
        print("Listening....")
        query = takeCommand()
        sites = [["Youtube", "https://www.youtube.com/"],["WikiPedia", "https://www.wikipedia.com/"],
                 ["Google", "https://www.google.com/"],["chat gpt", "https://chat.openai.com/"]]
        for site in sites:

            if "open" in query.lower() and any(site[0].lower() in query.lower() for site in sites):
                site_name = next(site[0] for site in sites if site[0].lower() in query.lower())
                speaker.speak(f"What do you want to search on {site_name}?")
                search_query = takeCommand()
                search_url = next(site[1] for site in sites if site[0].lower() == site_name.lower())
                if search_query:
                    webbrowser.open(f"{search_url}/search?q={search_query}")
                    speaker.speak(f"Searching {search_query} on {site_name}.")
                else:
                    # If no search query provided, just open the site
                    webbrowser.open(search_url)
                    speaker.speak(f"Opening {site_name}.")
                break

            if "play music" in query:
                musicPath = "E:\Death Note\Itro - Never Let You Down [NCS Release].mp3"
                speaker.speak("Opening Music Sir")
                print("Opening Music Sir......")
                os.startfile(musicPath)
                break

            elif "who are you" in query:
                speaker.speak("I am a smart AI chatot, My name is project Oam")
                break

            elif "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                speaker.speak(f"Sir time is {hour} Buj kar {min} minute")
                break
                #speaker.speak(query)

            elif "who is Gaurav" in query:
                speaker.speak("Gaurav is my God, because he creates me.")
                break

            elif "who is Anshita" in query:
                speaker.speak("Anshita chota Bacha hai.")
                break

            elif "open notepad" in query:
                subprocess.Popen([notepad.exe])
                speaker.speak("Opening notepad sir")
                break

            elif "using artificial intelligence".lower() in query.lower():
                ai(prompt=query)
                break

            elif "open camera" in query:
                speaker.speak("Opening camera sir")
                open_camera()
                break

            elif "weather in".lower() in query.lower():
                city = query.split("weather in")[1].strip()
                weather_info = get_weather(city)
                print(weather_info)
                speaker.speak(weather_info)
                break

            elif "latest news".lower() in query.lower():
                get_news()
                break

            elif "find the movie rating" in query:
                movie_title = query.split("movie rating of")[1].strip()
                rating_info = get_movie_rating(movie_title)
                print(rating_info)
                speaker.speak(rating_info)
                break



            else:
                chat(query)
                break