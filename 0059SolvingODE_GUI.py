import matplotlib
import matplotlib.pyplot as plt
import tkinter
import time

myRoot = tkinter.Tk()
myRoot.title("LCCDE Solver")

coeffLabel0 = tkinter.Label(myRoot, text="Coefficient: ", font=("System", 24), pady=20)
aEntry = tkinter.Entry(myRoot, width=4, font=("System", 22), justify="center")
coeffLabel_ddy = tkinter.Label(myRoot, text="y''(t)+", font=("System", 24))
bEntry = tkinter.Entry(myRoot, width=4, font=("System", 22), justify="center")
coeffLabel_dy = tkinter.Label(myRoot, text="y'(t)+", font=("System", 24))
cEntry = tkinter.Entry(myRoot, width=4, font=("System", 22), justify="center")
coeffLabel_y = tkinter.Label(myRoot, text="y(t)+", font=("System", 24))
dEntry = tkinter.Entry(myRoot, width=4, font=("System", 22), justify="center")
coeffLabel_Last = tkinter.Label(myRoot, text = "=0", font=("System", 24))

coeffLabel0.grid(row=0, column=0)
aEntry.grid(row=0, column=1)
coeffLabel_ddy.grid(row=0, column=2)
bEntry.grid(row=0, column=3)
coeffLabel_dy.grid(row=0, column=4)
cEntry.grid(row=0, column=5)
coeffLabel_y.grid(row=0, column=6)
dEntry.grid(row=0, column=7)
coeffLabel_Last.grid(row=0, column=8)


icLabel0 = tkinter.Label(myRoot, text="Initial Condition: ", font=("System", 24), pady=20)
icLabel_t = tkinter.Label(myRoot, text="t=", font=("System", 24))
tEntry = tkinter.Entry(myRoot, font=("System", 22), width=3, justify="center")
icLabel_y = tkinter.Label(myRoot, text=",  y(t)=", font=("System", 24))
yEntry = tkinter.Entry(myRoot, font=("System", 22), width=3, justify="center")
icLabel_dy = tkinter.Label(myRoot, text=",  y'(t)=", font=("System", 24))
dyEntry = tkinter.Entry(myRoot, font=("System", 22), width=3, justify="center")

icLabel0.grid(row=1, column=0)
icLabel_t.grid(row=1, column=1)
tEntry.grid(row=1, column=2)
icLabel_y.grid(row=1, column=3)
yEntry.grid(row=1, column=4)
icLabel_dy.grid(row=1, column=5)
dyEntry.grid(row=1, column=6)

def initialLavelChange():
    if tEntry.get()=='':
        icLabel_y.config(text=",  y(" + 't' + ")=")
        icLabel_dy.config(text=",  y'(" + 't' + ")=")
    else:
        icLabel_y.config(text=",  y("+tEntry.get()+")=")
        icLabel_dy.config(text=",  y'("+tEntry.get()+")=")

intervalLabel01 = tkinter.Label(myRoot, font=("System", 24), text="Interval: ", pady=20)
minEntry = tkinter.Entry(myRoot, font=("System", 22), width=4, justify="center")
intervalLabel02 = tkinter.Label(myRoot, font=("System", 24), text="< t <")
maxEntry = tkinter.Entry(myRoot, font=("System", 22), width=4, justify="center")

intervalLabel01.grid(row=2, column=0)
minEntry.grid(row=2, column=1)
intervalLabel02.grid(row=2, column=2)
maxEntry.grid(row=2, column=3)

def buttonPress_Test():
    ax = plt.subplot()
    ax.plot([1,2,3,4], [1,4,9,16])
    plt.show()

def buttonPress():
    global aEntry
    global bEntry
    global cEntry
    global dEntry
    global tEntry
    global yEntry
    global dyEntry
    global minEntry
    global maxEntry

    xAxis = []
    yAxis = []

    #Coefficients
    a=float(aEntry.get())
    b=float(bEntry.get())
    c=float(cEntry.get())
    d=float(dEntry.get())

    #Initial Conditions
    t=float(tEntry.get())
    y=float(yEntry.get())
    dydt=float(dyEntry.get())
    ddydtdt = None
    dt = 1e-4

    #Interval
    minVal = float(minEntry.get())
    maxVal = float(maxEntry.get())

    xAxis.append(t)
    yAxis.append(y)

    while(t<maxVal):
        ddydtdt = (-1) * (b*dydt + c*y + d) / a
        y = y + dt*dydt
        dydt = dydt + dt*ddydtdt
        t += dt
        xAxis.append(t)
        yAxis.append(y)

    xAxis.reverse()
    yAxis.reverse()

    t = float(tEntry.get())
    y = float(yEntry.get())
    dydt = float(dyEntry.get())
    ddydtdt = None

    while(t>minVal):
        ddydtdt = (-1) * (b*dydt + c*y + d) / a
        y = y - dt * dydt
        dydt = dydt - dt * ddydtdt
        t -= dt
        xAxis.append(t)
        yAxis.append(y)

    xAxis.reverse()
    yAxis.reverse()

    ax = plt.subplot()
    ax.plot(xAxis, yAxis)
    ax.grid(True, which="both")
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()


solveButton = tkinter.Button(myRoot, font=("System", 20),text="Solve", command=buttonPress)
solveButton.grid(row=3, column=3)

emptyLabel_Below = tkinter.Label(myRoot, text=" ")
emptyLabel_Below.grid(row=4, column=0)


while (True):
    myRoot.update()
    initialLavelChange()
    time.sleep(0.01)
