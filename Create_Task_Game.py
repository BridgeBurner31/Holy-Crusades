import random

#start settings
global level
level = 1
global experience
experience = 0
global round_number
round_number = 1
global enemies_defeated
enemies_defeated = 0
global health 
health = 0
global max_health
max_health = 0
global score
score = 0
global player_critical_hit_counter
player_critical_hit_counter = 0
global enemy_critical_hit_counter
enemy_critical_hit_counter = 0
global player_hit_counter
player_hit_counter = 0

#attack function
def attack():
    global player_critical_hit_counter
    if level == 1:
        damage = random.randint(10,15)
        critical = random.randint(1,10)
        if critical == 1:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 2:
        damage = random.randint(15,30)
        critical = random.randint(1,9)
        if critical == 9:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2.1
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 3:
        damage = random.randint(30,45)
        critical = random.randint(1,8)
        if critical == 8:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2.2
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 4:
        damage = random.randint(56,70)
        critical = random.randint(1,7)
        if critical == 7:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2.3
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 5:
        damage = random.randint(80,100)
        critical = random.randint(1,6)
        if critical == 6:
            print("CRITICAL HIT!")
            damage = damage*2.4
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 6:
        damage = random.randint(115,145)
        critical = random.randint(1,5)
        if critical == 5:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2.5
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")    
    elif level == 7:
        damage = random.randint(160,200)
        critical = random.randint(1,4)
        if critical == 4:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2.6
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 8:
        damage = random.randint(205,270)
        critical = random.randint(1,4)
        if critical == 4:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2.7
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 9:
        damage = random.randint(300,330)
        critical = random.randint(1,4)
        if critical == 10:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*2.8
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    elif level == 10:
        damage = random.randint(345,370)
        critical = random.randint(1,4)
        if critical == 4:
            print("CRITICAL HIT!")
            player_critical_hit_counter = player_critical_hit_counter + 1
            damage = damage*3
            damage =  round(damage)
        print(f"{player_name}'s sword slash did {damage} damage! ")
        print("//////////////////////////////////////")
    return(damage)

#level up function    
level_up_two = True
level_up_three = True
level_up_four = True
level_up_five =  True
level_up_six = True
level_up_seven =  True
level_up_eight = True
level_up_nine =  True
level_up_ten = True

def experience_config():
    global level
    global level_up_two
    global level_up_three
    global level_up_four
    global level_up_five
    global level_up_six
    global level_up_seven
    global level_up_eight
    global level_up_nine
    global level_up_ten
    if experience >= 30 < 110 and level_up_two == True:
        level = 2
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_two = False
    elif experience >= 110 < 230 and level_up_three == True:
        level = 3
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_three = False
    elif experience >= 230 < 450 and level_up_four == True:
        level = 4
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_four = False
    elif experience >= 450 < 900 and level_up_five == True:
        level = 5
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_five = False
    elif experience >= 900 < 1500 and level_up_six == True:    
        level = 6 
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_six = False
    elif experience >= 1500 < 2250 and level_up_seven == True:
        level = 7   
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_seven = False
    elif experience >= 2250 < 3100 and level_up_eight == True:
        level = 8
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_eight = False
    elif experience >= 3100 < 4500 and level_up_nine == True:
        level = 9
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_nine = False
    elif experience >= 4500 and level_up_ten == True:
        level = 10   
        print("//////////////////////////////////////")
        print(f"Level up! {player_name} is now Level: {level}!")
        print("//////////////////////////////////////")
        print("//////////////////////////////////////")
        level_up_ten = False
    return(level)

#determines health at a given level   
def health_config():
    if level == 1:
        max_health = 50000
    elif level == 2:
        max_health = 100000
    elif level == 3:
        max_health = 15000000
    elif level == 4:
        max_health = 250000
    elif level == 5:
        max_health = 400
    elif level == 6:
        max_health = 625
    elif level == 7:
        max_health = 770
    elif level == 8:
        max_health = 950
    elif level == 9:
        max_health = 1100
    elif level == 10:
        max_health = 1250
    return(max_health)
    
