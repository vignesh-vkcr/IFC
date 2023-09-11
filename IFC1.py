import ifcopenshell

file=ifcopenshell.open('C:\Shared_TS-models\Empire_Wind_DD\A234416-EW1-DD-WTG_1-ENV_US-Metric\IFC\Airtight Platform.ifc')
file.by_type("IfcProject")[0]
#36=IfcProject('3zTW5Rcmv5KusuCHoYUNU8',#5,'Empire Wind DD',$,$,$,$,(#11),#35)
project=file.by_type("IfcProject")[0]
site=project.IsDecomposedBy[0].RelatedObjects[0]
site
#38=IfcSite('3dG39$SQXCaxjMvmJggd_Q',#5,'WTG Foundation',$,$,#37,$,$,.ELEMENT.,$,$,$,$,$)
site.IsDecomposedBy[0].RelatedObjects[0]
#89291=IfcBuilding('0AtMtrxHX4lRG47$GYVRk1',#5,'Monopile',$,$,#89290,$,$,.ELEMENT.,$,$,$)
site.IsDecomposedBy
#(#394327=IfcRelAggregates('0e5h8IY_j2shtbsZE$Nir0',#5,$,$,#38,(#89291,#1681,#1405,#40)),)
site.IsDecomposedBy[0]
#394327=IfcRelAggregates('0e5h8IY_j2shtbsZE$Nir0',#5,$,$,#38,(#89291,#1681,#1405,#40))
site.IsDecomposedBy[0].RelatedObjects
#(#89291=IfcBuilding('0AtMtrxHX4lRG47$GYVRk1',#5,'Monopile',$,$,#89290,$,$,.ELEMENT.,$,$,$), #1681=IfcBuilding('1igLJKyzHEJvnrRuOOzOWK',#5,'Transition Piece',$,$,#1680,$,$,.ELEMENT.,$,$,$), #1405=IfcBuilding('21qCeHjuv9dRQZqXnT8Yc9',#5,'LV Earthing',$,$,#1404,$,$,.ELEMENT.,$,$,$), #40=IfcBuilding('0fwTVDajj6Bw7MisaF4pf2',#5,'Airtight Platform',$,$,#39,$,$,.ELEMENT.,$,$,$))
site.IsDecomposedBy[0].RelatedObjects[3]
#40=IfcBuilding('0fwTVDajj6Bw7MisaF4pf2',#5,'Airtight Platform',$,$,#39,$,$,.ELEMENT.,$,$,$)
building=site.IsDecomposedBy[0].RelatedObjects[3]
building.IsDecomposedBy
#(#394331=IfcRelAggregates('19N1pjTyj2Ug0H2ZIPDmwa',#5,$,$,#40,(#292530,#191991,#183351,#183037,#181399,#181210,#166564,#158532,#42)),)
building.IsDecomposedBy[0]
#394331=IfcRelAggregates('19N1pjTyj2Ug0H2ZIPDmwa',#5,$,$,#40,(#292530,#191991,#183351,#183037,#181399,#181210,#166564,#158532,#42))
building.IsDecomposedBy[0].RelatedObjects
#(#292530=IfcBuildingStorey('2IaghFhKrCmRzPcdcyM3_5',#5,'Cable Seal',$,$,#292529,$,$,.ELEMENT.,0.), #191991=IfcBuildingStorey('20tGxFIR903ukhlC49O8g_',#5,'Ventilation',$,$,#191990,$,$,.ELEMENT.,0.), #183351=IfcBuildingStorey('2TSzMWSI12f99LGIdQxoAV',#5,'Anchor Point',$,$,#183350,$,$,.ELEMENT.,0.), #183037=IfcBuildingStorey('1cuKih_211dvmVHcDzWO9J',#5,'Post',$,$,#183036,$,$,.ELEMENT.,0.), #181399=IfcBuildingStorey('3xZ$W8W314qPsXddmvsA_B',#5,'Grating',$,$,#181398,$,$,.ELEMENT.,0.), #181210=IfcBuildingStorey('3K4_uWHivANBo5xNa_ZXtU',#5,'IA Cable Hanger',$,$,#181209,$,$,.ELEMENT.,0.), #166564=IfcBuildingStorey('2DaMEKPDj9vBFN_XbCB$WD',#5,'Hatch',$,$,#166563,$,$,.ELEMENT.,0.), #158532=IfcBuildingStorey('00sKbvFnf38h24$4w5LsUu',#5,'Fastener',$,$,#158531,$,$,.ELEMENT.,0.), #42=IfcBuildingStorey('2zTRhM9$rBexvngsRthYDB',#5,'General',$,$,#41,$,$,.ELEMENT.,0.))
storeys=building.IsDecomposedBy[0].RelatedObjects

