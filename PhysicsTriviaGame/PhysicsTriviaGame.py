#-----------------------------------------------------------------------------
# Name:        Physics Trivia Game
# Purpose:     Final Project
#
# Author:      Vamiq Valji
# Created:     29-Oct-2020
# Updated:     06-Nov-2020
#-----------------------------------------------------------------------------
# YOU WILL NEED PYGAME ZERO TO RUN THIS PROGRAM.
# EVERY SINGLE ASSET EXCEPT TEXT FONTS IN THE PROGRAM WAS CREATED BY VAMIQ VALJI. THIS MEANS I CREATED THE USED IMAGES AND MUSIC. PLEASE READ THE READ.md FOR ANY MORE INFORMATION
# ON WHAT PORTIONS I CREATED.
# THE POPPINS FONT I USED CAN BE FOUND HERE: https://fonts.google.com/specimen/Poppins?query=poppins
#
# I think this project deserves a 4+ OR A 100% because ...
# I took a simple concept of a trivia game and went above and beyond in every way of what was being asked of me in the project criteria.
#
#Features Added:
#   - Random trivia question generated each time game refreshes via lists (after player picks correct or incorrect answer from previous question, a new question is shown)
#   - Extensive list of trivia questions and images
#   - Usage of import random
#   - Usage of import operator to sort dictionaries by value when the dictionary had both a string and integer component to it
#   - Visual feedback to user when they answer a question (correct and incorrect game state screens)
#   - Added a play again option; allowing player to try again without restarting with MU controls.
#   - Displays strikes IN IMAGE FORMAT (three wrong answer inputs from the player, and they are out)
#   - Displays SMOOTH time left bar - Beep sounds play within the last few seconds of the round, indicating to the player that they are running out of time to answer the given question - Also changes color depending on how much
#     time the player has left to answer the question. The amount of time left changes the color from green to yellow to red, from most to least amount of time the player has to answer the question left.
#     Not only does the player now have a visual representation of how much time they have to answer the question (in a format that stands out),
#     though they also have sound feedback (the game starts playing beep sounds within the last few seconds of time left to indicate to the player that their time to answer the question is running out)
#   - Score system - The faster you answer a question and get it right, the more points you get. Your highest amount of points at the end of a game gets saved on the user's
#     storage drive. You can view your ranking compared to other "players" on the scoreboard game state screen
#   - Game stopped when going to the menu - When you are in the midst of a game, you can always go back and navigate throughout the start screen. Your game
#     progress will be saved as long as the application is open.
#   - Back button included
#   - Start screen included
#   - Detailed help screen included
#   - Win screen (game state "highscoreBeat") included
#   - Lose screen (game state "highscoreNotBeat")  included
#   - Help screen included
#   - Scoreboard screen included - This screen has a reset high score button and updates live.
#   - Global sounds to provide user feedback - Different sounds were used for different events. For example, a user click would play a different sound than when the game ends.
#   - Global music to provide user engagement - This music changes depending on what screen you are on. For example, the music that plays on the game screen is different than the music that plays on the start screen.
#   - Sound on and off toggle image button included (on start screen)
#   - UI is clean and easy to follow - Everything is displayed with cleanliness in mind; text won't fall out of place via usage of text boxes - Lots of pictures to keep user engagement
#   - Graphics are used uniquely on each screen to provide context and user engagement
#   - Billy the stickman is the mascot of the game. He acts as a buddy to the player on their learning adventure together. He greets you on the start screen with
#     a randomized message. He also encourages you and and gives you compliments if you do well, via speech bubble and randomly picked text. He is seen constantly
#     throughout the application, and you will see what I mean quickly once you play the game.
#   - Question and profile data are primarly saved under "QuestionData.py"; displaying elegant file management and utilization
#   - The question and profile data are set up in a very modular way, in such that the developer can add a question or profile in a very easily understandable format which
#     which doesn't require going back and fixing code in the main file (PhysicsTriviaGame.py). More information on this is is "QuestionData.py"
#   - Use of more than one font
#   - There are two different TYPES of questions. There are multiple choice questions in this game, and true or false questions; providing variety to the player. This creates
#     for a more fun and memorable experience.
#   - Use of different Python file (QuestionData.py) to store information used in this script in a modular and elegant way. Please read through "QuestionData.py" for more information.
#   - Different (though similar) end screens based on whether the player beat their high score or not.
#-----------------------------------------------------------------------------

