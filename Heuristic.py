
#from asyncio.windows_events import NULL


#KT = 1
#L = []
#C = []
#SoDinh = int(input("Nhap so dinh cua do thi: "))
#M =[0]*SoDinh
#for i in range (SoDinh):
#    M[i] = [0]*SoDinh
#for i in range (SoDinh):
#    for j in range(SoDinh):
#        if(i == j):
#            M[i][j] = 2
#        else:
#            M[i][j] = int(input("Nhap gia tri M["+str(i)+"]["+str(j)+"]:"))
#for i in range(SoDinh):
#    for j in range(SoDinh):
#        print(M[i][j], end=" ")
#    print("\n")
#dis={
#    1:12,
#    2:3,
#    3:8,
#    4:9,
#    5:4,
#    6:0,
#    7:12
#    }
#DinhXuatPhat = int(input("Dinh xuat phat: "))
#L.append(DinhXuatPhat)
#DinhKetThuc = int(input("Dinh ket thuc: "))
#while(KT==1):
#    DinhDangXet=L.pop(0)
#    if (L==NULL):
#        print("Tim kiem that bai")
#    if(DinhXuatPhat==DinhKetThuc):
#        print("Da tim duoc dich")
#    else:
#        for i in range(SoDinh):
#            if(M[i][DinhDangXet]==1):
#                print(i,end='<--')
#                DinhDangXet=i
#            if(int(dis.get(DinhDangXet))<int(dis.get(i))):
def LeoDoi(mang, h, start, end):
    L = []
    C = []
    path = []
    L.append(start)
    while L:
        DiemDangXet = L.pop(0)
        C.append(DiemDangXet)
        LS = {}
        if DiemDangXet != end:
            for Diem in range(len(mang)):
                if mang[DiemDangXet][Diem] == 1 and Diem not in L and Diem not in C:
                    LS[Diem] = h[Diem]
                    mang[DiemDangXet][Diem] = 2
            v = sorted(LS, key=lambda x: LS[x])
            L = v + L
        else:
            f = end
            path.append(f)
            while f != start:
               for i in range(len(mang)):
                    if mang[i][f] == 2:
                       f = i
                       path.append(f)
                    if f == start:
                        return path[::-1]
    return None

def bestFS(mang, h, start, end):
    L = []
    LS = {}
    C = []
    path = []
    L.append(start)
    LS[start] = 0
    while L:
        DiemDangXet = L.pop(0)
        del LS[DiemDangXet]
        C.append(DiemDangXet)
        if DiemDangXet != end:
            for Diem in range(len(mang)):
                if mang[DiemDangXet][Diem] == 1 and Diem not in L and Diem not in C:
                    LS[Diem] = h[Diem]
                    L = sorted(LS, key=lambda x: LS[x])
                    mang[DiemDangXet][Diem] = 2
        else:
            f = end
            path.append(f)
            while f != start:
               for i in range(len(mang)):
                    if mang[i][f] == 2:
                       f = i
                       path.append(f)
                    if f == start:
                        return path[::-1]
    return None
# mang = [[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 1, 0 ,0 ,1],
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# h = {0: 20, 1: 0, 2: 15, 3: 6, 4: 7, 5: 10, 6: 5, 7: 3, 8: 8, 9: 12}

mang = [[0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,0]]
h = {0:20, 1:8, 2:37, 3:9, 4:5, 5:0, 6:12, 7:4}

start = int(input('Nhập đỉnh bắt đầu: '))
end = int(input('Nhập đỉnh kết thúc: '))

KetQua = bestFS(mang, h, start, end)

if KetQua:
    print(f'Đường đi từ {start} đến {end} là {KetQua}')
else:
    print('Không tìm thấy đường đi')

mang = [[0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0,0]]
h = {0:20, 1:8, 2:37, 3:9, 4:5, 5:0, 6:12, 7:4}
KetQua= LeoDoi(mang,h,start,end)
if KetQua:
    print(f'Đường đi từ {start} đến {end} là {KetQua}')
else:
    print('Không tìm thấy đường đi')

