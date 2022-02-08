print(('=' * 10) +' Selamat Datang di Perhitungan Cache dengan Metode Second Chance ' + ('=' * 10),'\n')
jumlahpageref = int(input('Masukkan jumlah page references : '))
a = [None] * jumlahpageref
for i in range(jumlahpageref) : 
    b = int(input('Masukkan page reference ke '+ str(i+1) + ': '))
    a[i] = b
kapasitas = int(input("Masukkan jumlah frame : "))
print('\n')
hit = 0 
fault = 0  
tampung = [None] * kapasitas
panjangumur = [0] * kapasitas
tampung2 = [None] * kapasitas
bitref = [0] * kapasitas
for i in a :
    for k in range(kapasitas) : 
        if tampung[k] != tampung2[k] : 
            panjangumur[k] = 0
            tampung2[k] = tampung[k]
        else : 
            panjangumur[k] = panjangumur[k] + 1
    if i not in tampung :
        fault+= 1
        if None in tampung :
            print(str(i)+ ' BELUM ada di memory dan MASIH ada frame yang kosong, maka : ')
            print(str(i) + ' --> fault , memory = ',end='')  
            for j in range(kapasitas) : 
                if tampung[j] == None : 
                    tampung[j] = i
                    print(tampung,end=' ')
                    print(', bit reference = ',bitref,'\n')
                    break
        else :
            print(str(i)+ ' BELUM ada di memory dan TIDAK ada frame yang kosong, maka : ') 
            tua = 0
            for l in range(kapasitas) : 
                if l == 0 : 
                    tua = panjangumur[l]
                else : 
                    if panjangumur[l] > tua : 
                        tua = panjangumur[l]
            indekstertua = panjangumur.index(tua)
            if bitref[indekstertua] == 0 : 
                tampung[indekstertua] = i
            else : 
                counter = 1
                while True : 
                    simpan3 = tua - counter
                    if simpan3 in panjangumur : 
                        indextua1 = panjangumur.index(simpan3)
                        tua1 = panjangumur[indextua1]
                        break
                    counter+=1
                for t in range(kapasitas) : 
                    if panjangumur[t] == tua1 : 
                        simpan2 = panjangumur[t]
                        indekstertua1 = panjangumur.index(simpan2)
                        tampung[indekstertua1] = i
                        bitref[indekstertua] = 0 
                        break
            print(str(i) + ' --> fault , memory = ',end='')
            print(tampung,end=' ')
            print(', bit reference = ',bitref,'\n')
    else :
        print(str(i)+ ' SUDAH ada di memory, maka : ')
        hit += 1
        ambilindex = tampung.index(i)
        bitref[ambilindex] = 1
        print(str(i) + ' --> hit , memory = ',end='')
        print(tampung,end=' ')
        print(', bit reference = ',bitref,'\n')
        pass
print('Memory Final = ' + str(tampung))
print('Hit Rate = ' + str(hit/(fault+hit)*100)+'%')
print('Fault Rate = ' + str(fault/(fault+hit)*100)+'%')
#Contoh test case 5,4,2,5,3,1,4,4,6,7,1,2 (3 frame) harusnya 7 1 2
#Contoh test case 2,3,2,1,5,2,4,5,3,2,5,2 (3 frame) harusnya 3 5 2