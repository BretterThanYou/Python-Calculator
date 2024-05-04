import tkinter as tk
import math

# Create the UI window
window = tk.Tk()

# Add a title to the top of the webpage
window.title("Brett's Calculator")

# Display the text for variable one input
varone = tk.Label(text="Variable One")

# Create the entry box for variable one
entryone = tk.Entry()

# Pack the variable one label
varone.pack()

# Pack the entry box for variable one
entryone.pack()

# Display the text for variable two input
vartwo = tk.Label(text="Variable Two")

# Create the entry box for variable two
entrytwo = tk.Entry()

# Pack the variable two label
vartwo.pack()

# Pack the variable two entry box
entrytwo.pack()

# Create the buttons for the calculator

# Create the addition button
button_sum = tk.Button(text="Addition")

# Pack the addition button
button_sum.pack()

# Create a frame for the addition button
sum_frame = tk.Frame(window)

# Pack the frame for the addition button
sum_frame.pack()

# Create the function for the addition button
def addition(event):
    # Retrieve the value of entryone and convert it to int
    var1 = int(entryone.get())

    # Retrieve the value of entrytwo and convert it to int
    var2 = int(entrytwo.get())

    # Add the two variables together
    sum = var1 + var2

    # Display the result
    sum_label.config(text="Result: " + str(sum))

# Create a label for the result
sum_label = tk.Label(sum_frame)

# Pack the result label
sum_label.pack()

# Bind the addition function to the addition button
button_sum.bind("<Button-1>", addition)

# Create the subtraction button
button_sub = tk.Button(text="Subtraction")

# Pack the subtraction button
button_sub.pack()

# Create a frame for the subtraction button
sub_frame = tk.Frame(window)

# Pack the frame for the subtraction button
sub_frame.pack()

# Create the function for the subtraction button
def subtraction(event):
    # Retrieve the value of entryone and convert it to int
    var1 = int(entryone.get())

    # Retrieve the value of entrytwo and convert it to int
    var2 = int(entrytwo.get())

    # Subtract var2 from var1
    sub = var1 - var2

    # Display the result
    sub_label.config(text="Result: " + str(sub))

# Create a label for the result
sub_label = tk.Label(sub_frame)

# Pack the result label
sub_label.pack()

# Bind the subtraction function to the subtraction button
button_sub.bind("<Button-1>", subtraction)

# Create the multiplication button
button_multi = tk.Button(text="Multiplication")

# Pack the multiplication button
button_multi.pack()

# Create a frame for the multiplication button
multi_frame = tk.Frame(window)

# Pack the frame for the multiplication button
multi_frame.pack()

# Create the function for the multiplication button
def multiplication(event):
    # Retrieve the value of entryone and convert it to int
    var1 = int(entryone.get())

    # Retrieve the value of entrytwo and convert it to int
    var2 = int(entrytwo.get())

    # Multiply var1 and var2
    product = var1 * var2

    # Display the result
    multi_label.config(text="Result: " + str(product))

# Create a label for the result
multi_label = tk.Label(multi_frame)

# Pack the result label
multi_label.pack()

# Bind the multiplication function to the multiplication button
button_multi.bind("<Button-1>", multiplication)

# Create the division button
button_divide = tk.Button(text="Division")

# Pack the division button
button_divide.pack()

# Create a frame for the division button
divide_frame = tk.Frame(window)

# Pack the frame for the division button
divide_frame.pack()

# Create the function for the division button
def division(event):
    # Retrieve the value of entryone and convert it to int
    var1 = int(entryone.get())

    # Retrieve the value of entrytwo and convert it to int
    var2 = int(entrytwo.get())

    # Divide var1 by var2
    quotient = var1 / var2

    # Display the result
    divide_label.config(text="Result: " + str(quotient))

# Create a label for the result
divide_label = tk.Label(divide_frame)

# Pack the result label
divide_label.pack()

# Bind the division function to the division button
button_divide.bind("<Button-1>", division)

# Create the exponent button
button_exponent = tk.Button(text="Exponent")

# Pack the exponent button
button_exponent.pack()

# Create a frame for the exponent button
exponent_frame = tk.Frame(window)

# Pack the frame for the exponent button
exponent_frame.pack()

# Create the function forthe exponent button
def exponent(event):
    # Retrieve the value of entryone and convert it to int
    var1 = int(entryone.get())

    # Retrieve the value of entrytwo and convert it to int
    var2 = int(entrytwo.get())

    # Raise var1 to the power of var2
    exponent = var1 ** var2

    # Display the result
    exponent_label.config(text="Result: " + str(exponent))

# Create a label for the result
exponent_label = tk.Label(exponent_frame)

# Pack the result label
exponent_label.pack()

# Bind the exponent function to the exponent button
button_exponent.bind("<Button-1>", exponent)

# Create the square root button
button_sqrt = tk.Button(text="Square Root")

# Pack the square root button
button_sqrt.pack()

# Create a frame for the square root button
sqrt_frame = tk.Frame(window)

# Pack the frame for the square root button
sqrt_frame.pack()

# Create the function for the square root button
def square_root(event):
    # Retrieve the value of entryone and convert it to int
    var1 = int(entryone.get())

    # Calculate the square root of var1
    sqrt = math.sqrt(var1)

    # Display the result
    sqrt_label.config(text="Result: " + str(sqrt))

# Create a label for the result
sqrt_label = tk.Label(sqrt_frame)

# Pack the result label
sqrt_label.pack()

# Bind the square root function to the square root button
button_sqrt.bind("<Button-1>", square_root)

# Start the tkinter event loop
window.mainloop()