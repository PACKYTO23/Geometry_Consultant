import a_point as po
import b_line as l
import c_triangle as t
import d_square as s
import e_pentagon as pe
import f_hexagon as hex
import g_heptagon as hep
import h_octagon as o
import i_nonagon as n
import j_decagon as d
import k_circle as c
import l_art as a

calculate = True


def geometry_consultant():
    def choice():
        property_choice = None
        figure_choice = input("Please select the geometric option desired to explore:\n"
                              "Point  |  Line  |  Triangle  |  Square  |  Pentagon  |  "
                              "Hexagon  |  Heptagon  |  Octagon  |  Nonagon  |  Decagon  |  Circle\n").lower()

        if figure_choice == "point":
            property_choice = input(f"Please select the {figure_choice}'s geometric data of choice:\n"
                                    "Coordinates  |  Information\n").lower()
        elif figure_choice == "line":
            property_choice = input(f"Please select the {figure_choice}'s geometric characteristic of choice:\n"
                                    "Coordinates  |  Segment Length and Angle\n").lower()
        elif figure_choice == "triangle":
            property_choice = input(f"Please select the {figure_choice}'s geometric characteristic of choice:\n"
                                    "Side Length  |  Apothem/Inscribed Circle Radius  |  Perimeter  |  "
                                    "Area  |  Circumscribed Circle Radius  |  Altitude (Height)\n").lower()
        elif (figure_choice == "square" or figure_choice == "pentagon" or figure_choice == "hexagon" or
                figure_choice == "heptagon" or figure_choice == "octagon" or figure_choice == "nonagon" or
                figure_choice == "decagon"):
            property_choice = input(f"Please select the {figure_choice}'s geometric characteristic of choice:\n"
                                    "Side Length  |  Apothem/Inscribed Circle Radius  |  Perimeter  |  "
                                    "Area  |  Circumscribed Circle Radius\n").lower()
        elif figure_choice == "circle":
            property_choice = input(f"Please select the {figure_choice}'s geometric characteristic of choice:\n"
                                    "Radius  |  Diameter  |  Circumference  (Perimeter)  |  Area\n").lower()

        selection = (figure_choice, property_choice)

        return selection

    selections = choice()

    if selections[0] == "point":  # Point's Section---------------------------------------------------------------------
        po_calculate = po.calculate_point(selections[1])
        po_message = None

        if selections[1] == "information" or selections[1] == "info":
            po_message = (f"This is a general introduction to the {selections[0]}'s world...\n\n"
                          f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                          f"{po_calculate}\n"
                          "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")
        elif selections[1] == "coordinates":
            po_message = (f"This {selections[0]}'s data is as follows...\n\n"
                          f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                          f"Coordinates: {po_calculate[0]}\nDistance from point to origin: {po_calculate[1]} units.\n\n"
                          f"In more general terms...\n\n{po_calculate[2]}\n"
                          "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(po_message)  # -------------------------------------------------------------------------------------------

    elif selections[0] == "line":  # Line's Section---------------------------------------------------------------------
        l_calculate = l.calculate_line(selections[1])
        l_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                     f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                     f"Coordinates: {l_calculate[0]}.\nLength: {l_calculate[1]} units.\n"
                     f"Angle (with respect from the horizontal): {l_calculate[2]}°.\n"
                     "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(l_message)  # --------------------------------------------------------------------------------------------

    elif selections[0] == "triangle":  # Triangle's Section-------------------------------------------------------------
        t_calculate = t.calculate_triangle(selections[1])
        t_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                     f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                     f"Side length: {t_calculate[0]} units.\n"
                     f"Apothem and inscribed circle radius: {t_calculate[1]} units.\n"
                     f"Perimeter: {t_calculate[2]} units.\nArea: {t_calculate[3]} squared units.\n"
                     f"Circumscribed circle radius: {t_calculate[4]} units.\n"
                     f"Altitude (height): {t_calculate[5]} units.\n"
                     "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(t_message)  # --------------------------------------------------------------------------------------------

    elif selections[0] == "square":  # Square's Section-----------------------------------------------------------------
        s_calculate = s.calculate_square(selections[1])
        s_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                     f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                     f"Side length: {s_calculate[0]} units.\n"
                     f"Apothem and inscribed circle radius: {s_calculate[1]} units.\n"
                     f"Perimeter: {s_calculate[2]} units.\nArea: {s_calculate[3]} squared units.\n"
                     f"Circumscribed circle radius: {s_calculate[4]} units.\n"
                     "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(s_message)  # --------------------------------------------------------------------------------------------

    elif selections[0] == "pentagon":  # Pentagon's Section-------------------------------------------------------------
        pe_calculate = pe.calculate_pentagon(selections[1])
        pe_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                      f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                      f"Side length: {pe_calculate[0]} units.\n"
                      f"Apothem and inscribed circle radius: {pe_calculate[1]} units.\n"
                      f"Perimeter: {pe_calculate[2]} units.\nArea: {pe_calculate[3]} squared units.\n"
                      f"Circumscribed circle radius: {pe_calculate[4]} units.\n"
                      "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(pe_message)  # -------------------------------------------------------------------------------------------

    elif selections[0] == "hexagon":  # Hexagon's Section---------------------------------------------------------------
        hex_calculate = hex.calculate_hexagon(selections[1])

        hex_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                       f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                       f"Side length: {hex_calculate[0]} units.\n"
                       f"Apothem and inscribed circle radius: {hex_calculate[1]} units.\n"
                       f"Perimeter: {hex_calculate[2]} units.\nArea: {hex_calculate[3]} squared units.\n"
                       f"Circumscribed circle radius: {hex_calculate[4]} units.\n"
                       "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(hex_message)  # ------------------------------------------------------------------------------------------

    elif selections[0] == "heptagon":  # Heptagon's Section-------------------------------------------------------------
        hep_calculate = hep.calculate_heptagon(selections[1])

        hep_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                       f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                       f"Side length: {hep_calculate[0]} units.\n"
                       f"Apothem and inscribed circle radius: {hep_calculate[1]} units.\n"
                       f"Perimeter: {hep_calculate[2]} units.\nArea: {hep_calculate[3]} squared units.\n"
                       f"Circumscribed circle radius: {hep_calculate[4]} units.\n"
                       "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(hep_message)  # ------------------------------------------------------------------------------------------

    elif selections[0] == "octagon":  # Octagon's Section---------------------------------------------------------------
        o_calculate = o.calculate_octagon(selections[1])

        o_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                     f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                     f"Side length: {o_calculate[0]} units.\n"
                     f"Apothem and inscribed circle radius: {o_calculate[1]} units.\n"
                     f"Perimeter: {o_calculate[2]} units.\nArea: {o_calculate[3]} squared units.\n"
                     f"Circumscribed circle radius: {o_calculate[4]} units.\n"
                     "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(o_message)  # --------------------------------------------------------------------------------------------

    elif selections[0] == "nonagon":  # Nonagon's Section---------------------------------------------------------------
        n_calculate = n.calculate_nonagon(selections[1])

        n_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                     f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                     f"Side length: {n_calculate[0]} units.\n"
                     f"Apothem and inscribed circle radius: {n_calculate[1]} units.\n"
                     f"Perimeter is: {n_calculate[2]} units.\nArea is: {n_calculate[3]} squared units.\n"
                     f"Circumscribed circle radius is: {n_calculate[4]} units.\n"
                     "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(n_message)  # --------------------------------------------------------------------------------------------

    elif selections[0] == "decagon":  # Decagon's Section---------------------------------------------------------------
        d_calculate = d.calculate_decagon(selections[1])

        d_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                     f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                     f"Side length: {d_calculate[0]} units.\n"
                     f"Apothem and inscribed circle radius: {d_calculate[1]} units.\n"
                     f"Perimeter: {d_calculate[2]} units.\nArea: {d_calculate[3]} squared units.\n"
                     f"Circumscribed circle radius: {d_calculate[4]} units.\n"
                     "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(d_message)  # --------------------------------------------------------------------------------------------

    elif selections[0] == "circle":  # Circle's Section-----------------------------------------------------------------
        c_calculate = c.calculate_circle(selections[1])

        c_message = (f"\nThis {selections[0]}'s data is as follows...\n\n"
                     f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                     f"Radius: {c_calculate[0]} units.\nDiameter: {c_calculate[1]} units.\n"
                     f"Circumference (perimeter): {c_calculate[2]} units.\nArea: {c_calculate[3]} squared units.\n"
                     "‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾|-|‾\n")

        print(c_message)  # --------------------------------------------------------------------------------------------


def need_more_calculations():
    calculate_more = input("Would you like to explore more geometric concepts?  Yes  |  No:\n").lower()

    if calculate_more == "no" or calculate_more == "n":
        print("\nWe'll explore more figures next time! See you soon! 🤓📐📏\n")
        global calculate
        calculate = False

        return calculate


print(f"\nWelcome to the GEOMETRY CONSULTANT!{a.art}\nHere you'll be able to explore the properties of an array of "
      f"geometric concepts based on a specific characteristic given by you. Let's begin!\n")

while calculate:
    geometry_consultant()
    need_more_calculations()
