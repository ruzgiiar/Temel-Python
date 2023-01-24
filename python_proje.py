
## 1. Soru ##

''' Bir listeyi düzleştiren (flatten) fonksiyon yazin.
Elemanlari birden çok katmanli listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5] '''

l = [1,'a',['cat'],2,[[[3]],'dog'],4,5]

new_l = []

def regular(x):
    for i in x:
        if isinstance(i,list):
            regular(i)
        else:
            new_l.append(i)

regular(l)
print(new_l)

## 2. Soru ##

''' Verilen listenin içindeki elemanlari tersine döndüren bir fonksiyon yazin. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onlarin elemanlarini da tersine döndürün. 
Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]] '''
            
l1 = [[1,2],[3,4],[5,6,7]]


def invers(z):
    z = z[::-1]
    z = [i[::-1] for i in z] 
    return z

print(invers(l1))








