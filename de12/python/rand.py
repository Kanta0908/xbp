import random
import time
# ゲームの設定
WORD_LIST = ["python", "programming", "typing", "game", "challenge"]
ROUND_DURATION = 30  # ゲームの制限時間（秒）

# ゲームルール
def print_rules():
    print("********** タイピングゲーム **********")
    print("ルール: 指定された単語をできるだけ早くタイプしてください。")
    print("制限時間: {}秒".format(ROUND_DURATION))
    print("*************************************")
def main():
    print_rules()
    input("エンターキーを押してゲームを開始...")
    
    start_time = time.time()
    while time.time() - start_time < ROUND_DURATION:
        word = random.choice(WORD_LIST)
        print("タイプ: {}".format(word))
        user_input = input()
        
        if user_input == word:
            print("正解！")
        else:
            print("不正解...")
    
    print("ゲーム終了！")
if __name__ == "__main__":
    main()
