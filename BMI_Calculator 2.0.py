# Amal K. 11/05/2022
# BMI Calculator using Python with IF Statements

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Write your code below this line 👇
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese

bmi=int(weight/(height*height))
print(f"Your BMI is {bmi}")
if bmi<18.5:
  print("You are underweight")
elif bmi<25:
  print("You are normal weight")
elif bmi<30:
  print("You are slightly over weight")
elif bmi<35:
  print("You are obese")
elif bmi>35:
  print("You are clinically obese")
else:
  print("Can't calculate BMI")

#End of Code
