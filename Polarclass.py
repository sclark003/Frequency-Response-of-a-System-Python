from math import*
                
class Polar_Convert:
    def __init__(self,r,theta):
        self.r = r
        self.theta = theta
    
    def convert_cart(self):
        x = self.r*cos(self.theta)
        y = self.r*sin(self.theta)
        return x, y
    
    def convert_polar(self,x,y):
        r = ((x**2)+(y**2))**0.5
        theta = atan(y/x)
        return r, theta

class Polar_Maths:
    
    def add(self,r1,theta1,r2,theta2):
        a = Polar_Convert(r1,theta1)
        b = Polar_Convert(r2,theta2)
        x1,y1 = a.convert_cart()
        x2,y2 = b.convert_cart()
        x3 = x1 + x2
        y3 = y1 + y2
        r3,theta3 = a.convert_polar(x3,y3)
#        print("r= ", r3)
#        print("theta= ", theta3)
        return r3, theta3
    
    def subtract(self,r1,theta1,r2,theta2):
        a = Polar_Convert(r1,theta1)
        b = Polar_Convert(r2,theta2)
        x1,y1 = a.convert_cart()
        x2,y2 = b.convert_cart()
        x3 = x1 - x2
        y3 = y1 - y2
        r3,theta3 = a.convert_polar(x3,y3)
#        print("r= ", r3)
#        print("theta= ", theta3)
        return r3, theta3
    
    def multiply(self,r1,theta1,r2,theta2):
        r3 = r1 * r2
        theta3 = theta1 + theta2
#        print("r= ", r3)
#        print("theta= ", theta3)
        return r3, theta3

    def divide(self,r1,theta1,r2,theta2):
        r3 = r1/r2
        theta3 = theta1 - theta2
#        print("r= ", r3)
#        print("theta= ", theta3)
        return r3, theta3
    
    def power(self,r,theta,n):
        r_out = r**n
        theta_out = n*theta
#        print("r= ", r_out)
#        print("theta= ", theta_out)
        return r_out, theta_out
        
        