import matplotlib.pyplot as plt

def bao_cao_ban_hang():
    so_luong = {'Laptop': 10, 'Mouse': 50, 'Keyboard': 30}
    bang_gia = {'Laptop': 15000000, 'Mouse': 200000, 'Keyboard': 500000}
    
    doanh_thu_tung_mon = {}
    tong_doanh_thu = 0

    print(" BÁO CÁO DOANH THU")
    for sp, sl in so_luong.items():
        dt = sl * bang_gia[sp]
        doanh_thu_tung_mon[sp] = dt
        tong_doanh_thu += dt
        print(f"{sp}: {dt:,} VND")
    
    print(f"==> Tổng doanh thu: {tong_doanh_thu} VND")

    
    plt.bar(so_luong.keys(), so_luong.values(), color='skyblue')
    plt.xlabel('Sản phẩm')
    plt.ylabel('Số lượng đã bán')
    plt.title('Biểu đồ sản lượng bán ra')
    plt.show()

bao_cao_ban_hang()