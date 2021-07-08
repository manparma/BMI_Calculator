# BMI Calculator

# Get users height and weight using input function and convert the input string to float
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# Calculate the BMI
# Formula to calculate BMI is $weight (kg)/{height (m)}^2$
# By dividing the height by 100 to convert the centimetres into meters
BMI = weight / (height/100)**2

# Print a statement to state the current health of the user based on their BMI.
print(f"You BMI is {BMI}")

# if conditionals for classification
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")