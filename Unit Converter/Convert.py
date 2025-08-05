from Conveter import length_measurement, mass_measurement, time_measurement
import pyfiglet as pyg
from termcolor import *


def unit_length():
    print(
        "\nYou are in length(l) measurement \nIndex of the unit\n1)Millimeter(mm)\n2)Centimeter(cm)\n3)Meter("
        "m)\n4)Kilometer(km)\n5)Back")
    choice = input("Please choose the unit which you  want to convert into another unit :\t")

    if choice == "1":
        value = input("Enter the Millimeter(mm) :\t")
        unit = length_measurement.Millimeter(int(value))
        print("\nIndex of the unit\n1)Centimeter(cm)\n2)Meter(m)\n3)Kilometer(km)\n")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.mm_to_cm()) + "cm \n")
        elif utc == "2":
            print("Answer is " + str(unit.mm_to_m()) + "m \n")
        elif utc == "3":
            print("Answer is " + str(unit.mm_to_km()) + "km \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_length()

    elif choice == "2":
        value = input("Enter the Centimeter(cm) :\t")
        unit = length_measurement.Centimeter(int(value))
        print("\nIndex of the unit\n1)Millimeter(mm)\n2)Meter(m)\n3)Kilometer(km)\n")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.cm_to_mm()) + "mm \n")
        elif utc == "2":
            print("Answer is " + str(unit.cm_to_m()) + "m \n")
        elif utc == "3":
            print("Answer is " + str(unit.cm_to_km()) + "km \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_length()

    elif choice == "3":
        value = input("Enter the Meter(m) :\t")
        unit = length_measurement.Meter(int(value))
        print("\nIndex of the unit\n1)Millimeter(mm)\n2)Centimeter(cm)\n3)Kilometer(km)")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.m_to_mm()) + "mm \n")
        elif utc == "2":
            print("Answer is " + str(unit.m_to_cm()) + "cm \n")
        elif utc == "3":
            print("Answer is " + str(unit.m_to_km()) + "km \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_length()
    elif choice == "4":
        value = input("Enter the Kilometer(km): \t")
        unit = length_measurement.Kilometer(int(value))
        print("\nIndex of the unit\n1)Millimeter(mm)\n2)Centimeter(cm)\n3)Meter(m)")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.km_to_mm()) + "mm \n")
        elif utc == "2":
            print("Answer is " + str(unit.km_to_cm()) + "cm \n")
        elif utc == "3":
            print("Answer is " + str(unit.km_to_m()) + "m \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_length()

    elif choice == "5":
        return

    else:
        print("Please enter the write choice. You entered wrong choice")
        unit_length()


def unit_mass():
    print(
        "\nYou are in length(l) measurement \nIndex of the unit\n1)Milligram(mg)\n2)Gram(g)\n3)Kilogram(kg)\n4)Tonne("
        "t)\n5)Back")
    choice = input("Please choose the unit which you  want to convert into another unit :\t")

    if choice == "1":
        value = input("Enter the Milligram(mg): \t")
        unit = mass_measurement.Milligram(int(value))
        print("\nIndex of the unit\n1)Gram(g)\n2)Kilogram(kg)\n3)Tonne(t)\n4)Back")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.mg_to_g()) + "g \n")
        elif utc == "2":
            print("Answer is " + str(unit.mg_to_kg()) + "kg \n")
        elif utc == "3":
            print("Answer is " + str(unit.mg_to_t()) + "t \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_mass()

    elif choice == "2":
        value = input("Enter the Gram(g) :\t")
        unit = mass_measurement.Gram(int(value))
        print("\nIndex of the unit\n1)Milligram(mg)\n2)Kilogram(kg)\n3)Tonne(t)\n4)Back")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.g_to_mg()) + "mg \n")
        elif utc == "2":
            print("Answer is " + str(unit.g_to_kg()) + "kg \n")
        elif utc == "3":
            print("Answer is " + str(unit.g_to_t()) + "t \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_mass()

    elif choice == "3":
        value = input("Enter the Kilogram(kg) :\t")
        unit = mass_measurement.Kilogram(int(value))
        print("\nIndex of the unit\n1)Milligram(mg)\n2)Gram(g)\n3)Tonne(t)\n4)Back")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.kg_to_mg()) + "mg \n")
        elif utc == "2":
            print("Answer is " + str(unit.kg_to_g()) + "g \n")
        elif utc == "3":
            print("Answer is " + str(unit.kg_to_t()) + "t \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_mass()

    elif choice == "4":
        value = input("Enter the Tonne(t) :\t")
        unit = mass_measurement.Tonne(int(value))
        print("\nIndex of the unit\n1)Milligram(mg)\n2)Gram(g)\n3)Kilogram(kg)\n4)Back")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.t_to_mg()) + "mg \n")
        elif utc == "2":
            print("Answer is " + str(unit.t_to_g()) + "g \n")
        elif utc == "3":
            print("Answer is " + str(unit.t_to_kg()) + "kg \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_mass()
    elif choice == "5":
        return

    else:
        print("Please enter the write choice. You entered wrong choice")
        unit_mass()


def unit_time():
    print(
        "\nYou are in time(t) measurement \nIndex of the unit\n1)Second(sec)\n2)Minutes(min)\n3)Hours("
        "hr)\n4)Days\n5)Week\n6)Back")
    choice = input("Please choose the unit which you  want to convert into another unit :\t")

    if choice == "1":
        value = input("Enter the Second(sec) :\t")
        unit = time_measurement.Second(int(value))
        print("\nIndex of the unit\n1)Minutes(min)\n2)Hour(hr)\n3)Day\n4)Week")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.s_to_m()) + "min \n")
        elif utc == "2":
            print("Answer is " + str(unit.s_to_h()) + "hr \n")
        elif utc == "3":
            print("Answer is " + str(unit.s_to_d()) + "day/days \n")
        elif utc == "4":
            print("Answer is " + str(unit.s_to_w()) + "week/weeks \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_time()

    elif choice == "2":
        value = input("Enter the Minutes(min) :\t")
        unit = time_measurement.Minutes(int(value))
        print("\nIndex of the unit\n1)Second(sec)\n2)Hour(hr)\n3)Day\n4)Week")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.m_to_s()) + "sec \n")
        elif utc == "2":
            print("Answer is " + str(unit.m_to_h()) + "hr \n")
        elif utc == "3":
            print("Answer is " + str(unit.m_to_d()) + "day/days \n")
        elif utc == "4":
            print("Answer is " + str(unit.m_to_w()) + "week/weeks \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_time()

    elif choice == "3":
        value = input("Enter the Hours(hr) :\t")
        unit = time_measurement.Hours(int(value))
        print("\nIndex of the unit\n1)Second(sec)\n2)Minutes(min)\n3)Days\n4)Week")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.h_to_s()) + "sec \n")
        elif utc == "2":
            print("Answer is " + str(unit.h_to_m()) + "min \n")
        elif utc == "3":
            print("Answer is " + str(unit.h_to_d()) + "day/days \n")
        elif utc == "4":
            print("Answer is " + str(unit.h_to_w()) + "week/weeks \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_time()

    elif choice == "4":
        value = input("Enter the Days :\t")
        unit = time_measurement.Day(int(value))
        print("\nIndex of the unit\n1)Second(sec)\n2)Minutes(min)\n3)Hours(hr)\n4)Week")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.d_to_s()) + "sec \n")
        elif utc == "2":
            print("Answer is " + str(unit.d_to_m()) + "min \n")
        elif utc == "3":
            print("Answer is " + str(unit.d_to_h()) + "hr \n")
        elif utc == "4":
            print("Answer is " + str(unit.d_to_w()) + "week/weeks \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_time()

    elif choice == "5":
        value = input("Enter the Week :\t")
        unit = time_measurement.Week(int(value))
        print("\nIndex of the unit\n1)Second(sec)\n2)Minutes(min)\n3)Hours(hr)\n4)Day\n")
        utc = input("Please choose the unit in which you want to convert your unit :\t")
        if utc == "1":
            print("Answer is " + str(unit.w_to_s()) + "sec \n")
        elif utc == "2":
            print("Answer is " + str(unit.w_to_m()) + "min \n")
        elif utc == "3":
            print("Answer is " + str(unit.w_to_h()) + "hr \n")
        elif utc == "4":
            print("Answer is " + str(unit.w_to_d()) + "day/days \n")
        else:
            print("Please enter the write choice. You entered wrong choice")
            unit_time()

    elif choice == "6":
        return

    else:
        print("Please enter the write choice. You entered wrong choice")
        unit_time()


def colored(param, param1):
    pass


if __name__ == '__main__':
    res = colored(pyg.figlet_format("SI Unit System (MKS)", font="digital"), "red")
    print(res)

    while True:

        print("Please enter write index of your measurement \n 01.Length(l) \n 02.Mass(m) \n 03.Time(t) \n 04.Exit\n"
              "Note:Please "
              "enter proper index")
        fch = input("Please enter the measurement\'s index :\t")
        print()
        if fch == "1":
            unit_length()
        elif fch == "2":
            unit_mass()
        elif fch == "3":
            unit_time()
        elif fch == "4":
            exit()
        else:
            print("Please enter the write choice. You entered wrong choice")
