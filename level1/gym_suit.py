def solution(n, lost, reserve):
    answer = 0
    lost.sort()  # 1

    for e in reversed(lost):  # 2
        if e in reserve:
            lost.remove(e)
            reserve.remove(e)

    for e in reversed(lost):  # 3
        if e+1 in reserve:
            lost.remove(e)
            reserve.remove(e+1)

        elif e-1 in reserve:
            lost.remove(e)
            reserve.remove(e-1)

    answer = n - len(lost)

    return answer


# 1
'''
문제에서 정렬되어 있다는 언급이 없었는데,
정렬되어 있다고 생각하고 푼 실수

'''

# 2
'''
lost와 reserve에 공통적으로 들어가는 원소 제거 부분
체육복을 도난당했지만, 여분의 체육복이 있는 경우 

lost로 for문 돌아도 될거 같은데, 전자로 하지 않으면 테스트 케이스 6,7 통과하지 못함
    - ??왜 그런지 아직 이유를 모르겠음 - 굳이 이 부분에서 순서가 중요한 이유가 있나??
    - (#3 찾고 얼결에 #2에 reversed(lost)적용하고 풀린 케이스)
'''


# 3
'''
체육복을 도난 당한 학생이 자신과 체격이 비슷한 여벌 체육복을 찾는 부분

여기서 reversed(lost)가 아닌 lost로 for문 돌면, 뒷 번호에 해당하는 학생이
체육복을 빌릴 수 있음에도, 못 빌리는 경우가 생겨 최대한 많은 인원이 체육복을 입을 수 있어야 한다는 충족 시키지 못하게 된다.
    - n=5, lost = [3, 5], reserve = [2, 4]의 경우 
        5가 4를 빌리고, 3이 2를 빌려 5명 모두 체육복을 입을 수 있지만,
        3이 먼저 4한테 먼저 빌리면, 5는 체육복을 입을 수 없다. 

순서가 중요!!
(!!이 부분 찾느라고 많은 시간 소모!!)

'''
