import sys

def solve_case(lines, idx):
    # Lê N, M, I
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx >= len(lines):
        return idx, False  # sem mais casos
    try:
        N, M, I = map(int, lines[idx].split())
    except:
        return idx, False
    idx += 1

    # Lê idades (1..N)
    age_vals = list(map(int, lines[idx].split()))
    idx += 1
    age = [0] + age_vals  # 1-indexed

    # Grafo de posições (arestas X->Y significam X gerencia Y)
    # Para consultas de gerente mais jovem, é útil o grafo reverso: Y->X
    rev_adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, lines[idx].split())
        idx += 1
        rev_adj[y].append(x)

    # Inicialmente, empregado i está na posição i
    emp_at_pos = [0] * (N + 1)
    pos_of_emp = [0] * (N + 1)
    for i in range(1, N + 1):
        emp_at_pos[i] = i
        pos_of_emp[i] = i

    out = []
    from collections import deque

    for _ in range(I):
        parts = lines[idx].split()
        idx += 1

        if parts[0] == 'P':
            e = int(parts[1])
            start_pos = pos_of_emp[e]

            # BFS/DFS no grafo reverso para subir para os gerentes
            visited = [False] * (N + 1)
            q = deque()
            visited[start_pos] = True
            q.append(start_pos)

            best = None
            while q:
                u = q.popleft()
                for v in rev_adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        emp = emp_at_pos[v]
                        a = age[emp]
                        if best is None or a < best:
                            best = a

            out.append(str(best) if best is not None else '*')

        elif parts[0] == 'T':
            a, b = int(parts[1]), int(parts[2])
            # Trocar posições de A e B
            pa, pb = pos_of_emp[a], pos_of_emp[b]
            # swap emp_at_pos
            emp_at_pos[pa], emp_at_pos[pb] = emp_at_pos[pb], emp_at_pos[pa]
            # atualizar pos_of_emp
            pos_of_emp[a], pos_of_emp[b] = pb, pa

        else:
            # Linha inesperada (ignora)
            pass

    print("\n".join(out))
    return idx, True


def main():
    data = sys.stdin.read().strip().splitlines()
    idx = 0
    first = True
    while True:
        prev_idx = idx
        idx, ok = solve_case(data, idx)
        if not ok:
            break

if __name__ == "__main__":
    main()