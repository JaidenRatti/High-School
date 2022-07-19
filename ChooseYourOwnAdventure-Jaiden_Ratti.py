import time
import math
import random
import os
import datetime


global bag
bag = []
global money
money = 0
global loan
loan = 0
global payback
payback = True
global start_time
global rate
rate = 0
global damage
damage = 0

def question(first,second):
    length = len(first)*3
    print("*"*length)
    print(f'{first[0]} - {first}')
    print("-"*length)
    print(f'{second[0]} - {second}')
    print("*"*length)
    choose = input("Choose a letter wisely ").lower()
    if(choose == 'backpack'):
        backpack()
        return question(first,second)
    return choose

def question2(first,second,third):
    length = len(first)*3
    print("*"*length)
    print(f'{first[0]} - {first}')
    print("-"*length)
    print(f'{second[0]} - {second}')
    print("-"*length)
    print(f'{third[0]} - {third}')
    print("*"*length)
    choose = input("Choose a letter wisely ").lower()
    if(choose == 'backpack'):
        backpack()
        return question2(first,second,third)
    return choose

def fetch_time():
    time = datetime.datetime.now()

    seconds = time.second
    minutes = time.minute*60
    hours = time.hour*3600

    return seconds+minutes+hours

def backpack():
    global money
    print("Here you go")
    if(money == 0):
        print("YOU HAVE NO MONEY")
    else:
        print(f'You have ${money}')
    if(len(bag) == 0):
        print("BAG HAS NO ITEMS")
    else:
        print(bag)
    waiting = input("Press enter to continue")


def first_message():
    print("!WARNING!\n"*4)
    #time.sleep(2)
    print(f'The game you are about to play WILL induce severe rage.\n')
    #time.sleep(2)

    one = "Yes"
    two = "No"
    begin_game = question(one,two)

    if begin_game == one.lower() or begin_game == one[0].lower():
        print("\nAlright, I warned you though.")
        #time.sleep(1)
        print("Game starting in")
    elif begin_game == two.lower() or begin_game == two[0].lower():
        print("\nTOO BAD. You have no other choice")
        #time.sleep(1)
        print("Game starting in")
    else:
        print("You somehow managed to get that wrong.... wow...")
        #time.sleep(1)
        print("Lets try this again....\n")
        #time.sleep(3)
        first_message()
    print("3..")
    #time.sleep(1)
    print("2..")
    #time.sleep(1)
    print("1..")
    game_intro()


def game_intro():
    title = "~Welcome to 'Survive the Unknown'~\n"
    print(("*" + len(title) * " " + "*\n") *10)
    print(f'{title:^38}')
    print(("*" + len(title) * " " + "*\n") * 10)
    earth()
    

def earth():
    global money
    print("Earth is blowing up and you have been sent on an escape pod to another planet. Your goal is to SURVIVE with the MOST AMOUNT OF MONEY POSSIBLE\nYou can choose to take one item with you")
    one = "$500,000"
    two = "Medicine Kit"
    #time.sleep(1)
    choice = question(one,two)
    #time.sleep(3)
    if(choice == one[0].lower() or choice == one[0]):
       print("Interesting choice. If you EVER want to see what you are carrying, type in 'backpack' at any moment.")
       money = 500000
    elif (choice == two[0].lower()):
       print("Great choice. If you EVER want to see what you are carrying, type in 'backpack' at any moment.")
       bag.append("Medicine Kit")
    else:
        print("Invalid. Start again")
        earth()
        return

    bag_test = input("Try it now!").lower()
    if(bag_test == 'backpack'):
        backpack()
        print("Nice! Now back to Earth blowing up")
        approach()
    else:
        print("Wow, following instructions is a bit difficult for you huh? Don't think this game is for you. I'll give you another shot.")
        bag_test_again = input("Pleaseee type in backpack")
        if(bag_test_again == 'backpack'):
            print("Second time is a charm")
            print(bag)
            approach()
        else:
            print("I've had enough of this. This is not gonna work. Bye")
            restart()
            return
         
