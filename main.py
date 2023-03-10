import matplotlib.pyplot as plt


def coordinate():
    x = int(input("Please enter an x value:"))
    y = int(input("Please enter a y value:"))
    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return x_values, y_values


def run():
    values = path()
    plt.plot(values[0], values[1], "r--o")
    plt.show()


run()


'''
We wish to create a program to display the path Beep and Bop are taking through Robo City.

The program should consist of the following three functions:

The first function should be named coordinate and should have no parameters.
The function should start by prompting the user to enter an x value.
The function should then read in the user's response and store it in a variable named x.
The function should then prompt the user to enter a y value.
The function should then read in the user's response and store it in a variable named y.
Finally, the function should return a tuple containing x and y.
The second function should be named path and should have no parameters. 
The function should start by displaying the message "Retrieving path...".
The function should then create an empty list named x_values.
The function should then create an empty list named y_values.
The function should then create a loop that iterates 4 times and on each iteration does the following:
    Calls the first function and stores the result in a variable named data.
    Adds the first item of data (the x value) to x_values.
    Adds the second item of data (the y value) to y_values.
Finally, the function should return a list containing x_values and y_values.
The third function should be named run and should have no parameters.
The function call the second function and store the result in variable named values.
The function should then display a line plot using values[0] for the x values and values[1] for the y values.
The line plot should draw a red dashed line with circle markers and contain suitable labels for the axes.

A sample line plot is shown below for the coordinates (1,5), (1,10),(5,5),(5,10):

PyPlot Path
'''