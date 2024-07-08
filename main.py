"""
Aplikasi deteksi gempa terkini
"""
# from gempaterkini import ekstraksi_data, tampilkan_data
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)