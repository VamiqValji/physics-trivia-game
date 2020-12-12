#-----------------------------------------------------------------------------
# Name:        Question Data
# Purpose:     Secondary file to store and organize some data that is used in "PhysicsTriviaGame.py" (final project)
#
# Author:      Vamiq Valji
# Created:     29-Oct-2020
# Updated:     06-Nov-2020
#-----------------------------------------------------------------------------
#I think this project deserves a 4+ OR A 100% because ...
#
#Features Added:
#   Please refer to "PhysicsTriviaGame.py"
#-----------------------------------------------------------------------------

# I designed this python file to be very modular in the sense that you can simply just add a question or profile here, and the game
# be able to recognize it as long as you use the proper formats as shown below.

questions = [] # List that holds all of the questions (dictionaries). Questions are randomly picked through this list via this concept of picking out an index from a list: "questions[randomInt]".
# The "randomInt" uses commands from "import random" to assign itself a random value

# In this circumstance, using dictionaries make organizing data easy, convenient, and accessible

# Though not many, some of these questions re-use images, that is why you may see a question dictionary that has a different question number than the image.

# The following formatting is for multiple choice questions. How I formatted true or false questions can be found in this Python file.

# IF YOU WOULD LIKE TO MAKE A QUESTION OF YOUR OWN, MAKE SURE THE IMAGE IS 350 x 400 PIXELS.

question1 =	{
  "question": "If Billy started at point A, went through point C, and ended at point B, what was his DISPLACEMENT?", # Place your question key value in the "question" key
  "answer1": "5m", # Place your multiple choice possible answers in each of the answer key inputs ("answer1", "answer2", "answer3", "answer4")
  "answer2": "2m",
  "answer3": "3m",
  "answer4": "4m",
  "image": "question1image", # When your image is in the program's "images" folder directory, write the name of the image here. # If you do not have an image for now, write "placeholder"
  "answer": 4, # This is the key that tells the program which answer out of the 4 possible choices is actually correct. In this case, the "answer" key has a key value of an integer of 4,
  # meaning "answer4" is the correct answer in this situation. The player must pick the correct answers in order to not gain strikes, though gain points.
  "trueOrFalse": "False" # Denotes whether this question is a true or false question
}
questions.append(question1)

# Follows the same format as the above question
question2 =	{
  "question": "If Billy started at point A, went through point C, and ended at point B, what was his DISTANCE TRAVELED?",
  "answer1": "5m",
  "answer2": "2m",
  "answer3": "3m",
  "answer4": "4m",
  "image": "question1image",
  "answer": 1,
  "trueOrFalse": "False"
}
questions.append(question2)

question3 =	{
  "question": "What is the formula for potential energy?",
  "answer1": "PE = 1/2mV^2",
  "answer2": "PE = mgh",
  "answer3": "PE = mg^h",
  "answer4": "There is no formula for calculating potential energy.",
  "image": "question3image",
  "answer": 2,
  "trueOrFalse": "False"
}
questions.append(question3)

question4 =	{
  "question": "What does the E in E = mc^2 stand for?",
  "answer1": "Elephant",
  "answer2": "Egg",
  "answer3": "Energy",
  "answer4": "English",
  "image": "question4image",
  "answer": 3,
  "trueOrFalse": "False"
}
questions.append(question4)

question5 =	{
  "question": "Which is the correct formula for calculating force?",
  "answer1": "F = a/m",
  "answer2": "F = m^a",
  "answer3": "F = m/a",
  "answer4": "F = ma",
  "image": "question5image",
  "answer": 4,
  "trueOrFalse": "False"
}
questions.append(question5)

question6 =	{
  "question": "What is the formula for work (in joules)?",
  "answer1": "W = FD",
  "answer2": "W = F^D",
  "answer3": "W = D^F",
  "answer4": "There is no formula for calculating work.",
  "image": "question6image",
  "answer": 1,
  "trueOrFalse": "False"
}
questions.append(question6)

question7 =	{
  "question": "Which one of these units are not real?",
  "answer1": "Newtons",
  "answer2": "Joules",
  "answer3": "Nizen",
  "answer4": "Ampere",
  "image": "question7image",
  "answer": 3,
  "trueOrFalse": "False"
}
questions.append(question7)

