# Ваш код здесь
text = "учеба, кодинг, отдых, прогулка"
example = text.split(",")

Wort = example[0].strip().capitalize()
Wort1 = example[1].strip().capitalize()
Wort2 = example[2].strip().capitalize()
Wort3 = example[3].strip().capitalize()

Text2 = [Wort, Wort1, Wort2, Wort3]

Text3 = ", ".join(Text2)

print(Text3)


