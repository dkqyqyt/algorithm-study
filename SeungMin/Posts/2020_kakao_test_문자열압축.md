# 2020 카카오 블라인트 테스트

## 문자열 압축

###### 문제 설명

데이터 처리 전문가가 되고 싶은 **어피치**는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만, 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- s의 길이는 1 이상 1,000 이하입니다.
- s는 알파벳 소문자로만 이루어져 있습니다.

##### 입출력 예

| s                            | result |
| ---------------------------- | ------ |
| `"aabbaccc"`                 | 7      |
| `"ababcdcdababcdcd"`         | 9      |
| `"abcabcdede"`               | 8      |
| `"abcabcabcabcdededededede"` | 14     |
| `"xababcdcdababcdcd"`        | 17     |

### 입출력 예에 대한 설명

**입출력 예 #1**

문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.

**입출력 예 #2**

문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.

**입출력 예 #3**

문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.

**입출력 예 #4**

문자열을 2개 단위로 자르면 abcabcabcabc6de 가 됩니다.
문자열을 3개 단위로 자르면 4abcdededededede 가 됩니다.
문자열을 4개 단위로 자르면 abcabcabcabc3dede 가 됩니다.
문자열을 6개 단위로 자를 경우 2abcabc2dedede가 되며, 이때의 길이가 14로 가장 짧습니다.

**입출력 예 #5**

문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

---

### Codes

```python
def solution(s):
    idx = len(s)
    min_len = len(s)
    for i in range(1,idx):
        letters = s[0:i]
        current_letter = s[0:i]
        current_idx = i
        while current_idx < idx:
            next_letter = s[current_idx:current_idx+i]
            if next_letter == current_letter:
                if 97 <= ord(letters[-1]) <= 122:
                    letters += "2"
                else:
                    new_letter = chr(ord(letters[-1])+1)
                    # print(new_letter)
                    letters = letters[:-1] + new_letter
            else:
                letters += next_letter
                current_letter = next_letter
                
            current_idx += i

        if len(letters) < min_len:
            min_len = len(letters)

    return min_len
```

> 실패하는 케이스들이 존재한다.
>
> 반복되는 문자열이 두자리수 또는 세자리수로 넘어갈 때 아스키코드 변환에서 문제가 생겼다. 

---

**반복 문자열 갯수 세는 방식을 수정했다.**

```python
def my_solution(s):
    # 문자열 총 길이
    idx = len(s)

    # 최소 문자열 길이 | Default : 기존 문자열 길이
    min_len = len(s)

    # 만들어지는 문자열 확인용
    final_letter = s

    # 1개부터 짤라본다. 절반 초과의 길이는 자를 필요가 없다.
    # i : 자를 문자열 길이
    for i in range(1, idx//2+1):
        # 초기값 설정
        letters = s[0:i]  # 가장 처음 문자열, 이후에 값들을 추가해 갈 변수
        current_letter = s[0:i]  # 현재 선택된 문자열, 이후의 문자열과 비교 용도
        current_idx = i  # 현재 index 저장 변수
        
        # current_idx 를 자르는 길이만큼 늘려주면서 문자열 총 길이보다 크거나 같아 지면 종료
        while current_idx < idx:
            next_letter = s[current_idx:current_idx+i]  # 다음 i 길이의 문자열
            
            # 다음 문자열과 현재 문자열이 같음
            if next_letter == current_letter:
                # 마지막 character 가 a~z 사이인 경우 "2" 만 추가
                if 97 <= ord(letters[-1]) <= 122:
                    letters += "2"
                
                # 마지막 character 가 숫자인 경우
                else:
                    # 현재까지 반복된 갯수를 센다.
                    num_idx = len(letters)-1
                    while 48 <= ord(letters[num_idx]) <= 57:
                        num_idx -= 1
                    num_idx += 1
                    num = int(letters[num_idx:]) + 1  # 현재까지 반복된 갯수에 1을 추가
                    letters = letters[:num_idx] + str(num)  # 반복된 갯수를 문자열 마지막에 추가
            # 다음 문자열과 현재 문자열이 다른 경우
            # 다음 문자열을 최종 문자열에 추가한 후, 현재 문자열 갱신
            else:
                letters += next_letter
                current_letter = next_letter
            
            # 다음 자를 문자열로 넘어간다.
            current_idx += i
        
        # 압축된 문자열의 길이가 현재까지의 최소 압축 문자열 길이보다 작으면 갱신
        if len(letters) < min_len:
            min_len = len(letters)
            final_letter = letters

    return min_len
```



