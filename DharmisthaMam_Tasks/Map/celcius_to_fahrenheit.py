# a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. 
# Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]

celcius_temp=[0,100,36]
print(list(map(lambda x:x*9/5+32,celcius_temp)))