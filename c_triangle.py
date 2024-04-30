from math import *

# EQUILATERAL TRIANGLE
T = "triangle"
SIDES = 3
DEGREES = 360
SEMICIRCLE = DEGREES / 2  # 180°
SYMMETRY_ROTATION = (DEGREES / SIDES) / 2  # 60°
INTERNAL_ANGLE = SEMICIRCLE - SYMMETRY_ROTATION  # 120°
HALF_ANGLE_EQUAL_TRIANGLES = DEGREES / (2 * SIDES)  # 60°


def side_length():
    """Returns the results of the 6 properties left given the side length."""
    s_length = float(input(f"Enter the length of the {T}'s side:\n"))

    if s_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        side_length()
    else:
        side = float(s_length)
        apothem = side * (sqrt(3) / 6)  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = (side ** 2) * (sqrt(3) / 4)
        ccr = 2 * apothem
        altitude = side * (sqrt(3) / 2)
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        final_altitude = "{:.5f}".format(altitude)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr, final_altitude)

        return results


def apothem_icr_length():
    """Returns the results of the 5 properties left given the apothem/inscribed circle radius."""
    ap_length = float(input(f"Enter the length of the {T}'s apothem or inscribed circle radius:\n"))

    if ap_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        apothem_icr_length()
    else:
        side = ap_length / (sqrt(3) / 6)
        apothem = float(ap_length)  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = (side ** 2) * (sqrt(3) / 4)
        ccr = 2 * apothem
        altitude = side * (sqrt(3) / 2)
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        final_altitude = "{:.5f}".format(altitude)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr, final_altitude)

        return results


def perimeter_length():
    """Returns the results of the 6 properties left given the perimeter."""
    p_length = float(input(f"Enter the length of the {T}'s perimeter:\n"))

    if p_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        perimeter_length()
    else:
        side = p_length / SIDES
        apothem = side * (sqrt(3) / 6)  # Also inscribed circle radius.
        perimeter = float(p_length)
        area = (side ** 2) * (sqrt(3) / 4)
        ccr = 2 * apothem
        altitude = side * (sqrt(3) / 2)
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        final_altitude = "{:.5f}".format(altitude)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr, final_altitude)

        return results


def area_surface():
    """Returns the results of the 6 properties left given the area."""
    a_surface = float(input(f"Enter the surface of the {T}'s area:\n"))

    if a_surface < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        area_surface()
    else:
        side = sqrt(a_surface / (sqrt(3) / 4))
        apothem = side * (sqrt(3) / 6)  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = float(a_surface)
        ccr = 2 * apothem
        altitude = side * (sqrt(3) / 2)
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        final_altitude = "{:.5f}".format(altitude)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr, final_altitude)

        return results


def circumradius_length():
    """Returns the results of the 6 properties left given the circumscribed circle radius."""
    ccr_length = float(input(f"Enter the length of the {T}'s circumscribed circle radius:\n"))

    if ccr_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        circumradius_length()
    else:
        side = (ccr_length / 2) / (sqrt(3) / 6)
        apothem = side * (sqrt(3) / 6)  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = (side ** 2) * (sqrt(3) / 4)
        ccr = float(ccr_length)
        altitude = side * (sqrt(3) / 2)
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        final_altitude = "{:.5f}".format(altitude)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr, final_altitude)

        return results
    
    
def altitude_length():
    """Returns the results of the 6 properties left given the altitude."""
    alt_length = float(input(f"Enter the length of the {T}'s altitude (height):\n"))

    if alt_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        altitude_length()
    else:
        side = alt_length / (sqrt(3) / 2)
        apothem = side * (sqrt(3) / 6)  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = (side ** 2) * (sqrt(3) / 4)
        ccr = 2 * apothem
        altitude = float(alt_length)
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        final_altitude = "{:.5f}".format(altitude)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr, final_altitude)

        return results


def calculate_triangle(characteristic):
    """Returns the total results given the specified property."""
    if characteristic == "side length":
        return side_length()
    elif characteristic == "apothem" or characteristic == "inscribed circle radius":
        return apothem_icr_length()
    elif characteristic == "perimeter":
        return perimeter_length()
    elif characteristic == "area":
        return area_surface()
    elif characteristic == "circumscribed circle radius":
        return circumradius_length()
    elif characteristic == "altitude" or characteristic == "height":
        return altitude_length()
