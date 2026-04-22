def chuan_hoa_ten(ho_ten):
    return " ".join(ho_ten.strip().split()).title()
def sap_xep_theo_ten(danh_sach):
    danh_sach.sort(key=lambda x: x.split()[-1])
    return danh_sach
n = int(input("Nhập số lượng khách hàng: "))
khach_hang = []
for i in range(n):
    ten = input(f"Nhập họ tên khách hàng thứ {i+1}: ")
    khach_hang.append(ten)

chuan_hoa = [chuan_hoa_ten(name) for name in khach_hang]
ket_qua = sap_xep_theo_ten(chuan_hoa)

print("\nKết quả cuối cùng: ")
for h in ket_qua:
    print(f"- {h}")