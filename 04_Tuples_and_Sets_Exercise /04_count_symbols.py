text = [el for el in input()]

sybol_repeat = dict()

for sym in text:
    if sym not in sybol_repeat:
        sybol_repeat[sym] = 0
    sybol_repeat[sym] += 1

for key, value in sorted(sybol_repeat.items()):
    print(f"{key}: {value} time/s")
