def contains(list, city):
    return city in list

cities = ["Barcelona", "Madrid", "Manchester", "Stockholm", "Beograd"]

write = input("type a city")

print(contains(cities, write))