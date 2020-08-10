game_list=[0,1,2]
def game_display(game_list):
    print("Here is the game list: ")
    print(game_list)
def postion_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice = input("pick a postion (0,1,2): ")
        if choice not in ['0','1','2']:
            print("sorry invalid choice!")
            
    return int(choice)
def replacement_choice(game_list,postion):
    user_input = input("enter string to place at postion: ")
    game_list[postion] = user_input
    return game_list
def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice = input("Do you want to play Yes or No (Y or N): ")
        if choice not in ['Y','N']:
            print("sorry invalid choice!")
    if choice == 'Y':
        return True
    else:
        return False
gameon = True
game_list = [0,1,2]

while gameon:
    game_display(game_list)
    
    postion = postion_choice()
    game_list = replacement_choice(game_list,postion)
    game_display(game_list)
    
    gameon = gameon_choice()
    
