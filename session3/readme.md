# **Running Notebook**

`jupyter lab`

# **Reference**

`https://jupyter.org/`

# **Decorators**

* Write a decorator to print: 
   
   ```<function-name>: start\end```
   
   before and after a function is executed
* Write a factory function that according to the arguments type return a suitable sum
  ```
    [1, 2, 3, 4] --> 10
    ['k', 'e', 'r', 'e', 'n'] --> 'keren'
    ['k', 3, 'r'] --> 'k3r' (mixed become a string)
  ```
  
# **Generator**

* Define generator function get_lengths that returns the length of each one of the items in the list
  ```
    lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
    for value in get_lengths(lannister):
        print(value)
  ```
* Create the same with generator expression
  ```
    lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

    # Create a generator object: lengths
    lengths = << your code goes here >>

    # Iterate over and print the values in lengths
    for value in lengths:
        print(value)
  ```