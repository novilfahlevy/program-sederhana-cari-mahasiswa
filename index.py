data_mahasiswa = [
  { 'nim': '2109116095', 'nama': 'Albygael Fahlevy', 'prodi': 'Sistem Informasi', 'semester': 3 },
  { 'nim': '2109116095', 'nama': 'Muhammad Novil Fahlevy', 'prodi': 'Sistem Informasi', 'semester': 2 },
]

kata_kunci_pencarian = ''

pilihan_kolom = ['NIM', 'Nama', 'Prodi', 'Semester']
index_kolom = None

# Fungsi untuk melakukan algortima sorting merge sort
def merge_sort(lst) :
  if len(lst) <= 1 : return lst
  
  mid = len(lst) // 2
  
  left = merge_sort(lst[:mid])
  right = merge_sort(lst[mid:])

  return merge(left, right)

# fungsi untuk menggabungkan 2 buah list menjadi satu list yang telah terurut
# berdasarkan algoritma merge sort
def merge(left, right) :
  result = []
  i, j = 0, 0

  while i < len(left) and j < len(right) :
    if left[i][pilihan_kolom[index_kolom].lower()] < right[j][pilihan_kolom[index_kolom].lower()] :
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result += left[i:]
  result += right[j:]
  
  return result

# Fungsi untuk menentukan apakah data mahasiswa sesuai dengan kata kunci
def fungsi_pencarian_mahasiswa(mahasiswa) :
  kata_kunci_sesuai_nim = kata_kunci_pencarian in mahasiswa['nim']
  kata_kunci_sesuai_nama = kata_kunci_pencarian in mahasiswa['nama']
  kata_kunci_sesuai_prodi = kata_kunci_pencarian in mahasiswa['prodi']
  kata_kunci_sesuai_semester = kata_kunci_pencarian in str(mahasiswa['semester'])

  return kata_kunci_sesuai_nim or kata_kunci_sesuai_nama or kata_kunci_sesuai_prodi or kata_kunci_sesuai_semester

# Fungsi untuk mengambil data mahasiswa berdasarkan kata kunci
def ambil_data_mahasiswa() :
  # cari mahasiswa berdasarkan kata kunci
  data_mahasiswa_yang_dicari = list(filter(fungsi_pencarian_mahasiswa, data_mahasiswa))

  # urutkan mahasiswa secara ascending
  data_mahasiswa_yang_diurutkan = merge_sort(data_mahasiswa_yang_dicari) if pilihan_kolom[index_kolom].lower() is not None else data_mahasiswa_yang_dicari

  return data_mahasiswa_yang_diurutkan

def pilih_kolom_yang_ingin_diurutkan() :
  print('\n[1] NIM')
  print('[2] Nama')
  print('[3] Program Studi')
  print('[4] Semester')

  return int(input('Pilih kolom yang ingin diurutkan: ')) - 1

def menu_cari_mahasiswa() :
  global kata_kunci_pencarian, index_kolom

  kata_kunci_pencarian = input('\nSilakan masukan kata kunci untuk mencari mahasiswa:\n> ')
  index_kolom = pilih_kolom_yang_ingin_diurutkan()

  mahasiswa_yang_dicari = ambil_data_mahasiswa()

  print(f"\nMahasiswa dengan kata kunci '{kata_kunci_pencarian}' yang ditemukan:\n")
  
  for mahasiswa in mahasiswa_yang_dicari :
    print('NIM           :', mahasiswa['nim'])
    print('Nama          :', mahasiswa['nama'])
    print('Program Studi :', mahasiswa['prodi'])
    print('Semester      :', mahasiswa['semester'], '\n')

  return app()

def menu_tambah_mahasiswa() :
  print('\nMasukan data mahasiswa')

  nim      = input('NIM           : ')
  nama     = input('Nama          : ')
  prodi    = input('Program studi : ')
  semester = int(input('Semester      : '))

  data_mahasiswa.append({
    'nim': nim,
    'nama': nama,
    'prodi': prodi,
    'semester': semester
  })

  print('Berhasil menambah data mahasiswa.\n')

  return app()

def pilih_menu() :
  print('[1] Tambah data mahasiswa')
  print('[2] Cari mahasiswa')
  print('[3] Keluar')

  return input('Pilih menu: ')

# Fungsi utama
def app(show_title=False) :
  if show_title :
    print("\nAplikasi Data Mahasiswa")
    print('- ' * 15, '\n')

  try :
    index_menu = int(pilih_menu())

    if index_menu == 1 :
      return menu_tambah_mahasiswa()
    elif index_menu == 2 :
      return menu_cari_mahasiswa()
    elif index_menu == 3 :
      print('Sampai jumpa :)')
      exit()
  except KeyboardInterrupt :
    exit()

app(show_title=True)
