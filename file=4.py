height = float(input ("Enter your height in cm"))
weight = float(input ("Enter your weight"))
BMI = weight / (height/100)**2

print ("your BMI is:", BMI)
if BMI <= 18.4:
    print ("You are under weight")
elif BMI <= 24.9:
    print ("You are healthy")
elif BMI <= 29.9:
    print ("Your are overweight")
elif BMI <= 34.9:
    print ("You are severly overweight")
elif BMI <= 39.9:
    print ("You are obese")
else:
    print ("You are severly obese")