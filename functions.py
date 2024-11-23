# Function - reusable collection of code that performs a particular task

def greet(name, age, country='Australia'):
    print(f'Hello, {name}! You are {age} years old.')
    print(f'{name} lives in {country}.')
    
# Call the function. "Call" means execute or run the code in the function, then come back here when the function finishes

greet('Adrian', 35, 'New Zealand')