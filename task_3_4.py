def thesaurus(*args):
    """
    Функция thesaurus() принимает в качестве аргументов имена сотрудников
    и возвращает словарь, в котором ключи — первые буквы имён, а значения
    — списки, содержащие имена, начинающиеся с соответствующей буквы.
    Например: thesaurus("Иван", "Мария", "Петр", "Илья")
    {
        "И": ["Иван", "Илья"], 
        "М": ["Мария"], "П": ["Петр"]
    }
    """

    dd = {}
    for item in args:
        if item[0] not in dd.keys():
            dd[item[0]] = list(filter(lambda el: el.startswith(item[0]), args))
    return dd


print(thesaurus("Ivan", "Mary", "Petr", "Ilya", "Pavel"))


def thesaurus_adv(*args):
    dd = {}
    for item in args:
        fam_let = item.split(' ')[-1][0] # family letter
        if fam_let not in dd.keys():
            # create list of people with the same family letter
            list_sfl = list(filter(lambda el: el.split(' ')[-1].startswith(fam_let), args))
            dd_sfl = {}
            for item_sfl in list_sfl:
                name_let = item_sfl.split(' ')[0][0]  # name letter
                if name_let not in dd_sfl.keys():
                    dd_sfl[name_let] = list(filter(lambda el: el.split(' ')[0].startswith(name_let), list_sfl))
            dd[fam_let] = dd_sfl
    return dd


print(thesaurus_adv("Ivan Sergeev", "Inna Serova", "Petr Alekseev", "Ilya Ivanov", "Anna Saveleva"))