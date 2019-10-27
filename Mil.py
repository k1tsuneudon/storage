#距離（m） = 大きさ（m） * 1000 / 大きさ（ミル）
#大きさ（m） = 大きさ（ミル） / 1000 * 距離（m）

finish = "c"

while finish == "c":
    select = input("距離を求めるなら[d]を、大きさを求めるなら[s]を入力してください [e]で終了します:")

    #距離を求める場合  selefct = d
    if select == "d" :
        #libs = {"人 （1.8m）": 1.8, "窓 （1.1m）": 1.1,"電柱 （12.0m）": 12,"車 （2.0m）": 2}
        height = input("対象物の大きさ（m）を入力してください:")

        #入力された数値が整数か少数なのか判断するif文
        if str.isdecimal(height) :
            height = int(height)
        else :
            height = float(height)


        mil = int(input("対象物の大きさ（mil）を入力してください:"))

        distance = height * 1000 / mil

        print("対象物との距離は " + str(round(distance,2)) + "mでした")

        finish = input("終了する場合は[e]を、続ける場合は[c]を入力してください:")


    #大きさを求める場合  select = s
    elif select == "s":
        mil = int(input("対象物の大きさ（mil）を入力してください:"))

        distance = int(input("対象物との距離（m）を入力してください:"))

        size = mil / 1000 * distance

        print("対象物の大きさは " + str(round(size,2)) + "mでした")

        finish = input("終了する場合は[e]を、続ける場合は[c]を入力してください:")


    else :
        finish = "e"


input("キーを押すと終了します")



