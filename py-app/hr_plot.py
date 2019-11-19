# -*- coding: utf-8 -*-
import json

import hip
import scatter_plot
import static_star_data

# static_star_dataに定義したデータもオプションとして追加
if __name__ == '__main__':
    data = hip.fileIn(hip.lineToDatum, '../data/hip_main.dat')
    absMagData = scatter_plot.absMagFilterAndParse(data)
    hip.jsonFileOut('../data/hr-plot.json', absMagData, static_star_data.ALL_LIST)