def approach():
    global money
    global loan
    print("While approaching the planet in your high-tech escape pod, you can either crash land or eject and parachute downwards")
    one = "Crash Land"
    two = "Eject & Parachute"
    choice = question(one,two)
    if(choice == one[0].lower()):
        crash()
    elif(choice == two[0].lower()):
        eject()
    else:
        print("Invalid option")
        restart()
        return
    
def crash():
    global money
    global loan
    money += 1000000
    loan = 1000000
    print("Your crash has resulted in over $2,000,000 in property damage (converted from alien currency to dolloars of course)\nYou must pay it back or you will be hunted and killed! Fortunately a kind alien has gifted you $1,000,000 but you still need more!) ")
    print("There are two ways to get the money. Play Blackjack or Invest in the crazy markets")
    money += 1000000
    one = "Blackjack"
    two = "Invest"
    choice = question(one,two)
    if(choice == one[0].lower()):
        blackjack()
    elif(choice == two[0].lower()):
        invest()
    else:
        print("Invalid option")
        restart()
        return

def blackjack():
    global money
    total = 0
    print("Welcome to Blackjack. The aim of the game is simple. You are going to be given 2 cards and you need to be closer to 21 than the dealer!")
    print("You can hit if you would like another card but make sure you don't bust!")
    dealer_one = random.randint(1,11)
    dealer_two = random.randint(1,10)

    d_total_two = dealer_one + dealer_two


    user_one = random.randint(1,11)
    user_two = random.randint(1,10)

    u_total_two = user_one + user_two

    print(f'Your two cards are {user_one} and {user_two} for a total of {u_total_two}')
    if(u_total_two == 21):
        print("WOWOWOWOW You won already!! You have tripled your initial bet!!")
        money*=3
        evaluation()

    user_updated_total = hit(u_total_two)
    print(f'The dealers two cards are {dealer_one} and {dealer_two} for a total of {d_total_two}')
    dealer_game(user_updated_total,d_total_two)
    
def hit(total):
    global money
    choose = input("Would you like to hit or stay?")
    if choose == "hit":
        user = random.randint(1,11)
        print(f'You got a {user}')
        total += user
        print(f'Your new total is {total}')
        if(total > 21):
            print("BUST. There's no recovering from this loss. Since you can't pay back the money you have been terminated")
            restart()
        elif total == 21:
            print("WOW. You have doubled your initial bet!!")
            money *= 2
            evaluation()
        return hit(total)
    if choose == "stay":
        return total
    else:
        print("INVALID")
        restart()

def dealer_game(user_total,d_total):
    if(d_total > user_total and d_total <= 21):
        print("LOOKS LIKE YOU LOST")
        restart()
    elif(d_total == user_total):
        print("Tie means LOSS!")
        restart()
    elif d_total> 21:
        print("Dealer busted... you won double your bet!")
        evaluation()
    elif d_total < 16:
        print("Dealer is hitting again")
        dealer_three = random.randint(1,11)
        d_total += dealer_three
        print(f'Dealer got a {dealer_three}')
        print(f'Dealers new total is {d_total}')
        dealer_game(user_total,d_total)
    elif d_total > 16 and user_total > d_total and user_total < 21:
        print("NICE. You won double your bet!")
        evaluation()


