def calculate_area(name):
  name = name.lower()
  if name == "rectangle":
    l = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))
    rect_area = l * b
    print("Area of rectangle is",rect_area) 
  elif name == "square":
    s = int(input("Enter square's side length: "))
    sqt_area = s * s
    print("Area of square is",sqt_area)
  elif name == "triangle":
    h = int(input("Enter triangle's height: "))
    b = int(input("Enter triangle's breadth: "))
    tri_area = 0.5 * b * h
    print(f"Area of triangle is",tri_area)
  elif name == "circle":
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
    circ_area = pi * r * r
    print(f"The area of triangle is",circ_area)        
  else:
    print("Sorry! This shape is not available")


print("Calculate Shape Area")
shape_name = input("Enter the name of shape whose area you want to find: ")
calculate_area(shape_name)
