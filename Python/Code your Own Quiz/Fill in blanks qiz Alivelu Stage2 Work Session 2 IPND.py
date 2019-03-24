def choose_level():
    """Define a function name choose_level. keep all the game data in a dictionary. It should return a selected level, user_selected_quiz, use_selected_ans_list according to the input from user."""
    game_data = {"easy": {"selected_quiz": "The Taj Mahal is a _1_ built in the 17th century by the Mughal emperor, _2_, in memory of his wife, Mumtaz Mahal. She was his _3_ wife. Eventually, Shah Jahan was entombed in the Taj Mahal with his wife. The building is in the city of _4_, Uttar Pradesh.", "selected_ans_list": ["tomb", "shahjahan", "third", "agra"]},
                 "med": {"selected_quiz": "Data analysis, also known as _1_ of data or data analytics, is a process of inspecting, cleansing, transforming, and modeling _2_ with the goal of discovering useful _3_, suggesting conclusions, and _4_ decision-making.", "selected_ans_list": ["analysis", "data", "information", "supporting"]},
                 "adv": {"selected_quiz": "My name is _1_. My occupation is Software test _2_. Now I am learning introduction to programming from _3_. After this course I want to learn _4_ analysis.", "selected_ans_list": ["alivelu", "engineer", "udacity", "data"]},
                 "final": {"selected_quiz": "A _1_ is created with the def keyword. You specify the inputs a _1_ takes by adding _2_ separated by commas between the parentheses. _1_s by default return _3_ if youdon't specify the value to return. _2_ can be standard data types such as string, number, dictionary, tuple, and _4_ or can be more complicated such as objects and lambda functions.", "selected_ans_list": ["function", "arguments", "none", "lists"]}}
    level = raw_input("Please select a game difficulty by typing it in!\nPossible choices include easy, med, adv , final:\n" ).lower()
    if level in game_data:
        user_selected_quiz = game_data[level]["selected_quiz"]
        print "You have chosen " + level + "! \nThe current paragraph reads as such..\n" + user_selected_quiz
        user_selected_ans_list = game_data[level]["selected_ans_list"]
    else:
        print "That's not an option! \nWrong..Please enter the correct level from easy, med, adv"
        return choose_level()
    select_level = level
    return select_level, user_selected_quiz, user_selected_ans_list
def input_guess_count_frm_user():
    """Define a function name input_guess_count_frm_user. In this function user can input his own number of guesses. It should return guess count"""
    try:
        guess_count1 = int(raw_input(" Enter a number i.e how many guesses you want for this fill in the blanks quiz?..." ))
        print "You will get " + str(guess_count1) + " guesses per problem"           
    except:
        print "Your input is wrong.Please enter a number."
        return input_guess_count_frm_user()
   
    return guess_count1

def main_quiz_game():
    """Define a function name main_quiz_game() to compare user guessed answers with real answers i.e user selected answers list. It should print a paragraph with correct answers.If all the answers are wrong it should exit"""
    select_level, user_selected_quiz, user_selected_ans_list = choose_level()
    guess_count1 = input_guess_count_frm_user()
    pos = 0
    for blank in ["_1_", "_2_", "_3_", "_4_"]:
        guess_count = guess_count1 
        while guess_count!=0:            
            answer_guess_frm_user = raw_input("\n What should be substitued in for " + blank + " ?\n" ).lower()
            if answer_guess_frm_user == user_selected_ans_list[pos]:
                user_selected_quiz = user_selected_quiz.replace(blank, answer_guess_frm_user)
                print "Correct\nThe current paragraph reads as such:\n" + user_selected_quiz
                break
            else:
                print "That isn't the correct answer! Let's try again; You have " + str(guess_count-1) + " trys left.\nThe current paragraph reads as such:\n" + user_selected_quiz
            guess_count = guess_count-1
        else:
            return False
        pos = pos+1

main_quiz_game()

