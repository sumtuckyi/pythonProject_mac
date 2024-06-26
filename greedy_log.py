def check(s, e):  # s에서 e로 이동이 가능한지 확인
    global flag
    cur = s  # 현재 통나무
    cnt = 0
    num = -1
    for i in range(1, len(logs)): # 모든 통나무를 탐색
        if logs[s][0] <= logs[i][0] <= logs[s][1] and logs[s][1] < logs[i][1]:  # 겹치는 통나무가 있다면
            cnt += 1
            num = i  # 겹치는 통나무의 번호를 저장
            if cnt == 2:  # 겹치는 통나무가 2개 이상인 경우
                break
    if cnt == 1: # 겹치는 통나무가 하나인 경우(다음 통나무로 이동 가능한 경우)
        # 다음 통나무가 도착점인지 확인
        if num == e:
            flag = True
            return
        else:  # 이동가능한 통나무가 있지만 도착점은 아닌 경우
            check(num, e)



N, Q = map(int, input().split())
logs = []
queries = []
flag = False  # 도착 가능 여부
for i in range(N):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, y))
for i in range(Q):
    s, e = map(int, input().split())
    queries.append((s, e))
logs = [(0, 0, 0)] + logs

for s, e in queries:
    flag = False
    check(s, e)
    if flag:
        print(1)
    else:
        print(0)