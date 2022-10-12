from tkinter import *
from pynput.keyboard import Controller
import os
import threading
import speech_recognition as sr

#프로그램 이름 출력
print("============= Callin' ============")

#파일 불러오기
file = open('voice.txt', 'r', encoding='utf-8')
voice_word = file.readlines()
file.close
voice_word = [line.rstrip('\n') for line in voice_word]

#메뉴 선택 출력
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
