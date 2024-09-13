fav_fruit = ["apple", "banana", "guava", "peach", "watermelon"]
fav_fruit.append("pineapple")
fav_fruit.append("melon")
fav_fruit.pop()
print(fav_fruit)

numbers = (1, 2, 3, 4, 5)


try: 
    numbers[1] = 10

except TypeError as e:
    print(f"An error occured: {e}")