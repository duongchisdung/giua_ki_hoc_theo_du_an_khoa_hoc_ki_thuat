def chuyen_doi_nhiet_do():
    try:
        lua_chon = input("Nhập 1: C sang F, 2: F sang C: ")
        gia_tri = float(input("Nhập giá trị nhiệt độ: "))
        if lua_chon == '1':
            print(f"Kết quả: {gia_tri * 9/5 + 32} °F")
        else:
            print(f"Kết quả: {(gia_tri - 32) * 5/9} °C")
    except ValueError:
        print("Vui lòng chỉ nhập số!")
def chuyen_doi_tien_te():
    try:
        usd = float(input("Nhập số tiền USD: "))
        ty_gia = float(input("Nhập tỷ giá (1 USD = ? VND): "))
        print(f"Số tiền tương ứng: {usd * ty_gia} VND")
    except ValueError:
        print("Dữ liệu nhập vào phải là con số!")
chuyen_doi_nhiet_do()
chuyen_doi_tien_te()