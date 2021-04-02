print('Masukan nama dan jenis kelamin anda (l/p)!')
la = 'Bapak'
pi = 'Nyonya'
nama= str(input('Nama :'))
jenis_kelamin= str(input('Jenis kelamin (l/p) :'))
if jenis_kelamin == 'l' :
    print("Selamat datang, " + la +" "+ nama + ' !')
elif jenis_kelamin == 'p':
    print("Selamat datang, "+ pi +" "+ nama + ' !')
else:
    pass


