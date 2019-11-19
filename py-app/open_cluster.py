# -*- coding: utf-8 -*-
import json

import hip
import scatter_plot
import static_star_data

def isM67(datum):
    if float(datum['raDeg']) < static_star_data.M67['ra'] - static_star_data.M67['apparentRadius']:
        return False
    if float(datum['raDeg']) > static_star_data.M67['ra'] + static_star_data.M67['apparentRadius']:
        return False
    if float(datum['decDeg']) < static_star_data.M67['dec'] - static_star_data.M67['apparentRadius']:
        return False
    if float(datum['decDeg']) > static_star_data.M67['dec'] + static_star_data.M67['apparentRadius']:
        return False
    return True

def isNGC188(datum):
    if float(datum['raDeg']) < static_star_data.Ngc188['ra'] - static_star_data.Ngc188['apparentRadius']:
        return False
    if float(datum['raDeg']) > static_star_data.Ngc188['ra'] + static_star_data.Ngc188['apparentRadius']:
        return False
    if float(datum['decDeg']) < static_star_data.Ngc188['dec'] - static_star_data.Ngc188['apparentRadius']:
        return False
    if float(datum['decDeg']) > static_star_data.Ngc188['dec'] + static_star_data.Ngc188['apparentRadius']:
        return False
    return True

def filter(data):
    m67 = list()
    ngc188 = list()
    for datum in data:
        if len(datum['vMag']) < 1 or len(datum['parallax']) < 1 or len(datum['decDeg']) < 1 or len(datum['raDeg']) < 1:
            continue
        if isM67(datum):
            m67.append(datum)
            continue
        if isNGC188(datum):
            ngc188.append(datum)
            continue
        continue
    return m67, ngc188

# static_star_dataに定義したデータもオプションとして追加
if __name__ == '__main__':
    data = hip.fileIn(hip.lineToDatum, '../data/hip_main.dat')
    m67, ngc188 = filter(data)
    hip.jsonFileOut('../data/ngc188-plot.json', ngc188)
    hip.jsonFileOut('../data/m67-plot.json', m67)

