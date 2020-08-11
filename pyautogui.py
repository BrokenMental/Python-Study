#pyautogui 라이브러리 추가
#pip install pyautogui
import pyautogui #듀얼모니터는 인식 안됨

#마우스 현재 좌표 출력
#pyautogui.position()

#해당 좌표로 마우스 이동
#pyautogui.moveTo(40, 154)

#이미지 추출 라이브러리 추가
#pip install opencv-python

#해당하는 이미지와 유사한 화면이 존재하는 위치로 이동(출력결과 : x축 값, y축 값 , 가로 길이, 세로 길이)
#pyautogui.locateOnScreen('')

#좌표, 저장될 이미지 길이(x축 값, y축 값, 가로 길이, 세로 길이)를 지정하면 해당 좌표를 스크린샷 후 특정 이름으로 저장
pyautogui.screenshot('1.png', region=(1584, 613, 30, 30))

#해당 경로에 존재하는 이미지와 유사한 화면 위치 정가운데로 이동(출력결과 : x축 값 y축 값)
num1 = pyautogui.locateCenterOnScreen('1.png')
num7 = pyautogui.locateCenterOnScreen('7.png')

#마우스 클릭 이벤트(값이 없으면 마우스 현재 위치 클릭)
pyautogui.click(num1)
pyautogui.click(num7)