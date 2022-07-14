def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    answer = 0

    for i in range(len(cities)):
        cur = cities[i].lower()
        if cur in cache:
            cache.remove(cur)
            cache.append(cur)
            answer += 1
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(cur)

    return answer

print(solution(2, [
    "jeju", "Pangyo", 
    "Seoul", "NewYork", 
    "LA", "SanFrancisco", 
    "Seoul", "Rome", 
    "Paris", "Jeju", 
    "NewYork", "Rome"
]))