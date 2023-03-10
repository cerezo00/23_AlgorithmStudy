#메모리 30840KB, 시간 108ms

N, K = map(int, input().split()) # N : 동전의 종류, K : 만들고자 하는 가치의 합 
moneys = [] #N개의 동적의 가치를 입력받아 저장할 moneys 배열 생성
cnt = 0 # cnt : K를 만들 때 필요한 동전 개수의 최소값

for i in range(N):
    moneys.append(int(input())) #동전의 종류의 개수만큼 반복문을 돌며 오른차순으로 주어지는 동전의 가치를 moneys 배열에 차례대로 저장

#동전 개수의 최솟값을 구하기 위해서는 동전의 가치가 큰 값부터 K를 채워나가야 한다. (그리디)
#그렇기 때문에 오름차순으로 입력받아 저장되어 있는 moneys 배열을 reverse 시켜줌으로써 동전의 가치가 큰 것부터 하나씩 비교해 나간다.
moneys.reverse() 

for coin in moneys: #내림차순으로 정렬되어 있는 moneys 배열의 첫번째 원소부터 하나씩 비교해 나가며
    if K // coin == 0: ##만약 K를 원소로 나누었을 때 몫이 0이라면, 즉, 비교하고자 하는 원소가 현재 K값보다 크다면
                        ##현재 원소로 K를 구성하는 것은 불가능하다는 것이므로 아무런 실행없이 continue 문으로 다음 원소로 비교 차례를 넘긴다.
        continue
    else: #만약 몫이 0이 아니라면, 즉, 비교하고자 하는 현재 원소가 현재 K 값보다 작다면
        dev = K // coin #dev 변수에 현재 K를 현재 원소로 나눈 몫을 저장한 후
        K %= coin #K에는 K를 현재 원소로 나눈 나머지를 저장하고
        cnt += dev #사용되는 동전 개수를 저장하는 cnt 변수에는 dev 변수값을 더해 나가준다.

print(cnt)