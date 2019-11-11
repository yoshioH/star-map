# -*- coding: utf-8 -*-
import os
import json

import hip

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

def vMagFilterAndParse(data):
    ret = list()
    for datum in data:
        if len(datum['vMag']) < 1:
            continue
        try:
            vMag = float(datum['vMag'])
            bvColor = float(datum['bvColor'])
        except ValueError:
            # パースに失敗した場合はスキップ
            print(json.dumps(datum))
            continue
        tmp = {
            'vMag':vMag,
            'bvColor':bvColor
        }
        ret.append(tmp)
    return ret

def absMagFilterAndParse(data):
    ret = list()
    for datum in data:
        if len(datum['vMag']) < 1 or float(datum['vMag']) > MAGNITUDE_LOWER_LIMIT:
            continue
        try:
            vMag = float(datum['vMag'])
            parallax = float(datum['parallax'])
            bvColor = float(datum['bvColor'])
        except ValueError:
            # パースに失敗した場合はスキップ
            print(json.dumps(datum))
            continue
        tmp = {
            'absMag':vMag, #TODO
            'bvColor':bvColor
        }
        ret.append(tmp)
    return ret

if __name__ == '__main__':
    # 効率は悪いけど、ひとつづつステップを踏んだ処理をします（趣味のプログラミングだしね）
    data = hip.fileIn(lineToDatum, '../data/hip_main.dat')
    vmagData = vMagFilterAndParse(data)
    # absMagData = absMagFilterAndParse(data)
    hip.jsonFileOut('../data/vmag_scatter-plot.json', vmagData)

