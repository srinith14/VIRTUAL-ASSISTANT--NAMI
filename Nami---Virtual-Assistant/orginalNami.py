import os
import speech_recognition as sr
import pyttsx3

import webbrowser
import pywhatkit
import wikipedia
import datetime
import pyjokes

import password_gen as pg
#import livefacerecognizer as lfr

import random

listener = sr.Recognizer()
engine = pyttsx3.init()



# List of general responses
general_responses = ['Sorry, I didn\'t understand what you said.', 'Can you please rephrase that?', 'I\'m not sure what you mean.']

def files():
    db_dir1 = './music'
    if not os.path.exists(db_dir1):
        os.mkdir(db_dir1)

    log_path = './log.txt'
    with open(log_path, 'a') as f:
                    f.write('{:<5} | {:<10} | {}\t '.format("Entry", str(datetime.datetime.now()),("\t#"*4)))
                    f.close()
    
    with open(log_path, 'a') as f:
                    f.write('{:<5} | {:<10} | {}\n'.format("Exit", str(datetime.datetime.now()),""))
                    f.close()

    db_dir2 = './notes'
    if not os.path.exists(db_dir2):
        os.mkdir(db_dir2)
    #print("Log Files created")


def talk(text):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 2.0)
    engine.say(text)
    engine.runAndWait()


def greeting():
    greets = ['Hello!', 'Hi!', 'Hey there!', 'Greetings!']
    talk(random.choice(greets))

    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        talk ("Good morning!")
    elif 12 <= hour < 18:
        talk ("Good afternoon!")
    elif 18 <= hour < 21:
        talk ("Good evening!")
    else:
        talk ("Good evening!")
    
    talk("I am Nami version 1")
    # This is a simple greeting & it informs the user that the assistant has started
    #engine.say("Hello, I am Nami version 1")
    #engine.say("How could I assist you today?")
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('\nlistening...')
            voice = listener.listen(source)
            listener.pause_threshold = 1
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}\n")
            
            if 'Nami' in command:
                command = command.replace('Nami', '')
                #print(command)
    except Exception as e:
        talk(random.choice(general_responses))
        return None

    return command


def run_Nami():
    
    files()
    greeting()

    command = take_command()
    print(command)
    
    if 'play some tracks from my desktop' in command or 'some tunes from my computer' in command or 'play some music from my computer' in command or 'play a song from my laptop':
        music_dir = 'C:\\Users\\yasha\\source\\repos\\NAMI Virtual assistant\\music\\'
        musics = os.listdir(music_dir)
    
        if not musics:
            talk("Sorry, there are no music files in the specified directory.")
            return
    
        music_file = random.choice(musics)
        file_path = os.path.join(music_dir, music_file)
    
        os.startfile(file_path)
        talk(f"Playing {music_file}. Enjoy!")

    elif 'play' in command or 'can you play' in command or 'please play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        print("Enjoy...!")

    elif 'tell a joke' in command or 'joke' in command or 'make me laugh' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'who is nami' in command or 'who are you' in command:
        talk('I am nami, a virtual assistant')

    elif 'How is nami' in command or 'how are you' in command or 'How are you doing' in command:
        talk('I am Fine, Thanks for asking')

    elif 'time' in command or 'whats time' in command or 'could u please tell whats the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)
        
    elif 'date' in command or 'whats date' in command or 'could u please tell whats today' in command:
        date = datetime.datetime.now().strftime('%d /%m /%y')
        talk('Current date is ' + date)
        print('Today date is ' + date)

    elif 'whats today' in command or 'today' in command or 'which day' in command:
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        if day in Day_dict.keys():
            weekday = Day_dict[day]
        talk("Today is " + weekday)
        print("Today is " + weekday)

    elif 'who is' in command or 'talk about' in command:
        person = command.replace('who is', '').replace('talk about', '')
        try:
            info = wikipedia.summary(person, 1)
            talk(info)
            print(info)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:3]
            talk(f"Which {person} do you mean?")
            for i, option in enumerate(options):
                talk(f"{i+1}. {option}")
            option = take_command()
            if option.isdigit() and int(option) <= len(options):
                info = wikipedia.summary(options[int(option)-1], 1)
                talk(info)
                print(info)
            else:
                talk("Sorry, I didn't understand your choice.")

    elif 'generat password' in command or 'password' in command:
        talk("Generating Password please wait...")
        talk("Enter the required details.")
        pg.generate()

    elif 'show password' in command or 'retrive password' in command:
        talk("Retriving Password please wait...")
        talk("Enter the required details.")
        pg.retrive()

    elif 'Write a to-do' in command or 'Capture an idea' in command or 'Record a thought' in command or 'Note down a task' in command:
        talk("What should I write, sir?")
        note = take_command()
        file_path = os.path.join(db_dir2, 'Notes.txt')
        with open(file_path, 'a') as file:
            talk("Hmm... Should I include date and time?")
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        talk("Your note has been saved, sir.")

    elif 'List my notes' in command or 'read my notes' in command or 'Access my notes' in command or 'Show my recorded notes' in command:
        talk("Showing Notes")
        file_path = os.path.join(db_dir2, 'Notes.txt')
        with open(file_path, "r") as file:
            notes = file.readlines()
            if len(notes) == 0:
                talk("You don't have any notes saved, sir.")
            else:
                for note in notes:
                    talk(note.strip())


    else:
        talk('Please say the command again.')


while True:
    run_Nami()