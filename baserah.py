1import random
import time

# from termcolor import colored  # لإضافة الألوان

# إنشاء قائمة من الأرقام من 2 إلى 10
nums = [i for i in range(2, 11)]
# قائمة للرموز مثل J, Q, K, A
figures = ["J", "Q", "Κ", "A"]
# دمج الأرقام مع الرموز
axia = nums + figures
# قائمة للألوان (الشكل) الخاصة بالورق
color = ["♠", "♦", "♥", "♣"]

# إنشاء قائمة فارغة لحفظ جميع الأوراق
cards = []
# إنشاء مجموعة الورق
for i in axia:
    for j in color:
        cards.append([i, j])

# خلط الورق بشكل عشوائي
random.shuffle(cards)

# إنشاء قوائم فارغة لتخزين ورق اللاعب والمنافس والمجموعات
mpaza_antipalos = []
antipalos = []
mpaza_player = []
player = []
val = []
# نقاط إضافية ("xeres") عندما يأخذ اللاعب أو الكمبيوتر ورقة واحدة فقط
xeres_antipalos = 0
xeres_player = 0

# إنشاء القائمة الرئيسية على الطاولة
table = []
top_card = []

# توزيع 4 أوراق على الطاولة في بداية اللعبة
while True:
    for i in range(4):
        table.append(cards.pop())
    
    top_card = table[-1]
    # إذا كانت الورقة الأعلى هي J، نعيد خلط الأوراق
    if top_card[0] == "J":
        cards.append(table.pop())
        random.shuffle(cards)
        continue
    else:
        break

