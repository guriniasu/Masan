print("「マサン」を出力する回数を入力してください（半角数字）")
n=input()
with open("masan.txt",mode="w",encoding="shift_jis") as txt:
    print("マサンを"+n+"回出力します\nつまり"+str(int(n)*3)+"文字分！")
    for i in range(int(n)):
        txt.write("マサン")
    print("同じ階層に「masan.txt」ができたよ")
input()
    