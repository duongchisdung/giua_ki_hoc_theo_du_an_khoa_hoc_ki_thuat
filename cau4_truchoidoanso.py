import random
def tro_choi_doan_so():
    so_may_chon = random.randint(1, 100)
    so_luot_choi = 7
    thang = False
    print("Máy đã chọn 1 số từ 1-100. Bạn có 7 lượt đoán!")
    for i in range(1, so_luot_choi + 1):
        try:
            doan = int(input(f"Lượt {i} - Nhập số đoán: "))
            if doan == so_may_chon:
                print(f"Chúc mừng! Bạn thắng ở lượt thứ {i}.")
                luu_ky_luc(i)
                thang = True
                break
            elif doan < so_may_chon:
                print("Lớn hơn!")
            else:
                print("Nhỏ hơn!")
            if i == 3:
                goi_y = "chẵn" if so_may_chon % 2 == 0 else "lẻ"
                print(f"Gợi ý: Số cần tìm là số {goi_y}.")
        except ValueError:
            print("Vui lòng nhập số nguyên")

    if not thang:
        print(f"Bạn đã hết lượt. Số đúng là: {so_may_chon}")

def luu_ky_luc(so_lan):
    try:
        with open("kiluc.txt", "r") as f:
            best = int(f.read())
    except:
        best = 999
    
    if so_lan < best:
        with open("kiluc.txt", "w") as f:
            f.write(str(so_lan))
        print("KỶ LỤC MỚI!")

tro_choi_doan_so()