#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """
answer1  =raw_input("Is the car silent when you turn the key:")
if(answer1 == "Y"):
  answer2 = raw_input("Are the battery terminal corroded:")
  if(answer2 == "Y"):
    print("clean terminals")
  else:
    print("Replace cables")
else:
  answer3 = raw_input("Does it make a clicking noice?")
  if(answer3 == "Y"):
      print("replace the battery")
  else:
      answer4 = raw_input("Does it crank u but fail to start?")
      if(answer4 =="Y"):
          print("check the spark plug connection!")
      else:
          answer5 = raw_input("Does the engine start and then die?")
          if(answer5 == "Y"):
              answer6 = raw_input("Does your car have fuel injection?")
              if(raw_input =="y"):
                  print("Get it in for service")
              else:
                  print("Check the choke is opening and closing")
          else:
              print("Unable to identify the problem")