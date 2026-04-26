# Convert temperature, degrees Fahrenheit to degrees Celsius and vice versa. 
# C = (5/9) * (F - 32) &  F = C * 9/5 + 32


print(f"1) Convert celsius to fahrenheit\n2) Convert fahrenheit into celcius")
choice=int(input("Enter a choice: "))
if choice==1:
    celcius_inp=int(input("Enter Celcius temperature: "))
    output_fah=celcius_inp*9/5 + 32
    print(f"{celcius_inp} in fahrenheit is {output_fah}")
else:
    fahrenheit_inp=int(input("Enter Fahrenheit temperature: "))
    output_cel=5/9*(fahrenheit_inp-32)
    print(f"{fahrenheit_inp} in celcius is {output_cel}")