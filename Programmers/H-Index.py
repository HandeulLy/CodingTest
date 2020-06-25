def solution(citations):
    citations, size = sorted(citations), len(citations)
    for i in range(size) :
        if citations[i] >= size - 1 : return size-i
    return 0

input_citations = [22, 42]
solution(input_citations)