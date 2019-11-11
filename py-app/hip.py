# -*- coding: utf-8 -*-
import os
import json

MAGNITUDE_LOWER_LIMIT = 7.0

def lineToDatum(line):
    datum = line.split('|')
    tmp = {
        'hipNum' : datum[1].strip(),
        'vMag' : datum[5].strip(),
        'raDeg' : datum[8].strip(),
        'decDeg' : datum[9].strip(),
        'parallax' : datum[11].strip(),
        'bvColor' : datum[37].strip()
    }
    return tmp

def fileIn(toDatum, srcPath):
    data = list()
    with open(srcPath) as lines:
        for line in lines:
            tmp = toDatum(line)
            data.append(tmp)
    return data

def filterAndParse(data):
    ret = list()
    for datum in data:
        if len(datum['vMag']) < 1 or float(datum['vMag']) > MAGNITUDE_LOWER_LIMIT:
            continue
        try:
            vMag = float(datum['vMag'])
            raDeg = float(datum['raDeg']) if float(datum['raDeg']) <= 180 else (180 - (float(datum['raDeg']) - 180))* -1
            decDeg = float(datum['decDeg'])
            parallax = float(datum['parallax'])
            bvColor = float(datum['bvColor'])
        except ValueError:
            # パースに失敗した場合はスキップ
            print(json.dumps(datum))
            continue

        # D3がGeoJSONの形式で受け取る関係上、赤緯と赤経を配列として格納している
        # Web側でキレイに整形してあげるのがいいんだろうけど、めんどくさいのでここで帳尻を合わせる。
        # TODO D3用のAPIとして提供するスタンスなら、まぁ許容範囲
        tmp = list()
        option = {
            'vMag':vMag,
            'parallax':parallax,
            'bvColor':bvColor
        }
        tmp.append(-1*raDeg)#地球儀の反対面からみる感じ。反転させる
        tmp.append(decDeg)
        tmp.append(option)
        ret.append(tmp)
    return ret

def jsonFileOut(dstPath, data):
    with open(dstPath, mode='w') as f:
        f.write('{"data":')
        f.write(json.dumps(data))
        f.write('}')

if __name__ == '__main__':
    # 効率は悪いけど、ひとつづつステップを踏んだ処理をします（趣味のプログラミングだしね）
    data = fileIn(lineToDatum, '../data/hip_main.dat')
    data = filterAndParse(data)
    jsonFileOut('../data/hip.json', data)