import random # Used to randomize questions, Billy the stickman's messages (you will understand this better as you read more of the comments), and more
from QuestionData import * # Imports all data from QuestionData.py
import operator # I used commands from this to sort dictionaries by integer value when the integer value had a string counterpart. This can be seen in the scoreboard portion of my program.

WIDTH = 1024 # Sets the width of the application
HEIGHT = 768 # Sets the height of the application

# SOME OF MU'S PRE-CREATED FUNCTIONS WOULDN'T ACCEPT FUNCTION ARGUMENTS - SO I USED "global"

# BOX AND COLOR ASSIGNMENTS
WHITE = 255,255,255
GREY = 200,200,200
BLACK = 0,0,0
startColor = 16,16,16
startFill = Rect((0, 0), (1024, 768))
startButtonBox = Rect((400, 308), (200, 50))
helpButtonBox = Rect((400, 368), (200, 50))
scoreboardButtonBox = Rect((400, 428), (200, 50))
#playAgainBox = Rect((170, 250), (250, 75))
backButtonBox = Rect((10, 10), (100, 50))
quitRect = Rect((715, 560), (75, 30))
resetQuestionScreenRect = Rect((630, 560), (75, 30))
currentSizeBox = Rect((635, 60), (140, 25))
resetQuestionBox = Rect( (635, 30), (75, 25) )
soundButtonBox = Rect((10, 680), (100, 100))
multipleChoiceBox1 = Rect((615, 255), (300, 80))
multipleChoiceBox2 = Rect((615, 360), (300, 80))
multipleChoiceBox3 = Rect((615, 465), (300, 80))
multipleChoiceBox4 = Rect((615, 570), (300, 80))
trueBox = Rect((615, 280), (300, 160))
falseBox = Rect((615, 460), (300, 160))
questionImageBox = Rect((255, 250), (350, 400))
resetHighscoreBox = Rect((840, 10), (173, 35))

# VARIABLE ASSIGNMENTS

currentScore = 0
highScore = 0
strikes = 0
gameState = "initializeStart"
# Highscore file read
highScoreRead = open("highscore.txt", "r")
highScore = int(highScoreRead.read())
#Sound variables
sound = True # This variable controls if sound is on or off # If the sound variable is True, sounds play
soundS = "On" #
# Answer variable - Used to indicate answer of question given to the player
answer = ""
# Reset question variable
resetQuestion = 1
# Clock / time variables
timer = 0
timeLeft = 15
timeLeftSmooth = 900
# Scoreboard update highScore
profiles["YOU"] = highScore # Adds player profile to "profiles" dictionary (from "QuestionData.py")
sortedProfiles = (sorted(profiles.items(), key=operator.itemgetter(1),reverse=True)) # The "itemgetter(1)" is referencing the index of the dictionary, ex:
# dict = {e: 20}
# The '.itemgetter(1)' would reference the "20" (2nd index), meaning it is sorting by number value in this case
# print(sortedProfiles)#[1][1] # The first "[1]" would reference a dictionary in the dictionary (one of the profile dictionaries inside the of the "profiles"
# dictionary that encases all of the profiles, more on this at the bottom of "QuestionData.py"). The second "[1]" references the index of the component of the dictionary in that dictionary.
# Again, to better understand what I mean, looking at the bottom of "QuestionData.py" will help to gain a better perspective.
previousAnswerRightWrong = "start" # This variable is used in functions regarding Billy's encouragement messages. Billy will display "Good luck!" at the beginning of each game.
# These variables are also used in regard to Billy's messages, though are used to randomly pick a message from a list in "QuestionData.py"
randomNumRight = randomInt = random.randint(0, len(encouragementRight) - 1)
randomNumWrong = randomInt = random.randint(0, len(encouragementWrong) - 1)
randomNumWelcome = randomInt = random.randint(0, len(welcomeMessages) - 1)

