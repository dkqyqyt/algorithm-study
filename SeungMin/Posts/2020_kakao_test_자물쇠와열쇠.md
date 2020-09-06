# 2020 카카오 블라인트 테스트

## 자물쇠와 열쇠

###### 문제 설명

고고학자인 **튜브**는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열려고 살펴보니 특이한 형태의 **자물쇠**로 잠겨 있었고 문 앞에는 특이한 형태의 **열쇠**와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 **`1 x 1`**인 **`N x N`** 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 **`M x M`** 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
- lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
- M은 항상 N 이하입니다.
- key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
  - 0은 홈 부분, 1은 돌기 부분을 나타냅니다.

------

### 입출력 예

| key                               | lock                              | result |
| --------------------------------- | --------------------------------- | ------ |
| [[0, 0, 0], [1, 0, 0], [0, 1, 1]] | [[1, 1, 1], [1, 1, 0], [1, 0, 1]] | true   |

### 입출력 예에 대한 설명

![자물쇠.jpg](https://grepp-programmers.s3.amazonaws.com/files/production/469703690b/79f2f473-5d13-47b9-96e0-a10e17b7d49a.jpg)

key를 시계 방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히 모두 채울 수 있습니다.

---

### Codes

```python
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
        for i in range(len(lock)): # 틀린 부분
            for j in range(len(lock)): # 틀린 부분
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
```

> 자물쇠를 오른쪽과 아래쪽으로 이동하는 경우만 계산했다. 
>
> 왼쪽과 위쪽으로 이동하는 경우를 추가하기 위해 for문의 범위를 수정하였다.

```Python
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
```

