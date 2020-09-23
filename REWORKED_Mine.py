#current status: working, new scraper and some fancy python project
import time
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
glaDOSname="GlaDOS"
myname="query"

def speak(audioString):#say text
    #print(glaDOSname,':',audioString)
    print("{}: {}".format(glaDOSname,audioString))
    engine.say(audioString)
    engine.runAndWait()

def getQuery():#get text
    data=""
    data=input("{}: ".format(myname))
    return(data)

def getNews():
    import requests
    from bs4 import BeautifulSoup
    
    my_url_news='https://www.bbc.com/news/world/'
    news_webpage_view_choice2=''
    speak("No problem")
    speak("Where are you now exactly? ")
    
    print("-World\n-Africa\n-Australia\n-Europe\n-Latin America\n-Middle East\n-US and Canada")
    news_region_choose=input("query: ")

    if str.lower(news_region_choose) in ["africa"]:
        my_url_news +="africa"
    elif str.lower(news_region_choose) in ["australia","aussie"]:
        my_url_news += "australia"
    elif str.lower(news_region_choose) in ["europe","eu"]:
        my_url_news += "europe"
    elif str.lower(news_region_choose) in ["latin america"]:
        my_url_news += "latin_america"
    elif str.lower(news_region_choose) in ["middle east","middleeast"]:
        my_url_news += "middle_east"
    elif str.lower(news_region_choose) in ["us and canada","us","canada"]:
        my_url_news += "us_and_canada"
    elif str.lower(news_region_choose) in ["world","all"]:
        my_url_news = 'https://www.bbc.com/news/world/'

    else:
        speak("Unavailable region")
        speak("So, I've decided to open the World News by default")


    speak("Do you want me to read headlines?")
    headlineRead=input("query: ")
    if headlineRead in ['yes','Yes','y','yep','YES','Y','sure']:#readingheadlines

        speak("Please wait a bit")
               
        source=requests.get(my_url_news).text
        soup=BeautifulSoup(source,'lxml')

        article1=soup.find('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor"})
        speak("\nNews headlines provided by BBC news")
        speak("\nMain headline: "+article1.text)

        articlez=soup.find_all('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})
        for i in range(6):
            speak(articlez[i].text)
        print()
    else:
        speak("Please wait a bit")
               
        source=requests.get(my_url_news).text
        soup=BeautifulSoup(source,'lxml')

        article1=soup.find('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor"})
        print("\nNews headlines provided by BBC news")
        print("\nMain headline: "+article1.text)

        articlez=soup.find_all('a', attrs={"class":"gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})
        for i in range(6):
            time.sleep(0.5)
            print(articlez[i].text)
        speak("Here you go!\n")

    speak("Would you like to visit the webpage?")
    news_webpage_view_choice=input("me: ")
    if news_webpage_view_choice in ['yes','Yes','y','yep','YES','Y','sure']:
        from selenium import webdriver
        speak("Please wait for page to load. It might take awhile.")
        PATH=r"C:\Users\asus\AppData\Local\Programs\Python\Python37\tests"

        driver = webdriver.Firefox(PATH)
        driver.get(my_url_news)
        driver.maximize_window()

        speak("When you are finished, you can just close the browser ")

def joke():
        import requests
        from bs4 import BeautifulSoup

        
        my_url_joke='https://icanhazdadjoke.com/'

        speak("Here's a joke for you")
        

        source=requests.get(my_url_joke).text
        soup=BeautifulSoup(source,'lxml')

        joke1=soup.find('p', attrs={"class":"subtitle"})

        speak(joke1.text)
        speak("Ha ha ha")

def wikipedia():
    speak("Here's a random wikipedia article")
    from selenium import webdriver
    PATH=r"C:\Users\asus\AppData\Local\Programs\Python\Python37\tests"

    driver = webdriver.Firefox(PATH)
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    driver.maximize_window()

def brawlstars():
    import random
    brawlstars_char=["Shelly","Nita","Colt","Bull","Jessie","Brock","Dynamike","Bo","Tick","8-Bit","Emz",
    "El Primo","Barley","Poco","Rosa","Rico","Darryl","Penny","Carl","Piper","Pam","Frank","Bibi","Bea",
    "Mortis","Tara","Gene","Max","Mr. P","Spike","Crow","Leon","Sandy","Gale","Surge"] 
    random_brawler=random.randint(1,35)
    print(brawlstars_char[34])
    speak("Here's a random Brawlstars character")
    speak(brawlstars_char[random_brawler])

def wolframA():
    global questionWolf
    if questionWolf == "":
        question=data
    else:
        question=questionWolf
        
    speak("I'm thinking, please wait a bit")
    import wolframalpha
    
    app_id = '3G7H4A-A83G9LY4G6'
    client = wolframalpha.Client(app_id) 
    res = client.query(question)
    answer = next(res.results).text 
    speak(answer)

def gamePong():
    import importlib
    module=importlib.import_module("pong", package=None)
    importlib.reload(module)

def changeMyName():
    global dataOrig
    global myname
    yourName=[]
    yourName=dataOrig.split()
    myname=yourName[-1]
    speak(myname)
    speak("Sure. I guess that's your name now")

def changeHerName():
    global dataOrig
    global glaDOSname
    glaDOSname1=[]
    glaDOSname1=dataOrig.split()
    glaDOSname=glaDOSname1[-1]
    speak(glaDOSname)
    speak("Sure. I guess that's my new name now")

def GladosMain(data):#main process
    global dataOrig
    dataOrig = data
    data=str.lower(data)

    if "how are you" in data or "how are you?" in data:
        speak("I am fine")

    elif "stop" in data or "good bye" in data or "quit" in data:#END LOOP
        speak("Good bye")
        global mainLoopChk
        mainLoopChk=False

    elif 'hello' in data or 'hi' in data:
        speak("Hi!")

    elif "kill me" in data:
        speak("Bang!")

    elif 'play game' in data or 'play pong' in data:
        gamePong()

    elif 'brawlstars' in data or 'brawler' in data:
        brawlstars()

    elif 'joke' in data:
        joke()
        
    elif 'wikipedia' in data or 'wiki' in data:
        wikipedia()

    elif 'compute' in data or 'do you know' in data or 'wolfram' in data or 'i have a question' in data or 'ask you a question' in data:
        global questionWolf
        speak("Sure. I'll try my best to answer. What is your question?")
        questionWolf=input("{}: ".format(myname))
        wolframA()

    elif "news" in data:#apiKey=6f7902d95ff74002ac01a5d90cbf7477' from newsapi.
        getNews()

    elif "your name is" in data:
        changeHerName()

    elif "call me" in data or "my name is" in data:
        changeMyName()
        
    elif "say my name" in data:
        speak(myname)

    elif "say your name" in data:
        speak(glaDOSname)
    
    else:
    #    speak("I'm sorry, I couldn't understand you. Please, repeat your query")
        wolframA()




#LOOP STARTS

time.sleep(2)
speak("Hello! What can I do for you?")

mainLoopChk=True
while mainLoopChk:
    questionWolf=""#not to answer the same question
    data=getQuery()
    GladosMain(data)

