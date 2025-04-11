def solution():
    a, b = map(int, input().split())
    lucky = []
    for i in range (a, b+1):
        flag = True
        x = i
        ls = []
        while x!=0:
            ls.append(x%10)
            x//=10
        for l in ls:
            if l != 4 and l != 7:
                flag = False
                break
        if flag == False:
            continue
        lucky.append(i)

    if not lucky:
        print(-1)
    else:
        for i in lucky:
            print(i, end=" ")

def main():
    tc = 1
    # tc = int(input())
    for _ in range(tc):
        solution()

if __name__ == "__main__":
    main()