def draw(): # Draws out most objects # draw() can't take any arguments, so I will use globals
    global gameState
    global randomInt
    global choiceBox1
    global choiceBox2
    global choiceBox3
    global choiceBox4
    global answer
    global strikes
    global currentScore
    global highScore
    global randomInt
    global resetQuestion
    global timeLeft
    global timer
    global previousAnswerRightWrong
    global strikeCrosses
    global sound
    global soundS
    global timeLeftSmooth
    if resetQuestion == 1: # When resetQuestion is set to '1', the question changes. I opted for using an if statement in this case instead of a function due to earlier issues of a function not working here as a viable option.
        randomInt = random.randint(0, len(questions))
        if randomInt > (len(questions)-1):
            randomInt -= 1
        resetQuestion = 0
        timeLeft = 15
        timeLeftSmooth = 900
    if gameState == "play":
        screen.draw.filled_rect(startFill, startColor) # Clears the screen
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("Pick The Correct Answer", midtop=(500, 75), fontsize=30)
        screen.draw.text("Current Score: " + str(currentScore), midtop=(878, 700), fontsize=40)
        screen.draw.text("High Score: " + str(highScore), midtop=(900, 730), fontsize=40)
        if timeLeft > 9: # The amount of time left changes the color from green to yellow to red, from most to least amount of time to answer the question left.
            screen.draw.filled_rect(Rect((300, 130), (400 * (timeLeftSmooth / 900), 35)),  (64, 255, 0)) # SMOOTH timer bar - Visually displays how much time is left for the player to answer their given question
        elif timeLeft > 5:
            screen.draw.filled_rect(Rect((300, 130), (400 * (timeLeftSmooth / 900), 35)),  (242, 255, 0))
        else:
            screen.draw.filled_rect(Rect((300, 130), (400 * (timeLeftSmooth / 900), 35)),  (255, 0, 0))
        screen.draw.text("TIME REMAINING: " + str(int(timeLeftSmooth / 60)) + "s", midtop=(500, 129), fontsize=25, fontname='poppinsregular',scolor = "black",shadow=(1.0,1.0)) # Drawn after everything so the timer bar doesn't interfere with the visibility of the text
        screen.draw.rect(Rect((300, 130), (400, 35)),  WHITE) # White rect that outline the time left box (for style and visibility of how much time has passed)
        displayEncouragement(previousAnswerRightWrong,randomNumRight,randomNumWrong) # Billy's encouragement questions # The function is near the bottom of this Python file
        displayStrikes() # Calls function that displays the current amount of strikes at the bottom of the screen # Only called on certain game states
        # The following code will make more sense when looking at this example (found in "QuestionData.py"):
        #question2 =	{
        #  "question": "If Billy started at point A, went through point C, and ended at point B, what was his DISTANCE TRAVELED?",
        #  "answer1": "5m",
        #  "answer2": "2m",
        #  "answer3": "3m",
        #  "answer4": "4m",
        #  "image": "question1image",
        #  "answer": 1,
        #  "trueOrFalse": "False"
        #} Please keep in mind the above code when looking at the following code. It will help you see where it is grabbing the question data from.
        screen.draw.textbox( (((questions[randomInt])["question"])) , (212, 190, 724, 60)) # (((questions[randomInt])["question"])) is simply accessing a random question ([randomInt]) key value of the key "question" from the "questions" dictionary.
        # This dictionary can be found in "QuestionData.py"
        if (((questions[randomInt])["image"])) == "placeholder": # If the developer or someone adding questions doesn't have an image for their question yet (more information on this in "QuestionData.py")
            screen.draw.filled_rect(questionImageBox, startColor)
        else:
            screen.blit( (((questions[randomInt])["image"])) , (255, 250) )
        if (((questions[randomInt])["trueOrFalse"])) == "False":
            screen.draw.filled_rect(multipleChoiceBox1, WHITE)
            screen.draw.filled_rect(multipleChoiceBox2, WHITE)
            screen.draw.filled_rect(multipleChoiceBox3, WHITE)
            screen.draw.filled_rect(multipleChoiceBox4, WHITE)
            screen.draw.textbox( (((questions[randomInt])["answer1"])) , (615, 255, 300, 80), color="black") # Accessing the randomly picked ([randomInt]) answers to the corresponding randomly picked question
            screen.draw.textbox( (((questions[randomInt])["answer2"])) , (615, 360, 300, 80), color="black")
            screen.draw.textbox( (((questions[randomInt])["answer3"])) , (615, 465, 300, 80), color="black")
            screen.draw.textbox( (((questions[randomInt])["answer4"])) , (615, 570, 300, 80), color="black")
        elif (((questions[randomInt])["trueOrFalse"])) == "True": # Checks if this is a true or false question from the key "trueOrFalse" from a randomly picked question from the "questions" dictionary
            screen.draw.filled_rect(trueBox, WHITE)
            screen.draw.filled_rect(falseBox, WHITE)
            screen.draw.textbox( "True" , (615, 280, 300, 160), color="black")
            screen.draw.textbox( "False" , (615, 460, 300, 160), color="black")
    if gameState == "correct":
        previousAnswerRightWrong = "right"
        screen.draw.filled_rect(startFill, startColor)
        resetQuestion = 1
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("Your answer was correct!", midtop=(500, 100), fontsize=60, color = "green")
        screen.draw.text("Press any key to continue playing!", midtop=(500, 150), fontsize=40)
        screen.draw.text("Current Score: " + str(currentScore), midtop=(878, 700), fontsize=40)
        screen.draw.text("High Score: " + str(highScore), midtop=(900, 730), fontsize=40)
        displayStrikes()
        screen.draw.filled_rect(backButtonBox, WHITE)
        screen.draw.text("BACK", (23, 23), fontsize=35, color ="#000000")
        winEncouragement(randomNumRight, 0)
        displayBillyLeftRight() # You also see this on the title screen (Billy the stickman on the right and left of the screen)
    if gameState == "incorrect" or timeLeft == 0:
        previousAnswerRightWrong = "wrong"
        screen.draw.filled_rect(startFill, startColor)
        resetQuestion = 1
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("Incorrect! Better luck next time!", midtop=(500, 100), fontsize=60, color = "red")
        screen.draw.text("Press any key to continue playing!", midtop=(500, 150), fontsize=40)
        screen.draw.text("Current Score: " + str(currentScore), midtop=(878, 700), fontsize=40)
        screen.draw.text("High Score: " + str(highScore), midtop=(900, 730), fontsize=40)
        displayStrikes()
        loseEncouragement(randomNumWrong, 0) # This second argument is the y value offset the displayed objects should have
        displayBillyLeftRight()
    if gameState == "start":
        screen.draw.filled_rect(startFill, startColor)
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("Click the button below to start!", midtop=(500, 120), fontsize=35)
        screen.draw.filled_rect(startButtonBox, WHITE)
        screen.draw.text("PLAY", midtop=(500, 324), fontsize=30, color ="#000000")
        screen.draw.filled_rect(helpButtonBox, WHITE)
        screen.draw.text("HELP", midtop=(500, 384), fontsize=30, color ="#000000")
        screen.draw.filled_rect(scoreboardButtonBox, WHITE)
        screen.draw.text("SCOREBOARD", midtop=(500, 444), fontsize=30, color ="#000000")
        displayBillyLeftRight() # Billy is the mascot of the game; the stickman you see often in the application!
        displayRandomWelcome(randomNumWelcome, 268) # This second argument is the y value offset the displayed objects should have
        screen.draw.filled_rect(soundButtonBox, startColor)
        if sound == True: # This sound controller also displays the volume on and off image you see on the start screen
            soundS = "On"
            screen.blit('volume_on', (-5 , 660))
        else:
            soundS = "Off"
            screen.blit('volume_off', (-5 , 660))
    if gameState == "help":
        screen.draw.filled_rect(startFill, startColor)
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("Instructions", midtop=(500, 90), fontsize=40)
        screen.draw.text("You will be given a question, an image, and a few", midtop=(500, 170), fontsize=35)
        screen.draw.text("possible answers to pick from that correspond to the", midtop=(500, 200), fontsize=35)
        screen.draw.text("given question. You must try to pick the correct answer!", midtop=(500, 230), fontsize=35)
        screen.draw.text("Three strikes, and you're out! Those are the basics,", midtop=(500, 260), fontsize=35)
        screen.draw.text("you will learn quick.", midtop=(500, 290), fontsize=35)
        screen.draw.text("Good luck!", midtop=(500, 320), fontsize=35)
        # Some pictures were inserted here to add some more interesting things to look at on the help screen
        showcasePicture1 = Actor('question8image', (200, 500)) # Creating the actors of these images allowed me to access and change the displayed rotation
        showcasePicture1.angle = -25
        showcasePicture1.draw() # Used again on lose screen, though values are different there because these values are only assigned in this if statement's scope
        showcasePicture2 = Actor('question3image', (500, 470))
        showcasePicture2.angle = 25
        showcasePicture2.draw()
        showcasePicture3 = Actor('question12image', (750, 520))
        showcasePicture3.angle = -20
        showcasePicture3.draw()
        screen.draw.text("Billy is the stickman you constantly see throughout this game. He will be your buddy for your learning adventure!", midtop=(505, 730), fontsize=25)
    if gameState == "beatHighscore": # This screen will display if you beat your highscore
        screen.draw.filled_rect(startFill, startColor)
        resetQuestion = 1
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("Congratulations, you beat your highscore! Billy is very proud of you!", midtop=(500, 100), fontsize=40)
        screen.draw.text("Press the play again button to continue playing!", midtop=(500, 150), fontsize=40)
        screen.draw.filled_rect(startButtonBox, (255, 241, 41))
        screen.draw.text("PLAY AGAIN", midtop=(500, 324), fontsize=30, color ="#000000")
        displayBillyLeftRight()
        winEncouragement(randomNumRight, 200)
    if gameState == "highscoreNotBeat": # This screen will display if you did NOT beat your highscore
        screen.draw.filled_rect(startFill, startColor)
        resetQuestion = 1
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("Unfortunately, you didn't beat your highscore. Better luck next time!", midtop=(500, 100), fontsize=40)
        screen.draw.text("Press the play again button to continue playing!", midtop=(500, 150), fontsize=40)
        screen.draw.filled_rect(startButtonBox, (255, 241, 41))
        screen.draw.text("PLAY AGAIN", midtop=(500, 324), fontsize=30, color ="#000000")
        displayBillyLeftRight()
        loseEncouragement(randomNumWrong, 200)
    if gameState == "scoreboard":
        screen.draw.filled_rect(startFill, startColor)
        screen.draw.text("Physics Trivia Game", midtop=(500, 30), fontsize=35, fontname='poppinsregular')
        screen.draw.text("High Score: " + str(highScore), midtop=(900, 730), fontsize=40)
        screen.draw.text("Scoreboard", midtop=(500, 90), fontsize=40)
        screen.draw.filled_rect(resetHighscoreBox, WHITE)
        screen.draw.text("Reset Highscore", (848, 18), color = "#000000", fontsize = 30)
        screen.draw.text("Name" , (300, 180), color="white", fontsize=60)
        screen.draw.text("Score" , (674, 180), color="white", fontsize=60)
        billySad = Actor('billy_sad', (-100, 300))
        billySad.angle = -25
        billySad.draw() # Used again on lose screen, though values are different there because these values are only assigned in this if statement's scope
        billyHappy = Actor('billy_happy', (670, 520))
        billyHappy.angle = 25
        billyHappy.draw() # Used again on lose screen, though values are different there because these values are only assigned in this if statement's scope
        profiles["YOU"] = highScore
        sortedProfiles = (sorted(profiles.items(), key=operator.itemgetter(1),reverse=True)) # Actively sorts scoreboard profiles by key value (score) from greatest to least, and updates live
        for user in range(0,len(profiles)): # Runs through each scoreboard profile (from QuestionData.py)
            if user < 8: # Display up to 8 users on the scoreboard at once
                if len(sortedProfiles[user][0]) > 15: # This if statement fixes any scoreboard format breaks that occur when a user's name is too long.
                    screen.draw.text( (sortedProfiles[user][0])[:15] + "...", (300, 250 + (user  * 50) ), color="white", fontsize=50) # sortedProfiles[user][0] accesses user name
                    screen.draw.text( str(sortedProfiles[user][1]), (674, 250 + (user  * 50)), color="white", fontsize=50) # (sortedProfiles[user][1]) accesses score
                    # Without this if statement code, a long enough name would have its text overlap with its score text.
                elif sortedProfiles[user][0] == "YOU": # If the "user" in "profiles" key value is equal to "YOU", it displays that information from that "user" in green. In other terms, the player's stats are displayed in green to stand out and be easily findable on the scoreboard.
                    screen.draw.text( sortedProfiles[user][0], (300, 250 + (user  * 50) ), color="green", fontsize=50)
                    screen.draw.text( str(sortedProfiles[user][1]), (674, 250 + (user  * 50)), color="green", fontsize=50)
                else:
                    screen.draw.text( sortedProfiles[user][0], (300, 250 + (user  * 50) ), color="white", fontsize=50)
                    screen.draw.text( str(sortedProfiles[user][1]), (674, 250 + (user  * 50)), color="white", fontsize=50)
    if gameState != "start": # Drawn after everything else is drawn so that none of the screen clears ( screen.draw.filled_rect(startFill, startColor) ) interfere with the back button's visibility.
        # I first had the following two lines in every game state in the draw function, then tried putting the same two lines into a function and calling it from anywhere I had it before hand in the draw function.
        # Though, I soon realized just displaying it using this simple if statement was the most efficient way to display my back button.
        screen.draw.filled_rect(backButtonBox, WHITE) # The back button appears on every screen (or game state) in the application, except the start screen
        screen.draw.text("BACK", (23, 23), fontsize=35, color ="#000000")

