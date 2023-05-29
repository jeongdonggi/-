import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

Path = '../data/'
Name = 'RGBColors.JPG'
FullName = Path + Name

image = cv.imread(FullName)     # read as 3 channel. default.
assert image is not None, f"No image file: [{FullName}]....!"  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

imgRGB = image[..., ::-1]   # = image[:, :, ::-1]. 같은 표현
plt.ion()       # interactive mode로 설정

plt.figure(num='Report1: Original image & its processed images')
plt.suptitle("Report1: Original image & its processed images", fontsize=10, fontweight='bold')
plt.waitforbuttonpress() # 사용자가 입력학면 true

# 1) 서브 화면 1 - 원본 컬러 영상, title="Original Color Image"
plt.subplot(221) #row = 2, col = 2, index = 1 (1,1 위치)
plt.imshow(imgRGB) # 위에서 변환해준 이미지를 보여준다.
plt.axis('off')             # plt.xticks([]), plt.yticks([]) 축과 라벨 끄기
plt.title('Original Color Image')
plt.waitforbuttonpress()        # 키 혹은 버튼 입력을 기다린다.

# 2) 서브 화면 2 - 모노 영상, title="Mono Image"
plt.subplot(222)
imgM = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    # 3채널 영상을 1채널 gray로 변환
plt.imshow(imgM, cmap='gray') #단일 채널 이미지를 gray 색상 채널에 매핑해준다.
plt.axis('off')             # plt.xticks([]), plt.yticks([]) 축과 라벨 끄기
plt.title("Mono Image")
plt.waitforbuttonpress()        # 키 혹은 버튼 입력을 기다린다.

# 3) 서브 화면 3 - 원본 컬러 영상에서 각 컬러 채널에  1.5를 곱하여 밝게 만든 영상, title="Original * 1.5"
imgF = imgRGB/255       # RGB 원본영상의 정규화 영상을 만든다. 0~1 범위의 부동소수 영상이다.
imgShow = imgF * 1.5
plt.subplot(223)
# [0, 1] 범위를 넘어서서는 값들은 imshow() 함수 내부에서 모두 truncation 다른 말로는 clip 동작이 일어난 후 화면에 출력된다.
# clip 동작: 0보다 작으면 0, 1보다 더 크면 1으로 변환되고, 그 사이의 값들은 그대로 유지된다.
plt.imshow(imgShow) # 위에서 변환해준 이미지를 보여준다.
plt.axis('off')             # plt.xticks([]), plt.yticks([]) 축과 라벨 끄기
plt.title('Original * 1.5')
plt.waitforbuttonpress()        # 키 혹은 버튼 입력을 기다린다.


# 4) 서브 화면 4 - 원본 컬러 영상에서 R 컬러 채널만  2로 곱하여 Red 색상만 높게 반영한 영상, title="Original[..., 0] * 2"
imgF = imgRGB/255       # RGB 원본영상의 정규화 영상을 만든다. 0~1 범위의 부동소수 영상이다.
imgF[..., 0] = imgF[..., 0] * 2
plt.subplot(224)
plt.imshow(imgF) # 위에서 변환해준 이미지를 보여준다.
plt.axis('off')             # plt.xticks([]), plt.yticks([]) 축과 라벨 끄기
plt.title('Original[..., 0] * 2')
plt.waitforbuttonpress()        # 키 혹은 버튼 입력을 기다린다.