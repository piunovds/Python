# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

duration = int(input("Введиде количество секунд: "))
if duration < 0:
    duration *= -1
    print("Значение duration заменено на положительное", duration)
days = duration // (24 * 3600)
duration %= 24 * 3600
hours = duration // 3600
duration %= 3600
minuts = duration // 60
seconds = duration % 60
if days:
    print(days, "дн", hours, "час", minuts, "мин", seconds, "сек")
elif hours:
    print(hours, "час", minuts, "мин", seconds, "сек")
elif minuts:
    print(minuts, "мин", seconds, "сек")
else:
    print(seconds, "сек")
