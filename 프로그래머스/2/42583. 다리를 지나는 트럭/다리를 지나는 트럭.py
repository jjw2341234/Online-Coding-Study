def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridges = sum(bridge)
    while bridge:
        answer+=1
        bridges -= bridge.pop(0)
        if truck_weights:
            if bridges + truck_weights[0] <= weight:
                new = truck_weights.pop(0)
                bridge.append(new)
                bridges += new
            else:
                bridge.append(0)
    return answer