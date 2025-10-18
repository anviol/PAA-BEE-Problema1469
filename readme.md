# 🧩 Iks – Cadeia de Comando (PAA/BEE – Problema 1469)

Analisa a rede de comando da empresa fictícia **Iks**.  
O programa responde a duas operações principais:

1. **Pergunta (P E)** → retorna a **idade do gerente mais jovem** (direto ou indireto) de um empregado.  
2. **Troca (T A B)** → faz com que **dois empregados troquem de posição** no organograma (a estrutura do grafo permanece a mesma).

---

## 🧠 Ideia da solução

- As relações “X gerencia Y” formam um **grafo dirigido de posições**: aresta `X → Y`.
- **Empregados** ocupam **posições**.  
  - As **idades** pertencem aos empregados.  
  - As **arestas** pertencem às posições.
- Quando ocorre uma **troca**, apenas os **ocupantes** das posições são trocados — o grafo não muda.
- Uma **pergunta (P E)** exige encontrar o **menor valor de idade** entre todos os **gerentes (diretos ou indiretos)** de `E`.

---

## 🏗️ Estruturas de dados

| Estrutura | Função |
|------------|--------|
| `rev_adj[pos]` | Lista de **gerentes diretos** da posição `pos` (grafo **reverso**) |
| `emp_at_pos[pos]` | Empregado que ocupa a **posição** `pos` |
| `pos_of_emp[emp]` | Posição atualmente ocupada pelo **empregado** `emp` |
| `age[emp]` | Idade do empregado |

### Por que usar o **grafo reverso**?
Perguntar “quem gerencia E?” significa **subir** no grafo original.  
Ao usar o grafo **reverso** (subordinado → gerente), basta percorrer as arestas “para frente” via BFS/DFS.

---

## ⚙️ Operações

### 🔹 Pergunta `P E`
1. Identifica a posição de `E`: `start = pos_of_emp[E]`.
2. Executa uma **BFS/DFS no grafo reverso** a partir de `start` (subindo para os gerentes).
3. Coleta a idade de cada gerente `age[emp_at_pos[q]]` e guarda o menor valor.
4. Se nenhum gerente for encontrado, imprime `*`.

### 🔹 Troca `T A B`
Troca os ocupantes das posições de `A` e `B`:
```python
pa, pb = pos_of_emp[a], pos_of_emp[b]
emp_at_pos[pa], emp_at_pos[pb] = emp_at_pos[pb], emp_at_pos[pa]
pos_of_emp[a], pos_of_emp[b] = pb, pa
