# -*- coding: utf-8 -*-
import json

import hip
import scatter_plot
import static_star_data

def jsonFileOut(dstPath, data, options):
    with open(dstPath, mode='w') as f:
        f.write('{"data":')
        f.write(json.dumps(data))
        f.write(', "options":')
        f.write(json.dumps(options))
        f.write('}')

# static_star_dataに定義したデータもオプションとして追加
if __name__ == '__main__':
    data = hip.fileIn(hip.lineToDatum, '../data/hip_main.dat')
    absMagData = scatter_plot.absMagFilterAndParse(data)
    jsonFileOut('../data/hr-plot.json', absMagData, static_star_data.ALL_LIST)

