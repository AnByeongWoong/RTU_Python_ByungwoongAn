import math

a = 77.
deltax = 0.005
vmax=0
xmax=0;

myfile = open("data.txt", "w");

x = 0.;

while (x<6.):
   y = a * math.sin(x)*math.exp(-x/100.);
   if (y > vmax):
       vmax = y;
       xmax = x;
   text = str(x) + " " + str(y) + "\n"
   myfile.write(text)
   x = x + deltax;

print("Max = ", vmax, ", x = ", xmax)

myfile.close();

