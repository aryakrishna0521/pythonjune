from json import load
f=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\jsonWorks\\countries.json",encoding="UTF-8")
country=load(f)
#1 no of countries
# print(len(country))


#2 list of countries
countries=[c.get("name")for c in country]
# print(countries)

#3 countries under asian region
asian_countries=[c.get("name") for c in  country if c.get("region")=="Asia"]
# print(asian_countries)

#4 countries with domain
domain=[(c.get("name"),c.get("topLevelDomain"))for c in country]
# print(domain)

#5 languages speaks in india
indian_languages=[l.get("languages")for l in country if  l.get("name")=="India"]
#print(indian_languages)

#6 capital of france
capital=[c.get("capital") for c in country if c.get("name")=="France"]
# print(capital)

#7 currencies
currency=[c.get("currencies") for c in country if c.get("name")=="India"]
# print(currency)

#8 borders of india
border=[b.get("borders")for b in country if b.get("name")=="India"]
# print(border)

#9 country with highest population

def get_population(dic):
    return dic.get("population")
high_population=max(country,key=get_population)
# print(high_population.get("name"),high_population.get("population"))

#10 country withh lowest population
lowest_population=min(country,key=get_population)
# print(lowest_population.get("name"),lowest_population.get("population"))


#11 country andd native names
native=[[n.get("name"),n.get("nativeName")] for n in country]
# print(native)


#12 countries they are not independanted yet

not_indipendant=[i.get("name")for i in country  if i.get("independent")==False]
# print(not_indipendant)

#13 india  demonym
demonym_of_france=[d.get("demonym")for d in country if d.get("name")=="France"]
# print(demonym_of_france)

#14 flag
flags_of_india=[d.get("flags")for d in country if d.get("name")=="India"]
# print(flags_of_india)

#15 translation of br in 

translation=[[t.get("name"),t.get("translations").get("br")] for t in country]
# print(translation)

#16 countries with area

area=[[d.get("name"),d.get("area")]for d in country]
# print(area)

#17  numeric code of india
numeric_code=[l.get("numericCode")for l in country if  l.get("name")=="India"]
# print(numeric_code)


#18
time_zone=[l.get("timezones")for l in country if  l.get("name")=="Afghanistan"]
# print(time_zone)

#19
code=[l.get("callingCodes")for l in country if  l.get("name")=="Afghanistan"]
# print(code)


#20
lat=[l.get("latlng")for l in country if  l.get("name")=="Afghanistan"]
# print(lat)

#21 highest area

def get_area(dic):
    if "area" in dic:
        return dic.get("area")
    else:
        return 0
biggest_country_by_area=max(country,key=get_area)
# print(biggest_country_by_area.get("name"),biggest_country_by_area.get("area"))



#22 largest region by area 

all_regions={c.get("region") for c in country}
print(all_regions)
region_summary={}
for c in country :
    region_name=c.get("region")
    if region_name in region_summary:
        region_summary[region_name]+=c.get("area",0)
    else:
        region_summary[region_name]=c.get("area",0)    
print(region_summary)
value_key=[(v,k)for k,v in region_summary.items()]
print(max(value_key))