def on_mouse_down(pos): # Called on mouse down, used for checking if mouse clicks from the user collided with on screen buttons (rects) - More comments below
    global randomInt
    global choiceBox1
    global choiceBox2
    global choiceBox3
    global choiceBox4
    global gameState
    global answer
    global strikes
    global currentScore
    global highScore
    global sound
    global soundS
    global resetQuestion
    global timer
    global randomNumWelcome
    if gameState != "start":
        if backButtonBox.collidepoint(pos): # Not start screen (though the invisible back button would take you to the start screen either way)
            print("Back Button Pressed")
            playClickSound(sound)
    if gameState == "help" or gameState == "beatHighscore" or gameState == "scoreboard": # Not start screen (though the invisible back button would take you to the start screen either way)
        if backButtonBox.collidepoint(pos):
            gameState = "start"
    if gameState == "play" or gameState == "correct" or gameState == "incorrect" or gameState == "beatHighscore" or gameState == "highscoreNotBeat":
        if backButtonBox.collidepoint(pos):
            randomNumWelcome = randomInt = random.randint(0, len(welcomeMessages) - 1)
            gameState = "initializeStart" # I did not want the track 'bells' being played when clicking back from the the game states mentioned in the if statement
    if gameState == "play":
        if (((questions[randomInt])["trueOrFalse"])) == "False": # If player answer is the answer that is said to be correct in the dictionary that is being checked, reset using the appropriate function # More information on this is in "QuestionsData.py"
            if multipleChoiceBox1.collidepoint(pos):
                if (((questions[randomInt])["answer"])) == 1:
                    print("multipleChoiceBox1 Pressed")
                    correctReset()
                else:
                    wrongReset()
            if multipleChoiceBox2.collidepoint(pos):
                if (((questions[randomInt])["answer"])) == 2:
                    print("multipleChoiceBox2 Pressed")
                    correctReset()
                else:
                    wrongReset()
            if multipleChoiceBox3.collidepoint(pos):
                if (((questions[randomInt])["answer"])) == 3:
                    print("multipleChoiceBox3 Pressed")
                    correctReset()
                else:
                    wrongReset()
            elif multipleChoiceBox4.collidepoint(pos):
                if (((questions[randomInt])["answer"])) == 4:
                    print("multipleChoiceBox4 Pressed")
                    correctReset()
                else:
                    wrongReset()
        elif (((questions[randomInt])["trueOrFalse"])) == "True": # Same thing as above, though for true and false questions
            if trueBox.collidepoint(pos):
                if (((questions[randomInt])["answer"])) == "True":
                    correctReset()
                else:
                    wrongReset()
            if falseBox.collidepoint(pos):
                if (((questions[randomInt])["answer"])) == "False":
                    correctReset()
                else:
                    wrongReset()
    if gameState == "start":
        if startButtonBox.collidepoint(pos):
            playClickSound(sound)
            gameState = "initializePlay" # "initializePlay" and "initializeStart" only last for about a frame, just to turn on the desired sound track for a different game state, without the sound track constantly repeating in the first second of the song. # It is changed through the update() function
        if helpButtonBox.collidepoint(pos):
            playClickSound(sound)
            gameState = "help"
        if scoreboardButtonBox.collidepoint(pos):
            playClickSound(sound)
            gameState = "scoreboard"
        if soundButtonBox.collidepoint(pos): # Sound ON or OFF toggle controller # The sound controller in game state "start" controls the image
            playClickSound(sound)
            print("Sound Toggle Button Pressed.")
            if sound == True:
                sound = False
                print("Sound: " + soundS)
            if soundS == False or soundS == "Off":
                sound = True
                print("Sound: " + soundS)
    if gameState == "beatHighscore" or gameState == "highscoreNotBeat":
        if startButtonBox.collidepoint(pos):
            playClickSound(sound)
            gameState = "play"
    if gameState == "scoreboard":
        if resetHighscoreBox.collidepoint(pos): # Resets player's high score
            playClickSound(sound)
            highScore = 0
            highWrite(highScore)

