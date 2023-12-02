# main.py

import livefacerecognizer as lfr
import orginalNami as nami

## run face recognition
#recognized = lfr.recognition()
lfr
## if recognized, run Nami
#if recognized:
#    nami.run_Nami()
#else:
#    exit()

#def run_Nami():
#    command = take_command()
#    print(command)
#    if 'play' in command or 'can you play' in command or 'please play' in command:
#        song = command.replace('play', '') 
#        talk('playing ' + song)
#        pywhatkit.playonyt(song)
#        print("Enjoy...!")


#    elif 'play music from pc' in command or "play some rock music" in command:
#            talk("ok playing music from system")
#            music_dir = './music'
#            musics = os.listdir(music_dir)
#            os.startfile(os.path.join(music_dir, musics[0]))


#    elif 'tell a joke' in command or 'joke' in command or 'make me laugh' in command:
#        joke = pyjokes.get_joke()
#        talk(joke)
#        print(joke)


#    elif 'who is nami' in command or 'who are you' in command:
#        talk('I am nami, a virtual assistant')


#    elif 'How is nami' in command or 'how are you' in command or 'How are you doing' in command:
#        talk('I am Fine, Thanks for asking')


#    elif 'time' in command or 'whats time' in command or 'could u please tell whats the time' in command:
#        time = datetime.datetime.now().strftime('%I:%M %p')
#        talk('Current time is ' + time)
#        print('Current time is ' + time)
        

#    elif 'date' in command or 'whats date' in command or 'could u please tell whats today' in command:
#        date = datetime.datetime.now().strftime('%d /%m /%y')
#        talk('Current date is ' + date)
#        print('Today date is ' + date)


#    elif 'whats today' in command or 'today' in command or 'which day' in command:
#        day = datetime.datetime.today().weekday() + 1
#        # assigning a number of makes it a bit cleaner
#        Day_dict = {1: 'Monday', 2: 'Tuesday',
#                    3: 'Wednesday', 4: 'Thursday',
#                    5: 'Friday', 6: 'Saturday',
#                    7: 'Sunday'}
#        if day in Day_dict.keys():
#            weekday = Day_dict[day]
#        talk("Today is " + weekday)
#        print("Today is " + weekday)


#    elif 'who is' or 'talk about' in command:
#        person = command.replace('who is', '')
#        info = wikipedia.summary(person, 1)
#        talk(info)
#        print(info)