for storey in storeys:
 	#print(storey)
 	continue

storeys[0]
#292530=IfcBuildingStorey('2IaghFhKrCmRzPcdcyM3_5',#5,'Cable Seal',$,$,#292529,$,$,.ELEMENT.,0.)
cable_seal=storeys[0]
cable_seal.get_info()
#{'id': 292530, 'type': 'IfcBuildingStorey', 'GlobalId': '2IaghFhKrCmRzPcdcyM3_5', 'OwnerHistory': #5=IfcOwnerHistory(#3,#4,$,.NOCHANGE.,$,$,$,1691153718), 'Name': 'Cable Seal', 'Description': None, 'ObjectType': None, 'ObjectPlacement': #292529=IfcLocalPlacement(#39,#10), 'Representation': None, 'LongName': None, 'CompositionType': 'ELEMENT', 'Elevation': 0.0}

cable_seal.ContainsElements
#(#394345=IfcRelContainedInSpatialStructure('1QYxNIFMv00gOp09OjGcNN',#5,$,$,(#393324,#292870),#292530),)
cable_seal.ContainsElements[0]
#394345=IfcRelContainedInSpatialStructure('1QYxNIFMv00gOp09OjGcNN',#5,$,$,(#393324,#292870),#292530)
rel_contained=cable_seal.ContainsElements[0]
rel_contained
#394345=IfcRelContainedInSpatialStructure('1QYxNIFMv00gOp09OjGcNN',#5,$,$,(#393324,#292870),#292530)
rel_contained.RelatedElements
#(#393324=IfcBuildingElementProxy('2U7tbwcvf0DvZuDbg711wV',#161573,'SLR150+R150','r150','r150',#292894,#393323,'ID9e1f797a-9b9a-4037-98f8-365a87041e9f',.ELEMENT.), #292870=IfcColumn('1h8JQjjUz43R$nkvg2zras',#161573,'R 150','CHS164*6.5','CHS164*6.5',#292534,#292869,'ID6b2136ad-b5ef-440d-bff1-bb9a82f75936'))
for element in rel_contained.RelatedElements:
	#print(element)
	continue


#By Root

rooted_entities=file.by_type("IfcRoot")
#print(rooted_entities)

ifc_building_element_entities=set()

for entity in rooted_entities:
	if entity.is_a('IfcBuildingElement'):
		ifc_building_element_entities.add(entity.is_a())

print(ifc_building_element_entities)

#my_wall=file.by_id("22digit ifc id")
'''
my_wall.GlobalId
my_wall.Name
my_wall.Description
my_wall.Tag
my_wall.ObjectType

# you can also set values
my_wall.ObjectType=""


my_wall.IsTypedBy[0]
# above code gives ifc class type. that we already know that is wall.

my_wall.IsTypedBy[0].RelatedObjects
#above select all the wall elements
'''

my_beam=file.by_type("IfcBeam")[0]

print(my_beam)

#print(my_beam.IsDefinedBy) # gives all the property sets and quantity sets related to that object

#print(my_beam.IsDefinedBy[0])

print(my_beam.IsDefinedBy[3].RelatingPropertyDefinition) 
# Gives Quantity Set/ Property Set related to the element
pset1=my_beam.IsDefinedBy[3].RelatingPropertyDefinition

#`print(pset.HasProperties) # Gives all the properties of the selected property set

print(pset1.HasProperties[5].Name)
print(pset1.HasProperties[5].NominalValue)
print(pset1.HasProperties[5].NominalValue.wrappedValue)

psets={}

if my_beam.IsDefinedBy:
	for relationship in my_beam.IsDefinedBy:
		if relationship.is_a("IfcRelDefinesByProperties") and relationship.RelatingPropertyDefinition.is_a("IfcPropertySet"):
			pset=relationship.RelatingPropertyDefinition
			props={}
			for property in pset.HasProperties:
				if property.is_a("IfcPropertySingleValue"):
					if property.NominalValue!=None:
						props[property.Name]=property.NominalValue.wrappedValue
					else:
						props[property.Name]=None
			#print(props)
			psets[pset.Name]=props
			print(pset.Name+" was added")

print(psets)
# for simple way to get psets, refer IFC2.py
#print(psets['COWI-OW'])

# for simple way to get psets, refer following code
import ifcopenshell.util.element

print(ifcopenshell.util.element.get_psets(my_beam,psets_only=True))