import collections

def solution(genres, plays):
    answer = []
    album_list = collections.defaultdict(list)
    genre_total_plays = collections.defaultdict(int)
    result = - float('inf')
    cur = 0
    
    # 장르를 키로 그 장르에 속한 음악 리스트를 값으로 하는 dictionary 생성
    # 음악 리스트의 원소는 (인덱스, 플레이 횟수)이고 플레이 횟수로 정렬된다
    for i, g in enumerate(genres):
        album_list[g].append((i, plays[i]))
        album_list[g].sort(key= lambda x: -x[1])
        genre_total_plays[g] += plays[i]

    # 가장 플레이수가 많은 장르 부터 앨범에 넣는다
    for g, _ in sorted(genre_total_plays.items(), key= lambda x: -x[1]):
        if len(album_list[g]) < 2:
            answer.append(album_list[g][0][0])
            continue
        
        for i in range(2):
            answer.append(album_list[g][i][0])
            
    return answer