"""Evaluating the distance travelled by a ball after bouncing"""
h=eval(input("Enter initial height:\n"))
b=eval(input("Enter number of bounces:\n"))
(su,k)=(h,0.6*h)
for i in range(1,b):
	su+=2*k
	k*=0.6
su+=k
print("distance: ",su)