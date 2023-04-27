import random

def son_top_user (x=10):
    tasodifiy_raqam = random.randint(1, x)
    print(f"Men 1 dan {x} gacha  son oyladim topib kor!", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input('Son kriting: '))
        if taxmin < tasodifiy_raqam:
            print("Xato, men oylagan son bundan kattaroq, Harakat qilib koring", end="")
        elif taxmin > tasodifiy_raqam:
            print("Xato, men oyalgan son bundan kichikroq, Harakat qiling!", end="")
        else:
            break
    print(f"Togri, tabriklayman {taxminlar} taxmin bilan topdingiz.")
    return taxmin
def son_top_pc(x=10):
    input(f"1 dan {x} gacha bolgan soni oylang men topaman va hohlagan tugmani bosing!")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini oyladingiz"
                      f"Agar togri bolsa 't' tugmasini"
                      f"Siz oylagan son kichikroq bolsa '-'"
                      f"Siz oylagan son katta bolsa '+' "
                      f"Tugamalarini bosing!!!".lower())
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
        if quyi == yuqori:
            taxmin = quyi
            break
    print(f"Men {taxminlar} bilan topdim ")
    return taxminlar
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top_user(x)
        taxminlar_pc = son_top_pc(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim, Yuttim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Men {taxminlar_user} taxmin blan topdingiz, Yutug sizda")
        else:
            print("Durrang!")
        yana = int(input("Yana oynaymizmi ? Ha(1)/Yoq(0): "))
play()