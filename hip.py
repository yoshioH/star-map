# -*- coding: utf-8 -*-
import os
import json

def fileIn():
    data = list()
    with open('./data/hip_main.dat') as lines:
        for line in lines:
            datum = line.split('|')
            tmp = {
                'hipNum' : datum[1].strip(),
                'vMag' : datum[5].strip(),
                'raDeg' : datum[8].strip(),
                'decDeg' : datum[9].strip(),
                'bvColor' : datum[37].strip()
            }
            data.append(tmp)
    return data

def filterAndParse(data):
    ret = list()
    for datum in data:
        if len(datum['vMag']) < 1 or float(datum['vMag']) > 3:
            continue
        vMag = float(datum['vMag'])
        raDeg = float(datum['raDeg']) if float(datum['raDeg']) <= 180 else (180 - (float(datum['raDeg']) - 180))* -1
        decDeg = float(datum['decDeg'])
        bvColor = float(datum['bvColor'])

        # D3がGeoJSONの形式で受け取る関係上、赤緯と赤経を配列として格納している
        # Web側でキレイに整形してあげるのがいいんだろうけど、めんどくさいのでここで帳尻を合わせる。
        # TODO D3用のAPIとして提供するスタンスなら、まぁ許容範囲
        tmp = list()
        option = {
            'vMag':vMag,
            'bvColor':bvColor
        }
        tmp.append(-1*raDeg)#地球儀の反対面からみる感じ。反転させる
        tmp.append(decDeg)
        tmp.append(option)
        # tmp = {
        #     'hipNum' : datum['hipNum'],
        #     'vMag' : vMag,
        #     'raDeg' : raDeg,
        #     'decDeg' : decDeg,
        #     'bvColor' : bvColor
        # }
        ret.append(tmp)
    return ret

def jsonFileOut(data):
    with open('./data/hip.json', mode='w') as f:
        f.write('{"data":')
        f.write(json.dumps(data))
        f.write('}')

if __name__ == '__main__':
    # 効率は悪いけど、ひとつづつステップを踏んだ処理をします（趣味のプログラミングだしね）
    data = fileIn()
    data = filterAndParse(data)
    jsonFileOut(data)

