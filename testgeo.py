import geojson
geojson.geometry.DEFAULT_PRECISION = 6


d = ["POI1", 2.26, 49, "Chartreuse", "xxxx"]

listPoi = [
# 0      1    2   3             4
["POI1", 2.2, 49, "Chartreuse", "1111"],
["POI2", 2.3, 49, "Chartreuse", "2222"],
["POI3", 2.4, 49, "Chartreuse", "3333"]
]

listFeatures =[]
for poi in listPoi:
    print("--------")
    point = geojson.Point((poi[1], poi[2]))
    print(point)
    print("--------")
    properties = { "_umap_options": { "color": poi[3], "iconClass": "Drop", "showLabel": None, }, "name": poi[0], "description": poi[4] }
    feature = geojson.Feature(geometry=point, properties=properties)
    print(feature)
    listFeatures.append(feature)
    print("--------")
print("++++++++")
featureCollection = geojson.FeatureCollection(listFeatures)
print(featureCollection)
print("++++++++")


