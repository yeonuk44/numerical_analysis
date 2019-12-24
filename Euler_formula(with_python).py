import math

a = 1.0 # first time
b = 2.0 # final time
N = 10 # time term
alpha = 4.2 # initial value

f = lambda t, y : ((-2 * y) * (1 / t)) + (t * t) # Differential equation
g = lambda t : ((t * t * t) * (1 / 5)) + (4 * (1 / (t * t))) # Solution equation

h = (b - a) / N
t = a
y = alpha

print("Euler formula")
print("Time \t\t Approximation \t\t Exact_value \t\t error \t\t relative_error")
print("-------------------------------------------------------------------------------------------")
print(t,"\t\t",y,"\t\t",y,"\t\t",y-y,"\t\t",y-y)

for i in range(0,N):
    y = y + (h * (f(t,y)))
    t = a + ((i + 1) * h)
    exact = g(t) # Exact_value
    error = abs(y - exact)
    relative_error = ((y - exact) / exact) * 100
    print("%1.1f\t\t"%t ,"%1.4f\t\t"%y ,"%1.4f\t\t"%exact ,"%1.4f\t\t"%error ,"%1.4f\t\t"%relative_error)
