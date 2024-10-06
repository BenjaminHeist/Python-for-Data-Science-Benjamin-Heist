Exercise 1

def FizzBuzz (n):
    if n%3 ==0 and n%5 ==0: 
        print('FizzBuzz')
    elif n%5 ==0: 
        print('Buzz')
    elif n%3==0:
        print('Fizz')

for i in range(1,20):
    print(FizzBuzz(i))

Exercise 2 

list_mix = [10, 2.5,'Hello',True,95]
list_integers = [i for i in list_mix if type(i)==int]
print(list_integers)

Exercise 3 

todo_list=[]
def add_task(task):
    todo_list.append(task)

def show_tasks():
    print(todo_list)

add_task('groceries')
add_task('cleaning')
show_tasks()

Exercise 4 

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5 )+32
    print(fahrenheit)

celsius_to_fahrenheit(22)
celsius_to_fahrenheit(46)
celsius_to_fahrenheit(51)
celsius_to_fahrenheit(76)
