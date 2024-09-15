import random

BO_CAU_HOI_FILE_NAME = 'bo_cau_hoi.txt'
CAU_TRA_LOI_FILE_NAME = 'cau_tra_loi.txt'
GIAI_THUONG_FILE_NAME = "giai_thuong.txt"
FIFTY_FIFTY_FILE_NAME = "fifty_fifty.txt"
# Load dữ liệu câu hỏi, câu trả lời và giải thưởng từ file
with open(BO_CAU_HOI_FILE_NAME, "r", encoding='utf-8') as f:
    BO_CAU_HOI_LIST = [line.strip() for line in f.readlines()]

with open(CAU_TRA_LOI_FILE_NAME, "r", encoding='utf-8') as f:
    CAU_TRA_LOI_LIST = [line.strip() for line in f.readlines()]

with open(GIAI_THUONG_FILE_NAME, "r", encoding='utf-8') as f:
    GIAI_THUONG_LIST = [line.strip() for line in f.readlines()]
with open (FIFTY_FIFTY_FILE_NAME,"r",encoding = "utf-8")as f:
        FIFTY_FIFTY_LIST=[line.strip() for line in f.readlines()]
SO_THU_TU = 0
CAU_HOI_DA_RA = []
QUYEN_TRO_GIUP = [1, 2]  # Quyền trợ giúp có sẵn

# Hàm xử lý quyền trợ giúp 50/50
def quyen_tro_giup_50_50(VI_TRI_CAU_HOI):
    return FIFTY_FIFTY_LIST[VI_TRI_CAU_HOI]
    
def hien_thi_quyen_tro_giup(quyen_tro_giup_list):
    """Hiển thị các quyền trợ giúp có sẵn."""
    options = []
    if 1 in quyen_tro_giup_list:
        options.append("1. 50/50")
    if 2 in quyen_tro_giup_list:
        options.append("2. Khảo sát khán giả từ trường quay")
    options.append("3. Không cần trợ giúp")
    
    print("Bạn có muốn nhận quyền trợ giúp dưới đây:")
    for option in options:
        print(option)
    return options

# Vòng lặp chính của trò chơi
while SO_THU_TU < len(GIAI_THUONG_LIST):
    VI_TRI = random.randint(0, len(BO_CAU_HOI_LIST) - 1)
    while VI_TRI in CAU_HOI_DA_RA:
        VI_TRI = random.randint(0, len(BO_CAU_HOI_LIST) - 1)

    # Hiển thị câu hỏi
    print(BO_CAU_HOI_LIST[VI_TRI])
    
    if len(QUYEN_TRO_GIUP) > 0:
        options = hien_thi_quyen_tro_giup(QUYEN_TRO_GIUP)
        try:
            quyen_tro_giup = int(input("Chọn quyền trợ giúp (1, 2, hoặc 3): ").strip())
            if quyen_tro_giup == 1 and 1 in QUYEN_TRO_GIUP:
                print("Bạn đã chọn quyền trợ giúp 50/50.")
                print(quyen_tro_giup_50_50(VI_TRI))
                QUYEN_TRO_GIUP.remove(1)
            elif quyen_tro_giup == 2 and 2 in QUYEN_TRO_GIUP:
                print("Bạn đã chọn quyền trợ giúp khảo sát khán giả.")
                QUYEN_TRO_GIUP.remove(2)
            elif quyen_tro_giup == 3:
                print("Bạn đã không chọn quyền trợ giúp nào.")
            else:
                print("Lựa chọn không hợp lệ hoặc quyền trợ giúp đã được sử dụng.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    else:
        print("Bạn không còn quyền trợ giúp nào nữa!")


    user_answer = input("Mời bạn nhập câu trả lời: ").strip().lower()

    if user_answer == CAU_TRA_LOI_LIST[VI_TRI].strip().lower():
        print(f"Chúc mừng bạn đã trả lời đúng.\n-----> Giải thưởng của bạn là: {GIAI_THUONG_LIST[SO_THU_TU]} ĐỒNG")
        SO_THU_TU += 1

        if SO_THU_TU == len(GIAI_THUONG_LIST):
            print(f"Cảm ơn bạn đã chơi trò chơi. Tổng giải thưởng bạn nhận được là {GIAI_THUONG_LIST[SO_THU_TU - 1]} ĐỒNG")
            break

        CHOI_TIEP = input("Bạn có muốn tiếp tục? (yes/no): ").strip().lower()
        if CHOI_TIEP == "yes":
            CAU_HOI_DA_RA.append(VI_TRI)
        else:
            print(f"Cảm ơn bạn đã chơi trò chơi. Tổng giải thưởng của bạn là: {GIAI_THUONG_LIST[SO_THU_TU - 1]} ĐỒNG")
            break
    else:
        if SO_THU_TU == 0:
            print("Rất tiếc, bạn đã trả lời sai câu đầu tiên và không nhận được giải thưởng.")
        else:
            print(f"Rất tiếc, bạn đã trả lời sai. Giải thưởng của bạn là: {GIAI_THUONG_LIST[0]} ĐỒNG")
        break
