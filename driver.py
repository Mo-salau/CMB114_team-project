#!/usr/bin/python3

from mohammed.converter_ui import *
from mohammed.converter_engine import *
from yoyo.quiz import *

"""
main.py - Entry point for CMB114 CW2
Run: python main.py
"""

def main():
    print("\n========================================")
    print("      ENERGY UNIT CONVERTER v1.0")
    print("========================================")

    while True:
        print("\n  1. Convert a unit")
        print("  2. Physics Mode")
        print("  3. Compatibility check")
        print("  4. Conversion history")
        print("  5. Quiz")
        print("  6. Supported units")
        print("  h. How to use")
        print("  q. Quit")
        choice = input("\n  Select: ").strip().lower()

        if choice == "1":
            run_conversion()
        elif choice == "2":
            run_physics()
        elif choice == "3":
            run_compatibility_check()
        elif choice == "4":
            show_history()
        elif choice == "5":
            run_quiz()
        elif choice == "6":
            show_supported_units()
        elif choice == "h":
            show_help()
        elif choice == "q":
            print("\n  Goodbye!\n")
            break
        else:
            print("  Invalid option.")

if __name__ == "__main__":
    main()
