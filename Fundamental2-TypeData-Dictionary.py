# Type data Dictonary

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('Data ini dikirimkan oleh aplikasi Gojek untuk memberikan info driver di sekitar aplikasi')
data_dari_server_ojek ={
    'tanggal': '2021-07-31',
    'driver_list':[{'nama': 'One', 'jarak': '10'} ,
                    {'nama': 'Two', 'jarak': '20'},
                   {'nama': 'Three', 'jarak': '30'},
                   {'nama': 'Four', 'jarak': '70'}]
}

print(data_dari_server_ojek)
print(f"Driver disekitar sini {data_dari_server_ojek['driver_list']}")
print(f"Driver #1 {data_dari_server_ojek['driver_list'][1]}")
print(f"Driver #4 {data_dari_server_ojek['driver_list'][4]}")
print(f"Driver terdekat berjarak {data_dari_server_ojek['driver_list'][2]['jarak']} meter")