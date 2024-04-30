from math import *

# REGULAR HEXAGON
HEX = "hexagon"
SIDES = 6
DEGREES = 360
SEMICIRCLE = DEGREES / 2  # 180°
SYMMETRY_ROTATION = DEGREES / SIDES  # 60°
INTERNAL_ANGLE = SEMICIRCLE - SYMMETRY_ROTATION  # 120°
HALF_ANGLE_EQUAL_TRIANGLES = DEGREES / (2 * SIDES)  # 30°


def side_length():
    """Returns the results of the 5 properties left given the side length."""
    s_length = float(input(f"Enter the length of the {HEX}'s side:\n"))

    if s_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        side_length()
    else:
        side = float(s_length)  # Also circumscribed circle radius.
        apothem = sqrt(3 * side) / 2  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = (perimeter * float(apothem)) / 2
        ccr = side  # Also side length.
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr)

        return results


def apothem_icr_length():
    """Returns the results of the 4 properties left given the apothem/inscribed circle radius."""
    ap_length = float(input(f"Enter the length of the {HEX}'s apothem or inscribed circle radius:\n"))

    if ap_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        apothem_icr_length()
    else:
        side = ((2 * ap_length) ** 2) / 3   # Also circumscribed circle radius.
        apothem = float(ap_length)  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = (perimeter * float(apothem)) / 2
        ccr = side  # Also side length.
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr)

        return results


def perimeter_length():
    """Returns the results of the 5 properties left given the perimeter."""
    p_length = float(input(f"Enter the length of the {HEX}'s perimeter:\n"))

    if p_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        perimeter_length()
    else:
        side = p_length / SIDES  # Also circumscribed circle radius.
        apothem = sqrt(3 * side) / 2  # Also inscribed circle radius.
        perimeter = float(p_length)
        area = (perimeter * float(apothem)) / 2
        ccr = side  # Also side length.
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr)

        return results


def area_surface():
    """Returns the results of the 5 properties left given the area."""
    a_surface = float(input(f"Enter the surface of the {HEX}'s area:\n"))

    if a_surface < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        area_surface()
    else:
        side = 2 * (sqrt((a_surface * tan(radians(HALF_ANGLE_EQUAL_TRIANGLES))) / SIDES))  # Also cir... circle radius.
        apothem = sqrt(3 * side) / 2  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = float(a_surface)
        ccr = side  # Also side length.
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr)

        return results


def circumradius_length():
    """Returns the results of the 5 properties left given the circumscribed circle radius."""
    ccr_length = float(input(f"Enter the length of the {HEX}'s circumscribed circle radius:\n"))

    if ccr_length < 0:
        print("Negative values are invalid as anti-figures are yet to be discovered.")
        circumradius_length()
    else:
        side = float(ccr_length)  # Also circumscribed circle radius.
        apothem = sqrt(3 * side) / 2  # Also inscribed circle radius.
        perimeter = SIDES * side
        area = (perimeter * float(apothem)) / 2
        ccr = float(ccr_length)  # Also side length.
        final_side = "{:.5f}".format(side)
        final_apothem = "{:.5f}".format(apothem)
        final_perimeter = "{:.5f}".format(perimeter)
        final_area = "{:.5f}".format(area)
        final_ccr = "{:.5f}".format(ccr)
        results = (final_side, final_apothem, final_perimeter, final_area, final_ccr)

        return results


def calculate_hexagon(characteristic):
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