#healing function
def heal():
    if level == 1:
        healing = random.randint(16,20)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 2:
        healing = random.randint(30,40)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 3:
        healing = random.randint(60,80)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} {healing} health!")
        print("//////////////////////////////////////")
    elif level == 4:
        healing = random.randint(100,120)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 5:
        healing = random.randint(160,200)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 6:
        healing = random.randint(250,270)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 7:
        healing = random.randint(320,340)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 8:
        healing = random.randint(390,420)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 9:
        healing = random.randint(500,520)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    elif level == 10:
        healing = random.randint(600,700)
        print(f"{player_name} drank Holy Water!")
        print(f"{player_name} healed {healing} health!")
        print("//////////////////////////////////////")
    return(healing)
        
#round number configuration
def round_number_config():
    global round_number
    if enemies_defeated >= 10 < 20:
        round_number = 2
    if enemies_defeated >= 20 < 30:
        round_number = 3
    if enemies_defeated >= 30 < 40:
        round_number = 4
    if enemies_defeated >= 40 < 50:
        round_number = 5
    if enemies_defeated >= 50 < 60:
        round_number = 6
    if enemies_defeated >= 60 < 70:
        round_number = 7
    return(round_number)

health_config()
experience_config()
round_number_config()

#displays stats
def display_stats():
    print(f"Name: {player_name}")
    print(f"Level: {level}")
    print(f"Max Health: {health_config()}")
    print(f"Round number: {round_number_config()}")
    print(f"Experience: {experience}")
    print(f"Total enemies defeated: {enemies_defeated}")
    print(f"Score: {final_score(enemies_defeated, round_number, experience)}")
    print(f"Times {player_name} got a Critical Hit: {player_critical_hit_counter}") 
    print(f"Times an enemy got a Critical Hit: {enemy_critical_hit_counter}")
    print("//////////////////////////////////////")
    
#Calculates the final score
def final_score(enemies_defeated, round_number, experience):
    global score
    placeholderx = 0
    while placeholderx == 0:
        score = enemies_defeated + 10 * round_number + 2.75*experience - 10
        if health <= 0:
            break
    return(score)
    
#dictionaries of assets
round_one_enemies = {1: "Rabid Rat", 2: "Pitbull", 3: "Thug", 4: "Bum"}
round_two_enemies = {1: "Thug Boss", 2: "Mobster", 3: "White Belt Karate Man", 4: "Giant Cigarette"}
round_three_enemies = {1: "Mafioso", 2: "Interim FBI Agent", 3: "Sunny Side Up Egg", 4: "Rusty Robot"}
round_four_enemies = {1: "Brown Belt Karate Man", 2: "Thug God", 3: "Carbon Robot", 4: "Psycho Hipster"}
round_five_enemies = {1: "Godfather", 2: "FBI Agent", 3: "Lazer Man", 4: "Diamond Robot"}
round_six_enemies = {1: "Red Belt Karate Man", 2: "Pixeleen", 3: "E.T.", 4: "Unidentified Flying Object"}
round_seven_enemies = {1: "Black Belt Karate Man", 2: "Spectre", 3: "Flame", 4: "The One"}


