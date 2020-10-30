def PresortMode(Arr):
    i = 0 
    modelFrequency = 0
    n = len(Arr)
    while (i<=n-1):
        runlength = 1
        runvalue = Arr[i]
        while i+runlength <= n-1 and Arr[i+runlength] == runvalue:
            runlength = runlength +1
        if runlength > modelFrequency:
            modelFrequency = runlength
            modelvalue = runvalue
        i = i+runlength
    return modelvalue

print(PresortMode([200,2,3,4,5,6,7,8,5,5,7,2,42,4,12,2,2,2,2,2])) 
print('hihi')
print('Hello Chó Long')
