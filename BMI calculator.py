# 1st input: enter your height in meter
height = input()
# 2nd input: enter your weight in kilograms
weight = input()

# convert height and weight to float
height = float(height)
weight = float(weight)


# calculate BMI
bmi = weight /( height ** 2)
print(int(bmi))