def nhap_du_lieu():
    danh_sach = []
    while True:
        ten = input("Nhập tên món hàng (nhấn Enter để dừng): ")
        if ten == '':
            break
        gia = float(input(f"Nhập giá tiền cho {ten}: "))
        danh_sach.append((ten, gia))
    return danh_sach

def xu_ly_va_ghi_file(danh_sach):
    if not danh_sach:
        return
    
    tong_tien = sum(item[1] for item in danh_sach)
    mon_dat_nhat = max(danh_sach, key=lambda x: x[1])

    with open("chi_tieu.txt", "w", encoding="utf-8") as f:
        f.write("DANH SÁCH CHI TIÊU\n")
        for ten, gia in danh_sach:
            f.write(f"{ten}: {gia} VND\n")
        f.write("-" * 20 + "\n")
        f.write(f"Tổng cộng: {tong_tien} VND\n")
        f.write(f"Món đắt nhất: {mon_dat_nhat[0]} ({mon_dat_nhat[1]} VND)")
    print("Đã xuất báo cáo ra file chi_tieu.txt")





ds = nhap_du_lieu()
xu_ly_va_ghi_file(ds)