import sys
from collections import Counter, deque

sys.setrecursionlimit(2500)

class Edge:
    def __init__(self, target, capacity, reverse_edge_index):
        self.target = target
        self.capacity = capacity
        self.flow = 0
        self.reverse_edge_index = reverse_edge_index

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj = [[] for _ in range(num_nodes)]
        self.level = [-1] * num_nodes

    def add_edge(self, u, v, capacity):
        forward_edge = Edge(v, capacity, len(self.adj[v]))
        backward_edge = Edge(u, 0, len(self.adj[u]))

        self.adj[u].append(forward_edge)
        self.adj[v].append(backward_edge)

    def bfs(self, source, sink):
        self.level = [-1] * self.num_nodes
        self.level[source] = 0

        q = deque([source])
        while q:
            u = q.popleft()
            for edge in self.adj[u]:
                if self.level[edge.target] < 0 and edge.flow < edge.capacity:
                    self.level[edge.target] = self.level[u]+1
                    q.append(edge.target)
        return self.level[sink] >= 0

    def send_flow(self, u, flow, sink, start):
        if u == sink: return flow

        while start[u] < len(self.adj[u]):
            edge = self.adj[u][start[u]]

            if self.level[edge.target] == self.level[u]+1 and edge.flow < edge.capacity:
                curr_flow = min(flow, edge.capacity - edge.flow)
                temp_flow = self.send_flow(edge.target, curr_flow, sink, start)

                if temp_flow > 0:
                    edge.flow += temp_flow
                    self.adj[edge.target][edge.reverse_edge_index].flow -= temp_flow
                    return temp_flow
            start[u] += 1
        return 0

    def dinic_maxflow(self, source, sink):
        if source == sink: return -1

        total_flow = 0
        while self.bfs(source, sink):
            start = [0] * self.num_nodes
            while True:
                flow = self.send_flow(source, float('inf'), sink, start)
                if not flow: break
                total_flow += flow
        return total_flow

def sol():
    n = int(input())
    a = dict(Counter(input().split()))
    b = dict(Counter(input().split()))

    connect = {
        "DA": ["DM", "HA", "HM"],
        "DW": ["DA", "HA", "HW"],
        "DM": ["DW", "HW", "HM"],

        "HA": ["HM", "BA", "BM"],
        "HW": ["HA", "BA", "BW"],
        "HM": ["HW", "BW", "BM"],

        "BA": ["BM", "DA", "DM"],
        "BW": ["BA", "DA", "DW"],
        "BM": ["BW", "DW", "DM"]
    }

    nodes = list(connect.keys())
    # Bob Layer 1-9
    bob_index = {k: i+1 for i, k in enumerate(nodes)}
    # Alice Layer 10-18
    alice_index = {k: i+10 for i, k in enumerate(nodes)}

    g = Graph(20)

    # Source to Bob layer
    for val, count in b.items():
        g.add_edge(0, bob_index[val], count)

    # Bob Layer (1-9) to Alice Layer (10-18)
    for b_val, count in b.items():
        for a_val in connect[b_val]:
            g.add_edge(bob_index[b_val], alice_index[a_val], float('inf'))

    # Alice Layer to Sink
    for val, count in a.items():
        g.add_edge(alice_index[val], 19, count)

    print(g.dinic_maxflow(0, 19))

sol()
