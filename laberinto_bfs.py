from colorama import Fore as F
from collections import deque

class Node:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self, __o) -> bool:
        return (self.x, self.y) == (__o.x, __o.y)


class Solve:
    def __init__(self, maze: list, start: Node, destination: Node) -> None:
        self.maze = maze
        self.path = maze
        self.start = start
        self.destination = destination
        self.steps = []

    def get_path(self) -> None:
        str_steps = ''
        for step in range(len(self.steps)):
            if step == 0:
                str_steps += f'{ F.GREEN  }{step + 1}(INICIO): { F.WHITE }({self.steps[step][0]},{self.steps[step][1]}), '
            elif step == len(self.steps) - 1:
                str_steps += f'{ F.GREEN  }{step + 1}(FIN): { F.WHITE }({self.steps[step][0]},{self.steps[step][1]}), '
            else:
                str_steps += f'{ F.GREEN  }{step + 1}: { F.WHITE }({self.steps[step][0]},{self.steps[step][1]}), '

        print(f'{ F.RED }* * * BFS * * *')
        print(f'{ F.CYAN }Cantidad de pasos: { F.WHITE }{ len(self.steps) }')
        print(f'{ F.CYAN }Pasos-> { F.WHITE }{ str_steps[:-2] }.\n')

        self.path[self.start.x][self.start.y] = 's'
        self.path[self.destination.x][self.destination.y] = 'e'

        for i in range(len(self.path)):
            for j in range(len(self.path[i])):
                if (i,j) in self.steps and self.path[i][j] != 's' and self.path[i][j] != 'e':
                    print(f'{ F.CYAN }*', end=' ')
                elif self.path[i][j] == 1:
                    print(f'{ F.BLACK }#', end=' ')
                elif self.path[i][j] == 0:
                    print(f'{ F.GREEN }.', end=' ')
                else:
                    print(f'{ F.RED }{ self.path[i][j] }', end=' ')
            print()
    
    def bfs(self, current: Node) -> bool:
        """
            1:  Pared
            0:  Libre
            2: visitado
        """
        # Direcciones posibles para moverse (der, izq, arriba, abajo)
        neighbors = [Node(0, 1), Node(0, -1), Node(1, 0), Node(-1, 0)]

        # TDA Cola <queue>. # Agregar el nodo inicial  
        queue = deque([(current.x, current.y)])
      
        # Mientras no esté vacía la cola
        while queue:
            # Desencolar elemento de la cola
            x, y = queue.popleft()

            # Si ya llego al destino
            if Node(x, y) == self.destination:
                return True

            # Recorrer los adyacentes (vecinos)
            for n in neighbors:
                # (x, y) del nodo actual desencolado
                nx = x
                ny = y

                while 0 <= (nx + n.x) < len(self.maze) and 0 <= (ny + n.y) < len(self.maze[0]) and self.maze[nx + n.x][ny + n.y] != 1:
                    # Ir desplazando la cantidad (x, y) del vecino
                    nx += n.x
                    ny += n.y

                    # Si no esta en la lista de pasos, agregarlo
                    if (nx, ny) not in self.steps:
                        self.steps.append((nx,ny))
                    
                    # Si ya llego al destino
                    if Node(nx, ny) == self.destination:
                        return True
                
                # Verificar si ya ha sido visitado
                # 2: visitado
                if self.maze[nx][ny] != 2:
                    # Marcar como visitado
                    self.maze[nx][ny] = 2

                    # Si no esta en la lista de pasos, agregarlo
                    if (nx, ny) not in self.steps:
                        self.steps.append((nx,ny))
                    
                    # Encolar elemento
                    queue.append((nx, ny))
        return False       
        
        

if __name__ == '__main__':
    # Caso de Prueba
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],   
        [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],   
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                        
    ]
    start=Node(24, 2); destination=Node(1, 32) 
    s = Solve(maze, start, destination)

    if s.bfs(start):
        s.get_path()
    else:
        print('No existe una solución')
