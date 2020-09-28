import pyautogui
import datetime
import time
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good night"

time="{}!".format(greeting)
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
greeting=(time+"Welcome Ashikul Sir . How can I help you?")
speak.Speak(greeting)

a=True
while a==True:


        search=input("Write here what you want to know: ")
        if search=='time':
            import time
            # from gtts import gTTS

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
            current_time1 = str(current_time)
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(current_time1)
            # language = 'en'
            # name_obj1 = gTTS(text=current_time1, lang=language, slow=False)
            # name_obj1.save("time.mp3")
            # from playsound import playsound
            #
            # playsound('time.mp3')
        if search=='gmail':
            import smtplib
            sender= input("Sender name:")
            text=input("write your text here :")

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("shahriabig06@gmail.com", "shahriar222006@")
            server.sendmail("shahriabig06@gmail.com", sender, text)

            server.quit()
            successful = "Sent successfully"
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(successful)
            # language = 'en'
            # name_obj = gTTS(text=successful, lang=language, slow=False)
            # name_obj.save("sucessful.mp3")
            # from playsound import playsound
            #
            # playsound('sucessful.mp3')
        if search=='quit':
            a=False
            break
        if search=='wikipedia':
            try:
                search1=input("Write here:")
                import wikipedia
                name_text2="It will need some time. Please wait."
                # language = 'en'
                # name_obj = gTTS(text=name_text2, lang=language, slow=False)
                # name_obj.save("name_text2.mp3")
                # from playsound import playsound
                # playsound('name_text2.mp3')
                import win32com.client as wincl

                speak = wincl.Dispatch("SAPI.SpVoice")
                speak.Speak(name_text2)
                search_text=wikipedia.summary(search1)
                search_text1=str(search_text)
                print(search_text1)
                # language = 'en'
                # name_obj = gTTS(text=search_text1, lang=language, slow=False)
                # name_obj.save("wikisearch1.mp3")
                # from playsound import playsound
                # playsound('wikisearch1.mp3')
                import win32com.client as wincl

                speak = wincl.Dispatch("SAPI.SpVoice")
                speak.Speak(search_text1)
            except:
                cant="I can't find it. Please another."
                # language = 'en'
                # cant_obj = gTTS(text=cant, lang=language, slow=False)
                # cant_obj.save("cant.mp3")
                # from playsound import playsound
                #
                # playsound('cant.mp3')
                import win32com.client as wincl

                speak = wincl.Dispatch("SAPI.SpVoice")
                speak.Speak(cant)
        if search=='Take note':
            write_note= "Write Your note sir"
            # language = 'en'
            # note_speech = gTTS(text=cant, lang=language, slow=False)
            # note_speech.save("note.mp3")
            # from playsound import playsound
            #
            # playsound('note.mp3')
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(write_note)

            takenote=open('note.txt','a')
            note=input("Give your note:")
            takenote.write(note)

        if search=='show note':

            read_takenote=open('note.txt')
            read_file=read_takenote.read()
            speech_note=read_file
            # language = 'en'
            # speech_note1 = gTTS(text=read_file, lang=language, slow=False)
            # speech_note1.save("note.mp3")
            # from playsound import playsound
            #
            # playsound('note.mp3')
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(read_file)

            print(read_file)
            read_takenote.close()

        if search=='google translate':
            from googletrans import Translator
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("Please give your text and your source language and destination language.")


            translator = Translator()
            text=input("Give your text here:")
            sorce_language=input("Give your source language:")
            destination_language=input("Give your destination language:")



            result = translator.translate(text, dest=destination_language,src=sorce_language)

            print('From:',sorce_language)
            print('To:',destination_language)
            print('Your result is :',result.text)
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(result.text)
        if search=='website':
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("Give your website name in the text box below sir.")
            website=input("Write your website name:")
            website_url='http://'+website+'.com'
            import webbrowser

            webbrowser.open(website_url, new=2)
        if search=='calendar':
            import calendar
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("Please give your year and  month must be number .")


            # Enter the month and year
            yy = int(input("Enter year: "))
            mm = int(input("Enter month: "))

            # display the calendar
            print(calendar.month(yy, mm))
        if search=='today date':
            from datetime import date

            today = date.today()
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(today)
        if search=='messenger':
            from fbchat import Client
            from fbchat.models import *

            userid = {'abrar auntakib': '100052754273527', 'emran nader': '100043127960705',
                      'mohammed kalam': '100002460758668'}
            b = True
            while b == True:
                search = input("Write here:")
                if search == 'log in':
                    import win32com.client as wincl

                    speak = wincl.Dispatch("SAPI.SpVoice")
                    speak.Speak("logging in")
                    client = Client('amoona099.aa@gmail.com', 'shahriar')

                    client.login('amoona099.aa@gmail.com', 'shahriar')
                    import win32com.client as wincl

                    speak = wincl.Dispatch("SAPI.SpVoice")
                    speak.Speak('logged in successfully')
                if search == 'send message':
                    try:
                        userid = {'abrar muntakib': '100052754273527', 'emran nader': '100043127960705',
                                  'mohammed kalam': '100002460758668','farhan saeed':'100044099033695','awlad rahim':'100023223665820','helal sir':'100049397701683','500 tk apu':'100043423841363'}
                        username = input('Write user name:')
                        userid1 = userid.get(username)
                        userid2 = str(userid1)
                        text1 = input("Write your text:")
                        client.send(Message(text=text1), thread_id=userid2, thread_type=ThreadType.USER)
                        import win32com.client as wincl

                        speak = wincl.Dispatch("SAPI.SpVoice")
                        speak.Speak('sent sucessfully')
                    except:
                        import win32com.client as wincl
                        speak = wincl.Dispatch("SAPI.SpVoice")
                        speak.Speak("can't sent ")

                if search == 'find user':
                    user_name = input("User name:")

                    users = client.searchForUsers(user_name)
                    user = users[0]
                    print("User's ID: {}".format(user.uid))
                    dic_userid = user.uid
                    print("User's name: {}".format(user.name))
                    print("User's profile picture URL: {}".format(user.photo))
                    print("User's main URL: {}".format(user.url))

                # client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)
                if search == 'log out':
                    client.logout()
                    import win32com.client as wincl

                    speak = wincl.Dispatch("SAPI.SpVoice")
                    speak.Speak('log out in sucessfully')
                    b= False
        if search=='play a song':
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak('write your song name')
            songname=input("Write the song name:")
            songname1=songname+'.mp3'
            from pygame import mixer  # Load the popular external library

            mixer.init()
            mixer.music.load(songname1)
            mixer.music.play()

        if search=='read a poem':
            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak('write your poem name')
            poemname = input("Write the poem name:")
            poemname1 = poemname + '.mp3'
            from pygame import mixer  # Load the popular external library

            mixer.init()
            mixer.music.load(poemname1)
            mixer.music.play()

        if search=='alarm':
            import datetime

            import win32com.client as wincl

            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("write time and minute ")

            alarmHour = int(input("What hour do you wake up:"))
            alarmMinute = int(input("what minute do you want to wake up:"))
            alarm=input("Write your alarm note:")

            amPm = str(input("pm or am:"))

            if (amPm == 'pm'):
                alarmHour = alarmHour + 12

            while (1 == 1):
                if (alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):

                    import win32com.client as wincl

                    speak = wincl.Dispatch("SAPI.SpVoice")
                    speak.Speak(alarm)
                    a10=input("write here:")
                    if a10=='quit':
                        break

                    # from pygame import mixer  # Load the popular external library
                    #
                    # mixer.init()
                    # mixer.music.load('tune1.mp3')
                    # mixer.music.play()
                    # break


        if search=='take screenshot':
            import pyautogui

            name = input("Give your image name:")

            time = int(input("Write here your time:"))

            img = pyautogui.screenshot()

            name1 = name + '.jpg'
            img.save(name1)

        if search=='google search':
            import pyautogui
            import time

            a = input("search here Google:")
            b=input('minimize or maximize:')
            if b=='min':
                pyautogui.doubleClick(321, 764)
                time.sleep(5)
                pyautogui.click(258, 79)

                pyautogui.write(a)
                pyautogui.press('enter')
            if b=='max':
                pyautogui.doubleClick(321,764)
                time.sleep(5)
                pyautogui.click(424,56)
                pyautogui.write(a)
                pyautogui.press('enter')
        if search=='open word':
            write=input("whtat you want to write:")
            a1=input("file naem:")
            import time
            pyautogui.doubleClick(661,749)
            time.sleep(2)
            pyautogui.click(892,563)
            time.sleep(1)
            pyautogui.doubleClick(488,237)
            pyautogui.write(write,interval=0.09)
            time.sleep(1)
            pyautogui.click(31,43)
            time.sleep(1)
            pyautogui.click(42,199)
            time.sleep(1)
            pyautogui.click(259,215)
            time.sleep(1)
            pyautogui.click(545,205)
            time.sleep(1)
            pyautogui.press('backspace')
            time.sleep(1)
            pyautogui.click(373,347)
            time.sleep(1)
            pyautogui.write(a1,interval=0.09)
            time.sleep(1)
            pyautogui.click(504,472)
            pyautogui.click(1314,55)

        if search=='open gameloop':
            import time
            pyautogui.FAILSAFE=False
            pyautogui.doubleClick(1059,748)
            time.sleep(3)
            pyautogui.doubleClick(1139,636)
            # time.sleep(3)
            # pyautogui.click(803,422)







