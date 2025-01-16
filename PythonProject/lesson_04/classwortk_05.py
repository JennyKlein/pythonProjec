userName_1 = "Ann"
userName_2 = "Max"
userName_3 = "Lisa"

userLocation_1 = "Berlin"
userLocation_2 = "Munich"
userLocation_3 = "Koln"

userTotalSpends_1 = 12_242.56
userTotalSpends_2 = 2_780.50
userTotalSpends_3 = 42.94

print("|%-10s|%-15s|%-20s|" % ("User Name:", "User Location:", "User Total Spends:"))
print("|%-10s|%-15s|%20.2f|" % (userName_1, userLocation_1, userTotalSpends_1))
print("|%-10s|%-15s|%20.2f|" % (userName_2, userLocation_2, userTotalSpends_2))
print("|%-10s|%-15s|%20.2f|" % (userName_3, userLocation_3, userTotalSpends_3))