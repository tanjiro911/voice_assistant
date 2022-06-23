# Pre installed Modules
import datetime
import subprocess
import webbrowser
import platform
import time
import os
from playsound import playsound
# <---------------------------------------------->

# Modules to be installed manualy

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import pyautogui  # pip install pyautogui
import wikipedia  # pip install wikipedia
import wolframalpha
import requests
import pyjokes
import pywhatkit
import smtplib

# <--------------------------------------------->

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# To check which voice is installed in pc use the following command:
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)

# define speak fuction:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define wishme function that uses present time to greet you
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("vaishnavutkarsh.jpr@gmail.com", "utkarshvaishnav07619#")
    server.sendmail("vaishnavutkarsh.jpr@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # ---------> LOGICAL & COMPUTATIONAL QUERIES <--------------------------------------------------------------

        elif "Succeeder" in query:
            numb = int(input("of which no:  \n"))
            succeeder = numb + 1
            print(succeeder)

        elif "hcf" in query:
            num1 = int(input("Enter the First number:\n"))
            num2 = int(input("Enter the Second number:\n"))

            if num2 > num1:
                mn = num1

            else:
                mn = num2

            for i in range(1, mn + 1):
                if num1 % i == 0 and num2 % i == 0:
                    hcf = i

            print(f"The HCF of these two numbers is {hcf}")
            speak("The hcf of {num1} and {num2} is {hcf}")
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        elif "weather" in query:
            api_key = "a0bfb859d9737f01f4e9d1606e26ec9a"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(
                    " Temperature in kelvin unit is "
                    + str(current_temperature)
                    + "\n humidity in percentage is "
                    + str(current_humidiy)
                    + "\n description  "
                    + str(weather_description)
                )
                print(
                    " Temperature in kelvin unit = "
                    + str(current_temperature)
                    + "\n humidity (in percentage) = "
                    + str(current_humidiy)
                    + "\n description = "
                    + str(weather_description)
                )

        elif "calculate" in query:

            speak("calculating")
            # write your wolframalpha app_id here
            app_id = "9U75J8-KGK7EKP3YT"
            client = wolframalpha.Client(app_id)

            indx = query.lower().split().index("calculate")
            getinput = query.split()[indx + 1 :]
            res = client.query(" ".join(getinput))
            answer = next(res.results).text
            speak("The answer is " + answer)
            print("The answer is " + answer)

        elif "roman number" in query:

            def printRoman(number):
                num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
                sym = [
                    "I",
                    "IV",
                    "V",
                    "IX",
                    "X",
                    "XL",
                    "L",
                    "XC",
                    "C",
                    "CD",
                    "D",
                    "CM",
                    "M",
                ]
                i = 12
                while number:
                    div = number // num[i]
                    number %= num[i]

                    while div:
                        print(sym[i], end="")
                        div -= 1
                    i -= 1

            # Driver code
            if __name__ == "__main__":
                number = int(input("Enter the number:\n"))
                speak("Roman numeral is:", end=" ")
                printRoman(number, "\n")

        elif "lcm" in query:
            a = int(input("Enter first number:\n"))
            b = int(input("Enter second number:\n"))

            maxNum = max(a, b)

            while True:
                if maxNum % a == 0 and maxNum % b == 0:
                    break
                maxNum = maxNum + 1

            print(f"The LCM of {a} and {b} is {maxNum}")
            pyautogui.PAUSE = 6
            speak(f"the lcm of {a} and {b} is {maxNum}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "movies" in query:
            video_dir = "D:\\Non Critical\\MOVIES\\Mov"
            video = os.listdir(video_dir)
            speak("playing your movies")
            print(video)
            os.startfile(os.path.join(video_dir, video[0]))

        elif "punjabi" in query:
            music_dir = "D:\\Non Crritical\\songs\\Favorite Songs2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")

        if 'help' in query:
            speak('wait sir i am coming . coming satellite in 3........................2..........................1...................')

        if 'how are you' in query:
            speak('fine sir! what was your day in school')

        if 'exhausted' in query:
            speak('i know your feeling sir!')

        if 'why iron man choose you' in query:
            speak('because i"m very intelligent sir! LOL')

        elif 'tell me about yourself to my friend' in query:
            speak('Im JARVIS! . personal assistant of my sir Mr. Utkarsh')

        elif "hobbies" in query:
            speak(
                'Sir you would love to listen Punjabi and English songs and you have very uncoditional love towards football!')

        elif 'date' in query:
            speak('sorry, I have a headache')

        elif "hello" in query:
            speak("hey there")
            print("hi!")

        elif 'bye' in query:
            speak('bye sir! you can call me whenever you want')

        elif 'maybe' in query:
            speak('Sir! first of all complete your homework!')

        elif 'stop' in query:
            speak('ok sir as your wish!')

        if 'holiday' in query:
            speak('Oh Sorry Sir! By the way Sir did you have completed your homework?')

        elif "thank you" in query:
            speak("welcome, Quitting sir!")
            quit()

        elif "email to utkarsh" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "utkarshvaishnav.jpr@email.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir ! I am not able to send this email")

        elif "channel" in query:
            speak("ok sir wait for few minutes!")
            webbrowser.open("https://www.youtube.com/channel/UCDBJ-ctMQ09CEqMSh1t1kXw")

        elif "website" in query:
            speak("opening your website")
            webbrowser.open("https://linktr.ee/utkarsh_vaishnav")

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "rediffmail" in query:
            speak("opening rediff mail")
            webbrowser.open("mail.rediff.com")

        elif "open code" in query:
            speak("opening code!")
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open clipboard" in query or "show clipboard" in query:
            print("opening clipboard")
            pyautogui.keyDown("win")
            pyautogui.press("v")
            pyautogui.keyUp("win")

        elif "open task manager" in query:
            print("opening task manager")
            speak("opening task manager")
            pyautogui.keyDown("ctrl")
            pyautogui.keyDown("shift")
            pyautogui.keyDown("esc")
            pyautogui.keyUp("ctrl")
            pyautogui.keyUp("esc")
            pyautogui.keyUp("shift")

        elif 'volume up' in query or 'turn volume up' in query or 'up' in query:
            pyautogui.press("volumeup")
            speak('ok sir! turning volume up')

        elif 'volume down' in query:
            pyautogui.press("volumedown")
            speak("turning volume down!")

        elif 'mute' in query or 'volume' in query:
            pyautogui.press("volumemute")
            speak("ok sir!as your wish")

        if 'notepad' in query:
            speak("ok sir! opening notepad")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open workspace" in query:
            speak("opening folder")
            path_to_folder = "C:\\Program Files"
            os.startfile(path_to_folder)

        elif "minimise all" in query or "minimize all" in query:
            speak("ok sir! minimising all")
            pyautogui.keyDown("win")
            pyautogui.press("m")
            pyautogui.keyUp("win")

        elif "open ms" in query:
            speak("Opening Microsoft Word")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office.lnk')

        elif "make a note" in query:
            os.startfile(
                "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            )
            pyautogui.PAUSE = 5
            pyautogui.write(query)

        elif "clear the clutter" in query:
            speak("clearing the clutter")
            file = "G:\\main.py"
            os.startfile(file)
        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))
            else:
                speak(" City Not Found ")

        #elif "what is" in query or "who is" in query:

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'news' in query or 'latest news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "C:\\Users\\ASUS\\Downloads",
                                                       0)
            speak("Background changed successfully")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office.exe"
            os.startfile(power)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'search' in query:

            query = query.replace("search", "")
            webbrowser.open(query)

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
            speak("Recycle Bin Recycled")


        if 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        # ---------> PROBLEMS BASED ON QUESTION WORDS <-------------------------------------------------------------

        elif "what is your name" in query:
            speak("My name is Jarvis and I am Artificial Intelligence made by my honorable sir mr. Utkarsh Vaishnav")
            print("My name is Jarvis and I am Artificial Intelligence made by my honorable sir mr. Utkarsh Vaishnav")

        elif "who is your idol" in query:
            speak("my idol is my manufacturer, i mean Utkarsh")

        #elif "what" in query or "which" in query or "when" in query or "how" in query:
            #print("searching web...")
            #speak("searching web")
            #query = query.replace("search", "")
            #webbrowser.open_new_tab(query)
            #time.sleep(6)

        elif "what language" in query:
            print("i can speak english")

        elif "can you do my homework" in query:
            speak("no, but i can help you with your topics")

        elif "favourite colour" in query:
            speak("my favourite colour is orange")
            print("my favourite colour is orange!")

        elif "your age" in query:
            speak("my first version was released on 26 August two thousand twenty one")

        elif "address" in query:
            H_address = "your address"
            print(H_address)

        elif 'rock music' in query:
            music_dir = 'D:\\Rock Songs\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif (
            "find my phone" in query
            or "locate my phone" in query
            or "where is my phone" in query
        ):
            print("searching sir...")
            speak("searching sir")
            webbrowser.open("https://myaccount.google.com/find-your-phone?pli=1")
        elif "map" in query:
            print("ok sir wait for few seconds!")
            speak("ok sir wait for few seconds!")
            webbrowser.open("https://maps.google.com")

        elif 'current location' in query:
            webbrowser.open("https://earth.google.com//web//search//Jaipur,+Rajasthan//@26.88521061,75.79055741,433.20629213a,66393.52611984d,35y,0h,0t,0r//data=Cm4aRBI-CiQweDM5NmM0YWRmNGM1N2UyODE6MHhjZTFjNjNhMGNmMjJlMDkqFkphaXB1cgrgpJzgpK_gpKrgpYHgpLAYAiABIiYKJAkwfYUYNQM1QBEvfYUYNQM1wBmqISuZxblJQCGnISuZxblJwA")
            speak("sir wait for a few seconds !")
            time.sleep(15)
            speak("sir here is your current location!")
        elif 'metamask' in query:
            webbrowser.open("https://opensea.io/")
            speak("ok sir wait for few seconds !")

        # -------------------> TURN OFF THE PC <---------------------------------

        elif "log off" in query or "sign out" in query:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications"
            )
            print(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications"
            )
            subprocess.call(["shutdown", "/l"])

time.sleep(3)

# wolframalpha App ID = 9U75J8-KGK7EKP3YT