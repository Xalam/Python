hour = int(input("JAM : "))
minu = int(input("MENIT : "))
dura = int(input("DURASI MENIT : "))

cari_jam = (dura + minu) // 60
menit = (dura+minu)%60

jam = (hour+cari_jam)%24
print(jam)
print(menit)
print(jam, ":", menit)
