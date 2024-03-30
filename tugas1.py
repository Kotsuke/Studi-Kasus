# sebuah code untuk memberikan saran dalam mengatur keuangan 
def saldobulanini(pendapatan, persenan):
    budget = {}
    for kategori, persentase in persenan.items():
        budget[kategori] = (pendapatan * persentase) / 100
    return budget

def main():
    # Input pendapatan bulanan
    pendapatanbulanan = float(input("Masukkan pendapatan bulanan Anda: "))

    # Persentase pengeluaran untuk setiap kategori
    persentase = {
        'Kebutuhan : ' : 50,
        'Tabungan : ': 20,
        'Keinginan : ' : 30
    }

    # Menghitung pengeluaran berdasarkan persentase
    saldobulanan = saldobulanini(pendapatanbulanan, persentase)

    # Output budget untuk setiap kategori
    print("\nSaran Jumlah Penggunaan Keuangan Berdasarkan Katagori :")
    for kategori, jumlah in saldobulanan.items():
        print(f"{kategori}: Rp{jumlah:.2f}")

if __name__ == "__main__":
    main()