from googletrans import Translator
from sys import exit

def chose_lang():
    lang_mode = int(input("言語を選択してください[1:英語/2:中国語[簡体字]"))
    if lang_mode == 1:
        lang = "en"
    elif lang_mode == 2:
        lang= "zh-cn"
    else:
        print("指定の言語番号を選択してください")
        exit()
    return lang

def trans_ja_to_en_or_cn(lang, context):
    translator = Translator()
    trans_ja_to_select_lang = translator.translate(context, src="ja", dest=lang)
    translated_text = trans_ja_to_select_lang.text
    return translated_text


if __name__ == "__main__":
    lang = chose_lang()
    context = input("つぶやく内容を入力してください:")
    print(trans_ja_to_en_or_cn(lang, context))