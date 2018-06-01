cd Scripts
python3 -m venv fju_venv
source fju_venv/bin/activate
pip3 install requests



import request

res = request.get(https://www.prevision-meteo.ch/services/json/gingins)
dic = res.json()
#print(res.json())

#city = (dic["city_info"])
#print(city["elevation"])
dic["city_info"]["elevation"]


def alti(alt):
alti=dic["city_info"]["elevation"]
city=dic["city_info"]["name"]

print("Altitude de",city,":",alti)

for i in range (24):
    print("heure:",str(i)+"H00  ",end='' )
    print(dic["fcst_day_0"]["hourly_data"][str(i)+"H00"]["APCPsfc"])
