import math

def calcDiscrim(a, b, c):
    """
    Calculates and returns the discriminant if it's non-negative and -1 otherwise.
    :param a:
    :param b:
    :param c:
    :return: none
    """

    a = int(a)
    b = int(b)
    c = int(c)
    d = b ** 2 - 4 * a * c
    if d > 0:
        discrim1 = ( -b + math.sqrt(d))/ (2 * a)
        discrim2 = ( -b - math.sqrt(d))/ (2 * a)
        print("The roots are: ", discrim1, "and ", discrim2)
        return discrim1, discrim2
    elif d == 0:
        discrim1 = - b / (2 * a)
        print("The unique root is: ", discrim1)
    else:
        print("There are no roots")


def AnswerWasYes():
    """
    Asks the user if they wish to execute the program again
    :return:
    """
    ques = input("Execute again? ")
    if ques == "y" or "Y":
        return ques
    else:
        print("alright bye")
        return ques


def newX(x, n):
    """
    returns the new approximation based on the old value of x and the value of the given n
    :param x:
    :param n:
    :return:
    """

    nx = (1/2)*(x + (n/x))
    return nx


def approxRoot(n, numIterations):
    x = 1
    for i in range(numIterations):
        x = newX(x, n)

    return x

def midPoint(x1, y1, x2, y2):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    xmid = (x1 + x2)/2
    ymid = (y1 + y2)/2
    x = xmid
    y = ymid
    return x, y

def makeDot(myTurtle, dotColor, dotSize):
    """

    :param myTurtle:
    :param dotColor:
    :param dotSize:
    :return:
    """
