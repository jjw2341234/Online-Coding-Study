from collections import deque

def bfs(sx, sy, ex, ey):

    q = deque()
    q.append((sx, sy, [(sx, sy)]))
    while q:
        x,y,track = q.popleft()

        for d in range(7, 0, -1):
            for dx, dy in [(-d, d), (-d, -d), (d, -d), (d,d)]:
                nx, ny = x+dx, y+dy
                if 64<nx<73 and 0<ny<9:
                    if (nx, ny) == (ex, ey) and len(track)<5:
                        return f'{len(track)} ' + " ".join(f'{chr(i)} {j}' for i,j in track) + f' {chr(ex)} {ey}'
                    if (nx, ny) not in visit:
                        visit.add((nx, ny))
                        q.append((nx, ny, track + [(nx, ny)]))
    return "Impossible"

n = int(input())
for _ in range(n):
    sx,sy,ex,ey = input().split()

    visit = set()

    visit.add((ord(sx), int(sy)))
    if (sx, sy) == (ex, ey):
        print(0, sx, sy)
    else:
        print(bfs(ord(sx), int(sy), ord(ex), int(ey)))

    