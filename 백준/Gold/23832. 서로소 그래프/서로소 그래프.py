def count_coprime_edges(n):
    """
    Count the number of edges in the coprime graph
    """
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    
    return sum(phi[i] for i in range(2, n + 1))

n = int(input())
print(count_coprime_edges(n))