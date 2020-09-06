from copy import deepcopy

def solution(key, lock):
    # 자물쇠의 돌기 부분만 spins 배열에 좌표 저장
    spins = []
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j]:
                spins.append((i,j))
    answer = open_checker(lock) # 만약 처음부터 자물쇠를 열 수 있다면 바로 종료
    if not answer:
        answer = open_lock(spins,key,lock)

    return answer

# 시계방향으로 90도 씩 회전
def turn(key):
    turned_key = [[0 for j in range(len(key))] for i in range(len(key))]

    # 회전 후 돌기 부분만 spins 배열에 좌표 저장
    spins = []
    for i in range(len(key)):
        for j in range(len(key[i])):
            turned_key[j][len(key)-1-i] = key[i][j]
            if key[i][j]:
                spins.append((j,len(key)-1-i))
    return spins, turned_key

def open_lock(spins, key, lock):
    # 시계방향으로 3번 회전 반복
    for turn_count in range(4):
        # 키를 대입할 수 있는 모든 경우의 수 반복
        for i in range(-len(lock)+1,len(lock)):
            for j in range(-len(lock)+1,len(lock)):
                new_lock = deepcopy(lock)
                flag = False # 겹치는 돌기가 있는지 저장할 변수
                for k in range(len(spins)):
                    # 위치 이동후 키를 대입했을 때 lock 의 범위를 벗어나면 continue
                    if spins[k][0] + i >= len(lock) or spins[k][1] + j >= len(lock) or spins[k][0] + i < 0 or spins[k][1] + j < 0:
                        continue
                    # 비어있는 홈이면 채워넣는다.
                    if new_lock[spins[k][0]+i][spins[k][1]+j] == 0:
                        new_lock[spins[k][0] + i][spins[k][1] + j] = 1
                    # 돌기가 겹치면 flag에 True를 대입하고 break
                    else:
                        flag=True
                        break
                # flag가 True이면 자물쇠를 열 수 없는 방법이다.
                # flag가 False일 때 open_checker함수를 통해 자물쇠를 열 수 있는지 판단
                if not flag and open_checker(new_lock):
                    return True
        if turn_count != 3: # 마지막에는 따로 회전시킬 필요가 없다.
            spins,key = turn(key)
    return False

# 자물쇠를 열 수 있는지 체크
def open_checker(lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j]:
                continue
            else:
                return False
    return True

# key = [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
key = [[0,1,1,0],[1,0,0,1],[0,1,1,1],[0,1,0,0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


print(solution(key,lock))