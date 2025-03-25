# Vending Machine DFA

## Deskripsi
Program ini merupakan simulasi vending machine yang menggunakan konsep **Deterministic Finite Automata (DFA)** untuk mengelola transisi state berdasarkan jumlah uang yang dimasukkan dan pilihan minuman.

## Cara Menggunakan
1. Jalankan program Python dengan perintah:
   ```sh
   python3 vending_machine.py
   ```
2. Masukkan nominal uang yang diizinkan: **1000, 2000, 5000, atau 10000**.
3. Jika uang yang dimasukkan cukup, Anda dapat memilih minuman dengan memasukkan huruf:
   - **A** untuk Minuman A (3000)
   - **B** untuk Minuman B (4000)
   - **C** untuk Minuman C (6000)
4. Jika uang tidak cukup, mesin akan menampilkan pesan error.
5. Jika uang melebihi batas maksimum **10000**, program akan menampilkan pesan error.
6. Setelah pembelian sukses, mesin akan menampilkan jumlah kembalian (jika ada) dan program akan berhenti.

## Contoh Penggunaan
### 1. Membeli Minuman dengan Uang Pas
```
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): 2000
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): 1000
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): A
Drink A can be purchased. Status: ACCEPTED.
Returns: 0
```

### 2. Membeli Minuman dengan Kembalian
```
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): 5000
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): A
Drink A can be purchased. Status: ACCEPTED.
Returns: 2000
```

### 3. Kesalahan: Uang Tidak Cukup
```
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): 2000
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): A
Not enough money to buy Drink A. You have 2000.
```

### 4. Kesalahan: Uang Melebihi Batas Maksimum
```
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): 10000
Enter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): 1000
Error: If you enter 1000, the value exceeds the limit of 10000.
```

## Catatan
- Program hanya menerima input yang valid (uang dalam nominal yang diperbolehkan dan huruf minuman yang tersedia).
- Program akan terus meminta input hingga terjadi pembelian minuman atau error batas maksimal.
- Program akan berhenti setelah transaksi selesai atau terjadi error.

---

