import random
kill_zealot_cmd = "!kill zealot"
zealot_rate = 420
store_command = "!store"
exit_command = "!exit"
enderman_buy_command = "!buy enderman"

enderman_pet_level = 0
zealuck_buy_command = "!buy zealuck"
def kill_zealot():
    pass




def store(curent_zealuck_level,eye_ammount):
    while True:
        if enderman_pet_level == 0:
            print("\nLegendary Enderman Pet[Lv1] -> 10 !buy enderman")
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
                return curent_zealuck_level,eye_ammount
                break
            if curent_zealuck_level == 0 and eye_ammount < 1:
                print("You dont have enought Summoning Eyes for this level of zealuck")
            
            if curent_zealuck_level == 1 and eye_ammount >= 3:
                    print("you successfully bought zealuck level 2")
                    curent_zealuck_level = 2
                    eye_ammount = eye_ammount - 3
                    return curent_zealuck_level,eye_ammount
                    break
            if curent_zealuck_level == 1 and eye_ammount < 3:
                print("You dont have enought Summoning Eyes for this level of zealuck")
                    
            if curent_zealuck_level == 2 and eye_ammount >= 10:
                    print("you successfully bought zealuck level 3")
                    curent_zealuck_level = 3
                    eye_ammount = eye_ammount - 10
                    return curent_zealuck_level,eye_ammount
                    break
            if curent_zealuck_level == 2 and eye_ammount < 10:
                print("You dont have enought Summoning Eyes for this level of zealuck")
            
            if curent_zealuck_level == 3 and eye_ammount >= 25:
                    print("you successfully bought zealuck level 4")
                    curent_zealuck_level = 4
                    eye_ammount = eye_ammount - 25
                    return curent_zealuck_level,eye_ammount
                    break
            if curent_zealuck_level == 3 and eye_ammount < 25:
                print("You dont have enought Summoning Eyes for this level of zealuck")
            if curent_zealuck_level == 4 and eye_ammount >= 50:
                    print("you successfully bought zealuck level 5")
                    curent_zealuck_level = 5
                    eye_ammount = eye_ammount - 50
                    return curent_zealuck_level,eye_ammount
                    break
            if curent_zealuck_level == 0 and eye_ammount < 50:
                print("You dont have enought Summoning Eyes for this level of zealuck")
        if cmd ==  enderman_buy_command:
             if eye_ammount >= 10:
       
    





def main():
    eye_ammount = 24
    curent_zealuck_level = 0
    has_enderman = False
    while True:
        cmd = input(">")
        if cmd == kill_zealot_cmd:
            print("Kills")
        if cmd == store_command:
             print(eye_ammount)
             curent_zealuck_level,eye_ammount = store(curent_zealuck_level,eye_ammount)
             print(eye_ammount)






if __name__ == "__main__":
    main()