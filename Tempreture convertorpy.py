# Author: Vivi Du
# This program allows the user to convert temperatures between Fahrenheit and Celsius. It greets the user, provides a menu to choose a function, and loops based on user choice.

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def display_menu():
    """Display the menu of options."""
    print("\nTemperature Conversion Menu:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")

def get_temperature_input():
    """Prompt the user to enter a valid temperature value."""
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            return temperature
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Main program function."""
    print("Welcome to the Temperature Conversion Program!")
    user_name = input("What's your name? ")
    print(f"Hello, {user_name}! Let's get started.")

    while True:
        display_menu()
        choice = input("Please choose an option (1-3): ")

        if choice == "1":
            print("\nYou chose Fahrenheit to Celsius.")
            fahrenheit = get_temperature_input()
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
        elif choice == "2":
            print("\nYou chose Celsius to Fahrenheit.")
            celsius = get_temperature_input()
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
        elif choice == "3":
            print(f"Goodbye, {user_name}! Thanks for using the temperature converter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
