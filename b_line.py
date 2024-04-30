from math import *

# LINE SEGMENT
L = "line"
RIGHT_ANGLE = 90
POINT_A = (0.0, 0.0)
SIDES = 2
DEGREES = 360
SEMICIRCLE = DEGREES / 2  # 180°
SYMMETRY_ROTATION = (DEGREES / SIDES) / 2  # 90°
INTERNAL_ANGLE = SEMICIRCLE - SYMMETRY_ROTATION  # 90°
HALF_ANGLE_EQUAL_TRIANGLES = DEGREES / (2 * SIDES)  # 90°


def coordinates_points():
    """Returns the results of the 2 properties left given the segment's Point B x and y coordinates."""
    print(f"Point A of the {L} segment will always be given at coordinates (0, 0)\n"
          "Select coordinates for Point B:\n")

    final_conclusion = ""
    pa_x = POINT_A[0]
    pa_y = POINT_A[1]
    pb_x = float(input(f"Enter the value of the {L}'s segment, Point B, x coordinate:\n"))
    pb_y = float(input(f"Enter the value of the {L}'s segment, Point B, y coordinate:\n"))
    point_b = (pb_x, pb_y)

    if pb_x == 0 and pb_y == 0:
        length = 0
        angle = 0
        final_conclusion = "You've accidentally made a point!"
    else:
        length = sqrt(((pb_x - pa_x) ** 2) + ((pb_y - pa_y) ** 2))
        angle = degrees(asin(pb_y * (sin(radians(RIGHT_ANGLE)) / length)))

    final_coordinates = f"{POINT_A}, {point_b}"
    final_length = "{:.5f}".format(length)
    final_angle = "{:.10f}".format(angle)
    results = (final_coordinates, final_length, final_angle, final_conclusion)

    return results


def distance_and_angle():
    """Returns the results of the property left given the segment's length and angle
    with respect from the horizontal and counterclockwise."""
    print("\nIf no angle is given (press ENTER) it will be considered as: 0.00° with respect from the horizontal.\n"
          f"Select the length of the {L} and its angle with respect from the horizontal and counterclockwise:\n")

    x_coordinate = None
    y_coordinate = None
    a_degree = None
    d_length = float(input(f"Enter the length of the {L}'s segment:\n"))
    inclination = float(input(f"Enter the angle of the {L}'s segment:\n"))

    if d_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        distance_and_angle()
    elif inclination == "" or inclination == 0:
        a_degree = 0
        y_coordinate = 0
        x_coordinate = d_length
    else:
        a_degree = inclination
        y_coordinate = sin(radians(a_degree)) / (sin(radians(RIGHT_ANGLE)) / d_length)
        x_coordinate = sin(radians(SEMICIRCLE - RIGHT_ANGLE - a_degree)) / (sin(radians(RIGHT_ANGLE)) / d_length)

    pb_x = "{:.5f}".format(x_coordinate)
    pb_y = "{:.5f}".format(y_coordinate)
    point_b = (pb_x, pb_y)
    length = float(d_length)
    angle = float(a_degree)
    final_coordinates = f"{POINT_A}, {point_b}"
    final_length = "{:.5f}".format(length)
    final_angle = "{:.10f}".format(angle)
    results = (final_coordinates, final_length, final_angle)

    return results


def calculate_line(characteristic):
    """Returns the total results given the specified property."""
    if characteristic == "coordinates":
        return coordinates_points()
    elif (characteristic == "segment length" or characteristic == "angle" or
          characteristic == "segment length and angle"):
        return distance_and_angle()
