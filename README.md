# 2022_opensource

오픈소스 프로젝트 제안서 공개를 위한 깃허브입니다.

* 실습 내용:
- Github 페이지 생성, public으로 전체 공개 (5점)
- Github 페이지의 라이선스 형태 명시 (2점)
- 폴더 생성: src/  --> 폴더 안에 프로그래밍 파일 1개 이상 업로드 (2점)
- 폴더 생성: doc/ --> 폴더 안에 프로젝트 제안서 업로드 (2점) 
- 파일 수정: src/ --> 폴더 안에 파일 내용 수정 commit & push 1회 이상 (2점)
- Github 페이지의 README.md 생성 (2점)
- Github 페이지의 README.md 편 --> 5개 이상의 문법 요소 활용 (5점)
   e.g. 내용 작성, 문서 제목, 항목 열거, 문단 강조/나눔, 폰트 크기/스타일 변경, 링크 삽입 등

* 제출 방법 & 기한
- 게시글 제목 (비밀글) : "[제안] 학번, 이름"으로 게시글 작성. 과제 #1과 함께 제출
- 제출 기한: 10월 14일 (금요일) ~23:59
- 파일 제출: 제안서 양식(참고).docx를 주제(학번,이름).docx으로 파일 이름 변경 후 Git에 업로드. --> 개별 Git 링크 공개 + 파일을 게시글에 유첨하여 업로드.







다음은 개별제안서에 있는 아이디어 관련 코드로, Google Cloud Speech API의 오픈소스를 활용하였습니다.

'''python

from tkinter import *
from pynput.keyboard import Controller
import os
import threading
import speech_recognition as sr

#프로그램 이름 출력하기
print("============= Callin' ============")

#파일 불러오기
file = open('voice.txt', 'r', encoding='utf-8')
voice_word = file.readlines()
file.close
voice_word = [line.rstrip('\n') for line in voice_word]

#메뉴 선택 출력하기
while True:
    print("< 메뉴를 선택해주세요 >")
    print("1. 단어 리스트 추가")
    print("2. 음성 인식 시작")
    print("3. 단어 리스트 수정 ")
    print("4. 단어 리스트 확인")
    menu = input("메뉴의 번호 입력: ")

#메뉴1 단어입력 및 텍스트 파일 누적
    if menu == "1":
        print("----------------------------------")
        word = input("단어를 입력해주세요: ")
        with open('voice.txt', 'a', encoding='utf-8') as v:
            v.write(word + '\n')
            v.close()
        voice_word.append(word)
        print("----------------------------------")
        continue

#메뉴2 음성 인식 시작
    if menu == "2":
        print("----------------------------------")
        break

#메뉴3 단어 수정
    if menu == "3":
        print("----------------------------------")
        print("== 현재 입력된 단어 리스트 ==")
        print(voice_word)
        rem_word = input("삭제할 단어를 입력해주세요: ")
        voice_word.remove(rem_word)
        print("----------------------------------")
        #텍스트 파일 변경 -> 파일의 단어 삭제에 있어 오류 발생
        #with open("voice.txt", 'r', encoding='utf-8') as f:
        #    lines = f.readlines()
        #with open("voice.txt", 'w', encoding='utf-8') as f:
        #    f.truncate(rem_word)
        #continue
        
#메뉴4 입력된 단어 리스트 출력
    if menu == "4":
        print("----------------------------------")
        print(voice_word)
    
#음성 인식 실행(오픈소스 활용)
class voiceloop(threading.Thread):
    
    mykeyboard = Controller()

    def run(self) -> None:
        
        while True:
            voice = self.CollectVoice()

            if voice != False and myThread.rflag == True:
                print(voice)
                self.Pasting(voice)
            
            if myThread.rflag == False:
                break
    
    def Pasting(self, myvoice):
        for character in myvoice:
            self.mykeyboard.type(character)
        self.mykeyboard.type(" ")
    
    def CollectVoice(self):
        #get microphone device on notebook or desk top
        listener = sr.Recognizer()
        voice_data = ""
        
        with sr.Microphone() as raw_voice:
            
            try:
                img_frm.config(image=mic3_img)
                print("----------------------------------")
                print("준비중입니다...")
                listener.adjust_for_ambient_noise(raw_voice)
                
                #adjust setting values
                listener.dynamic_energy_adjustment_damping=0.2
                listener.pause_threshold = 0.6
                listener.energy_threshold = 600
                
                img_frm.config(image=mic1_img)
                
                print("소리를 감지중입니다...")
                audio = listener.listen(raw_voice)
                
                img_frm.config(image=mic2_img)
                
                voice_data = listener.recognize_google(audio, language='ko')
                
                #입력한 단어와 음성의 일치를 확인
                for i in voice_word:
                    if voice_data != i:
                        pass
                    else:
                        print("== 입력한 단어가 감지되었습니다. ==")
                        print("== 감지된 단어는 다음과 같습니다. ==")

            except UnboundLocalError:
                pass
            
            except sr.UnknownValueError:
                print("음성이 인식되지 못했습니다.")
                print("----------------------------------")
                return False
            
            return str(voice_data)
    
            
            
    
#프로그램 종료
def on_closing():
    myThread.rflag=False
    print("====== Callin'이 종료되었습니다. ======")
    #myThread.join()
    os._exit(1)
   
#GUI 설정 
root = Tk()
root.title("Callin'")
root.geometry("300x600+50+50")
    
mic1_img = PhotoImage(file="mic1.png")
mic2_img = PhotoImage(file="mic2.png")
mic3_img = PhotoImage(file="mic3.png")
    
img_frm = Label(root, image=mic2_img)
img_frm.pack();

myThread = voiceloop()
myThread.rflag = True
myThread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.wm_attributes("-topmost",1)
root.mainloop()
'''
