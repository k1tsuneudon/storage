import random

numbers = {"number1": 0,"number2": 0,"number3": 0,"number4": 0,"number5": 0,"number6": 0} 

times = int(input("何回サイコロを振りますか？(数字を入力):"))

count = 1

while count <= times :
    dice_number = random.randint(1,6)
    print(dice_number)
    if dice_number == 1 :
        numbers["number1"] += 1
        dice_number = random.randint(1,6)
        count += 1
    elif dice_number == 2 :
        numbers["number2"] += 1
        dice_number = random.randint(1,6)
        count += 1
    elif dice_number == 3 :
        numbers["number3"] += 1
        dice_number = random.randint(1,6)
        count += 1
    elif dice_number == 4 :
        numbers["number4"] +=1
        dice_number = random.randint(1,6)
        count += 1
    elif dice_number == 5 :
        numbers["number5"] += 1
        dice_number = random.randint(1,6)
        count += 1
    elif dice_number == 6 :
        numbers["number6"] += 1
        dice_number = random.randint(1,6)
        count += 1
    else:
        print("Error")
        break
    
    
print("---------- 結果 ----------")
for number in numbers :
    print(number + "は " + str(numbers[number]) + "回出ました")

input("キーを押すと終了します")