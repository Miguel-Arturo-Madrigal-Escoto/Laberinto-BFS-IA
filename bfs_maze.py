from colorama import Fore as F
from collections import deque

class Solve:
    def __init__(self, maze: list, start: tuple, end: tuple) -> None:
        self.maze           = maze
        self.trace_path     = maze
        self.shortest_path  = {}
        self.expanded_nodes = []
        self.start          = start
        self.end            = end
    
    def get_path(self) -> None:
        str_steps = ''
        for step in range(len(self.expanded_nodes)):
            if step == 0:
                str_steps += f'{ F.GREEN  }{step + 1}(INICIO): { F.WHITE }({self.expanded_nodes[step][0]},{self.expanded_nodes[step][1]}), '
            elif step == len(self.expanded_nodes) - 1:
                str_steps += f'{ F.GREEN  }{step + 1}(FIN): { F.WHITE }({self.expanded_nodes[step][0]},{self.expanded_nodes[step][1]}), '
            else:
                str_steps += f'{ F.GREEN  }{step + 1}: { F.WHITE }({self.expanded_nodes[step][0]},{self.expanded_nodes[step][1]}), '

        print(f'{ F.RED }* * * BFS * * *')
        print(f'{ F.CYAN }Ruta mínima: { F.WHITE }{ len(self.expanded_nodes) } pasos')
        print(f'{ F.CYAN }Pasos-> { F.WHITE }{ str_steps[:-2] }.\n')

        self.trace_path[self.start[0]][self.start[1]] = 's'
        self.trace_path[self.end[0]][self.end[1]] = 'e'

        for i in range(len(self.trace_path)):
            for j in range(len(self.trace_path[i])):
                if self.trace_path[i][j] == 's' or self.trace_path[i][j] == 'e':
                    print(f'{ F.RED }{ self.trace_path[i][j] }', end=' ')
                elif (i,j) in self.expanded_nodes and self.trace_path[i][j] != 's' and self.trace_path[i][j] != 'e':
                    print(f'{ F.CYAN }*', end=' ')
                elif self.trace_path[i][j] == 1:
                    print(f'{ F.BLACK }#', end=' ')
                else:
                    print(f'{ F.GREEN }.', end=' ')
            print()
    
    def backtracking(self):
        # Reconstrucción de la ruta mínima   
        node = self.shortest_path[(self.nx, self.ny)] # nodo final (sea el buscado o no)
        self.expanded_nodes = []            # resetear nodos expandidos

        # ir reconstruyendo por padres
        try:
            while node is not None:
                self.expanded_nodes.append(node)
                node = self.shortest_path[node]
        except:
            pass
        
        # Los pasos estan del ultimo al primero, voltearlos
        self.expanded_nodes.reverse()

    def bfs(self, curr: tuple) -> bool:
        """
            1:  Pared
            0:  Libre
            2:  Visitado
        """

        # Agregar a la ruta minima al nodo inicial
        self.shortest_path = { (curr[0], curr[1]): None }

        # Nodos adyacentes (der, izq, arriba, abajo)
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Nodos expandidos
        self.expanded_nodes.append(curr)

        # TDA cola
        queue = deque([curr])

        # Bandera de ruta encontrada
        found = False

        # Variables para almacenar las posiciones a desplazar
        self.nx = self.ny = None

        while queue:
            # (x, y) posicion actual
            x, y = queue.popleft()

            # Si ya llegó al destino
            if (x, y) == self.end:
                self.nx, self.ny = x, y
                found = True
                break

            # Recorrer los nodos adyacentes (vecinos)
            for n in neighbors:
                # Posicion self.nx, self.ny a desplazar
                self.nx, self.ny = x, y

                # Si se topa con pared
                if self.maze[self.nx + n[0]][self.ny + n[1]] == 1: continue

                # Padre del nodo actual
                parent = (self.nx, self.ny)

                # Desplazar el nodo actual en (x, y) posiciones del vecino
                self.nx += n[0]
                self.ny += n[1]

                # Checar si ya ha sido visitado
                if self.maze[self.nx][self.ny] != 2:
                    # Marcarlo como visitado
                    self.maze[self.nx][self.ny] = 2 

                    # Verificar si no se ha añadido a los nodos expandidos
                    if (self.nx, self.ny) not in self.expanded_nodes:
                        # Nodos expandidos
                        self.expanded_nodes.append(curr)

                        # Agregarlo al diccionario para sacar la ruta minima
                        self.shortest_path[(self.nx,self.ny)] = parent

                        # Encolar el nodo
                        queue.append((self.nx, self.ny))
        return found

if __name__ == '__main__':
    # Caso de Prueba
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],   
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],   
        [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],   
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                        
    ]
    start = (24, 2); end = (2, 37) 
    s = Solve(maze, start, end)
    ans = s.bfs(start)
    s.backtracking()
    s.get_path()
    if not ans:
        print(f'\n{ F.RED }No se encontró una ruta de { start } a { end }')
    