def on_key_down(): # When the player choses the incorrect or correct answer, they are taken to the "incorrect" or "correct" game screen. Which is a small "intermission" between itself and the primary game screen; giving
    # the player certain user-feedback and information in the process. Hitting any key on this screen will bring you back to the primary game screen.
    global gameState
    global strikes
    if gameState == "correct" or gameState == "incorrect":
        gameState = "play"

def correctReset(): # Called to reset and check values when the player chooses the correct answer
    global randomNumRight
    global currentScore
    global gameState
    if sound == True:
        tone.play('E4', 0.2) # Correct sound effect!
    currentScore += int(50 * (timeLeft / 10))
    gameState = "correct"
    randomNumRight = randomInt = random.randint(0, len(encouragementRight) - 1) # Randomizes Billy's encouragement message to something else (randomNumRight is the random integer that gets used to pick a random
    # An encouragement / a "job well done" message from Billy is displayed when you are correct. The same concept is applied to the variables "randomNumWrong" and "randomNumWelcome")

def wrongReset(): # Called to reset and check values when the player choses the incorrect answer
    global randomNumWrong
    global strikes
    global gameState
    global highScore
    global currentScore
    strikes += 1 #  Add a strike, this function is only called when the player answers a question wrong
    if sound == True:
        tone.play('E2', 0.2) # Wrong sound effect
    if strikes > 2:
        strikes = 3 # Makes it impossible to have more than 3 strikes
    if strikes < 3:
        gameState = "incorrect" # Used to be a function here called strikesIncorrect() that got called for each multipleChoiceBox wrong user click, though that
        # using that method would not allow the incorrect screen to show up for some reason. The function did the exact same thing as what is in the above else:
        # statement.
    if strikes > 2:
        if currentScore > highScore: # Depending on whether you beat your highscore or not, the below corresponding approriate commands will be executed
            highScore = currentScore
            highWrite(highScore) # Calls overwrite high score function if player has beat their high score
            gameState = "beatHighscore"
        else:
            gameState = "highscoreNotBeat"
        resetGame()
    randomNumWrong = randomInt = random.randint(0, len(encouragementWrong) - 1)