# Formatting of true or false questions are shown here. It is the same concept as the above multiple choice question format for the first two keys.
question8 =	{
  "question": "Your WEIGHT is different on Earth that it would be on Mars.",
  "image": "question8image",
  "answer": "True", # This key value can either be "True" or "False" to indicate whether the answer to the question is "True" or "False"
  "trueOrFalse": "True" # This tells the program that this question is in fact a true or false question, not a multiple choice question
}
questions.append(question8)

# The same true of false format continues below
question9 =	{
  "question": "Your MASS is different on Earth that it would be on Mars.",
  "image": "question8image",
  "answer": "False",
  "trueOrFalse": "True"
}
questions.append(question9)

question10 =	{
  "question": "The Doppler Effect can only be replicated if the sound source is stationary and the listener is moving.",
  "image": "question10image",
  "answer": "False",
  "trueOrFalse": "True"
}
questions.append(question10)

question11 =	{
  "question": "Kinetic, potential, and thermal are all forms of energy.",
  "image": "question11image",
  "answer": "True",
  "trueOrFalse": "True"
}
questions.append(question11)

question12 =	{
  "question": "Water's boiling point is 100°C and its freezing point is 5°C",
  "image": "question12image",
  "answer": "False",
  "trueOrFalse": "True"
}
questions.append(question12)

question13 =	{
  "question": "E = mc^2 can be used to explain why the sun and other stars shine.",
  "image": "question4image",
  "answer": "True",
  "trueOrFalse": "True"
}
questions.append(question13)

question14 =	{
  "question": "Who formulated the equation: E = mc^2?",
  "answer1": "Barack Obama",
  "answer2": "Albert Einstein",
  "answer3": "Michael Jackson",
  "answer4": "David Suzuki",
  "image": "question4image",
  "answer": 2,
  "trueOrFalse": "False"
}
questions.append(question14)

question15 =	{
  "question": "Find the total voltage given the picture.",
  "answer1": "5V",
  "answer2": "7V",
  "answer3": "3V",
  "answer4": "4V",
  "image": "question15image",
  "answer": 1,
  "trueOrFalse": "False"
}
questions.append(question15)

question16 =	{
  "question": "Temperature's effect on the speed of sound can be calculated via the formula in the image.",
  "image": "question16image",
  "answer": "True",
  "trueOrFalse": "True"
}
questions.append(question16)

question17 =	{
  "question": "The given formula in the picture can be used to determine acceleration.",
  "image": "question17image",
  "answer": "False",
  "trueOrFalse": "True"
}
questions.append(question17)

question18 =	{
  "question": "Near Earth's surface, gravitational acceleration is approximately 5m/s^2.",
  "image": "question18image",
  "answer": "False",
  "trueOrFalse": "True"
}
questions.append(question18)

question19 =	{
  "question": "A coefficient of friction equal to 0 means the object is unable to move against the surface it is on.",
  "image": "question19image",
  "answer": "False",
  "trueOrFalse": "True"
}
questions.append(question19)

question20 =	{
  "question": "The character in the image is called 'lambda'.",
  "image": "question20image",
  "answer": "True",
  "trueOrFalse": "True"
}
questions.append(question20)

# SCOREBOARD PROFILES

profiles = {} # This dictionary holds all of the user profiles

# Adding profiles to the "profiles" dictionary
profiles["Jahseh"] = 4740
profiles["COVID19"] = 2020
profiles["Juice"] = 3470
profiles["Black Bear"] = 440
profiles["The Kid Laroi"] = 2250
profiles["Ski Mask The Slump God"] = 930
profiles["Tecca"] = 1800

# Billy (The Stickman) Encouragement / Welcome Lists # These are the lists that hold the randomized messages that Billy says on different screens

encouragementRight = ["Good work!", "Well done!", "Great job!", "Good job!", "Great job!", "Amazing!", "Keep it coming!", "Nice!"] # Messages from when you get a question right or beat your high score
encouragementWrong = ["Nice try!", "Hang in there!", "Don't give up!", "Stay strong!", "Keep pushing!", "You can do it!"] # Messages from when you get a question wrong or didn't beat your high score
welcomeMessages = ["Welcome!", "How are you?", "How was your day?"] # Billy can be seen at the bottom of the start screen displaying one of these message options (randomized)