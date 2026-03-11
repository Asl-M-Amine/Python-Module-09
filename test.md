1️⃣ What Python really stores

When you do:

counter = mage_counter()

Python creates a function object that contains:

the function code (inner_count)

the captured variables (count)

So internally it is something like:

counter
   |
   v
Function object
   ├── code: inner_count
   └── closure:
        └── cell -> count = 0

The variable count is stored inside a cell object, not a dictionary.

2️⃣ You can actually see the closure

Python lets you inspect it:

counter = mage_counter()

print(counter.__closure__)

Example output:

(<cell at 0x...: int object at ...>,)

This means the function has a closure with one cell.

3️⃣ Reading the stored value

You can even see the value inside the closure:

print(counter.__closure__[0].cell_contents)

Output:

0

After calling:

counter()
counter()

Now:

print(counter.__closure__[0].cell_contents)

Output:

2

So the value changes but stays stored inside the closure cell.