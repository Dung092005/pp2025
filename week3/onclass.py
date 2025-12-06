def test1():
    while True:
        line = input("input here: ")
        if line == 'done':
            break
        print("in nốt dòng này")
    print("done")


# mày có thể thấy, break là break cái for or while cái hàm to nhất ấy, còn cái if chỉ là chỗ chứa break mà thôi 
def test2():
    while True: 
        line = input('> ')
        if line[0] == "#":
            continue
            print("thu 1")
        print("thử xem có in đc ko ")
        if line == 'done': 
            break
        print("thử break xem in đc ko ")
    print("done")


# Ở LẦN THỬ NÀY KHI # THÌ MÀY THẤY NÓ VẪN TIẾP TỤC RA CHỖ NHẬP INPUT CHỨ KO IN RA "THỬ XEM CO IN DC KO" ĐIỀU NÀY chứng tỏ 
# continue nó ko chỉ skip cái if, mà nó skip cả 1 lần interation, tức là skip hết lượt đó, chạy từ đầu 

a =  range(5)
print(a)