def invest():
    global money
    print("You are going to have to invest all your money in one of the following 3 companies.\n")
    one = "LiftOff Industries"
    two = "Big Bang Studio"
    three = "Reach4theStars"
    print(f'{one} --- {two} --- {three}')
    c1 = random.randint(0,2)
    if(c1 == 0):
        c2 = random.randint(1,2)
    elif(c1 == 1):
        c2 = random.randint(0,1)*2
    else:
        c2 = random.randint(0,1)
    c3 = 3-(c1+c2)
    choices = [" is facing some legal tension with Banana Inc", " just sent a missile to Earth"," just sent a rover to Jupiter"]
    print("COMPANY NEWS")
    print("*"*20)
    print(one + choices[c1])
    print(two+choices[c2])
    print(three+choices[c3]+"\n")
    print("PICK A STOCK")
    choice = question2(one,two,three)
    if choice == one[0].lower():
        news_num = c1
    elif choice == two[0].lower():
        news_num = c2
    elif choice == three[0].lower():
        news_num = c3
    else:
        print("INVALID")
        restart()

    if(news_num == 0):
        decrease = 0.50
        money *= decrease
        print("The company was just sued by Banana Inc. and their stock dropped by over 50%. Your balance is ")
        print("You have gone into so much debt that the aliens don't even give you a chance to earn back the money and vapourize you")
    elif news_num == 1:
        increase = random.randrange(60,81,10)
        print(f'The media just announced that the missile sent to Earth successfully exploded. Shares exploded upwards of {increase}%')
        print(f'Starting Value: ${money:.2f}\nCurrent Value: ${money*(1+increase/100):.2f}')
        money = money* (1+(increase/100))
        evaluation()
    elif news_num == 2:
        increase = random.randrange(60,91,10)
        print(f'They have just announced their successful rover landing on Jupiter and the stock rocketed over {increase}%')
        print(f'Starting Value: ${money:.2f}\nCurrent Value: ${money*(1+increase/100):.2f}')
        money = money*(1+(increase/100))
        evaluation()


def eject():
    print("You manage to land better than expected and end up in a majestic forest. Do you stay along the forest trail or head off the beaten path")
    one = "Trail"
    two = "Beaten Path"
    choice = question(one,two)
    if(choice == one[0].lower()):
        trail()
    elif(choice == two[0].lower()):
        beaten()
    else:
        print("INVALID")
        restart()
        
def trail():
    global money
    global loan
    print("After more walking, you come across the local casino. Since you are in need of some cash, you ask a nearby alien for a loan of $500,000 to gamble and make more money.")
    print("Choose a casino game below to play")
    loan = 500000
    money += loan

    one = "Blackjack"
    two = "Roulette"
    three = "Fill 'Em"
    choice = question2(one,two,three)
    if(choice == one[0].lower()):
        blackjack()
    elif(choice == two[0].lower()):
        roulette()
    elif(choice == three[0].lower()):
        fillem()
    else:
        print("INVALID")
        restart()

def roulette():
    print("Roulette on this planet works similar to Earth. There are 37 numbers in total. There are 18 red, 18 black, and 1 green (green is always 0).")
    print("Your goal is to guess either the number that will be picked or the colour that will be picked. Correct number triples bet and correct colour doubles bet (you are going all in)")
    one = "Number"
    two = "Colour"
    choice = question(one,two)
    if(choice == one[0].lower()):
        number()
    elif(choice == two[0].lower()):
        colour()
    else:
        print("INVALID")
        restart()

def number():
    global money
    global bag
    num_choice = int(input("Enter your number from 0-36: "))

    real_num = random.randint(0,36)
    print(f'The number picked on the roulette table is {real_num}')
    if num_choice == real_num:
        print("WOW!!!! Victory. You have tripled your money!!!")
        money = money*3
        evaluation()
    elif num_choice != real_num:
        loser()
    elif abs((num_choice - real_num) < 5 and num_choice != real_num):
        print("So close but not close enough")
        loser()
    else:
        print("Invalid input")
        number()

