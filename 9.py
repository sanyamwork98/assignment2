n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    cmd = command[0]
    
    if cmd == 'pop':
       
        smallest = min(s)
        s.remove(smallest)
    elif cmd == 'remove':
        val = int(command[1])
        s.remove(val)  
    elif cmd == 'discard':
        val = int(command[1])
        s.discard(val)

print(sum(s))
