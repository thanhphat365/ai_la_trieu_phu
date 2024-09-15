import random

BO_CAU_HOI_FILE_NAME = 'bo_cau_hoi.txt'
CAU_TRA_LOI_FILE_NAME = 'cau_tra_loi.txt'
PHAN_THUONG_FILE_NAME = 'giai_thuong.txt'

with open(BO_CAU_HOI_FILE_NAME, 'r', encoding='utf-8') as f:
    BO_CAU_HOI_LIST = [line.strip() for line in f.readlines()]
with open(CAU_TRA_LOI_FILE_NAME, 'r', encoding='utf-8') as f:
    CAU_TRA_LOI_LIST = [line.strip() for line in f.readlines()]
with open(PHAN_THUONG_FILE_NAME, 'r', encoding='utf-8') as f:
    PHAN_THUONG_LIST = [line.strip() for line in f.readlines()]
    
def quyen_tro_giup_50_50(VI_TRI_CAU_HOI):
    dap_an_1 = CAU_TRA_LOI_LIST[VI_TRI_CAU_HOI]
    dap_an_2 = chr(random.randint(65, 68))
    while dap_an_2.lower() == dap_an_1.lower():
        dap_an_2 = chr(random.randint(65, 68))

    dap_an_list = [dap_an_1, dap_an_2]
    dap_an_1_display = random.randint(0, 1)
    dap_an_2_display = 1 - dap_an_1_display
    print(f"Hai lựa chọn còn lại: {dap_an_list[dap_an_1_display]} --- {dap_an_list[dap_an_2_display]}")
    return

Quyen_Tro_Giup=[1,2]
def ho_tro(quyen_tro_giup_list):
    "Bạn đang có nhưng quyền trợ giúp sau : "
    options = []
    if 1 in quyen_tro_giup_list:
        options.append('1.50/50')
    if 2 in quyen_tro_giup_list:
        options.append('2.Khao sat truong quay')
    options.append('3.Khong can tro giup')
    print("Ban co can quyen tro giup :")
    for option in options:
        print(option)
    return options
SO_THU_TU = 0
CAU_HOI_DA_RA = []

while SO_THU_TU < len(PHAN_THUONG_LIST):
    VI_TRI = random.randint(0, len(BO_CAU_HOI_LIST) - 1)
    while VI_TRI in CAU_HOI_DA_RA:
        VI_TRI = random.randint(0, len(BO_CAU_HOI_LIST) - 1)
    print(BO_CAU_HOI_LIST[VI_TRI])
    
    if len(Quyen_Tro_Giup)>0:
        options = ho_tro(Quyen_Tro_Giup)
        quyen_tro_giup = int(input("Chọn quyền trợ giúp(1 ,2 hoặc 3) :").strip())
        if quyen_tro_giup ==1 and 1 in Quyen_Tro_Giup :
            print("Bạn đã chọn quyền trợ giúp 50/50.")
            quyen_tro_giup_50_50(VI_TRI)
            Quyen_Tro_Giup.remove(1)
            print("Quyền trợ giúp 50/50 đã được sử dụng.")
        elif quyen_tro_giup == 2 and 2 in Quyen_Tro_Giup:
            print("Bạn đã chọn quyền trợ giúp Khao sat truong quay.")
            Quyen_Tro_Giup.remove(2)
        elif quyen_tro_giup ==3:
            print("Bạn đã không chọn quyền trợ giúp nào.")
    else:
        print("Bạn không còn quyền trợ giúp nào nữa!")
        
    user_answer = input("Nhập câu trả lời của bạn: ")
    if user_answer.strip().upper() == CAU_TRA_LOI_LIST[VI_TRI].strip().upper():
        print(f"Xin chúc mừng, bạn đã trả lời đúng!\n---> Giải thưởng của bạn lúc này là {PHAN_THUONG_LIST[SO_THU_TU]} đồng!!!")
        SO_THU_TU += 1
        if SO_THU_TU == len(PHAN_THUONG_LIST):
            print(f"Chúc mừng bạn đã hoàn thành trò chơi với tổng giải thưởng là {PHAN_THUONG_LIST[SO_THU_TU - 1]} đồng!!!")
            break

        CHOI_TIEP = input("Bạn có muốn tiếp tục? (Yes/No): ").strip().lower()
        if CHOI_TIEP == 'yes':
            CAU_HOI_DA_RA.append(VI_TRI)
        else:
            print(f"Chúc mừng bạn đã hoàn thành trò chơi với tổng giải thưởng là {PHAN_THUONG_LIST[SO_THU_TU - 1]} đồng!!!")
            break
    else:
        if SO_THU_TU == 0:
            print("Rất tiếc, bạn đã trả lời sai câu hỏi đầu tiên! Bạn không nhận được giải thưởng.")
        else:
            print(f"Rất tiếc, bạn đã trả lời sai! Giải thưởng của bạn là {PHAN_THUONG_LIST[0]} đồng.")
        break
