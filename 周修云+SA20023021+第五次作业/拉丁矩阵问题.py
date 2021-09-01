def OK(c,r,b):
    for k in range(r):
        if b[r][c]==b[k][c]:
            return False
    return True

count=0
def backtrack(r,c,m,n,b):
    global  count
    #print(r,c)
    for i in range(c,n):
        b[r][i], b[r][c] = b[r][c], b[r][i]
        if(OK(c,r,b)):
            if c==n-1:
                if r==m-1:
                    count+=1
                    print(b)
                else:backtrack(r+1,0,m,n,b)
            else:backtrack(r,c+1,m,n,b)
        b[r][i], b[r][c] = b[r][c], b[r][i]

def main():

    f = open("input.txt", "r")
    m=int(f.readline())
    n=int(f.readline())
    f.close()

    print("输入m={0},n={1}".format(m,n))

    board=[[i for i in range(n)] for i in range(m)]
    backtrack(0,0,m,n,board)

    Res=count
    print(Res)

    f = open("output.txt", "w")
    f.write(str(Res))
    f.close()

if __name__ == '__main__':
    main()
