#by Copilot
import itertools

data = ['A', 'B', 'C']

permutations = list(itertools.permutations(data))

for perm in permutations:
    print(perm)

#執行結果
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
