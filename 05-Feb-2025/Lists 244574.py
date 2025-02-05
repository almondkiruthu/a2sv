# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    
    arr = []
    while(N > 0):
        command = input().split()
        action = command[0]
        if action == "insert":
            i, e = int(command[1]), int(command[2])
            arr.insert(i, e)
        elif action == "print":
            print(arr)
        elif action == "remove":
            e = int(command[1])
            arr.remove(e)
        elif action == "append":
            e = int(command[1])
            arr.append(e)
        elif action == "sort":
            arr.sort()
        elif action == "pop":
            arr.pop()
        elif action == "reverse":
            arr.reverse()
        N -= 1