#-----------------------------------------------------------------------------
# Name: Exercise 10 (Exercise10.py)
# Purpose: Display understanding of lists and tuples
#
# Author: vonlugersbutter
# Created: Tuesday, November 20, 2018
# Updated: Wednesday, November 21, 2018
#-----------------------------------------------------------------------------

print(r"                                       /@")
print(r"                       __        __   /\/")
print(r"                      /==\      /  \_/\/  ")
print(r"                    /======\    \/\__ \__")
print(r"                  /==/\  /\==\    /\_|__ \ ")
print(r"               /==/    ||    \=\ / / / /_/")
print(r"             /=/    /\ || /\   \=\/ /     ")
print(r"          /===/   /   \||/   \   \===\ ")
print(r"        /===/   /_________________ \===\ ")
print(r"     /====/   / |                /  \====\ ")
print(r"   /====/   /   |  _________    /  \   \===\    THE LEGEND OF ")
print(r"   /==/   /     | /   /  \ / / /  __________\_____      ______       ___")
print(r"  |===| /       |/   /____/ / /   \   _____ |\   /      \   _ \      \  \ ")
print(r"   \==\             /\   / / /     | |  /= \| | |        | | \ \     / _ \ ")
print(r"    \===\__    \   /  \ / / /   /  | | /===/  | |        | |  \ \   / / \ \ ")
print(r"     \==\ \    \\ /____/   /_\ //  | |_____/| | |        | |   | | / /___\ \ ")
print(r"      \===\ \  \\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |")
print(r"       \==\/     \\\\/ / //////   \| |/==/ \| | |        | |   | | | /   \ |")
print(r"        \==\    _ \\/ / /////    _ | |==/     | |        | |  / /  | |   | |")
print(r"         \==\  / \ / / ///      /|\| |_____/| | |_____/| | |_/ /   | |   | |")
print(r"          \==\ /  / / /________/ |/_________|/_________| /____/   /___\ /___\ ")
print(r"           \==\  /               | /==/")
print(r"            \=\ /________________|/=/    ")
print(r"             \==\     _____      /==/ ")
print(r"            / \===\   \   /    /===/")
print(r"           / / /\===\  \_/  /===/")
print(r"          / / /   \====\ /====/")
print(r"         / / /      \===|===/")
print(r"         |/_/         \===/")
print(r"                        =  ")

print()

name = input("One day you will tire of me. I have yet again forgotten your name. What is it, hero?")

print("Go now, " + name + ", to Hyrule. \n")


print(".")
print('.')
print('.')

print()

print("Jackie: Hi, " + name + "! Say, do you know what time it is right now?")

time = (8,37)

hour, minute = time
  
print("You tell Jackie that it is " + str(minute) + " minutes past " + str(hour) + ".")

print()
print("Jackie: Oh no! That means I'm going to be late for my math practice!! Hold on. I just had a great idea! " + name + ", would you like to help me with my math practice. \n")

print("a. Yes, I'll help.")
print("b. No, leave me alone.")
help_jackie = input("Will you help Jackie with her math practice?")
print()

if help_jackie == "a":
  print("Jackie: Thanks " + name + "! That's so nice of you. \n")

if help_jackie == "b":
  print("Erica jumps out of a barrel.")
  print("Erica: You're the Hero of Hyrule. You're supposed to help people.")
  print("And so, you are dragged against your will to help Jackie.")

print()

print("You and Jackie go to Jackie's house, where she pulls out a stone tablet to write on.")
print("Jackie: Today, I was planning on learning about the Cartesian plane and coordinates. \n")

print("Jackie: So, the first exercise is to find the coordinates of specific points on the plane, and then find the slope of the line that connects them.")

list_of_coordinates = [(3,4),(-5,2)]
coordinates1, coordinates2 = list_of_coordinates

def find_coordinates(coordinates1, coordinates2):
  '''
  User is returned with a message stating the coordinates of two points.

  User is shown the coordinates of two points, in the form of a message by Jackie.

  Parameters
  ----------
  coordinates1 : tuples
    The x and y values on a Cartesian plane for a point
  
  coordinates2 : tuples
    The x and y values on a Cartesian plane for another point

  Returns
  ----------
  string
    The message indicating the coordinates of each of the two points.
  '''

  # The assertion below will break, because the parameter is a tuple
  # assert isinstance(coordinates1, (int,float)), 'Expected an integer or a float for coordinate'

  return print("Jackie: The first set of coordinates are " + str(coordinates1) + " and the second set of coordinates are " + str(coordinates2) + ".")

find_coordinates(coordinates1, coordinates2)
print()

def find_slope(coordinates1,coordinates2):
  '''
  User is returned with the slope of two given points.

  Slope is calculated using the formula slope equals change in y value over change in x value, taken from 2 given coordinates. The slope is then returned to the user.

  Parameters
  ----------
  coordinates1 : tuples
    The x and y values on a Cartesian plane for a point
  
  coordinates2 : tuples
    The x and y values on a Cartesian plane for another point

  Returns
  ----------
  string
    The message indicating the slope of 2 given points.
  '''

  x1, y1 = coordinates1
  x2, y2 = coordinates2

  slope = (y2-y1)/(x2-x1)

  return print("Jackie: The slope of the line segment connecting the two coordinates is " + str(slope) + ".") 

find_slope(coordinates1,coordinates2)

print()
print("You tell Jackie to try to find the sum of all the integer y values on the line segment, for practice.\n")

line_segment_y_integers = [2,3,4]

print("Jackie: Well, the integer y-values present in the line segment are " + str(line_segment_y_integers) + ".")

def find_sum_of_integers(line_segment_y_integers):
  '''
  User is returned with the sum of all the components of a list of y values.

  The sum of values in a given list are added together using a for loop, and then returned to the user.

  Parameters
  ----------
  line_segment_y_integers : list
    The x and y values on a Cartesian plane for a point

  Returns
  ----------
  string
    The message indicating the sum of all the values in the parameter list.
  '''
  sum_of_y = 0
  for values in line_segment_y_integers:
    sum_of_y = values + sum_of_y
  
  return print("Jackie: The sum of the integer y values on the line segment is " + str(sum_of_y) + ".")

find_sum_of_integers(line_segment_y_integers)

print()
print("Good job! You helped Jackie well. Your adventure will continue in another exercise. Farewell for now, hero.")
