def convert_cel_to_far(c):
    return c * 9 / 5 + 32

def convert_far_to_cel(f):
    return (f - 32) * 5 / 9

f_temp = float(input("Enter a temperature in degrees F: "))
print(f"{f_temp} degrees F = {convert_far_to_cel(f_temp):.2f} degrees in C")

c_temp = float(input("Enter a temperature in degrees C: "))
print(f"{c_temp} degrees C = {convert_cel_to_far(c_temp):.2f} degrees in F")
