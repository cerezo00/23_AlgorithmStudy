## 메모리 64344 KB  시간 260 ms
##입력
n, k = map(int, input().split())
kid = list(map(int, input().split()))

## 키 차이가 최소가 되도록 해야하므로 각 원생사이의 키 차이를 구한다.
ans = []
for i in range(1, n):
    ans.append(kid[i] - kid[i-1])

## 최솟값을 구하는 것이므로 키 차이를 구한 ans 리스트를 역순으로 정렬
ans.sort(reverse=True)

## 만약 5명을 3그룹으로 나눈다면 원생사이의 키 차이가 가장 큰 두 원생을 기준으로 나누면 된다.
## 즉, k-1개의 키차이가 빠진 나머지 키차이의 합을 구하면 된다.
##  k-1부터 끝까지의 리스트 총 합을 구하면 된다.
print(sum(ans[k-1:]))

## 8명 중 4개의 그룹을 만든다고 할 때,
#1  2  3  5  6  8  11 16  -> 오름차순으로 입력된 아이들의 키
#  1  1  2  1  2  3   5  -> 인접한 아이들 간의 키 차이

# => 키 차이를 내림차순 정렬
# 5 3 2 2 1 1 1
# 여기서 값이 큰 것 k-1개, 즉 3개를 빼주면 5 3 2가 제거된다.
# 따라서 인덱스가 3인 값부터 끝까지 sum을 구해주면 2+1+1+1=5 -> 티셔츠의 최소 비용