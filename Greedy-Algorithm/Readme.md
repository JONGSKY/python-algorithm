# (당장 좋은 것만 선택하는) 그리디
: 현재 상황에서 지금 당장 좋은 것만 고르는 방법

(암기X, 많은 유형을 접하고 풀어보는 훈련이 필요함)

------------ 문제 풀이 ------------

### 예제 3-1) 거스름 돈

#### 가정상황
1. 거슬러야할 돈 (N원)
2. 동전 500, 100, 50, 10 (무수히 많다고 가정)

#### 문제
- 동전의 최소 개수는?

#### 해설
- **가장 큰 화폐 단위부터** 돈을 거슬러 주는 것
  
  (화폐의 종류 : K개 / 시간 복잡도 : O(k)
  
※ 가장 큰 단위가 작은 단위의 배수일 때 가능

  (동전이 500, 400, 100 일 때, 800원 도출 방법은 다름.)

