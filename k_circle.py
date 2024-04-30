from math import *

# CIRCLE
C = "circle"
SIDES = None
DEGREES = 360
SEMICIRCLE = DEGREES / 2  # 180°
SYMMETRY_ROTATION = None
INTERNAL_ANGLE = None
HALF_ANGLE_EQUAL_TRIANGLES = None


def radius_length():
    """Returns the results of the 3 properties left given the radius length."""
    r_length = float(input(f"Enter the length of the {C}'s radius:\n"))

    if r_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        radius_length()
    else:
        radius = float(r_length)
        diameter = 2 * radius
        circumference = pi * diameter
        area = pi * (radius ** 2)
        final_radius = "{:.5f}".format(radius)
        final_diameter = "{:.5f}".format(diameter)
        final_circumference = "{:.5f}".format(circumference)
        final_area = "{:.5f}".format(area)
        results = (final_radius, final_diameter, final_circumference, final_area)

        return results


def diameter_length():
    """Returns the results of the 3 properties left given the diameter length."""
    d_length = float(input(f"Enter the length of the {C}'s diameter:\n"))

    if d_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        diameter_length()
    else:
        radius = d_length / 2
        diameter = float(d_length)
        circumference = pi * diameter
        area = pi * (radius ** 2)
        final_radius = "{:.5f}".format(radius)
        final_diameter = "{:.5f}".format(diameter)
        final_circumference = "{:.5f}".format(circumference)
        final_area = "{:.5f}".format(area)
        results = (final_radius, final_diameter, final_circumference, final_area)

        return results


def circumference_length():
    """Returns the results of the 3 properties left given the circumference length."""
    c_length = float(input(f"Enter the length of the {C}'s circumference:\n"))

    if c_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        circumference_length()
    else:
        radius = (c_length / pi) / 2
        diameter = 2 * radius
        circumference = float(c_length)
        area = pi * (radius ** 2)
        final_radius = "{:.5f}".format(radius)
        final_diameter = "{:.5f}".format(diameter)
        final_circumference = "{:.5f}".format(circumference)
        final_area = "{:.5f}".format(area)
        results = (final_radius, final_diameter, final_circumference, final_area)

        return results


def area_surface():
    """Returns the results of the 3 properties left given the area."""
    a_surface = float(input(f"Enter the surface of the {C}'s area:\n"))

    if a_surface < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        area_surface()
    else:
        radius = sqrt(a_surface / pi)
        diameter = 2 * radius
        circumference = pi * diameter
        area = pi * (radius ** 2)
        final_radius = "{:.5f}".format(radius)
        final_diameter = "{:.5f}".format(diameter)
        final_circumference = "{:.5f}".format(circumference)
        final_area = "{:.5f}".format(area)
        results = (final_radius, final_diameter, final_circumference, final_area)

        return results


def calculate_circle(characteristic):
    """Returns the total results given the specified property."""
    if characteristic == "radius":
        return radius_length()
    elif characteristic == "diameter":
        return diameter_length()
    elif characteristic == "circumference" or characteristic == "perimeter":
        return circumference_length()
    elif characteristic == "area":
        return area_surface()