def resetGame(): # Resets many important game values - Called on game restart (when the player gets three strikes)
    global resetQuestion
    global strikes
    global currentScore
    global previousAnswerRightWrong
    #timeLeft = 30
    resetQuestion = 1 # This variable can be found used near the top of my draw() function
    strikes = 0
    currentScore = 0
    previousAnswerRightWrong = "start"
    randomNumRight = randomInt = random.randint(0, len(encouragementRight) - 1)
    randomNumWrong = randomInt = random.randint(0, len(encouragementWrong) - 1)

def highWrite(highScore): # Opens, writes the player's new highscore, and closes the "highscore.txt" file. Called when the player has beat their high score.
    f = open("highscore.txt", "w")
    f.write(str(highScore))
    f.close()

def update(): # These values are constantly checked and or updated
    global sound
    global gameState
    if gameState == "play":
        clock.schedule(time, 1)
        if timeLeft == 0:
            wrongReset()
        playAgainBox = Rect((170, 250), (250, 75))
    if sound == False:
        music.set_volume(0)
    else:
        music.set_volume(0.9) # I would turn this down even more as you mentioned to do, though this would cause a conflict in consistency of volume between
        # my Tone Generator beeps and my music. The Tone Generator does not have a command to lower its volume, so please adjust your volume in your system's
        # volume mixer. Thank you for understanding.
    if gameState == "initializePlay": # "initializePlay" and "initializeStart" have been used to get music playing on different screens without have the music being constantly called to play (repeating the sound track in the first second of it being played constantly).
        # "initializePlay" and "initializeStart" are only in effect for about a frame or so.
        music.stop()
        music.play('intensity')
        gameState = "play"
    if gameState == "initializeStart":
        music.stop()
        music.play('bells')
        gameState = "start"

