import yaml

# Declare a python object with data

books = [{'name': 'Think Python: An Introduction to Software Design', 'author': 'Allen B. Downey', 'price': '23'},

         {'name': 'Fluent Python: Clear, Concise, and Effective Programming', 'author': 'Luciano Ramalho',
          'price': '50'},

         {'name': 'Think Python: An Introduction to Software Design', 'author': 'Allen B. Downey', 'price': '33'}

         ]

# Convert and print the JSON data in YAML stream

print(yaml.dump(books))
