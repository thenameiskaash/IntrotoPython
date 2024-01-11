def greeting(name, department):
    print("Hello " + name)
    print("You are part of " + department)
greeting("Karl", "Mechanical")

friends = ["Jack", "Joe", "Bill", "Adam"]
for friend in friends:
    print("Hi " + friend)

for i in range(0, 10):
    print("hello, world")
number = 12
print("Hello " + str(number))

def area_triangle(base, height):
    return (base*height)/2

a = area_triangle(10,12)
b = area_triangle(2,6)
print("The area of both triangles sum together is " + str(a + b))

def conversion(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

#hours, minutes, remaining_seconds = conversion(50000)
#print("Hours: " + str(hours), "Minutes: " + str(minutes), "Remaining Seconds: " + str(remaining_seconds))