class Node:
    # Menyimpan state (nama lokasi/jalan) dan parent (node sebelumnya).
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


class StackFrontier:
    # Struktur data Frontier berbasis LIFO (Stack) untuk algoritma DFS.
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Frontier kosong!")
        # LIFO: mengambil elemen paling akhir (puncak stack)
        return self.frontier.pop()


class QueueFrontier(StackFrontier):
    # Struktur data Frontier berbasis FIFO (Queue) untuk algoritma BFS.
    def remove(self):
        if self.empty():
            raise Exception("Frontier kosong!")
        # FIFO: mengambil elemen paling awal (depan antrean)
        return self.frontier.pop(0)


# Representasi Graf Rute Jalan (Tanpa Bobot) dari CitraGarden Gowa ke UC Makassar (CPI)
ROAD_GRAPH = {
    "CitraGarden Gowa": ["Yusuf Bauti"],
    "Yusuf Bauti": ["CitraGarden Gowa", "Sultan Hasanuddin", "Tun Abdul Razak"],
    "Tun Abdul Razak": ["Hertasning", "Yusuf Bauti"],
    "Sultan Hasanuddin": ["Sultan Alauddin", "Yusuf Bauti"],
    "Hertasning": ["A.P. Pettarani", "Tun Abdul Razak"],
    "Sultan Alauddin": ["A.P. Pettarani", "Andi Djemma", "Danau Tj. Bunga", "Sultan Hasanuddin"],
    "A.P. Pettarani": ["Andi Djemma", "Hertasning", "Ratulangi", "Sultan Alauddin"],
    "Andi Djemma": ["A.P. Pettarani", "Ratulangi", "Sultan Alauddin"],
    "Ratulangi": ["A.P. Pettarani", "Andi Djemma", "Haji Bau"],
    "Danau Tj. Bunga": ["Metro Tj. Bunga", "Sultan Alauddin"],
    "Haji Bau": ["Metro Tj. Bunga", "Ratulangi"],
    "Metro Tj. Bunga": ["Danau Tj. Bunga", "Haji Bau", "UC Makassar (CPI)"],
    "UC Makassar (CPI)": ["Metro Tj. Bunga"]
}


def graph_search(start, goal, frontier):
    # Mencari jalur dari start ke goal menggunakan algoritma GRAPH-SEARCH.
    # Mengembalikan tuple: (jalur_solusi, daftar_node_explored)

    # Inisialisasi frontier dengan node awal
    frontier.add(Node(state=start, parent=None))

    # Explored set berbasis set sesuai ketentuan soal
    explored = set()
    explored_order = []  # Menyimpan urutan node yang diekspansi

    while not frontier.empty():
        # Keluarkan node dari frontier
        node = frontier.remove()

        # Goal test dilakukan saat node dikeluarkan dari frontier
        if node.state == goal:
            path = []
            curr = node
            while curr is not None:
                path.append(curr.state)
                curr = curr.parent
            path.reverse()
            return path, explored_order

        # Tandai state sebagai explored
        explored.add(node.state)
        explored_order.append(node.state)

        # Bangkitkan tetangga urut abjad (A-Z)
        neighbors = sorted(ROAD_GRAPH.get(node.state, []))

        # Saring node anak: jangan tambahkan jika sudah ada di frontier atau explored set
        valid_children = [
            nb for nb in neighbors
            if not frontier.contains_state(nb) and nb not in explored
        ]

        # Untuk DFS (StackFrontier), masukkan dalam urutan terbalik
        # agar tetangga dengan abjad terkecil berada di puncak stack (diekspansi lebih dulu)
        if type(frontier) is StackFrontier:
            for child_state in reversed(valid_children):
                frontier.add(Node(state=child_state, parent=node))
        else:
            for child_state in valid_children:
                frontier.add(Node(state=child_state, parent=node))

    return None, explored_order


# Eksekusi Program
if __name__ == "__main__":
    start_loc = "CitraGarden Gowa"
    goal_loc = "UC Makassar (CPI)"

    bfs_path, bfs_explored = graph_search(start_loc, goal_loc, QueueFrontier())
    print("=== HASIL BFS ===")
    print("Jalur Solusi :", " -> ".join(bfs_path))
    print("Explored     :", bfs_explored)

    dfs_path, dfs_explored = graph_search(start_loc, goal_loc, StackFrontier())
    print("\n=== HASIL DFS ===")
    print("Jalur Solusi :", " -> ".join(dfs_path))
    print("Explored     :", dfs_explored)