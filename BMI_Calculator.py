# Amal K. 30/04/2022
# BMI Calculator using Python

print("Body mass index, or BMI, is used to determine whether you are in a healthy weight range for your height.")
print("This calculator is only for educational use and not guaranteed in any way to work as intended")
height = input("enter your height in M: ") # Code to capture height
weight = input("enter your weight in kg: ") # Code to capture weight

BMI=(int(weight))/(float(height) ** 2) # Code to calcualt BMI, BMI=weight/height^2
# int_BMI= round(int(BMI), 4)
rounded_BMI=round(BMI, 2) # Round the BMI to two decimal places
print_BMI=str(rounded_BMI)
print("Your BMI is: " + print_BMI)

print("Meaning of BMI Ranges, Less than 18.5: Underweight, 18.5 to 24.9: Healthy weight, 25 to 29.9: Overweight but not obese") 
print("30 to 34.9: Obese class I, 35 to 39.9: Obese class II, 40 or more: Obese class III")

#End of Code
