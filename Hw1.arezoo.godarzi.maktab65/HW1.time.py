m=input('Enter time1:').split(':')
n=input('Enter time2:').split(':')
def time_display(m,n):
    time=[0,0,0]
    for i in range( 2,-1,-1):
        x=int(m[i])+int(n[i])
        time[i]=(x)
    for i in range(3,1,-1):
        if time[i-1]-60>0:
            time[i-2]+=int(time[i-1]/60)
            time[i-1]=time[i-1]%60
    return time

kol=time_display(m,n)
print(f" This is {kol[0]} hour(s) and {kol[1]} minute(s) and {kol[2]} second(s)")

