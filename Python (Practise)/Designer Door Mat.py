# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,input().split())

for i in range(1,n+1):
    k = ((n+1)//2)

    if(i == 1 or i == n): # top and bottom lines
        print('.|.'.center(m, '-'))
    elif(i == (n+1) // 2): # 'Welcome' condition
        print('WELCOME'.center(m,'-'))
    elif(i >= 1 and i < (n+1)//2): # dynamic printing, upper part
        print( (".|"+  "..|" * ((i-1) * 2) + ".").center(m,'-'))
    elif(i > (n+1)//2 and i <= n): # dynamic printing, lower part
        print( (".|"+ "..|" *     (((i - ((i - k)*2)) - 1) * 2)     + ".").center(m,'-'))
