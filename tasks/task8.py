import re
from collections import Counter

text = """
[Куплет 1]  
В истерике кружилась мама Валя  
На заднем фоне замер папа Толя  
В радиусе метра воцарился жесточайший хаос  
Когда всем понятно стало: сын остался без диплома  
Мама, не кричи, хватит плакать, не смей      
Я не спорю — надо, но послушай отец:  
Есть у меня своя волна, и на своей волне  
Меня где-то поджидает успех  

[Предприпев 1]      
Боже, как хотел я увидеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне  
Вдруг увидел солнце — и тогда себе я сказал:  

[Припев]  
Я выбираю — жить в кайф!    
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!       
Я выбираю — жить в кайф!

[Куплет 2]  
Это был сон, в котором я
Не прогорал, не огорчал родных и не нуждался ни в чём
В котором мне не пришлось скрывать глаза       
И лгать давним знакомым: мол, в жизни моей всё хорошо  
В моём рюкзаке пару маек, носки     
И пускай начало оставляет желать лучшего        
Все, кто меня помнит — знает, я не был таким  
А значит, и у вас получится     

[Предприпев 2]  
Ведь всё, что я хотел, это видеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне         
Вдруг услышав музыку — я сам себе сказал:  

[Припев]  
Я выбираю — жить в кайф!    
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!      
Я выбираю — жить в кайф!      

[Предприпев 1]  
Боже, как хотел я увидеть свет  
И, как посчитал бы нужным жить, мечтал  
И вот однажды, как обычно, я летал во сне             
Вдруг увидел солнце — и тогда себе я сказал:  

[Припев]  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!  
Я выбираю — жить в кайф!         
Я выбираю — жить в кайф!
"""

def parse_song(text):
    parts = re.findall(r"\[(.*?)\]\s*(.*?)\n(?=\[|\Z)", text, re.S)
    song_parts = {part_name.lower(): lyrics.strip() for part_name, lyrics in parts}
    return song_parts

song_parts = parse_song(text)

def print_section():
    section_name = input("Введите название части песни (например, куплет 1, припев): ").lower()
    if section_name in song_parts:
        print(song_parts[section_name])
    else:
        print("Неверное название части.")

def print_centered_text():
    cleaned_text = re.sub(r"\[.*?\]", "", text).strip()
    for line in cleaned_text.splitlines():
        if line.strip():
            print(line.center(80))

def count_words():
    part = input("Введите 'куплет' или 'песня' для подсчета: ").lower()
    
    if part == "куплет":
        kuplets_text = " ".join([lyrics for name, lyrics in song_parts.items() if 'куплет' in name])
        text_for_count = kuplets_text
    elif part == "песня":
        text_for_count = re.sub(r"\[.*?\]", "", text)
    else:
        print("Неверный ввод.")
        return
    
    words = re.findall(r'\b\w[\w-]*\b', text_for_count.lower())
    word_counts = Counter(words)
    
    most_common_words = word_counts.most_common(3)
    for i, (word, count) in enumerate(most_common_words, 1):
        print(f"{i}. \"{word}\" - {count} раз")

while True:
    command = input("Введите команду (1 - части песни, 2 - выравнивание, 3 - подсчет слов, выход - завершить): ").lower()
    if command == "1":
        print_section()
    elif command == "2":
        print_centered_text()
    elif command == "3":
        count_words()
    elif command == "выход":
        break
    else:
        print("Неверная команда.")
