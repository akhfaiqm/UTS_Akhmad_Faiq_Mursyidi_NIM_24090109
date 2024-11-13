
for i in range():
    inputanBb = int(input("Masukan Berat Badan (kg):"))
    inputanTb = int(input("Masukan Tinggi Badan (cm):"))

hasiltimbang = inputanBb /inputanTb**2

if hasiltimbang < 18.5:
        print('Berat badan kurang : ')

elif 18.5 <= hasiltimbang < 24.9:       
        print('berat badan normal :')
        
elif 25 <= hasiltimbang <29.9 :
    print (' berat badan kelebihan :')