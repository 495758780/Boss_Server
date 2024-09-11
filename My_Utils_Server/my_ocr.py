from cnocr import CnOcr
import numpy as np
ocr = CnOcr()
import time

def ocr_getResult(ocr, img_list):
    t1 = time.time()
    # 将列表转换为 NumPy 数组
    img_array = np.array(img_list)
    # 使用 cnocr 进行 OCR 识别
    ocr_result = ocr.ocr(img_array)
    print(ocr_result)
    print(f'耗时：{time.time()-t1}')
    return ocr_result