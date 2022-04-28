from random import choice

def get_jokes(qty=1, uniq=False):
    """
    Функция get_jokes возвращает qty шуток, сформированных из трех случайных слов,
    взятых из трёх списков (по одному из каждого).
    Аргумент uniq — флаг, разрешающий или запрещающий повторы слов в шутках.
    uniq = False - повторы разрешены
    uniq = True - повторы запрещены
    """
    
    nouns = ["car", "forest", "fire", "city", "home"]
    adverbs = ["today", "yesterday", "tomorrow", "two days ago", "at nigth"]
    adjectives = ["chirful", "bright", "green", "utopian", "soft"]
    result = []
    if uniq:
        qty_uniq_jokes = min(len(nouns), len(adverbs), len(adjectives))
        for i in range(min(qty, qty_uniq_jokes)):
            noun, adverb, adjective = choice(nouns), choice(adverbs), choice(adjectives)
            joke = noun + ' ' + adverb + ' ' + adjective
            result.append(joke)
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
    else:
        for i in range(qty):
            joke = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
            result.append(joke)
    return result


print(get_jokes(10, True))
