from calorie import Calorie
from temperature import Temperature


country = input("Enter the country name: ")
city = input("Enter the city name: ")

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(cm): "))
age = float(input("enter your age(years): "))


temperature = Temperature(country=country, city=city).get()
calorie = Calorie(weight=weight, height =height, age=age, temperature=temperature).calculate()

print(f"You need {calorie} kcal")