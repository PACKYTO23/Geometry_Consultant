from math import *

# POINT
PO = "point"
POINT_A = (0.0, 0.0)


def coordinates_point():
    """Returns the results of the distance to the origin given the point's x and y coordinates."""
    print(f"Select x and y coordinates for the {PO} or press ENTER to keep in origin.\n")

    origin_x = POINT_A[0]
    origin_y = POINT_A[1]
    point_x = float(input(f"Enter the value of the {PO}'s x coordinate:\n"))
    point_y = float(input(f"Enter the value of the {PO}'s y coordinate:\n"))

    if point_x == 0 or point_x == "" and point_y == 0 or point_y == "":
        b_point = POINT_A
        length = 0
    else:
        b_point = (point_x, point_y)
        length = sqrt(((point_x - origin_x) ** 2) + ((point_y - origin_y) ** 2))

    final_coordinates = f"{b_point}"
    final_length = "{:.5f}".format(length)
    final_message = ("'In geometry, a point is an abstract idealization of an exact position,\n"
                     "without size, in physical space, or its generalization to other kinds of mathematical "
                     "spaces.'\n\n'As zero-dimensional objects, points are usually taken to be the fundamental "
                     "indivisible elements\ncomprising the space, of which one-dimensional curves, two-dimensional "
                     "surfaces,\nand higher-dimensional objects consist; conversely,\na point can be determined by the "
                     "intersection of two curves or three surfaces,\ncalled a vertex or corner.'\n\nFor more "
                     "information visit the 'Point (geometry)' entry in Wikipedia.")
    results = (final_coordinates, final_length, final_message)

    return results


def information():
    results = ("'In geometry, a point is an abstract idealization of an exact position,\n"
               "without size, in physical space, or its generalization to other kinds of mathematical spaces.'\n\n"
               "'As zero-dimensional objects, points are usually taken to be the fundamental indivisible elements\n"
               "comprising the space, of which one-dimensional curves, two-dimensional surfaces,\n"
               "and higher-dimensional objects consist; conversely,\n"
               "a point can be determined by the intersection of two curves or three surfaces,\n"
               "called a vertex or corner.'\n\n"
               "For more information visit the 'Point (geometry)' entry in Wikipedia.")

    return results


def calculate_point(characteristic):
    """Returns the total results given the specified property."""
    if characteristic == "coordinates":
        return coordinates_point()
    elif characteristic == "information" or characteristic == "info":
        return information()
