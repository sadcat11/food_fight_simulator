import random
import matplotlib.pyplot as plt

random.seed()

#settings
days = 500
start_food = 5
n = 500
max_start_experience = 10
not_aggressive_fight = 5 #the probability of a fight when an aggressive and not aggressive meet (from 0 to 10)
percent_of_aggressive = 0.5 #form 0 to 1
max_food = 20

#fighting settings
random_fight_bonus = 4
food_for_win = 1.5
food_for_lose = -1.5
exp_for_win = 1
exp_for_lose = 0.5
random_fight_bonus_not_agr = 2 #if not agr can fight
#two neutral
food_for_two_neutral = 1
#agr vs not agr
food_for_agr = 2
food_for_not_agr = -0.5


class Animal:
    def __init__(self, aggressive, experience):
        self.aggressive = aggressive
        self.experience = experience
        self.food = start_food
        self.alive = True
    def check(self):
        if self.food > max_food:
            self.food = max_food


class RandomGeneration:
    def create_random(num = 100):
        list = []
        for i in range(0, int(num)):
            list.append(Animal(bool(random.getrandbits(1)), (random.randrange(1, max_start_experience * 10, 1)) / 10))
        return list

    def create_aggressive(num = 100):
        list = []
        for i in range(0, int(num)):
            list.append(Animal(True, (random.randrange(1, max_start_experience * 10, 1)) / 10))
        return list

    def create_not_aggressive(num = 100):
        list = []
        for i in range(0, int(num)):
            list.append(Animal(False, (random.randrange(1, max_start_experience * 10, 1)) / 10))
        return list

    def list_randomization(list1, list2 = []):
        list = list1 + list2
        random.shuffle(list)
        return list


def fight(first, second):
    attr1, attr2 = vars(first), vars(second)
    if attr1['aggressive'] == True and attr2['aggressive'] == True:
        if (random.randrange(0, random_fight_bonus, 1)) + attr1['experience'] \
                > (random.randrange(0, random_fight_bonus, 1)) + attr2['experience']:
            attr1['food'] += food_for_win
            attr2['food'] += food_for_lose
            attr1['experience'] += exp_for_win
            attr2['experience'] += exp_for_lose
            Animal.check(first)
            Animal.check(second)
        elif (random.randrange(0, random_fight_bonus, 1)) + attr1['experience'] \
                < (random.randrange(0, random_fight_bonus, 1)) + attr2['experience']:
            attr2['food'] += food_for_win
            attr1['food'] += food_for_lose
            attr2['experience'] += exp_for_win
            attr1['experience'] += exp_for_lose
            Animal.check(first)
            Animal.check(second)
        else:
            attr1['food'] += food_for_lose
            attr2['food'] += food_for_lose
            attr1['experience'] += exp_for_win
            attr2['experience'] += exp_for_win
            Animal.check(first)
            Animal.check(second)
    elif attr1['aggressive'] == True and attr2['aggressive'] == False:
        if random.randrange(0, 10, 1) < not_aggressive_fight:
            attr1['food'] += food_for_agr
            attr2['food'] += food_for_not_agr
            Animal.check(first)
            Animal.check(second)
        else:
            if (random.randrange(0, random_fight_bonus, 1)) + attr1['experience'] \
                    > (random.randrange(0, random_fight_bonus_not_agr, 1)) + attr2['experience']:
                attr1['food'] += food_for_win
                attr2['food'] += food_for_lose
                attr1['experience'] += exp_for_win
                attr2['experience'] += exp_for_lose
                Animal.check(first)
                Animal.check(second)
            elif (random.randrange(0, random_fight_bonus, 1)) + attr1['experience'] \
                    < (random.randrange(0, random_fight_bonus_not_agr, 1)) + attr2['experience']:
                attr2['food'] += food_for_win
                attr1['food'] += food_for_lose
                attr2['experience'] += exp_for_win
                attr1['experience'] += exp_for_lose
                Animal.check(first)
                Animal.check(second)
    elif attr1['aggressive'] == False and attr2['aggressive'] == True:
        if random.randrange(0, 10, 1) < not_aggressive_fight:
            attr2['food'] += food_for_agr
            attr1['food'] += food_for_not_agr
            Animal.check(first)
            Animal.check(second)
        else:
            if (random.randrange(0, random_fight_bonus_not_agr, 1)) + attr1['experience'] \
                    > (random.randrange(0, random_fight_bonus, 1)) + attr2['experience']:
                attr1['food'] += food_for_win
                attr2['food'] += food_for_lose
                attr1['experience'] += exp_for_win
                attr2['experience'] += exp_for_lose
                Animal.check(first)
                Animal.check(second)
            elif (random.randrange(0, random_fight_bonus, 1)) + attr1['experience'] \
                    < (random.randrange(0, random_fight_bonus_not_agr, 1)) + attr2['experience']:
                attr2['food'] += food_for_win
                attr1['food'] += food_for_lose
                attr2['experience'] += exp_for_win
                attr1['experience'] += exp_for_lose
                Animal.check(first)
                Animal.check(second)
    else:
        attr1['food'] += food_for_two_neutral
        attr2['food'] += food_for_two_neutral
        Animal.check(first)
        Animal.check(second)


def plot_g(list_days, list_agr, list_not):
    plot = plt.figure()
    plt.plot(list_days, list_agr, label="aggressive")
    plt.plot(list_days, list_not, label="not aggressive")
    plt.legend()
    plt.grid()
    plt.show()


def print_animals(animals):
    for i in animals:
        attrs = vars(i)
        print(', '.join("%s: %s" % item for item in attrs.items()))


if __name__ == "__main__":
    agr = 0
    dead_agr = 0
    dead_not_agr = 0
    day = 0
    agr_alive = []
    not_agr_alive = []
    #animals = RandomGeneration.create_random(n)
    animals1 = RandomGeneration.create_aggressive(n * percent_of_aggressive)
    animals2 = RandomGeneration.create_not_aggressive(n * (1 - percent_of_aggressive))
    animals = RandomGeneration.list_randomization(animals1, animals2)
    #for i in animals:
    #    attrs = vars(i)
    #    print(', '.join("%s: %s" % item for item in attrs.items()))
    for q in range(1, days + 1):
        print(len(animals))
        print((len(animals) // 2))
        for i in range(0, (len(animals) // 2)):
            fight(animals[i], animals[len(animals) - i - 1])
        for i in animals:
            attrs = vars(i)
            if attrs['food'] <= 0:
                attrs['alive'] = False
                if attrs['aggressive'] == True:
                    dead_agr += 1
                else:
                    dead_not_agr += 1
                animals.remove(i)
            if dead_agr + dead_not_agr >= n - 1:
                print("dead")
                print_animals(animals)
                print(str(day) + "\n" + str(agr_alive) + "\n" + str(not_agr_alive))
                list_days = list(range(1, day + 1))
                plot_g(list_days, agr_alive, not_agr_alive)
                exit(1)
        agr_alive.append(n * percent_of_aggressive - dead_agr)
        not_agr_alive.append(n * (1 - percent_of_aggressive) - dead_not_agr)
        #print(', '.join("%s: %s" % item for item in attrs.items()))
        print(dead_agr, dead_not_agr, day)
        day += 1
    print(str(agr_alive) + "\n" + str(not_agr_alive))
    list_days = list(range(1, days + 1))
    plot_g(list_days, agr_alive, not_agr_alive)