def time(): # Controls the time left counter on the game screen # Only plays on gameState == "play"
    global timer
    global timeLeft
    global timeLeftSmooth
    timer += 1 # Every frame (about 60fps)
    timeLeftSmooth -= 1 # Every frame (about 60fps)
    timeLeftBeep = tone.create('E3', 0.1)
    gameEndBeep = tone.create('A2', 0.5)
    if timer % 60 == 0: # % 100 turned out to last 25 seconds instead of 15 (last 60% longer than what it was supposed to). # Only divisible to equal 0 every second
        timeLeft -= 1
        if timeLeft == 0:
            if sound == True: # If sound is turned on
                gameEndBeep.play()
        elif timeLeft <= 5: # Beep every second when the amount of time left is under 5 seconds (unless the amount of time left is equal to 0, then play a longer game end beep sound) to indicate the player to answer
        # the question on screen before time runs out; it is better to try than not to try at all!
            if sound == True:
                timeLeftBeep.play()

def playClickSound(sound): # Simple play click sound function
    clickSound = tone.create('B2', 0.1)
    if sound == True:
        clickSound.play()

def displayStrikes(): # Displays the amount of strikes on the screen
        # Strikes - Tried using a for loop, though this will have to do for now.
        if strikes == 3:
            strikeCrosses = ["placeholder","placeholder","placeholder"]
        elif strikes == 2:
            strikeCrosses = ["placeholder","placeholder"]
        elif strikes == 1:
            strikeCrosses = ["placeholder"]
        else:
            strikeCrosses = []
        screen.draw.text("Strikes: ", midtop=(400, 730), fontsize=40)
        strikeCounter = 0
        for crosses in strikeCrosses:
            strikeCounter += 1
            screen.blit('strike_cross', (400 + (50 * strikeCounter), 700))

