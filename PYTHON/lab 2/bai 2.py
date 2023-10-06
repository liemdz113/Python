# cau 1: Đọc danh sách sinh viên từ tập tin (txt/csv)
file = open("DSSV.txt", "r", encoding="utf8")
read = file.readlines()

listSv = []
sv = []
def XuatDssv(sv):
    for i in read:
        if i not in listSv:
            listSv.append(i.strip())
            for i in listSv:
                sv.sort()
                sv += i.split("\t")
XuatDssv(sv)
print(f"Danh sach sinh vien ban dau: {listSv}")
listSv.sort()
print(f"Danh sach sinh vien sau khi sap xep giam dan theo ten: {listSv}")
listSv.reverse()
print(f"Danh sach sinh vien sau khi sap xep tang dan theo ten: {listSv}")