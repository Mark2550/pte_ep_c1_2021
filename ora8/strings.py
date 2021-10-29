# Karakter lekérése: [ ]
# Szövegrész lekérése: [ : ]
# Ismétlés: *
# Tartalmaz: in
# Nem tart.: not in

python = "akármilyenhosszúszövegmegteszi:)"
print("'python string' 1. karaktere:",python[0])
print("utolsó: ",python[5])
print("utolsó: ",python[-1])
print("utolsó: ",python[len(python) - 1])

str2 = "hallgató"
str3 = "Hiába a hegyni anyag, a hallgató gyorsan halad"
print(str2 in str3)
print(python in str3)
print(str2.upper() in str3.upper())
print(str3[0:3])
print(python+str2+str3)
print(python, str3, str2, sep="")
str4 = "HALLGATÓ"
print(str4 in str3)

