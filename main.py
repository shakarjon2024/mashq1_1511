# 1 - misol
sonlar = [3, 6, 8, 11, 20, 25, 30]
natija = [x**2 for x in sonlar if x % 2 == 0]
print(natija)


# 2 - misol
sozlar = ["python", "java", "flask", "web", "developer", "api"]
natija = [s.capitalize() for s in sozlar if len(s) > 5]
print(natija)


# 3 - misol
natija = ["katta" if x > 15 else "oddiy" for x in range(1, 31) if x % 3 == 0]
print(natija)


# 4 - misol
matn = "Pyth0n 3.9 D@ta!"
natija = [ch for ch in matn if ch.isalpha()]
print(natija)


# 5 - misol
gaplar = [
    "Python dasturlash tili",
    "List comprehension juda qulay",
    "Bugun havo yaxshi",
    "AI kelajakni o'zgartiradi",
    "Dasturchilar uchun juda foydali"
]

natija = [len(gap.split()) for gap in gaplar]
print(natija)

































