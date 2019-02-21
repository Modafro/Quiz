# Text associated with difficulty level

easy_phrase="___1___ is known as the capital of love and also coincides with being \
the capital of ___2___. On top of being the love city, ___1___ boasts incredible tourist\
 attractions with the most popular of them being the ___3___ Tower and Le Louvre museum. If you ever have a chance\
 to fly across the ___4___ Ocean (assuming you live in Canada), do stop by ___1___ whether be it single or with a lover, you'll enjoy it! "

medium_phrase="Although ___1___ lost a US presidential election, he went on to become a leader in environmental issues.\
 Political aficionados will remember the contentious key state, ___2___, that caused ___1___ to lose the election. Many called foul play since his opponent's brother, ___3___,\
 was the governor of ___2___ at the time. Alas, the ___4___ party was back in power. "

hard_phrase="When looking upon the sky, we simply refer to it as the air or more accurately the atmosphere. However, the atmosphere is composed of different layers. The\
 ___1___ is the outermost layer, it's where you'd see the stars. Next is the ___2___, which is where a satellite or space shuttle would hover around. If now we were to see\
 a meteor coming to earth Armageddon style, that big ball of fire we would see would be in the ___3___. Next is the ___4___ which is also where the ozone layer is located.\
 Finally, the ___5___ is the lowest layer of Earth's atmosphere. It's where you see the clouds or the cruising altitude of a plane!"

#solutions:

Solution_Easy=["PARIS", "FRANCE", "EIFFEL", "ATLANTIC"]
Solution_Medium=["AL GORE", "FLORIDA", "JEB BUSH", "REPUBLICAN"]
Solution_Hard=["EXOSPHERE", "THERMOSPHERE", "MESOSPHERE", "STRATOSPHERE", "TROPOSPHERE"]


#User select difficulty levels & number of attempts

userchoice=(input("Please select your difficulty level. Choose between Easy, Medium and Hard: " "")).capitalize() #input is a command that prompts the user to input something
#validate user choice of difficulty
while userchoice =='':
    userchoice = (input("\nYou must choose a difficulty level. Choose between Easy, Medium and Hard: " "")).capitalize()

while (userchoice != 'Easy' and userchoice != 'Medium' and userchoice != 'Hard'):
    userchoice = (input("\nPlease enter a valid difficulty level. Choose between Easy, Medium and Hard: " "")).capitalize()

usercount=(input("\nPlease decide how many wrong guesses you can make before you lose: " "")) #int allows you to take user's input as a whole number instead of a default string
#validate user input for counts

while usercount.isdigit() == False or usercount == '0':
    usercount=(input("\nPlease enter a valid number (at least 1). Enter how many wrong guesses you can make before you lose: " ""))

#cast usercount to integer
usercount = int(usercount)


# Let's code the game itself. Input will be the phrase (string) and answer (list). If answer is correct, move on to the next one until the last blank. If wrong, prompt user to try again.
def replace_in_phrase(phrase,answers):
    count=0
    index=0
    while count <=usercount:#sets the number of cycles with respect to wrong answers. If count>usercount, user loses
        while index<len(answers):
            user_input=(input("\nWhat should go in"+" "+ "___"+str(index+1)+"___"+" "+"?"" ")).upper()
            if answers[index]==user_input:
                phrase=phrase.replace("___"+str(index+1)+"___", user_input) #blanks start at 1 and not 0
                print ("\nGood job! Here's how the text looks like now:\n\n" + phrase + "\n")
                index+=1 #if the answer is good, we go to the next blank (+1)
            else: #if user is wrong
                if count<usercount: #if it's the user's last try (i.e:count==usercount), we don't want to print "Wrong answer, Try again" if he fails. This condition sets that.
                    print ("\nWrong answer! Try again!\n")
                break; #breaking out of the secondary while loop to either increase the count (+1) or confirm if the user has won or if the user has lost
        if index==len(answers):
            return "\nYou won :)"
        else:
            count+=1
    return "\nYou lost :("

#
def quiz(level, attempts):
    if level== "Easy":
        phrase = easy_phrase
        print ("\nEasy it is. You will have" + " "+str(attempts)+" " + "attempt(s) to get it right. Here is the phrase:" + "\n"*2 + phrase + "\n")
        return replace_in_phrase (easy_phrase, Solution_Easy)
    if level=="Medium":
        phrase = medium_phrase
        print ("\nMedium it is. Hope you are politically astute. You will have" +" "+ str(attempts)+" "+ "attempt(s) to get it right. Here is the phrase:" + "\n"*2 + phrase + "\n")
        return replace_in_phrase (medium_phrase, Solution_Medium)
    if level=="Hard":
        phrase = hard_phrase
        print ("\nThink you can handle hard? Let's find out! You will have" +" " +str(attempts) +" "+ "attempt(s) to get it right! Here is the phrase:" + "\n"*2 + phrase + "\n")
        return replace_in_phrase (hard_phrase, Solution_Hard)


print (quiz (userchoice, usercount))
