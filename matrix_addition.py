# addition of two list 

# Given m row and n colums ,,take input from user and add the two matrix lists 

def get_userInput(m):
    temp =[]
    for i in range(m):
        user_input = list(map(int,input().split()))
        temp.append(user_input)
    return temp

def addition_of_matrix(list_a,list_b,m,n):
    for i in range(m):
        temp =[]
        for j in range(n):
            res = list_a[i][j]+list_b[i][j]
            temp.append(res)
        print(temp)

def main():
    m, n = map(int,input().split())
    list_a = get_userInput(m)
    list_b = get_userInput(m)
    addition_of_matrix(list_a,list_b,m,n)

main()


