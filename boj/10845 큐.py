import sys

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    l = sys.stdin.readline().split()
    if l[0] == "push":
        q.append(l[1])
    elif l[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif l[0] == "size":
        print(len(q))
    elif l[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif l[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])