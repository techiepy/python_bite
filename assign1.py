
Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

x = Sessions_Attended.values()
y = str(x).split(",")
z = len(y)
a = Sessions_Attended.keys()
print("I have attended",z,*a,"\b!!")

