# H-index

def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return idx+1

# Test
print(solution([3, 0, 6, 1, 5])) # 3