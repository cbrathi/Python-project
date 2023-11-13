questions = ["What is the capital of France?", "What is the capital of Germany", "What is the capital of Norway?", "What is the capital of Russia?"]
# Create a list called questions

print ("Hello. Welcome to my quiz.")
#Welcome the user to the program

correctAnswers = 0
#Set my integer equivalent to 0

def questionone():
  isValid = False
  print (questions[0])
  #Access the question from the list
  response = input()
  #Save the answer inside the variable
  if response.lower() == "paris":
    print ("Correct")
    isValid = True
    global correctAnswers
    correctAnswers += 1
    #Add the point to their final score
  else:
    print ("Incorrect")99

  #Loop until the user gets the answer correct
  while isValid is False:
    print (questions[0])
    #Access the question from the list
    response = input()
    #Save the answer inside the variable
    if response.lower() == "paris":
      print ("Correct")
      isValid = True
      correctAnswers += 1
      #Add the point to their final score
    else:
      print ("Incorrect")
    
questionone()
#End the first question function



def questiontwo():
  isValid = False
  print (questions[1])
  #Access the question from the list
  response = input()
  #Save the answer inside the variable
  if response.lower() == "berlin":
    print ("Correct")
    isValid = True
    global correctAnswers
    correctAnswers += 1
    #Add the point to their final score
  else:
    print ("Incorrect")

  #Loop until the user gets the answer correct
  while isValid is False:
    print (questions[1])
    #Access the question from the list
    response = input()
    #Save the answer inside the variable
    if response.lower() == "berlin":
      print ("Correct")
      isValid = True
      correctAnswers += 1
      #Add the point to their final score
    else:
      print ("Incorrect")

questiontwo()
#End the second question function





def questionthree():
  isValid = False
  print (questions[2])
  #Access the question from the list
  response = input()
  #Save the answer inside the variable
  if response.lower() == "oslo":
    print ("Correct")
    isValid = True
    global correctAnswers
    correctAnswers += 1
    #Add the point to their final score
  else:
    print ("Incorrect")
    
  #Loop until the user gets the answer correct
  while isValid is False:
    print (questions[2])
    #Access the question from the list
    response = input()
    #Save the answer inside the variable
    if response.lower() == "oslo":
      print ("Correct")
      isValid = True
      correctAnswers += 1
      #Add the point to their final score
    else:
      print ("Incorrect")

questionthree()
#End the third question function




def questionfour():
  isValid = False
  print (questions[3])
  #Access the question from the list
  response = input()
  #Save the answer inside the variable
  if response.lower() == "moscow":
    print ("Correct")
    isValid = True
    global correctAnswers
    correctAnswers += 1
    #Add the point to their final score
  else:
    print ("Incorrect")

  #Loop until the user gets the answer correct
  while isValid is False:
    print (questions[3])
    #Access the question from the list
    response = input()
    #Save the answer inside the variable
    if response.lower() == "moscow":
      print ("Correct")
      isValid = True
      correctAnswers += 1
      #Add the point to their final score
    else:
      print ("Incorrect")

questionfour()
#End fourth question function



print ("Congratulations on finishing the quiz. Your final score is")
print (correctAnswers)
#Inform the user that the program is over and what their final score is.