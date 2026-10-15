#Name:Daza,Liecel
#Section: Camia

first_number = int(input("First number: "))
second_number = int(input("Second number: "))

def calculate_sum():
    global first_number, second_number

    sum = first_number + second_number
    print(f"The sum is: {sum}")

def calculate_difference():
    global first_number, second_number

    difference = first_number - second_number
    print(f"The difference is: {difference}")

calculate_sum()
calculate_difference()