def colour():
    global money
    global bag
    col_choice = input("Enter 'red' 'green' or 'black': ")
    possible_colours = ['green','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    if(col_choice not in possible_colours):
        print("Invalid colour")
        colour()
    real_colour = random.choice(possible_colours)
    print(f'The colour that the ball landed on is: {real_colour}')
    if col_choice == real_colour:
        print("WOW!!!! Victory. You have doubled your money!!!")
        money = money*2
        evaluation()
    elif col_choice != real_colour:
        loser()

def fillem():
    print("In Fill Em, your success is determined by you *for the most part*. Basically there are containers that get filled with astericks and your job is to guess which container you think will have the most astericks in it")
    print("The catch is that YOU get to determine how many containers there are.\n You must have at least 2 containers and at max 5 containers.")
    print("If you guess correctly, you get your initial bet (all of your current money) multiplied by the number of total containers in play")
    print("The higher the risk.. the higher the reward!")
    amount = int(input("Enter the number of containers between 2-5 you would like."))
    guess = int(input("Which container is going to have the most astericks?"))
    if(guess > amount):
        print("You must choose a container within the range. You chose too high")
        fillem()
    elif (guess < 1):
        print("You must choose a container within the range. You chose too low")
        fillem()

    containers(amount,guess)
def containers(number_of,choice):
    global money
    global bag
    if (number_of == 2):
        total = random.randint(0,24)*"*"
        print(('['+total+']\n'))
        total2 = random.randint(0,24)*"*"
        print(('['+total2+']\n'))
        if choice == 1:
            chosen_string = total
        elif choice == 2:
            chosen_string = total2
        if len(chosen_string) == max(len(total), len(total2)):
            print("Wow you doubled your money")
            money *= 2
            evaluation()
        else:
            print("Unlucky")
            loser()

    elif (number_of == 3):
        total = random.randint(0,24)*"*"
        print(('['+total+']\n'))
        total2 = random.randint(0,24)*"*"
        print(('['+total2+']\n'))
        total3 = random.randint(0,24)*"*"
        print(('['+total3+']\n'))

        if choice == 1:
            chosen_string = total
        elif choice == 2:
            chosen_string = total2
        elif choice == 3:
            chosen_string = total3
        if len(chosen_string) == max(len(total), len(total2),len(total3)):
            print("Wow you tripled your money")
            money *= 3
            evaluation()
        else:
            print("Unlucky")
            loser()

    elif (number_of == 4):
        total = random.randint(0,24)*"*"
        print(('['+total+']\n'))
        total2 = random.randint(0,24)*"*"
        print(('['+total2+']\n'))
        total3 = random.randint(0,24)*"*"
        print(('['+total3+']\n'))
        total4 = random.randint(0,24)*"*"
        print(('['+total4+']\n'))

        if choice == 1:
            chosen_string = total
        elif choice == 2:
            chosen_string = total2
        elif choice == 3:
            chosen_string = total3
        elif choice == 4:
            chosen_string = total4
        if len(chosen_string) == max(len(total), len(total2),len(total3), len(total4)):
            print("Wow you quadrupled your money")
            money *= 4
            evaluation()
        else:
            print("Unlucky")
            loser()
    elif(number_of == 5):
        total = random.randint(0,24)*"*"
        print(('['+total+']\n'))
        total2 = random.randint(0,24)*"*"
        print(('['+total2+']\n'))
        total3 = random.randint(0,24)*"*"
        print(('['+total3+']\n'))
        total4 = random.randint(0,24)*"*"
        print(('['+total4+']\n'))
        total5 = random.randint(0,24)*"*"
        print(('['+total5+']\n'))
        if choice == 1:
            chosen_string = total
        elif choice == 2:
            chosen_string = total2
        elif choice == 3:
            chosen_string = total3
        elif choice == 4:
            chosen_string = total4
        elif choice == 5:
            chosen_string = total5
        if len(chosen_string) == max(len(total), len(total2),len(total3), len(total4),len(total5)):
            print("Wow you quintupled your money")
            money *= 5
            evaluation()
        else:
            print("Unlucky")
            loser()
    else:
        print("Invalid amount. Between 2-5 please")
        fillem()

    
def loser():
    print("Damn must suck to suck at probability games. Welp since you can't pay back the loan, you have been vapourized")
    restart()
        

def beaten():
    print("After hours on this beaten path and many bruises later, you approach a cliff with water. Do you turn around and go to the trail or jump into the water")
    one = "Trail"
    two = "Jump"
    choice = question(one,two)
    if(choice == one[0].lower()):
        trail()
    elif(choice == two[0].lower()):
        jump_cliff()
    else:
        print("INVALID")
        restart()


def jump_cliff():
    global bag
    print("After jumping (for some strange reason), it turns out that the liquid at the bottom of the cliff was not water, but simply a mirage from hallucinations.")
    print("You have sustained severe injuries")
    if 'Medicine Kit' in bag:
        print("Fortunately you have your medicine kit in your bag and can heal yourself.")
        healing = input("Press [x] to heal ")
        if(healing == 'x'.lower()):
            print("Great. Full health and ready to go")
            bag.remove('Medicine Kit')
            trail()
        else:
            print("INVALID")
            jump_cliff()

    else:
        print("Unfortunately you do not have any sort of medicine kit and end up DYING from wounds")
        restart()
        
def evaluation():
    global money
    global loan
    global payback
    print(f'\nYou now have ${money:.2f}.\nDo you repay ${loan:.2f} to the alien or try and runaway with it')
    one = "Pay up"
    two = "Runaway"
    choice = question(one,two)
    if(choice == one[0].lower()):
        payback = True
        paid()
    elif(choice == two[0].lower()):
        payback = False
        ranaway()
    else:
        print("INVALID")
        restart()

def paid():
    global money
    global loan
    money -= loan
    print(f"You paid the alien and are left with ${money}")
    print("Do you try and find and a job in the town or venture off to explore the rest of the planet?")
    one = "Venture"
    two = "Job"
    choice = question(one,two)
    if(choice == one[0].lower()):
        explore()
    elif(choice == two[0].lower()):
        job()
    else:
        print("INVALID")
        restart()
def ranaway():
    global money
    global loan
    print(f'You managed to escape with ${money} but are severely burned from the ray gun that you have been shot with during your escape.')
    if 'Medicine Kit' in bag:
        print("Thankfully you have your Medicine Kit from launch and can heal yourself")
        healing = input("Press [x] to heal ")
        if(healing == 'x'.lower()):
            print("Great. Full health and ready to go")
            bag.remove('Medicine Kit')
        else:
            print("INVALID")
            restart()
    else:
        print("The damage is bearable and you can move on without a medicine kit. Keep in mind your health will be impacted. ")

    explore()


def explore():
    global money
    print("After a lot of exploring, you get tired and need a place to sleep for the night.")
    print("Would you like to sleep in the Popular Motel Moon ($50/night) or Light Year Lodge ($45/night)")
    one = "Motel Moon"
    two = "Light Year Lodge"
    choice = question(one,two)
    if(choice == one[0].lower()):
        money -= 50
        motel_moon()
    elif(choice == two[0].lower()):
        money -= 45
        lodge()
    else:
        print("INVALID")
        restart()

def motel_moon():
    global payback
    if(payback == False):
        print("In the middle of the night, the alien that you did not repay finds you and brutally turns you into ashes (DEAD!)")
        restart()
    lodge()


def lodge():
    print("In the middle of the night, an alien with a weapon attempts to break into your room and kidnap you with a ray gun. Fight back like the courageous human you are... or get kidnapped")
    one = "Fight"
    two = "Kidnap"
    choice = question(one,two)
    if(choice == one[0].lower()):
        fight()
    elif(choice == two[0].lower()):
        kidnap()
    else:
        print("INVALID")
        restart()

def kidnap():
    global money
    global bag
    money = money/2
    print("Since you gave up that easily, the kidnapper is stealing half of your money!")
    print("Also..")
    boss()
    
def fight():
    print("Quite the fiesty human I see. The alien pulls out his ray gun and points it at your head.\nDo you try and knock it out of his hands or jump out of the way.")
    one = "Knock"
    two = "Jump Away"
    choice = question(one,two)
    if(choice == one[0].lower()):
        knock()
    elif(choice == two[0].lower()):
        jump()
    else:
        print("INVALID")
        restart()


def knock():
    print("You managed to hit the gun across the room.. but now its an old fashioned fist fight.")
    print("Quickly type in the hints on your screen to avoid getting beat to DEATH. Timing, case and precision both matter!!")
    max_time = 10
    start_time = fetch_time()
    if(user_typed("punch") and user_typed("left") and user_typed("hook") and user_typed("right") and user_typed("left") and user_typed("jab")):
        end_time = fetch_time()
        user_time = end_time - start_time
        if(user_time > max_time):
            print(f'You took too long! You have to be under {max_time} seconds and you were {user_time} seconds!')
        else:
            victor()
            return
    print("DEATH. At least you went out with a bang. Told you this would be rage inducing.")
    restart()
def jump():
    print("You jump to the other side of the room and need to doge his bullets now. Quickly type in the directions on your screen to avoid gettting vaporized.")
    print("Timing and precision matter!!")
    max_time = 10
    start_time = fetch_time()
    if(user_typed("right") and user_typed("jump") and user_typed("duck") and user_typed("left") and user_typed("pounce")):
        end_time = fetch_time()
        user_time = end_time - start_time
        if(user_time > max_time):
            print(f'You took too long! You have to be under {max_time} seconds and you were {user_time} seconds!')
        else:
            victor()
            return
    print("DEATH. Vapourized just like that. Told you this would be rage inducing.")
    restart()
    
def user_typed(text):
    user = input(f'Type "{text}": ')
    return user == text



def victor():
    global bag
    bag.append("Shield")
    print("Intense battle but you pulled through! The alien has been killed and their portable shield has been added to your inventory (it will surely come in handy later)")
    boss()

def job():
    print("You desperately need a job.")
    print("Which one do you plan on taking")
    one = 'Typewriter'
    two = 'Rope Walker'
    three = 'Chef'
    choice = question2(one,two,three)
    if(choice == one[0].lower()):
        typer()
    elif(choice == two[0].lower()):
        tightrope()
    elif(choice == three[0].lower()):
        chef()
    else:
        print("INVALID")
        restart()

def chef():
    global money
    print("For your culinary evaluation, you will need to answer a series of questions all correctly. Any wrong answer will result in the removal of your existence")
    print("*"*20)
    print("How can you tell if a cranberry is ripe?")
    first = "If it smells good"
    second = "If it bounces"
    third = "If it is bright red"
    fourth = "If it is 1 mm in diameter"
    chef_quiz(first,second,third,fourth)
    choose = input("Pick a letter".lower())
    if(choose == 'b'.lower()):
        print("Correct")
        print("*"*20)
        print("Which Vitamin is the ONLY one that is not found in an egg")
        first = "Vitamin A"
        second = "Vitamin B"
        third = "Vitamin C"
        fourth = "Vitamin D"
        chef_quiz(first,second,third,fourth)
        choose = input("Pick a letter".lower())
        if(choose == 'c'.lower()):
            money += 6000
            print("Wow! 100%.\n You've been rewarded $6000")
            boss()
        else:
            print("Hmm. Looks like this planet isn't for you if you can't get that one right. Goodbye!")
            restart()
    else:
        print("Hmm. Looks like this planet isn't for you if you can't get that one right. Goodbye!")
        restart()

def chef_quiz(one,two,three,four):
    print(f'[a] - {one}')
    print(f'[b] - {two}')
    print(f'[c] - {three}')
    print(f'[d] - {four}')
    return

def tightrope():
    print("Yea.... not too sure why you picked a rope walker when you have no experience")
    print("You fall into a 500 ft valley during an event and DIE")
    restart()
    
def typer():
    global money
    global bag
    print("Your career as a typewriter is going quite well.\nYou must get 100% accuracy (including punctuation) on this next court case or else its GAME OVER")
    print("_"*30)
    text = "Sir, I think you are mistaken. My client did not intend on running that man over with his car!"
    print(text)
    test = input("Type it out!")
    if(test == text):
        money += 5000
        print("Fantastic job. You've been rewarded $5000")
        print("The King of the land sees you as a valuable asset to the Global Economy and wants to meet you!")
        boss()
    if(test != text):
        print("Looks like you messed up. Dissappointing..... Currently being exiled from the land. Cya!")
        restart()
    
def boss():
    global bag
    global money
    global rate
    global damage
    print("Due to your success on this new planet you are being taken to see the leader of the planet to determine your fate.")
    print("Your ENTIRE performance leading up this moment will dictate the outcome of this interaction!")
    if 'Medicine Kit' in bag:
        print("PS. Your Medicine Kit won't help you in this fight!")
    print("Before you enter the palace, you figure its a good idea to purchase some weapons outside")
    print("First, here is your bag")
    backpack()
    shop()
def shop():
    global bag
    global money
    global rate
    global damage
    global ar
    global rb
    global pistol
    global osw
    print("Choose which weapon you would like to purchase")
    first = "Pistol - $1000\nINFO: Fire rate of 1 bullet/s and 5 damage per shot"
    second = "Assault Rifle - $200000\nINFO: Fire rate of 5 bullets/s and 10 damage per shot"
    third = "Ray Bazooka - $450000\nINFO: Fire rate of 3 rays/s and 20 damage per shot"
    fourth = "One Shot Wonder - $4999954\nINFO: Fire rate of 1 ray/s and 100 damage per shot"
    chef_quiz(first,second,third,fourth)
    choice = input("Pick a letter")
    if(choice == 'a'.lower() and money >= 1000):
        print("Pistol Acquired")
        bag.append('Pistol')
        money -= 1000
        damage = 10
        rate = 1
    elif(choice == 'b'.lower() and money >=200000):
        print("Assault Rifle Acquired")
        bag.append('Assault Rifle')
        money -= 200000
        damage = 10
        rate = 5
    elif(choice == 'c'.lower() and money >= 450000):
        print("Ray Bazooka Acquired")
        bag.append('Ray Bazooka')
        money -= 450000
        damage = 20
        rate = 3
    elif(choice == 'd'.lower() and money >= 4999954):
        print("One Shot Wonder Acquired")
        bag.append('One Shot Wonder')
        money -= 4999954
        damage = 100
        rate = 1
    else:
        print("INVALID")
        shop()
        return

    print("You finally meet the Leader of the land, King ANUBIS")
    print("Just like many other situations on this island, your fate lies in your ability to fight")
    print("Lord ANUBIS will fight you 1-on-1. Winner becomes leader of the land and loser gets exiled")
    print("Do you agree to these terms?")
    one = "Yes"
    two = "No"
    decide = question(one,two)
    if(decide == one[0].lower()):
        print("Perfect")
    elif(decide == two[0].lower()):
        print("TOO BAD. You have no other choice")
    else:
        print("Regardless of what you tell me, this fight IS happening")
    print("Let the battle begin")

    print("The fight will be a standard battle with either two options, shoot or shield")
    print("RULES")
    print("\nThe amount of times you can consecutively type 'shoot' depends on the fire rate of the weapon. For example if your gun does 4 bullets per second. After you enter the 4th bullet, your gun will be on cooldown")
    print("\nYou only have a total of 8 shields in total. You should use your shield when you can no longer shoot")

    print("You will have 100hp and ANUBIS will have 100hp")

    anubis_hp = 100
    your_hp = 100
    cooldown_counter = 0
    shield_counter = 8

    final_scene(anubis_hp,your_hp,cooldown_counter,shield_counter)

def final_scene(anubis,your,cooldown,shield):
    global damage
    global rate
    if(anubis <= 0):
        print("YOU HAVE DEFEATED THE KING")
        final_statement()
        return
    elif (your <= 0):
        print("YOU HAVE LOST")
        print("It was a good run, so close yet so far")
        print("Lets try it again")
        restart()
    first = input("'Shoot or 'Shield'")
    hashtag_your = your//10
    amount_your = "#"*hashtag_your

    hashtag = anubis//10
    amount = "#"*hashtag

    if(first == "shoot"):
        if(cooldown >= rate):
            print("You shot during your cooldown!")
            your -= 10
            hashtag_your = your//10
            amount_your = "#"*hashtag_your
            dash_your = "-"*(10-hashtag_your)
            hashtag = anubis//10
            amount = "#"*hashtag
            dash = "-"*(10-hashtag)
            print(f'ANUBIS hp: [{amount}{dash}]')
            print(f'Your hp: [{amount_your}{dash_your}]')
            return(final_scene(anubis,your,cooldown,shield))
        else:
            cooldown += 1
            anubis -= damage
            hashtag_your = your//10
            amount_your = "#"*hashtag_your
            dash_your = "-"*(10-hashtag_your)
            hashtag = anubis//10
            amount = "#"*hashtag
            dash = "-"*(10-hashtag)
    
            print(f'ANUBIS hp: [{amount}{dash}]')
            print(f'Your hp: [{amount_your}{dash_your}]')
            return(final_scene(anubis,your,cooldown,shield))
    elif first == "shield":
        hashtag = anubis//10
        amount = "#"*hashtag
        hashtag_your = your//10
        amount_your = "#"*hashtag_your
        dash_your = "-"*(10-hashtag_your)
        hashtag = anubis//10
        amount = "#"*hashtag
        dash = "-"*(10-hashtag)
        if(shield <= 0):
            print("You have ran out of shields")
            print(f'ANUBIS hp: [{amount}{dash}]')
            your -= 10
            hashtag_your = your//10
            amount_your = "#"*hashtag_your
            dash_your = "-"*(10-hashtag_your)
            print(f'Your hp: [{amount_your}{dash_your}]')
        cooldown = 0
        shield -= 1
        if(shield >= 0):
            print(f'You have {shield} shield left')

        print(f'ANUBIS hp: [{amount}{dash}]')
        print(f'Your hp: [{amount_your}{dash_your}]')
        return(final_scene(anubis,your,cooldown,shield))
    else:
        print("You really managed to mess up between two words.... RUN IT BACK")
        restart()


def restart():
    time.sleep(3)
    print("This is what I meant by rage inducing!")
    print("I'm going to start over but this time everything must be PERFECT!")
    global money
    global bag
    global loan
    global payback
    global rate
    global damage
    money = 0
    bag = []
    payback = True
    rate = 0
    damage = 0
    first_message()

def final_statement():
    global bag
    global money
    global damage
    global rate
    global loan
    global payback
    print("Congratulations! You are one of the very few subjects to successfully complete the 'Survive the Unknown' Simulation!")
    print("If you remember at the beginning, the goal was to make it out alive with the most amount of money possible")
    print("Here are your statistics!")
    print(f'Left over cash = ${money}')
    max_num = 4799955
    diff = max_num - money
    print(f'You were ${diff} from getting the most amount of money possible! Play again with a different route to see if you can reach it')
    one = "Yes"
    two = "No"
    choice = question(one,two)
    if(choice == one[0]):
        earth()
        money = 0
        bag = []
        payback = True
        rate = 0
        damage = 0
    elif(choice == two[0]):
        earth()
        money = 0
        bag = []
        payback = True
        rate = 0
        damage = 0
    else:
        print("Don't know what that is. Cya!")
        exit()    
    
first_message()


