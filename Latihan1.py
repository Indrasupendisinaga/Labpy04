print ("------------------")
print ("Pertemuan ke 9")
print ("Latihan 1")
print ("------------------")

a = [10, 20, 30, 40, 50]

# gabungkan list B dengan list A

print (a)
print ("element ke empat = ", a[3])
print ("----------------------------")
print ("nilai element ke dua dan ke empat = ", a[2:4])
print ("----------------------------")
print ("ambil element terakhir = ",a[-1])
print ("----------------------------")

odd = a
odd [3] = 400
print ("ubah elemen ke empat =",odd) # ubah element ke empat dengan nilai nilainya
print ("----------------------------")

odd [1 : 5] = [200, 300, 400 ]
print ("ubah element ke empat dst = ", odd) # ubah element ke empat sampai seterusnya
print ("----------------------------")

odd [1 : 5] = (20, 30, 40, 50) # ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
print (odd)

odd = a
odd.append (60) # tambah list B dengan nilai string
print (odd)

odd.extend([70,80,90]) # tambah list B dengan 3 nilai
print (odd)

odd = [10,20,30,40,50,60]
odd.append(70)
print(odd)





