# Simple Decision Tree Example (without sklearn)

def decision_tree(weather):
    if weather == "sunny":
        return "Play Cricket"
    elif weather == "rainy":
        return "Stay Home"
    else:
        return "Go for Walk"

# input
weather = input("Enter weather (sunny/rainy/cloudy): ")

# decision
result = decision_tree(weather)

print("Decision:", result)
