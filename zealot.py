import random
kill_zealot_cmd = "!kill zealot"

store_command = "!store"
exit_command = "!exit"
enderman_buy_command = "!buy enderman"


zealuck_buy_command = "!buy zealuck"
def kill_zealot(currentkills,has_endermanpet,zealuck_level,eye_amount):
    base_zealot_rate = 420
    zealot_rate_new = 0
    if currentkills >= 420 and currentkills < 630:
        base_zealot_rate = base_zealot_rate / 2
    if currentkills >= 630 and currentkills < 840:
        base_zealot_rate = base_zealot_rate / 3
    if currentkills >= 840:
        base_zealot_rate = base_zealot_rate / 4
    
    if has_endermanpet == True:
        base_zealot_rate = base_zealot_rate / 1.25

    if zealuck_level == 1:  
        base_zealot_rate = base_zealot_rate * 0.98 
    if zealuck_level == 2:  
        base_zealot_rate = base_zealot_rate * 0.96 
    if zealuck_level == 3:  
        base_zealot_rate = base_zealot_rate * 0.94  
    if zealuck_level == 4:  
        base_zealot_rate = base_zealot_rate * 0.92 
    if zealuck_level == 5:  
        base_zealot_rate = base_zealot_rate * 0.9  

    zealot_rate_new = 1/base_zealot_rate
    
    if random.random() < zealot_rate_new:
        print("You got a SPECIAL ZEALOT it took you (",currentkills,") To get a SPECIAL ZEALOT",sep="")
        eye_amount = eye_amount + 1
        print("you now have",eye_amount,"summoning eyes")
        currentkills = 0
    else:
        currentkills = currentkills + 1 
        print("No special zealot, you are at(",currentkills,") kills since your last special",sep="")
    return currentkills,eye_amount

    




def store(curent_zealuck_level,eye_ammount,has_endermanpet):
    while True:
        if has_endermanpet == False:
            print("\nLegendary Enderman Pet[Lv100] -> 25 !buy enderman")
        if curent_zealuck_level == 0:
            print("\nZealuck level 1 -> 1   too buy this level type !buy zealuck")
        if curent_zealuck_level == 1:
            print("\nZealuck level 2 -> 3   too buy this level type !buy zealuck")
        if curent_zealuck_level == 2:
            print("\nZealuck level 3 -> 10   too buy this level type !buy zealuck")
        if curent_zealuck_level == 3:
            print("\nZealuck level 4 -> 25   too buy this level type !buy zealuck")
        if curent_zealuck_level == 5:
            print("\nZealuck level 5 -> 50   too buy this level type !buy zealuck")
        
            
        cmd = input('\nWhat would you like to buy?(Type "!exit" to leave store): ')
        if cmd == exit_command:
             break
        if cmd == zealuck_buy_command:
            if curent_zealuck_level == 0 and eye_ammount >= 1:
                print("you successfully bought zealuck level 1")
                curent_zealuck_level = 1
                eye_ammount = eye_ammount - 1
                return curent_zealuck_level,eye_ammount,has_endermanpet
                break
            if curent_zealuck_level == 0 and eye_ammount < 1:
                print("You dont have enought Summoning Eyes for this level of zealuck")
            
            if curent_zealuck_level == 1 and eye_ammount >= 3:
                    print("you successfully bought zealuck level 2")
                    curent_zealuck_level = 2
                    eye_ammount = eye_ammount - 3
                    return curent_zealuck_level,eye_ammount,has_endermanpet
                    break
            if curent_zealuck_level == 1 and eye_ammount < 3:
                print("You dont have enought Summoning Eyes for this level of zealuck")
                    
            if curent_zealuck_level == 2 and eye_ammount >= 10:
                    print("you successfully bought zealuck level 3")
                    curent_zealuck_level = 3
                    eye_ammount = eye_ammount - 10
                    return curent_zealuck_level,eye_ammount,has_endermanpet
                    break
            if curent_zealuck_level == 2 and eye_ammount < 10:
                print("You dont have enought Summoning Eyes for this level of zealuck")
            
            if curent_zealuck_level == 3 and eye_ammount >= 25:
                    print("you successfully bought zealuck level 4")
                    curent_zealuck_level = 4
                    eye_ammount = eye_ammount - 25
                    return curent_zealuck_level,eye_ammount,has_endermanpet
                    break
            if curent_zealuck_level == 3 and eye_ammount < 25:
                print("You dont have enought Summoning Eyes for this level of zealuck")
            if curent_zealuck_level == 4 and eye_ammount >= 50:
                    print("you successfully bought zealuck level 5")
                    curent_zealuck_level = 5
                    eye_ammount = eye_ammount - 50
                    return curent_zealuck_level,eye_ammount,has_endermanpet
                    break
            if curent_zealuck_level == 0 and eye_ammount < 50:
                print("You dont have enought Summoning Eyes for this level of zealuck")
        if cmd ==  enderman_buy_command:
            if eye_ammount >= 25 and has_endermanpet == False:
                has_endermanpet = True
                eye_ammount = eye_ammount - 25
                return curent_zealuck_level,eye_ammount,has_endermanpet
            else:
                print("you dont have enought money for the enderman pet or already have it")
       
    





def main():
    eye_ammount = 24
    curent_zealuck_level = 5
    curent_kills = 950
    has_endermanpet = True
    while True:
        cmd = input(">")
        if cmd == kill_zealot_cmd:
            curent_kills,eye_ammount = kill_zealot(curent_kills,has_endermanpet,curent_zealuck_level,eye_ammount)
        if cmd == store_command:
             print(eye_ammount)
             curent_zealuck_level,eye_ammount = store(curent_zealuck_level,eye_ammount,has_endermanpet)
             print(eye_ammount)






if __name__ == "__main__":
    main()