def displayBillyLeftRight(): # Displays Billy on the left and right side of the screen. Seen on such screens as the start screen (main menu)
    billySad = Actor('billy_sad', (-100, 270)) # Used again on lose screen, though values are different there because these values are only assigned in this if statement's scope
    billySad.angle = -25
    billySad.draw()
    billyHappy = Actor('billy_happy', (630, 490)) # Used again on lose screen, though values are different there because these values are only assigned in this if statement's scope
    billyHappy.angle = 25
    billyHappy.draw()

def displayRandomWelcome(randomNumWelcome, yOffset): # Displays the random welcome message you see Billy communicating via speech bubble on the start screen
    screen.blit('textbubble', (400 , 210 + yOffset))
    screen.blit('billy_happy_small', (35, 290 + yOffset))
    screen.draw.textbox( welcomeMessages[randomNumWelcome] , (422, 285 + yOffset, 150, 25), color="black") # randomNumWelcome is generated elsewhere in the code,
    # then used to pick a random welcome message in range. This randomly chosen message is then displayed in speech bubble format in the application.
    # Variables "randomNumRight" and "randomNumWrong" follow the same concept.

def winEncouragement(randomNumRight, yOffset): # Billy acknowledges your accomplishment (answering the question correctly) via speech bubble!
    screen.blit('textbubble', (400 , 210 + yOffset))
    screen.blit('billy_happy_small', (35, 290 + yOffset))
    screen.draw.textbox( encouragementRight[randomNumRight] , (422, 285 + yOffset, 150, 25), color="black")

def loseEncouragement(randomNumWrong, yOffset): # Billy encourages you to persevere (answering the question incorrectly) via speech bubble!
    screen.blit('textbubble', (400 , 210 + yOffset))
    screen.blit('billy_sad_small', (35, 290 + yOffset))
    screen.draw.textbox( encouragementWrong[randomNumWrong] , (422, 285 + yOffset, 150, 25), color="black")

def displayEncouragement(previousAnswerRightWrong,randomNumRight,randomNumWrong): # The displays of encouragement above are used on seperate screens than the primary game screen (gameState = "play")
    # This function displays the following on the primary game screen (towards the left side of the screen, rather than the other displays of encouragement above being displayed in the middle of the screen).
    screen.blit('textbubble', (10 , 140))
    if previousAnswerRightWrong == "start": # What is displayed when the game starts
        screen.blit('billy_happy', (-550, 170))
        screen.draw.textbox("Good luck!", (31, 215, 150, 25), color="black") # Text boxes are used in order to regulate text not slipping out of the 'textbubble' image, regardless of the amount of text.
    if previousAnswerRightWrong == "right": # What is displayed when the player answers a question correctly
        screen.blit('billy_happy', (-550, 170))
        screen.draw.textbox( encouragementRight[randomNumRight] , (31, 215, 150, 25), color="black")
    if previousAnswerRightWrong == "wrong": # What is displayed when the player answers a question incorrectly
        screen.blit('billy_sad', (-550, 170))
        screen.draw.textbox( encouragementWrong[randomNumWrong] , (31, 215, 150, 25), color="black")