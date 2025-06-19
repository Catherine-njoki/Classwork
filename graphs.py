from collections import deque


class Ge:


    def __init__(self,directed=False):
      self.directed = directed

     # """""""
      #graph ={#A an C are edges
       #   A :(B,2) (C,6) (D,4)#this is a turple
        #  C :(A,6) (F,2)
      #}
      #""""""

      self.adj_list =dict()

    def __repr__(self):
          graph_string=""
          for node ,neighbours in self.adj_list.items():
              graph_string += f"{node} -> {neighbours} \n"
          return graph_string

    def add_node(self ,node):#it adds a random vertice
        if node not in self.adj_list:
            self.adj_list[node] = set() #the square brackets is because its a list # [node] is the key set() is the value
        else:
            raise ValueError ("Node already exists")


    def add_edge(self,from_node ,to_node,weight =None):#we are specifying where the edge is coming from and where it is going to
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:#if it is directed
            self.adj_list[from_node].add(to_node)

            if not self.directed:#if weight is none but not directed
                self.adj_list[to_node].add(from_node)

        else:#if we have a weight but directed
           self.adj_list[from_node].add((to_node,weight))

        if not self.directed: #now we check if it's directed
            self.adj_list[to_node].add((from_node,weight))

    def remove_edge(self, edge):
        pass

    def bfs(self,start_node):
        visited = set()
        queue = deque([start_node])
        order =[]
        while queue:
            node = queue.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)#check if the neighbours have been visited

                for neighbour in neighbours:
                   if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                   if neighbour not in visited:
                        queue.append(neighbour)

    def dfs(self,start_node):
        visited = set()
        stack = deque([start_node])
        order =[]
        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)#check if the neighbours have been visited

                for neighbour in sorted (neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)

            return order




    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())

if __name__ == '__main__':
    graph_obj=Ge(directed=True)

    graph_obj.add_edge("A","B",2)
    graph_obj.add_edge("A","J",2)
    graph_obj.add_edge("A","C",3)
    graph_obj.add_edge("A","D",4)
    graph_obj.add_edge("D","C",7)
    graph_obj.add_edge("D","B",4)

    print(graph_obj)
    print("BREADTH FIST SEARCH: \n")
    print(graph_obj.bfs("A"))

    print("DEPTH FIRST SEARCH: \n")
    print(graph_obj.dfs("A"))






