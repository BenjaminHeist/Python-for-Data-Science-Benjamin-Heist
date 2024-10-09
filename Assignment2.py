#Exercise 1: FizzBuzz
#1. Write a FizzBuzz Function: Create a function fizzbuzz(n) that takes an integer n as a parameter.
#2. Implement FizzBuzz Logic: The function should print:
#○ "Fizz" for multiples of 3
#○ "Buzz" for multiples of 5
#○ "FizzBuzz" for multiples of both 3 and 5
#○ The number itself for other numbers
#3. Call the Function: Call the function for numbers 1 to 20.

def FizzBuzz (n):
    if n%3 ==0 and n%5 ==0: 
        print('FizzBuzz')
    elif n%5 ==0: 
        print('Buzz')
    elif n%3==0:
        print('Fizz')

for i in range(1,20):
    print(FizzBuzz(i))

#Exercise 2: Basic Data Filtering
#1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats.
#2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list.
#3. Print the New List: Output the filtered list of integers.

list_mix = [10, 2.5,'Hello',True,95]
list_integers = [i for i in list_mix if type(i)==int]
print(list_integers)

#Exercise 3: Simple To-Do List
#1. Create an Empty List: Start with an empty list called todo_list.
#2. Define Functions:
#○ A function add_task(task) that adds a task to the list.
#○ A function show_tasks() that prints all tasks in the list.

todo_list=[]
def add_task(task):
    todo_list.append(task)

def show_tasks():
    print(todo_list)

add_task('groceries')
add_task('cleaning')
show_tasks()

#Exercise 4: Temperature Converter
#1. Define a Conversion Function: Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit.
#2. Print the Result: Output the converted temperature for 22oF, 46oF, 51oF and 76oF.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5 )+32
    return(fahrenheit)

celsius_to_fahrenheit(22)
celsius_to_fahrenheit(46)
celsius_to_fahrenheit(51)
celsius_to_fahrenheit(76)
