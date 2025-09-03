import requests
import json
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict={"breaking news":"https://newsapi.org/v2/everything?q=tesla&from=2025-07-12&sortBy=publishedAt&apiKey=78a8c5fddb7d40d9aae4899f4cd8ef26",
             "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=78a8c5fddb7d40d9aae4899f4cd8ef26",
             "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=78a8c5fddb7d40d9aae4899f4cd8ef26",
             "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=78a8c5fddb7d40d9aae4899f4cd8ef26",
             "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=78a8c5fddb7d40d9aae4899f4cd8ef26"}
    
    content=None
    url = None
    speak("which feild news do you want, [breaking news], [entertainment], [health], [science], [sports]")
    field = input ("type the feild name that you want:")
    for key,value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
                print ("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak ("hear is the first news")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url= articles["url"]
        print(f"for more info visit:{news_url}")

        a=input("[press 1 to cont] and [press 2 to stop]")
        if str(a)=="1":
            pass
        elif str(a)=="2":
            break

        speak("thats all")