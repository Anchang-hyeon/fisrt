# Place for Studying Algorithm
## I will continue to *run* until the day I become a developer.
#
### 1.Bubble Sort(2020/04/09)
#### 인접한 두개의 원소를 순차적으로 처음부터 끝까지 비교해가며 계속 자리를 바꿔나감.
#### 시간복잡도:O(n^2)
#### 장점: 코드가 상당히 간단함.
#### 단점: 시간복잡도가 n^2이니 만큼 list의 길이가 길면 처리시간이 기하급수적으로 늘어난다.
![bubble](https://user-images.githubusercontent.com/61732687/79459907-faa21a80-802e-11ea-9bed-b3887767f942.png)
# 
### 2.Counting Sort(2020/04/10)
#### 리스트의 각 숫자별로 몇 개씩 있는지 count_list에 입력하고 갯수를 기반으로 순차적으로 정렬한뒤 반환.
#### 시간복잡도:O(n+k) k=max(list)
#### 장점: k가 작고, 각 숫자간의 간격이 좁다면 처리시간이 상당히 빠른정렬.
#### 단점: 코드가 복잡. 개인적으로 이해하는데 꽤 긴 시간이 소요됨. 
#### 만약 list=[1,0,5,10000,3]이라면 count_list에 10000까지의 공간을 창출해야하므로 상당한 메모리 낭비.
#### 즉 list의 최댓값 혹은 상위의 큰값들과 하위의 큰값들의 차가 크다면 비효율적.
![Counting](https://user-images.githubusercontent.com/61732687/79460662-1823b400-8030-11ea-88d4-6885d14054a7.png)
# 
### 3.Selection Sort(k번째 작은 수 찾기)(2020/04/16)
#### list의 첫번째 부터 순차적으로 비교해가며 k번째로 작은 수 반환.
#### 시간복잡도:O(kn)
#### 장점: Bubble sort와 마찬가지로 이 또한 코드 구현이 비교적 간단하다.
#### Conventional Selection Sort와 차이가 좀 있다. k번째로 작은 수 찾는 알고리즘이기 때문.
![Selection](https://user-images.githubusercontent.com/61732687/79461927-caa84680-8031-11ea-9dec-55f3fe6347b3.png)

