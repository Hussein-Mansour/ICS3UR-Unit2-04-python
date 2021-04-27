#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Tue/Apr27/2021
# This program calculates the cost of pizza


import constants


def main():
    # input
    diameter = int(
        input("Enter the diameter of the pizza you would " + "like (inch): ")
        )
    # process
    sub_total = (
        constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    )
    total = sub_total + (sub_total * constants.HST)
    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
