## 메모리 30616 KB 시간 36ms

## 입력받은 시간을 오름차순으로 정렬해 준 뒤 합을 계산하면 최솟값이 된다.

n = int(input())  ## 사람의 수
s = list(map(int, input().split()))  ## 각 사람이 돈을 인출하는데 걸리는 시간

num = 0 ## 돈을 인출하는 데 필요한 시간의 합의 최솟값
s.sort() ## 오름차순으로 정렬
for i in range(1,n): ## 반복문을 1부터 n까지 돌면서
    s[i] += s[i-1] ## i에 이전값을 더하고

print(sum(s)) ## 그 값들을 모두 더해준다.