# -*- coding: utf-8 -*-
import os
import json

import calc
import hip

def vMagFilterAndParse(data):
    ret = list()
    for datum in data:
        if len(datum['vMag']) < 1:
            continue
        try:
            vMag = float(datum['vMag'])
            bvColor = float(datum['bvColor'])
            if bvColor > 2 : continue
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
        if len(datum['vMag']) < 1 or len(datum['parallax']) < 1:
            continue
        try:
            vMag = float(datum['vMag'])
            parallax = float(datum['parallax'])
            bvColor = float(datum['bvColor'])
            parsec = calc.parallax_to_parsec(parallax)
            absMag = calc.abs_mag_by_parsec(vMag, parsec)
            # absMag = calc.parallax_to_abs_mag(vMag, parallax)
            if bvColor > 2 : continue
        except ValueError:
            # パースに失敗した場合はスキップ
            # print('value error : ' + json.dumps(datum))
            continue
        except ZeroDivisionError:
            # print('zero divisions : ' + json.dumps(datum))
            continue
        tmp = {
            'absMag':absMag,
            'bvColor':bvColor
        }
        ret.append(tmp)
    return ret

if __name__ == '__main__':
    data = hip.fileIn(hip.lineToDatum, '../data/hip_main.dat')
    vmagData = vMagFilterAndParse(data)
    hip.jsonFileOut('../data/vmag_scatter-plot.json', vmagData)
    absMagData = absMagFilterAndParse(data)
    hip.jsonFileOut('../data/absmag_scatter-plot.json', absMagData)

