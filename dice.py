import random
from typing import Dict
import re
from copy import deepcopy as dcp
def roll_the_dice(input_str:str)->Dict: #輸入為 3D6 形式
    num,dice = map(int,input_str.upper().split('D'))
    result_dict = {'num':num,
                    'dice':dice}
    result_list = []
    for _ in range(num) :
        result_list.append(random.randint(0,dice)+1)
    result_dict['result_list'] = result_list
    result_dict['result'] = sum(result_list)
    return  result_dict

def str_trains(input_str:str)->Dict :   #可輸入 ((3D6-29-2D7+36)*9-2d3*1d4)/2
    pattern = re.compile(r'(\d+[d|D]\d+)', re.I)
    dice_list = pattern.findall(input_str)
    input_str = re.sub(r'\d+[d|D]\d+','D', input_str)
    tmp_1 = tmp_2 = dcp(input_str)
    for i in dice_list :
        result_dict = roll_the_dice(i)
        tmp_1 = tmp_1.replace('D',str(result_dict['result_list']),1)
        tmp_2 = tmp_2.replace('D',str(result_dict['result']),1)
    return {'process':tmp_1,'res':tmp_2,'result':eval(tmp_2)}