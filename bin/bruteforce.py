import time

#membaca file dan menyimpan ke array
with open('file.txt') as f:
    lines = f.read().splitlines()
array_kata = []
for line in lines:
    if (line[0] == '+'):
        array_kata.append(line[1:])
    elif (line[-1] == '+'):
        array_kata.append(line[:-1])
    elif (line[0] == '-'):
        continue
    else:
        array_kata.append(line)

for line in lines:
    print(line)

start = time.time()

#inisialisasi dictionary
hurufDictionary =  {}
hurufArray = []

#fungsi yang mereturn true jika penjumlahan 2 operan = hasilnya
def isJumlahBenar(array):
    jumlah = 0
    hasil = 0
    for i in range(len(array) - 1):
        for j in range(len(array[i])):
            jumlah += hurufDictionary[array[i][j]] * (10**(len(array[i]) - 1 - j))
    for k in range(len(array[-1])):
        hasil += hurufDictionary[array[-1][k]] * (10**(len(array[-1]) - 1 - k))
    
    if (jumlah == hasil):
        return True
    else:
        return False

#inisialisasi huruf yang ada dalam operan
for kata in array_kata:
    for i in range(len(kata)):
        if(i == 0):
            if (not (kata[i] in hurufDictionary)):
                hurufDictionary[kata[i]] = 99
                hurufArray.insert(0,kata[i])
        else:
            if (not (kata[i] in hurufDictionary)):
                hurufDictionary[kata[i]] = 99
                hurufArray.append(kata[i])
for i in range(9):
    hurufArray.append('zz')

#fungsi cryptarithmetic
def crypto():
    count = 0
    for a in range(1,10):
        hurufDictionary[hurufArray[0]] = a
        for b in range(1,10):
            if(b == a):
                continue
            else:
                hurufDictionary[hurufArray[1]] = b
                for c in range(10):
                    if (c == b or c == a):
                        continue
                    else:
                        hurufDictionary[hurufArray[2]] = c
                        for d in range(10):
                            if (d == c or d == b or d == a):
                                continue
                            else:
                                hurufDictionary[hurufArray[3]] = d
                                for e in range(10):
                                    if (e == d or e == c or e == b or e == a):
                                        continue
                                    else:
                                        hurufDictionary[hurufArray[4]] = e
                                        for f in range(10):
                                            if (f == e or f == d or f == c or f == b or f == a):
                                                continue
                                            else:
                                                hurufDictionary[hurufArray[5]] = f
                                                for g in range(10):
                                                    if (g == f or g == e or g == d or g == c or g == b or g == a):
                                                        continue
                                                    else:
                                                        hurufDictionary[hurufArray[6]] = g
                                                        for h in range(10):
                                                            if (h == g or h == f or h == e or h == d or h == c or h == b or h == a):
                                                                continue
                                                            else:
                                                                hurufDictionary[hurufArray[7]] = h
                                                                for i in range(10):
                                                                    if (i == h or i == g or i == f or i == e or i == d or i == c or i == b or i == a):
                                                                        continue
                                                                    else:
                                                                        hurufDictionary[hurufArray[8]] = i
                                                                        for j in range(10):
                                                                            if (j == i or j == h or j == g or j == f or j == e or j == d or j == c or j == b or j == a):
                                                                                continue
                                                                            else:
                                                                                hurufDictionary[hurufArray[9]] = j
                                                                                count += 1
                                                                                if (isJumlahBenar(array_kata)):
                                                                                    return count


percobaan = crypto()
for i in range(len(array_kata) - 1):
    for j in range(len(array_kata[i])):
        print(str(hurufDictionary[array_kata[i][j]]),end ="")
    print("")
print('-------- +')
for k in array_kata[-1]:
    print(str(hurufDictionary[k]),end ="")

end = time.time()
print("\n\nJumlah percobaan: " + str(percobaan))
print("Waktu : " + str(end - start))

