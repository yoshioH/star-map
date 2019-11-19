import calc

Sun = {
    'vMag' : -26.75,
    'absMag': 4.82,
    'parallax' : 0,
    'bvColor': 0.65,
    'name':'Sun',
    'type_name':'主系列星'
}
Spica = {
    'vMag' : 0.97,
    'absMag': -3.5,
    'parallax' : 13.06,
    'bvColor':-0.23,
    'name':'Spica',
    'type_name':'青色巨星'
}
SiriusA = {
    'vMag' : -1.46,
    'absMag': 1.4,
    'parallax' : 379.21,
    'bvColor':-0.0,
    'name':'SiriusA',
    'type_name':'A型主系列星'
}
SiriusB = {
    'vMag' : 8.44,
    'absMag': 11.3,
    'parallax' : 379.21,
    'bvColor':-0.03,
    'name':'SeriusB',
    'type_name':'白色矮星'
}
Aldebaran = {
    'vMag' : 0.86,
    'absMag': 0.7,
    'parallax' : 48.94,
    'bvColor': 1.54,
    'name':'Aldebaran',
    'type_name':'赤色巨星'
}
Betelgeuse = {
    'vMag' : 0.42,
    'absMag': -5.5,
    'parallax' : 642.53,
    'bvColor': 1.85,
    'name':'Betelgeuse',
    'type_name':'赤色超巨星'
}
Pollux = {
    'vMag' : 1.14,
    'absMag': 1.1,
    'parallax' : 96.54,
    'bvColor': 1.0,
    'name':'Pollux',
    'type_name':'巨星'
}

ALL_LIST = list()
ALL_LIST.append(Sun)
ALL_LIST.append(Spica)
ALL_LIST.append(SiriusA)
ALL_LIST.append(SiriusB)
ALL_LIST.append(Aldebaran)
ALL_LIST.append(Betelgeuse)
ALL_LIST.append(Pollux)

Ngc188 = {
    'ra': calc.hms_to_degree(0, 48, 26),
    'dec':calc.dms_to_degree(85, 15, 18),
    'apparentRadius': calc.dms_to_degree(0, 15, 0)
}

M67 = {
    'ra': calc.hms_to_degree(8, 51, 18),
    'dec':calc.dms_to_degree(11, 48, 0),
    'apparentRadius': calc.dms_to_degree(0, 25, 0) # 視直径ではなく計算しやすい視半径
}

