for i in range(3):
    print(i,"人目")
    name=input("名前を入れてください") #文字だからダブルコーテーションがないと認識されない。
    waist=float(input("腹囲は？")) #floatは少数　intは整数
    age=int(input("年齢は？"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=85 and age>=40:#A and B
        print(name,"さん、内臓脂肪蓄積注意です")#タブキー
    else:
        print(name,"さん、腹囲は問題ありません")
        