def ekstraksi_data():
    """
    Tanggal: 08 Juli 2024
    Waktu: 11:33:40 WIB
    Magnitudo: 2.5
    Kedalaman: 6 km
    Lokasi LS: 7.00  BT: 107.18
    Pusat gempa: Pusat gempa berada di darat, 20 km tenggara Kab. Cianjur
    Dirasakan: Dirasakan (Skala MMI): II - III Cibeber, II - III Cempaka
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '08 Juli 2024'
    hasil['waktu'] = '11:33:40 WIB'
    hasil['magnitudo'] = 2.5
    hasil['kedalaman'] = 6
    hasil['lokasi'] = {'ls' : 7, 'bt' : 107.18}
    hasil['pusat'] = 'Pusat gempa berada di darat, 20 km tenggara Kab. Cianjur'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Cibeber, II - III Cempaka'
    return hasil


def tampilkan_data(result):
    print("Gempa terkini berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi LS {result['lokasi']['ls']}, BT {result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")