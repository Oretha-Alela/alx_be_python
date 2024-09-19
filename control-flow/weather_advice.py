# Ask for user input

weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Give recommendations

if (weather == "sunny"):
    recommendation = "Wear a t-shirt and sunglasses."
elif (weather == "rainy"):
    recommendation = "Don't forget your umbrella and a raincoat."
elif (weather == "cold"):
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."

# Print the recommendation
print(recommendation)
 