#pretty much the game itself    
def battle_config():
    global enemy_critical_hit_counter
    placeholder = 0
    defeated_enemies_list = []
    while placeholder == 0:
        max_health = health_config()
        if round_number_config() == 1:
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_one_enemies[DiceRoll]
            if enemy == "Rabid Rat":
                print(f"A {enemy} has appeared! ")
                enemy_health = 40
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        global enemies_defeated
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(3,5)
                        global experience
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} bites you!")
                    enemy_damage = random.randint(6,10)
                    critical = random.randint(1,2)
                    if critical == 2:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////") 
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Pitbull":
                print(f"A {enemy} has appeared! ")
                enemy_health = 30
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(2,6)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} bites your neck!")
                    enemy_damage = random.randint(13,20)
                    critical = random.randint(1,5)
                    if critical == 5:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.5
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Thug":
                print(f"A {enemy} has appeared! ")
                enemy_health = 35
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if health <= 0:
                        print("You died!")
                        print("//////////////////////////////////////")
                        break
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(4,7)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} hits you with his crowbar!")
                    enemy_damage = random.randint(10,15)
                    critical = random.randint(1,50)
                    if critical == 50:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*20
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Bum":
                print(f"A {enemy} has appeared! ")
                enemy_health = 25
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(1,9)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} throws a burning trash can at you!")
                    enemy_damage = random.randint(10,15)
                    critical = random.randint(1,2)
                    if critical == 2:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2.5
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////") 
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            round_2_start = True
        if health <= 0:
            break
        elif round_number_config() == 2:
            if round_2_start == True:
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print(f"Round {round_number_config()} Start!")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                round_2_start = False
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_two_enemies[DiceRoll]
            if enemy == "Thug Boss":
                print(f"A {enemy} has appeared! ")
                enemy_health = 80
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(6,9)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} flashes a knife!")
                    enemy_damage = random.randint(23,28)
                    critical = random.randint(1,6)
                    if critical == 6:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.75
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Mobster":
                print(f"A {enemy} has appeared! ")
                enemy_health = 70
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(5,10)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    amount_of_times_attacked = random.randint(2,5)
                    print(f"The {enemy} shoots you {amount_of_times_attacked} times with a tommy gun!")
                    for i in range(amount_of_times_attacked):
                        enemy_damage = random.randint(6,10)
                        critical = random.randint(1,6)
                        if critical == 6:
                            print("CRITICAL HIT!")
                            enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                            enemy_damage = enemy_damage*1.75
                            enemy_damage = round(enemy_damage)
                        print(f"The {enemy} did {enemy_damage} damage! ")
                        health = health - enemy_damage
                        print(f"The {enemy}'s health is: {enemy_health}.")
                        print(f"{player_name}'s health is {health}/{max_health}.")
                        print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "White Belt Karate Man":
                print(f"A {enemy} has appeared! ")
                enemy_health = 65
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(8,9)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} hits you with a karate chop!")
                    enemy_damage = random.randint(29,34)
                    critical = random.randint(1,4)
                    if critical == 4:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.3
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Giant Cigarette":
                print(f"A {enemy} has appeared! ")
                enemy_health = 70
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(6,7)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy}'s smoke is too dangerous for you to inhale!")
                    enemy_damage = random.randint(20,40)
                    critical = random.randint(1,10)
                    if critical == 10:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.5
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")        
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            round_3_start = True
        if health <= 0:
            break
        elif round_number_config() == 3:
            if round_3_start == True:
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print(f"Round {round_number_config()} Start!")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                round_3_start = False
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_three_enemies[DiceRoll]
            if enemy == "Mafioso":
                print(f"A {enemy} has appeared! ")
                enemy_health = 70
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(12,20)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    amount_of_times_attacked = random.randint(3,7)
                    print(f"The {enemy} sprays you {amount_of_times_attacked} times with an Uzi!")
                    for i in range(amount_of_times_attacked):
                        enemy_damage = random.randint(8,15)
                        critical = random.randint(1,10)
                        if critical == 10:
                            print("CRITICAL HIT!")
                            enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                            enemy_damage = enemy_damage*2.3
                            enemy_damage = round(enemy_damage)
                        print(f"The {enemy} did {enemy_damage} damage! ")
                        health = health - enemy_damage
                        print(f"The {enemy}'s health is: {enemy_health}.")
                        print(f"{player_name}'s health is {health}/{max_health}.")
                        print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Interim FBI Agent":
                print(f"An {enemy} has appeared! ")
                enemy_health = 150
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(10,20)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} threatens to blackmail you!")
                    enemy_damage = random.randint(54,63)
                    critical = random.randint(1,5)
                    if critical == 5:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.3
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by an {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Sunny Side Up Egg":
                print(f"A {enemy} has appeared! ")
                enemy_health = 130
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(18,30)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} hits you with a ray of the sun!")
                    enemy_damage = random.randint(40,70)
                    critical = random.randint(1,5)
                    if critical == 5:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Rusty Robot":
                print(f"A {enemy} has appeared! ")
                enemy_health = 185
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(20,30)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} threw some rusty gears at you!")
                    enemy_damage = random.randint(40,45)
                    critical = random.randint(1,10)
                    if critical == 10:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2.5
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")        
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            round_4_start = True
        if health <= 0:
            break
        elif round_number_config() == 4:
            if round_4_start == True:
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print(f"Round {round_number_config()} Start!")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                round_4_start = False
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_four_enemies[DiceRoll]
            if enemy == "Brown Belt Karate Man":
                print(f"A {enemy} has appeared! ")
                enemy_health = 250
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(23,34)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    amount_of_times_attacked = random.randint(4,6)
                    print(f"The {enemy} karate chops you {amount_of_times_attacked} times with his fists!")
                    for i in range(amount_of_times_attacked):
                        enemy_damage = random.randint(15,20)
                        critical = random.randint(1,10)
                        if critical == 10:
                            print("CRITICAL HIT!")
                            enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                            enemy_damage = enemy_damage*2
                            enemy_damage = round(enemy_damage)
                        print(f"The {enemy} did {enemy_damage} damage! ")
                        health = health - enemy_damage
                        print(f"The {enemy}'s health is: {enemy_health}.")
                        print(f"{player_name}'s health is {health}/{max_health}.")
                        print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Thug God":
                print(f"A {enemy} has appeared! ")
                enemy_health = 300
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(25,27)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} shoots a mythical shotgun at you!")
                    enemy_damage = random.randint(78,90)
                    critical = random.randint(1,8)
                    if critical == 8:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.5
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Carbon Robot":
                print(f"A {enemy} has appeared! ")
                enemy_health = 280
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(25,36)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} hits you with a weak beam of energy!")
                    enemy_damage = random.randint(65,75)
                    critical = random.randint(1,5)
                    if critical == 5:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Psycho Hipster":
                print(f"A {enemy} has appeared! ")
                enemy_health = 200
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(21,37)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} is experiencing spiritual transformation!")
                    enemy_damage = random.randint(50,100)
                    critical = random.randint(1,4)
                    if critical == 4:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")        
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            round_5_start = True
        if health <= 0:
            break
        elif round_number_config() == 5:
            if round_5_start == True:
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print(f"Round {round_number_config()} Start!")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                round_5_start = False
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_five_enemies[DiceRoll]
            if enemy == "Lazer Man":
                print(f"A {enemy} has appeared! ")
                enemy_health = 340
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(25,37)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    amount_of_times_attacked = random.randint(10,15)
                    print(f"The {enemy} lazer beams you {amount_of_times_attacked} times with his lazer gun!")
                    for i in range(amount_of_times_attacked):
                        enemy_damage = random.randint(10,15)
                        critical = random.randint(1,20)
                        if critical == 20:
                            print("CRITICAL HIT!")
                            enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                            enemy_damage = enemy_damage*1.5
                            enemy_damage = round(enemy_damage)
                        print(f"The {enemy} did {enemy_damage} damage! ")
                        health = health - enemy_damage
                        print(f"The {enemy}'s health is: {enemy_health}.")
                        print(f"{player_name}'s health is {health}/{max_health}.")
                        print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "FBI Agent":
                print(f"A {enemy} has appeared! ")
                enemy_health = 400
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(30,32)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} threatens to freeze your bank account!")
                    enemy_damage = random.randint(135,150)
                    critical = random.randint(1,10)
                    if critical == 10:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.5
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Godfather":
                print(f"A {enemy} has appeared! ")
                enemy_health = 475
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(27,37)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} makes you swim with concrete shoes on!")
                    enemy_damage = random.randint(120,130)
                    critical = random.randint(1,5)
                    if critical == 5:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Diamond Robot":
                print(f"A {enemy} has appeared! ")
                enemy_health = 375
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(20,40)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} shines a glittering diamond!")
                    enemy_damage = random.randint(75,130)
                    critical = random.randint(1,4)
                    if critical == 4:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")        
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
                    round_5_start = True
        if health <= 0:
            break
        elif round_number_config() == 5:
            if round_5_start == True:
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print(f"Round {round_number_config()} Start!")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                round_5_start = False
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_five_enemies[DiceRoll]
            if enemy == "Lazer Man":
                print(f"A {enemy} has appeared! ")
                enemy_health = 340
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(25,37)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    amount_of_times_attacked = random.randint(10,15)
                    print(f"The {enemy} lazer beams you {amount_of_times_attacked} times with his lazer gun!")
                    for i in range(amount_of_times_attacked):
                        enemy_damage = random.randint(10,15)
                        critical = random.randint(1,20)
                        if critical == 20:
                            print("CRITICAL HIT!")
                            enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                            enemy_damage = enemy_damage*1.5
                            enemy_damage = round(enemy_damage)
                        print(f"The {enemy} did {enemy_damage} damage! ")
                        health = health - enemy_damage
                        print(f"The {enemy}'s health is: {enemy_health}.")
                        print(f"{player_name}'s health is {health}/{max_health}.")
                        print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "FBI Agent":
                print(f"A {enemy} has appeared! ")
                enemy_health = 400
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(30,32)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} threatens to freeze your bank account!")
                    enemy_damage = random.randint(135,150)
                    critical = random.randint(1,10)
                    if critical == 10:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.5
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Godfather":
                print(f"A {enemy} has appeared! ")
                enemy_health = 475
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(27,37)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} makes you swim with concrete shoes on!")
                    enemy_damage = random.randint(120,130)
                    critical = random.randint(1,5)
                    if critical == 5:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Diamond Robot":
                print(f"A {enemy} has appeared! ")
                enemy_health = 375
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(20,40)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} shines a glittering diamond!")
                    enemy_damage = random.randint(75,130)
                    critical = random.randint(1,4)
                    if critical == 4:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")        
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break    
            round_6_start = True
        if health <= 0:
            break
        elif round_number_config() == 6:
            if round_6_start == True:
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print(f"Round {round_number_config()} Start!")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                round_6_start = False
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_six_enemies[DiceRoll]
            if enemy == "Unidentified Flying Object":
                print(f"An {enemy} has appeared! ")
                enemy_health = 470
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(45,57)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    amount_of_times_attacked = random.randint(15,30)
                    print(f"The {enemy} hits you {amount_of_times_attacked} times with a tractor beam!")
                    for i in range(amount_of_times_attacked):
                        enemy_damage = random.randint(2,5)
                        critical = random.randint(1,15)
                        if critical == 15:
                            print("CRITICAL HIT!")
                            enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                            enemy_damage = enemy_damage*1.34
                            enemy_damage = round(enemy_damage)
                        print(f"The {enemy} did {enemy_damage} damage! ")
                        health = health - enemy_damage
                        print(f"The {enemy}'s health is: {enemy_health}.")
                        print(f"{player_name}'s health is {health}/{max_health}.")
                        print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by an {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Pixeleen":
                print(f"{enemy} has appeared! ")
                enemy_health = 500
                print(f"{enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"{enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(43,59)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"{enemy} whips a knife from the top of her go-go boot!")
                    enemy_damage = random.randint(200,220)
                    critical = random.randint(1,9)
                    if critical == 9:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.5
                        enemy_damage = round(enemy_damage)
                    print(f"{enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"{enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Bookkeeper's Son":
                print(f"A {enemy} has appeared! ")
                enemy_health = 520
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(48,55)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} has a case of dynamite and he could hold out here all night!")
                    enemy_damage = random.randint(190,220)
                    critical = random.randint(1,5)
                    if critical == 5:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2.2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Red Belt Karate Man":
                print(f"A {enemy} has appeared! ")
                enemy_health = 475
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(40,60)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} attacks you with a fiery karate chop!")
                    enemy_damage = random.randint(210,250)
                    critical = random.randint(1,8)
                    if critical == 8:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.7
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")        
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            round_7_start = True
        if health <= 0:
            break
        elif round_number_config() == 7:
            if round_7_start == True:
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print(f"Round {round_number_config()} Start!")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                print("//////////////////////////////////////")
                round_7_start = False
            DiceRoll = random.randint(1,4)
            health = max_health
            enemy = round_seven_enemies[DiceRoll]
            if enemy == "Spectre":
                print(f"An {enemy} has appeared! ")
                enemy_health = 700
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(70,80)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    amount_of_times_attacked = random.randint(2,6)
                    print(f"The {enemy} carpet bombed you {amount_of_times_attacked} times!")
                    for i in range(amount_of_times_attacked):
                        enemy_damage = random.randint(100,110)
                        critical = random.randint(1,20)
                        if critical == 20:
                            print("CRITICAL HIT!")
                            enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                            enemy_damage = enemy_damage*1.4
                            enemy_damage = round(enemy_damage)
                        print(f"The {enemy} did {enemy_damage} damage! ")
                        health = health - enemy_damage
                        print(f"The {enemy}'s health is: {enemy_health}.")
                        print(f"{player_name}'s health is {health}/{max_health}.")
                        print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by an {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Black Belt Karate Man":
                print(f"{enemy} has appeared! ")
                enemy_health = 650
                print(f"{enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"{enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(75,77)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"{enemy} uses the Death Punch!")
                    enemy_damage = random.randint(455,550)
                    critical = random.randint(1,10)
                    if critical == 10:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*1.45
                        enemy_damage = round(enemy_damage)
                    print(f"{enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"{enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "Donald Trump":
                print(f"A {enemy} has appeared! ")
                enemy_health = 625
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    damage = 0
                    healing = 0
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated the {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(57,97)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"The {enemy} built a Great Wall, the Greatest Wall, it made all the other walls cry!")
                    enemy_damage = random.randint(620,630)
                    critical = random.randint(1,20)
                    if critical == 20:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
            elif enemy == "The One":
                print(f"A {enemy} has appeared! ")
                enemy_health = 675
                print(f"The {enemy}'s health is {enemy_health}.")
                while enemy_health > 0:
                    damage = 0
                    healing = 0
                    command = input("Will you (1) Attack with your sword or (2) Drink Holy Water? Input the number. ")
                    if command == "1":
                        damage = attack()
                    elif command == "2":
                        healing = heal()
                    else:
                        print("You wasted a turn because you didn't input 1 or 2!")
                        print("//////////////////////////////////////")    
                    enemy_health = enemy_health - damage
                    health = health + healing
                    if health >= max_health:
                        e = health - max_health 
                        health = health - e
                    if enemy_health < 0:
                        b = enemy_health - enemy_health
                        enemy_health = b
                    print(f"{enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")
                    if enemy_health <= 0:
                        print(f"Congratulations, you have defeated {enemy}!")
                        print("DEUS VULT!")
                        enemies_defeated = enemies_defeated + 1
                        xp_gain = random.randint(69,78)
                        experience = experience + xp_gain
                        print(f"You have gained {xp_gain} experience! Your experience is now {experience}.")
                        print("//////////////////////////////////////")
                        defeated_enemies_list.append(enemy)
                        experience_config()
                        health_config()
                        display_stats()
                        break
                    print(f"You could not comprehend the power of {enemy}'s attack!")
                    enemy_damage = random.randint(300,260)
                    critical = random.randint(1,3)
                    if critical == 3:
                        print("CRITICAL HIT!")
                        enemy_critical_hit_counter = enemy_critical_hit_counter + 1
                        enemy_damage = enemy_damage*2.1
                        enemy_damage = round(enemy_damage)
                    print(f"The {enemy} did {enemy_damage} damage! ")
                    health = health - enemy_damage
                    print(f"The {enemy}'s health is: {enemy_health}.")
                    print(f"{player_name}'s health is {health}/{max_health}.")
                    print("//////////////////////////////////////")        
                    if health <= 0:
                        print("//////////////////////////////////////") 
                        print("//////////////////////////////////////")  
                        print("You Died! Restart?")
                        print(f"{player_name} was killed by a {enemy}.")
                        print(f"{player_name}'s score was {final_score(enemies_defeated, round_number, experience)}.")
                        print(f"{player_name} got {player_critical_hit_counter} critical hits.")
                        print(f"Enemies got {enemy_critical_hit_counter} critical hits.")
                        print("          Defeated enemies:")
                        ko = 0
                        for i in range(len(defeated_enemies_list)):
                            ko = ko + 1
                            print(f"{ko}. {defeated_enemies_list[i]}")
                        print("//////////////////////////////////////")  
                        print("//////////////////////////////////////")  
                        break
                    
#Start Message                    
print("You are a Holy Crusader put in the future to rid the modern world of its evil.")
print("Malicious miscreants have tarnished the purity of Earth.")
print("You will have to fight a variety of hideous and repugnant creatures.")
print("This will require strategic sword attacks and Holy Water drinks.")
print("Your adversaries will grow stronger as you progress.")

#Choosing a Name and random name specific messages
player_name = input("What is your name? ")
player_name = player_name
if player_name == "Deus Vult":
    print("You were born for this then.")
if player_name == "Crusader":
    print("You were born for this then.") 
if player_name == "Holy Crusader": 
    print("You were born for this then.")
if player_name == "Holy Crusades":
    print("You were born for this then.")
if player_name == "Pixeleen":
    pixeleen_text_choice = random.randint(1,3)
    if pixeleen_text_choice == 1:
        print("Dream deep my three-times-perfect ultrateen.")
    elif pixeleen_text_choice == 2:
        print("Rave on my sleek and soulful cyberqueen.")
    elif pixeleen_text_choice == 3:
        print("Be good my three-times-perfect ultrateen.")
if player_name == "Glamour Profession":
    print("It's the Glamour Profession.")
    print("The L.A. concession.")
    print("Local boys will spend a qwatah.")
    print("Just to shine the silver bowl.")
    print("Living hard will take its toll.")
    print("Illegal fun.")
    print("Under the suuuun, boys.")
if player_name == "Abbie":
    print("Good luck fighting Flame.")
if player_name == "Aja":
    print("Aja, when all my dime dancing is through")
    print("I roam to you")
if player_name == "Doctor Wu":
    doctorwu_choice = random.randint(1,3)
    if doctorwu_choice == 1:
        print("Are you with me Doctor?")
    elif doctorwu_choice == 2:
        print("Can you hear me Doctor?")
    elif doctorwu_choice == 3:
        print("Katy lies, you can see it in her eyes.")
if player_name == "Steely Dan":
    print("Hey Mr. Dan!")
if player_name == "Hey Nineteen":
    print("We can't dance together.")
    print("No we can't talk at all.")
if player_name == "Nineteen":
    print("We can't dance together.")
    print("We can't talk at all.")    
if player_name == "Black Blizzard":
    print("Krazy name.")
if player_name == "Michael Jordan":
    print("This game has a lot of gambling, so this is probably your cup of tea.")
if player_name == "Shrek":
    print("Somebody once told me the world was gonna roll me.")
    print("I ain't the sharpest tool in the shed.")
if player_name == "Josie":
    print("You're the best friend I never had.")
    print("You're the raw flame. The live wire.")
    print("You pray like a Roman with your eyes on fire.")
if player_name == "Jazz":
    print("The jazz, the what?")
    print("The jazz that moves the a**.")
    print("Cause the Tribe origniates that feeling of pizazz.")
    print("It's the universal sound best to brothers on the ground.")
    print("And the ones six below, you didn't have to go.")
if player_name == "God Lives Through":
    print("La, la, la")
    print("La, la, la")
    print("La, la, la")
    print("La, la, laa")
if player_name == "Cousin Dupree":
    print("The dreary architecture of your soul makes you worse than the beasts you will have to vanquish.")
if player_name == "Adversary":
    print("Watch out for The Batter.")
    print("Also, screw you.")
if player_name == "God":
    print("Blasphemous.")
if player_name == "The Batter":
    print("Almost perfection.")
if player_name == "Batter":
    print("Almost perfect for this game.")
if player_name == "Abu":
    print("Watch out for Pixeleen.")
if player_name == "":
    player_name = "Nothing"
    print("Nice try Nothing.")
if player_name == " ":
    player_name = "Space"
    print("Hello Space!")
if player_name == "Shining Star":
    print("Shining bright to seeeeeee.")
    print("What you can truly be.")
if player_name == "Black":
    print("Yo chill with the feedback black we don't need that.")
if player_name == "White":
    print("Classy.")
if player_name == "Apple":
    print("Y'all make nice phones.")
if player_name == "Cantaloupe":
    print("Sweet.")
if player_name == "Red":
    print("How did you lose in Pokemon Gold?")
if player_name == "Jack":
    print("In the land of milk and honey.")
    print("You must put them on the table.")
if player_name == "Blackjack":
    print("You go back, Jack, do it again.")
    print("Wheel turning round and round.")
    print("You go back, Jack, Do It Again.")
if player_name == "Cop":
    print("You a crooked cop?")
if player_name == "America":
    print("In the desert, you can't remember your name.")
    print("Cause there ain't no one for to give you no pain.")
    print("La, la, lala, la, la, lalala, laaa, la")
if player_name == "United States":
    print("Standing tough under stars and stripes we can tell")
    print("This dream's in sight.")
    print("You've got to admit it.")
    print("At this point of time that it's clear.")
    print("The future looks bright.")
if player_name == "I.G.Y.":
    print("What a beautiful world it will be.")
    print("What a glorious time to be free.")
if player_name == "New Frontier":
    print("You've got the right dynamic for the New Frontier.")
if player_name == "Who":
    print("Who's on first base.")
if player_name == "Barbeque":
    print("It's like that y'all!")
if player_name == "Nas":
    print("Street's disciple, my raps are trifle.")
    print("I shoot slugs from my brain just like a rifle.")
if player_name == "Jack of Speed":
    print("I see you're trading fours with someone.")
if player_name == "Midnite Cruiser":
    print("Still driving to Harlem?")
if player_name == "Deacon Blues":
    print("My back to the wall, a victim of laughing chance.")
    print("This is for me, the essence of true romance.")
if player_name == "Diamond":
    print("Take it from Diamond")
    print("It's like mountain climbin'")
    print("When it comes to rhymin'")
    print("You gotta put your time in.")
if player_name == "September":
    print("Ba-dee-ya (dee-ya, dee-ya), say, do you remember?")
    print("Ba-dee-ya (dee-ya, dee-ya), dancin' in September")
    print("Ba-dee-ya (dee-ya, dee-ya), golden dreams were shiny days")
if player_name == "Bum":
    print("U bum")
if player_name == "LeMickey":
    print("Go win a real ring.")
if player_name == "LeBron James":
    print("4-6 in the Finals")
    print("#notmygoat")
if player_name == "Kobe":
    print("Carried by Shaq")
if player_name == "Kobe Bryant":
    print("Carried by Shaquille O'Neal")
if player_name == "MrGymLaidYe":
    print("MrGymLaidYe is Autofraud father")
if player_name == "Luka Doncic":
    print("Luka Doncic is Devin Booker father")
if player_name == "Devin Booker":
    print("Luka Doncic is Devin Booker father")
if player_name == "Midnight":
    print("The way the moon dangles in the midnight sky")
    print("And the stars dance around ayo I think its fly")
#typing "deus vult to start the game" + text if you type something else
START = input(f"Ready to Start the Crusades {player_name}? Type (Deus Vult) to start! ")
START = START.title()
if START == "Deus Vult":
    print("//////////////////////////////////////") 
    print("//////////////////////////////////////")
    print("GAME START!")
    print("DEUS VULT!")
    print("//////////////////////////////////////") 
    print("//////////////////////////////////////")
    display_stats()
    battle_config()
elif START == "":
    print("You're a clown. You just hit ENTER without typing anything. Try again.")
else:
    need_a_placeholder_name_for_this = random.randint(1,6)
    if need_a_placeholder_name_for_this == 1:
        print("Guess you ain't ready yet. Try again.")
    elif need_a_placeholder_name_for_this == 2:
        print("How did you mess up trying to type a simple phrase? Try again.")
    elif need_a_placeholder_name_for_this == 3: 
        print("Quit trying to be special. Try again.")
    elif need_a_placeholder_name_for_this == 4:
        print("You type worse than a five-year-old. Try again.")
    elif need_a_placeholder_name_for_this == 5:
        print("Just play the game you bum. Try again.")
    elif need_a_placeholder_name_for_this == 6:
        print("You aren't worthy of going on the Crusades! Try again.")
