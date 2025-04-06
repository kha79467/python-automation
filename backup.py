# Define the file name
filename = "data.txt"

# Open the file in write mode
with open(filename, "w") as file:
    # Number of entries (you can modify this)
    n = int(input("Enter the number of people: "))

    for _ in range(n):
        # Get user input
        name = input("Enter name: ")
        height = float(input("Enter height (in cm): "))
        weight = float(input("Enter weight (in kg): "))

        # Write data to file
        file.write(f"{name},{height},{weight}\n")

print(f"Data successfully saved to {filename}")