# تكرار اللعبة لـ 4 جولات
for rounds in range(4):
    # توزيع 6 أوراق لكل من اللاعب والمنافس في كل جولة
    for i in range(6):
        player.append(cards.pop())
    
    for i in range(6):
        antipalos.append(cards.pop())

    # عرض بداية الجولة
    print((25 * "=").center(50))
    time.sleep(0.5)
    text = str(rounds + 1)
    text = (10 * "*") + "Round" + text + "!" + (10 * "*")
    
    print(text.center(50))
    time.sleep(0.5)
    print((25 * "=").center(50))

    # عرض الأوراق على الطاولة في الجولة الأولى
    if rounds == 0:
        print("\nOn the table", table)
    time.sleep(0.5)

    # كل لاعب يلعب 6 دورات
    for turn in range(6):
        print("\nPlayer's Turn")
        time.sleep(0.5)

        # عرض يد اللاعب
        print("Your Hand")
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
      
        # عرض الأوراق بطريقة مرئية
        for i in range(len(player)):
            karta = player[i]
            if karta[0] == 10:
                list1 += ('┌────┐')
                list2 += ('│', karta[0], '     │')
                list3 += ('│    │')
                list4 += ('│   ', karta[1], '   │')
                list5 += ('│     ', karta[0], '│')
                list6 += ('└────┘')
            else:
                list1 += ('┌────┐')
                list2 += ('│', karta[0], '      │')
                list3 += ('│    │')
                list4 += ('│   ', karta[1], '   │')
                list5 += ('│     ', karta[0], ' │')
                list6 += ('└────┘')
        print(*list1)
        print(*list2)
        print(*list3)
        print(*list3)
        print(*list4)
        print(*list3)
        print(*list3)
        print(*list5)
        print(*list6)

        # عرض الورقة الأعلى على الطاولة
        if len(table) > 0:
            print("On the table")   
            karta = table[-1]
            if karta[0] == 10:
                list1 = ('┌────┐')
                list2 = ('│', karta[0], '     │')
                list3 = ('│    │')
                list4 = ('│   ', karta[1], '   │')
                list5 = ('│     ', karta[0], '│')
                list6 = ('└────┘')
            else:
                list1 = ('┌────┐')
                list2 = ('│', karta[0], '      │')
                list3 = ('│    │')
                list4 = ('│   ', karta[1], '   │')
                list5 = ('│     ', karta[0], ' │')
                list6 = ('└────┘')
            print(*list1)
            print(*list2)
            print(*list3)
            print(*list3)
            print(*list4)
            print(*list3)
            print(*list3)
            print(*list5)
            print(*list6)
        else:
            print("Table's empty")
            
        time.sleep(1)
        
        # طلب اللاعب اختيار ورقة للعب
        while True:
            try:
                print("\nChoose card to play. (From 1 to", len(player), ")")
                a = int(input())
                if range(len(player)).count((a - 1)) == 0:
                    continue
                else:
                    break
            except ValueError:
                continue
            
        player_num = player[a - 1]
        
        # عرض الورقة التي لعبها اللاعب
        print("You played")
        
        if player_num[0] == 10:
            list1 = ('┌────┐')
            list2 = ('│', player_num[0], '     │')
            list3 = ('│    │')
            list4 = ('│   ', player_num[1], '   │')
            list5 = ('│     ', player_num[0], '│')
            list6 = ('└────┘')
        else:
            list1 = ('┌────┐')
            list2 = ('│', player_num[0], '      │')
            list3 = ('│    │')
            list4 = ('│   ', player_num[1], '   │')
            list5 = ('│     ', player_num[0], ' │')
            list6 = ('└────┘')
        print(*list1)
        print(*list2)
        print(*list3)
        print(*list3)
        print(*list4)
        print(*list3)
        print(*list3)
        print(*list5)
        print(*list6)
        
        time.sleep(0.5)
        
        # إذا كانت الورقة تتطابق مع الورقة الأعلى على الطاولة، اللاعب يأخذ الأوراق
        if len(table) > 0:
            table_num = table[-1]
        else:
            table_num = [0, 0]

        if player_num[0] == table_num[0]:
            if len(table) == 1:
                xeres_player += 1
                print(("\nYou scored a 10-point!\n").center(50))
            print("You collected the cards.")
            last_to_take = 1
            table.append(player.pop(a - 1))
            for i in range(len(table)):
                mpaza_player.append(table.pop())
        elif player_num[0] == "J":
            print("You collected the cards.")
            table.append(player.pop(a - 1))
            for i in range(len(table)):
                mpaza_player.append(table.pop())
        else:
            table.append(player.pop(a - 1))
            
        time.sleep(0.5)

        # دور الكمبيوتر
        print("\nPC's turn!")
        
        # الكمبيوتر يحاول مطابقة الورقة الأعلى على الطاولة
        a = -1
        A = "false"
        xeri = 0
        if len(table) > 0:
            table_num = table[-1]
        else:
            table_num = [0, 0]

        for i in range(len(antipalos)):
            enemy_num = antipalos[i]
            if enemy_num[0] == table_num[0]:
                a = i
                A = "true"
                if len(table) == 1:
                    xeres_antipalos += 1
                    xeri = 1
            elif enemy_num[0] == "J" and len(table) > 0:
                a = i
                A = "true"
        
        # الكمبيوتر يلعب ورقة عشوائية إذا لم يجد مطابقة
        if a == -1 and len(antipalos) != 1:        
            while True:
                a = random.randrange(len(antipalos))
                val = antipalos[a]
                if val[0] != "J":
                    break

        if xeri == 1:
            print(("\nPC scored a 10-point!\n").center(50))
        print("PC played")
        
        enemy_num = antipalos[a]
        if enemy_num[0] == 10:
            list1 = ('┌────┐')
            list2 = ('│', enemy_num[0], '     │')
            list3 = ('│    │')
            list4 = ('│   ', enemy_num[1], '   │')
            list5 = ('│     ', enemy_num[0], '│')
            list6 = ('└────┘')
        else:
            list1 = ('┌────┐')
            list2 = ('│', enemy_num[0], '      │')
            list3 = ('│    │')
            list4 = ('│   ', enemy_num[1], '   │')
            list5 = ('│     ', enemy_num[0], ' │')
            list6 = ('└────┘')
        print(*list1)
        print(*list2)
        print(*list3)
        print(*list3)
        print(*list4)
        print(*list3)
        print(*list3)
        print(*list5)
        print(*list6)

        time.sleep(0.5)
        
        # إذا كانت الورقة تتطابق، الكمبيوتر يأخذ الأوراق
        if A == "true":
            print("PC collected the cards")
            last_to_take = 2
            table.append(antipalos.pop(a))
            for i in range(len(table)):
                mpaza_antipalos.append(table.pop())
        else:
            table.append(antipalos.pop(a))

        print(50 * "=")
        time.sleep(0.5)
        
    # نهاية الدورة وعرض النتيجة الحالية
    print("\nTurn End")
    print("Current score: Player:", (len(mpaza_player) + xeres_player * 10), "PC:", len(mpaza_antipalos) + (xeres_antipalos * 10))

# في نهاية الجولات، الشخص الذي أخذ آخر الأوراق يأخذ الباقي
if rounds == 4:
    if last_to_take == 1:
        for i in range(len(table)):
            mpaza_player.append(table.pop())
    elif last_to_take == 2:
        for i in range(len(table)):
            mpaza_antipalos.append(table.pop())

# عرض النتيجة النهائية
print("Final Score: Player:", (len(mpaza_player) + xeres_player * 10), "PC:", len(mpaza_antipalos) + (xeres_antipalos * 10))

# تحديد الفائز
if (len(mpaza_player) + xeres_player * 10) > (len(mpaza_antipalos) + (xeres_antipalos * 10)):
    print(("!!PLAYER WINS!!").center(50))
elif (len(mpaza_player) + xeres_player * 10) == (len(mpaza_antipalos) + (xeres_antipalos * 10)):
    print(("!!DRAW!!").center(50))
else:
    print(("!!PC WINS!!").center(50))

# انتظار المستخدم للضغط على زر إنهاء
k = input("Press enter to exit.")



