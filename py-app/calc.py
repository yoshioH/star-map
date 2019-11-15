import math

hipdata = {"vMag": 6.61, "parallax": 2.81, "bvColor": -0.019}
hipdata = {"vMag": 6.53, "parallax": 4.12, "bvColor": 0.955}
hipdata = {"vMag": 6.71, "parallax": 10.33, "bvColor": 0.382}
hipdata = {"vMag": 6.7, "parallax": 0.89, "bvColor": 1.969}
# Rigel = {"vMag": 0.13, "parallax": 3.78, "bvColor": 1.969}
Rigel = {"vMag": 0.18, "parallax": 4.22, "bvColor": -0.03}
Vega = {"vMag": 0.03, "parallax": 130.23, "bvColor": 1.969}


# ミリ秒(milliarcsecond)を秒(arcsecond)に修正
def milliarcsecond_to_arcsecond(milliarcseconds):
    return milliarcseconds / 1000

# 視差から絶対等級を産出する
def parallax_to_abs_mag(mag, parallax_milliarcseconds):
    parallax = milliarcsecond_to_arcsecond(parallax_milliarcseconds)
    return round(mag + 5 * (math.log(parallax, 10) + 1.0), 2)

# 距離(パーセク)で絶対等級を算出
def abs_mag_by_parsec(mag, distance):
    return round(mag - 5 * (math.log(distance, 10) - 1), 2)

# 視差からパーセクに変換する
def parallax_to_parsec(parallax):
    return 1000 / parallax

# abst magnitude
absMag = parallax_to_abs_mag(hipdata['vMag'], hipdata['parallax'])
print(absMag)

distance = parallax_to_parsec(hipdata['parallax'])
absMag = abs_mag_by_parsec(hipdata['vMag'], distance)
print(absMag)
