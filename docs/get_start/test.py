"""
计算机视觉石头剪刀布

Rock-Paper-Scissor
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import random


def get_winner(human_gesture, computer_gesture):
    """
    # 先描述逻辑
    返回胜利者
        human
        computer
        equal
    """
    # 平局
    if human_gesture == computer_gesture:
        return "equal"
    # 人类获胜
    if (
        (human_gesture == ROCK and computer_gesture == SCISSORS)
        or (human_gesture == SCISSORS and computer_gesture == PAPER)
        or (human_gesture == PAPER and computer_gesture == ROCK)
    ):
        return "human"
    # 其余情况都是电脑获胜
    return "computer"


def guess_human_gesture(finger):
    gesture_fingers_map = {0: ROCK, 5: PAPER, 2: SCISSORS}
    finger_num = finger[0] + finger[1] + finger[2] + finger[3] + finger[4]
    human_gesture = gesture_fingers_map.get(finger_num, None)
    print(f"你出了 {human_gesture} ({finger_num})")
    return human_gesture


def start_judging_and_draw(detector, hands, img):
    x, y = 200, 280
    # 两次游戏之间的间隔
    if hands:
        # 发现有手，就开始倒计时
        # 在此之前决定开始游戏
        if len(hands) == 1:  # 如果只有一只手
            # 识别出手势
            fingers0 = detector.fingersUp(hands[0])
            human_gesture = guess_human_gesture(fingers0)
            if human_gesture:  # 出了有意义的手势
                computer_gesture = random.choice([ROCK, SCISSORS, PAPER])
                if True:  # this_hand != latest_hand:
                    print("计算机出了:", computer_gesture)
                    if computer_gesture == PAPER:
                        pic_p = cv2.imread("p.jpg")
                        pic_p = cv2.resize(pic_p, (x, y))
                        img[0:y, 640 : 640 + x] = pic_p
                    if computer_gesture == SCISSORS:
                        pic_s = cv2.imread("s.jpg")
                        pic_s = cv2.resize(pic_s, (x, y))
                        img[0:y, 640 : 640 + x] = pic_s
                    if computer_gesture == ROCK:
                        pic_r = cv2.imread("r.jpg")
                        pic_r = cv2.resize(pic_r, (x, y))
                        img[0:y, 640 : 640 + x] = pic_r

                    winner = get_winner(human_gesture, computer_gesture)
                    print(f"{winner} 获胜")
                    if winner == "computer":
                        pic_no = cv2.imread("no.jpg")
                        pic_no = cv2.resize(pic_no, (x, y))
                        img[0:y, 1280 - x : 1280] = pic_no
                    if winner == "human":
                        pic_yes = cv2.imread("yes.jpg")
                        pic_yes = cv2.resize(pic_yes, (x, y))
                        img[0:y, 1280 - x : 1280] = pic_yes
                    if winner == "equal":
                        pic_equal = cv2.imread("equal.jpg")
                        pic_equal = cv2.resize(pic_equal, (x, y))
                        img[0:y, 1280 - x : 1280] = pic_equal
                    # latest_hand = this_hand

        elif len(hands) == 2:  # 如果识别出两只手
            pic_h = cv2.imread("heng.jpg")
            pic_h = cv2.resize(pic_h, (x, y))
            img[0:y, 640 - x : 640] = pic_h

        return img

class Timer:
    '''
    游戏计时器
    duration 计时时间
    四舍五入 3.4-0.4 -> 3-0
    '''
    def __init__(self, duration=3.4):
        self.duration = duration
        self.running = False
        self.begin_time = time.time()
        self.judging = False
        self.judging_img = None
        
    def begin(self):
        if not self.running:
            self.running = True
            self.begin_time = time.time()
            self.judging = False
        
    def step(self, img):
        running_duration = time.time()-self.begin_time
        if running_duration > self.duration + 2:  # 缓1秒再开始新一局
            self.running = False
        if self.running and running_duration <= 3.2:
            font_size = 10
            text = str(format(self.duration - running_duration,'.0f'))
            cv2.putText(img, text, (width//2, height//2), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0,0,255), 2, cv2.LINE_AA)

        if self.judging and type(self.judging_img) != type(None):
                img = self.judging_img

        return img, running_duration

ROCK = "ROCK"
SCISSORS = "SCISSORS"
PAPER = "PAPER"
cap = cv2.VideoCapture(0)  # 调用默认电脑摄像头
width = 1280
height = 960
cap.set(3, width)
cap.set(4, height)
latest_game_time = time.time()
detector = HandDetector()
game_timer = Timer()

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=True)  # 手势识别
    if hands:
        # 倒计时3秒开始判定
        game_timer.begin()
        # cv.putText(img, text,(width//2, height//2), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2,cv2.LINE_AA)
    img, running_duration = game_timer.step(img)
    # if running_duration > 
    # 满足某种条件判断一次
    if running_duration > game_timer.duration and not game_timer.judging:  # 0 出现之后的0.2秒 
            game_timer.judging_img = start_judging_and_draw(detector, hands, img)
            # 本轮已经判断过一次了
            game_timer.judging = True
    cv2.imshow("video", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break  # 退出
    if key == ord("v"):
        cv2.imwrite("hands.png", img)  # 拍照

cap.release()
cv2.destroyAllWindows()
