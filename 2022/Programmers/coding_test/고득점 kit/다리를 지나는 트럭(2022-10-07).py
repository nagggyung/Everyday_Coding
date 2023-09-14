# 강의 듣고 풀기!
# 문제 접근법 자체가 생각이 안났던 문제이다.
# 다리를 deque() 로 놓고 풀면 해결할 수 있는 문제이다.

'''
* 시간 초과 문제가 발생하여 원인을 찾아봤더니,
다음과 같은 답변을 찾아서 기록한다. 

sum() 함수가 O(n)이라 많이 잡아먹는듯 합니다. 
cross 또한 한번이긴 하지만 cross = deque([0] * bridge_length)로 줄일 수 있습니다.
sum() 대신에 sum_weight = 0 or current_weight = 0 변수할당하여 계산하면 시간 초과 문제를 해결할 수 있습니다.

<요약>
- sum 이 O(N) 이라 시간을 많이 잡아먹는다
- [0 for _ in len(bridge_length)] 보다 [0]*bridge_length 가 시간을 더 줄일 수 있다.
''' 

# 다리를 지나는 트럭

from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    time = 0
    truck_weights = deque(truck_weights)
    bridgesum = sum(bridge)
    while bridge:
        bridgesum -= bridge[0]
        bridge.popleft()
        time += 1
        
        if truck_weights:
            if  bridgesum + truck_weights[0] <= weight:
                bridgesum+=truck_weights[0]
                bridge.append(truck_weights.popleft())
                
            else:
                bridge.append(0)
    return time


