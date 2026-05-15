import os

# Set the variable (values must be strings)
os.environ['MYVAR'] = 'my_value'

# Get the variable
print(os.environ.get('MYVAR'))
