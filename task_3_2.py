def num_translate_adv(eng_name):
    """
    Функция num_translate_adv() переводит числительные
    от 0 до 10 c английского на русский язык
    """
    
    if eng_name.istitle():
        eng_name = eng_name.lower()
        print(dictionary_num.get(eng_name, 'Word not found').capitalize())
    else:
        print(dictionary_num.get(eng_name, 'Word not found'))


dictionary_num = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
num_translate_adv('ten')
num_translate_adv('Four')
