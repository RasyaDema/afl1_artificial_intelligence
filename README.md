# Graph Search: CitraGarden Gowa ke UC Makassar (CPI)

Implementasi GRAPH-SEARCH (BFS dan DFS) dengan Python pada graf tanpa bobot yang menggambarkan rute dari rumahku di CitraGarden Gowa menuju UC Makassar di CPI (Centre Point of Indonesia).

## File & Kelas

- `graph_search.py`: berisi `Node`, `StackFrontier` (LIFO), `QueueFrontier` (FIFO, turunan dari `StackFrontier`), `graph_search`, dan graf rute jalan (`ROAD_GRAPH`).

## Cara menjalankan

```
python graph_search.py
```

Program akan menampilkan jalur solusi dan daftar node yang di-expand (explored) untuk BFS dan DFS.

## Aturan yang diikuti

- Tetangga di-expand berdasarkan urutan abjad (untuk DFS dimasukkan ke stack dalam urutan terbalik, sehingga yang abjadnya terkecil di-pop lebih dulu).
- Goal test dilakukan saat node dikeluarkan dari frontier.
- Node anak tidak ditambahkan jika state-nya sudah ada di frontier atau explored set.
- Explored set menggunakan `set` Python.

## Graf

Setiap node adalah jalan yang dilalui dari CitraGarden Gowa menuju kampus. Semua jalan dianggap dua arah, sehingga grafnya tidak berarah. Dari CitraGarden Gowa, rute melewati Yusuf Bauti lalu bercabang ke dua arah:

- Lewat Sultan Hasanuddin dan Sultan Alauddin, lalu menuju Metro Tj. Bunga, bisa langsung lewat Danau Tj. Bunga atau lewat A.P. Pettarani, Ratulangi, dan Haji Bau.
- Lewat Tun Abdul Razak dan Hertasning, yang tersambung ke A.P. Pettarani.

Contoh rute:

- Pendek: CitraGarden Gowa > Yusuf Bauti > Sultan Hasanuddin > Sultan Alauddin > Danau Tj. Bunga > Metro Tj. Bunga > UC Makassar (CPI)
- Panjang: CitraGarden Gowa > Yusuf Bauti > Sultan Hasanuddin > Sultan Alauddin > A.P. Pettarani > Ratulangi > Haji Bau > Metro Tj. Bunga > UC Makassar (CPI)

## Hasil

| | Jalur | Node yang di-expand |
|---|---|---|
| BFS | CitraGarden Gowa, Yusuf Bauti, Sultan Hasanuddin, Sultan Alauddin, Danau Tj. Bunga, Metro Tj. Bunga, UC Makassar (CPI) | CitraGarden Gowa, Yusuf Bauti, Sultan Hasanuddin, Tun Abdul Razak, Sultan Alauddin, Hertasning, A.P. Pettarani, Andi Djemma, Danau Tj. Bunga, Ratulangi, Metro Tj. Bunga, Haji Bau |
| DFS | CitraGarden Gowa, Yusuf Bauti, Sultan Hasanuddin, Sultan Alauddin, A.P. Pettarani, Ratulangi, Haji Bau, Metro Tj. Bunga, UC Makassar (CPI) | CitraGarden Gowa, Yusuf Bauti, Sultan Hasanuddin, Sultan Alauddin, A.P. Pettarani, Hertasning, Ratulangi, Haji Bau, Metro Tj. Bunga |

BFS menghasilkan rute pendek (6 langkah, 12 node di-expand). DFS menghasilkan rute yang lebih panjang (8 langkah, 9 node di-expand). Pada graf tanpa bobot, BFS selalu menghasilkan jalur dengan jumlah langkah paling sedikit, sedangkan DFS tidak menjamin jalur terpendek. Di sini DFS masuk ke A.P. Pettarani lebih dulu karena urutan abjadnya mendahului Danau Tj. Bunga di antara tetangga Sultan Alauddin, sehingga DFS menemukan jalur yang lebih panjang terlebih dahulu.

## Analisis

**(1) Mengapa explored set diimplementasikan dengan set, bukan list?**

Untuk setiap tetangga dari setiap node yang di-expand, algoritma harus memeriksa apakah state tersebut sudah pernah di-explore. Pada `set` pemeriksaan ini rata-rata berjalan dalam waktu O(1) karena menggunakan hashing. Pada `list`, elemen harus diperiksa satu per satu sehingga waktunya O(n), dan semakin lama semakin lambat seiring bertambahnya isi list. `set` juga otomatis mengabaikan duplikat. Kekurangannya, `set` tidak punya urutan, sehingga urutan expand disimpan terpisah di dalam list (`explored_order`).
