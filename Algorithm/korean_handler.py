# -*- coding: utf-8 -*-
import re
import compare

# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def convert(label, stt):
    split_label_list = list(label)
    split_stt_list = list(stt)
    label_list = list()
    stt_list = list()

    for keyword in split_label_list:
        # 한글 여부 check 후 분리        
        result = list()
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            if char3==0:
                result.append('-')
            else:
                result.append(JONGSUNG_LIST[char3])
        else:
            result.append(keyword)
        
        label_list.append(result)

    for keyword in split_stt_list:
        # 한글 여부 check 후 분리        
        result = list()
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            if char_code < 0 :
                result.append(keyword)
                result.append('-')
                result.append('-')
            else :
                char1 = int(char_code / CHOSUNG)
                result.append(CHOSUNG_LIST[char1])
                char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
                result.append(JUNGSUNG_LIST[char2])
                char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
                if char3==0:
                    result.append('-')
                else:
                    result.append(JONGSUNG_LIST[char3])
        else:
            result.append(keyword)
        
        stt_list.append(result)

    print(label_list)
    print(stt_list)
    compare.compare_string(label_list,stt_list)

# __name__ 변수를 통해 현재 스크립트 파일이 시작점인지 모듈인지 판단
# korean_handler.py 파일은 main 프로그램으로 사용
if __name__ == '__main__':

    label = input("input your label text:")
    stt = input("input your stt text:")
    convert(label, stt)

