def getTrains(n):
    if(n < 2):
        return 1
    else:
        result = 0
        for i in range(n):
            result = result + getTrains(i)*getTrains(n-i-1)
        return result
