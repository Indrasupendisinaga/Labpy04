print ("------------------")
print ("Pertemuan ke 9")
print ("Tugas praktikum")
print ("------------------")

def perulangan():
    print ("")
nama    = str (input("input Nama            = "))
nim     = str (input("input Nim             = "))
tugas   = str (input("input Nilai  Tugas    = "))
uts     = str (input("input Nilai  UTS      = "))
uas     = str (input("input Nilai  UAS      = "))
akhir   = str (input("input Nilai Akhir     = "))

print("-----------------")


if nama>nim and nama>tugas and nama>uts and nama>uas and nama>akhir:
    if nim>tugas:
        print("Nama     :", nama)
        print("Nim      :", nim)
        print("Tugas    :", tugas)
        print("UTS      :", uts)
        print("UAS      :", uas)
        print("UTS      :", akhir)
    else:
        print("Nama     :", nama)
        print("Tugas    :", tugas)
        print("Nim      :", nim)
        print("UTS      :", uts)
        print("UAS      :", uas)
        print("Akhir    :", akhir)
elif nim>nama   and nim>tugas and nim>uts and nim>uas and nim>akhir:
    if nama>tugas:
        print("Nim      :", nim)
        print("Nama     :", nama)
        print("Tugas    :", tugas)
        print("uts      :", uts)
        print("UAS      :", uas)
        print("AKhir    :", akhir)
    else:
        print ("Nim     :", nim)
        print ("Tugas   :", tugas)
        print ("Nama    :", nama)
        print ("UTS     :", uts)
        print ("UAS     :", uas)
        print ("Akhir   :", akhir)
else :
    if nama>nim and nama>tugas and nama>uts and nama>uas:
        print("Tugas    :", tugas)
        print("Nama     :", nama)
        print("Nim      :", nim)
        print("UTS      :", uts)
        print("UAS      :", uas)
        print("Akhir    :", akhir)
    else:
        print("Tugas    :", tugas)
        print("Nim      :", nim)
        print("Nama     :", nama)
        print("UTS      :", uts)
        print("UAS      :", uas)
        print("Akhir    :", akhir)

print('=====================================================')
data = ['Nama','Nim', 'Nilai Tugas','Nilai UTS', 'Nilai UAS', 'Nilai Akhir']
print(data)
print('=====================================================')