import matplotlib.pyplot as plt
import numpy as np

#Coordinates (as a global...)
x,y = [], []

# Linear solver
def my_linfit(x,y):
    a = (sum(x)/len(x)*sum(y)/len(y)-sum(x*y)/len(x))/(sum(x)/len(x)*sum(x)/len(x)-sum(x*x)/len(x))
    b = sum(y)/len(y)-a*sum(x)/len(x)
    return a,b

#Mouse click event to record the coordinates
def OnClick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        ('double' if event.dblclick else 'single', event.button,
        event.x, event.y, event.xdata, event.ydata))
    if(event.button == 1):
        x.append(event.xdata)
        y.append(event.ydata)
        plt.clf()
        plt.gca().text(5, 10.7, "Left click on the canvas to record x,y coordinates.\nCalculates the linear model on the fly.\nRight click to show the final linear model with my fit.", ha="center", va="center")
        plt.axis([0, 10, 0, 10])
        plt.ylabel('y-axis')
        plt.xlabel('x-axis')
        if(len(x) > 1):
            x2 = np.array(x)
            y2 = np.array(y)
            a,b = my_linfit(x2, y2)
            plt.plot(x2, a * x2 + b, )
        plt.plot(x, y, 'kx')
        plt.show()
    if(event.button == 3):
        plt.clf()
        drawLinearModel(x, y)
        plt.close()

#Mouse events to figure
def cursorCapture():
    fig = plt.gcf()
    fig.canvas.mpl_connect('button_press_event', OnClick)
    plt.gca().text(5, 10.7, "Left click on the canvas to record x,y coordinates.\nCalculates the linear model on the fly.\nRight click to show the final linear model with my fit.", ha="center", va="center")
    plt.axis([0, 10, 0, 10])
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')
    plt.plot(x, y, 'kx')
    plt.show()

#Plots the linear model
def drawLinearModel(x, y):
    x = np.array(x)
    y = np.array(y)
    a,b = my_linfit(x, y)
    plt.plot(x, y, 'kx')
    plt.plot(x, a * x + b)
    plt.axis([0, 10, 0, 10])
    plt.title(f'My fit: a={a} and b={b}')
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')
    plt.show()

# Main
cursorCapture()
