# -*- coding: utf-8 -*-
from json import encoder
from typing import Dict
from dice import str_trains
import json
import os

def search(name:str,char_type:str)->Dict:   #從資料庫尋找資料
    if char_type == 'Monster' :
        if os.path.isfile('Monster.json') :
            with open('Monster.json',encoding='utf-8') as jsonfile :
                data = json.load(jsonfile)
        else :
            raise Exception('沒有'+char_type+'資料')
    for i in data :
        if i['name'] == name :
            return i
    raise Exception('查無資料')

def read(char_data:Dict) -> object: #讀取資料類別，回傳該資料類別的物件
    if char_data['type'] == 'Monster' :
        tmp = Monster(
            char_data['name'] ,
            char_data['ability'] ,
            char_data['life'] ,
            char_data['DB'] ,
            char_data['build'] ,
            char_data['mp'] ,
            char_data['mov'] ,
            char_data['attack times'] ,
            char_data['armor'] ,
            char_data['skill'] ,
            char_data['san loss'] ,
            char_data['remarks']
        )
        return tmp






class Monster :
    def __init__(self,name:str,ability:Dict,life:int,db:str,build:int,mp:int,mov:Dict,attack_times:int,armor:int,skill:Dict,san_loss:Dict,remarks:Dict={}) -> None:
        self.name = name
        self.type = 'Monster'
        self.ability = {
            'STR':ability['STR'],
            'CON':ability['CON'],
            'SIZ':ability['SIZ'],
            'DEX':ability['DEX'],
            'INT':ability['INT'],
            'POW':ability['POW']
            }
        self.life = life
        self.DB = db
        self.build = build
        self.mp = mp
        self.mov = mov
        self.attack_times = attack_times
        self.armor = armor  
        self.skill = skill
        self.san_loss = san_loss
        self.remarks = remarks

    def save(self)->None :
        if os.path.isfile('Monster.json') :
            with open('Monster.json',encoding='utf-8') as jsonfile :
                data = json.load(jsonfile)
            if data == '' :
                data = []
        else :
            data = []
        for i in data :
            if i['name'] == self.name :
                raise Exception('已有相同資料 : ' + str(i))
        with open('Monster.json','w',encoding='utf-8') as jsonfile :
            data.append(self.dict_trans())
            json.dump(data,jsonfile)
        return

    def dict_trans(self)->Dict :
        tmp_dict = {
            'name' : self.name,
            'type' : self.type,
            'ability' : self.ability,
            'life' : self.life,
            'DB' : self.DB,
            'build' : self.build,
            'mp' : self.mp,
            'mov' : self.mov,
            'attack times' : self.attack_times,
            'armor' : self.armor,
            'skill' : self.skill,
            'san loss' : self.san_loss,
            'remarks' : self.remarks
        }
        return tmp_dict

    def create_char(self,new_name:str) -> Dict :
        char = {
            'name' : new_name,
            'type' : self.type,
            'ability' : {},
            'life' : self.life,
            'DB' : self.DB,
            'build' : self.build,
            'mp' : self.mp,
            'mov' : self.mov,
            'attack times' : self.attack_times,
            'armor' : self.armor,
            'skill' : self.skill,
            'san loss' : self.san_loss,
            'remarks' : self.remarks
        }

        for i in self.ability :
            char['ability'][i] = str_trains(self.ability[i])['result']
        return  char

a = Monster('人類',{'STR':'3D6*5','CON':'3D6*5','SIZ':'3D6*5','DEX':'3D6*5','INT':'3D6*5','POW':'3D6*5'},15,'1D4+2',2,5,{'行走':8},1,0,{'手槍':40},{})
#a.save()
b = search('人類','Monster')

print(b)

c = read(b)

print(c.ability)

print(json.dumps(c.create_char('怪人'),indent=4,ensure_ascii=False))

