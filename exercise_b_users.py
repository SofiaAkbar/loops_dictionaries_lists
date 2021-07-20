users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown

print(users["Erik"]["home_town"])

# 3. Get the array of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty

print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])

smallest = 100
numbers = users["Erik"]["lottery_numbers"]
for number in numbers:
  if number < smallest:
    smallest = number
print(smallest)

# 6. Return an array of Avril's lottery numbers that are even

evens = []
av_number = users["Avril"]["lottery_numbers"]
for number in av_number:
  if number % 2 == 0:
    evens.append(number)
print(evens)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

erik_numbers = users["Erik"]["lottery_numbers"]
users["Erik"]["lottery_numbers"].append(7)

print(erik_numbers)

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"]= "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "Fluffy"

users["Erik"]["pets"].append(
  {
    "name": "fluffy",
    "species": "dog"
  }
)

# print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary

users["Bob"] = {
  "twitter": "bobbyb",
  "lottery_numbers": [1, 65, 4, 43, 9, 60],
  "home_town": "Glasgow",
  "pets": [
    {
      "name": "tortilla",
      "species": "seagull"
    },
    {
      "name": "juti",
      "species": "dog"
    },
    {
      "name": "chooa",
      "species": "mouse"
    }
  ]
}

print(users)
