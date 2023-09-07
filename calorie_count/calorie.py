from temperature import Temperature

class Calorie:
    """
    Object that contains data to calculate the calorie needed such as weight, 
    height and age using 
    BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5 - (10 * temperature)
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5 - (10 * self.temperature)        
        return result
    
if __name__ == "__main__":
    temperature = Temperature(country = "usa", city = "pleasanton").get()    
    calorie = Calorie(weight=72, height=178, age = 33, temperature = temperature)
    print(calorie.calculate())