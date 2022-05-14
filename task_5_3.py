from itertools import zip_longest

tutors = ['Ivan', 'Anastasya', 'Petr', 'Sergey', 'Dmitry', 'Boris', 'Elena']
klasses = ['9A', '7B', '9F', '9B', '8B']

gen = (tut_klas for tut_klas in zip_longest(tutors, klasses) if tut_klas[0] != None)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
