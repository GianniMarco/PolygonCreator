import turtle as t
x1 = int(input("Enter number of sides"))
angle = 360/x1
for x in range(x1):
  t.forward(26)
  t.left(angle)
t.mainloop()
