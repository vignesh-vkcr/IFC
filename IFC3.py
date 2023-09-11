import ifcopenshell
import ifcopenshell.util.element

file=ifcopenshell.open('C:\Shared_TS-models\Empire_Wind_DD\A234416-EW1-DD-WTG_1-ENV_US-Metric\IFC\Airtight Platform.ifc')

my_beam=file.by_type("IfcBeam")[0]

print(my_beam.IsDefinedBy[7].RelatingPropertyDefinition)
#it gives quantityset of the given element. number 7 is manualy found.
# number 7 is only for selected element. and varies per element

print(my_beam.IsDefinedBy[7].RelatingPropertyDefinition.Quantities)

print(my_beam.IsDefinedBy[7].RelatingPropertyDefinition.Quantities[0])

print(my_beam.IsDefinedBy[7].RelatingPropertyDefinition.Quantities[0].Name)

print(my_beam.IsDefinedBy[7].RelatingPropertyDefinition.Quantities[0].LengthValue)

print(my_beam.IsDefinedBy[7].RelatingPropertyDefinition.Quantities[1].AreaValue)
print(my_beam.IsDefinedBy[7].RelatingPropertyDefinition.Quantities[1][3])

q_sets={}

if my_beam.IsDefinedBy:
	for relationship in my_beam.IsDefinedBy:
		if relationship.is_a("IfcRelDefinesByProperties") and relationship.RelatingPropertyDefinition.is_a("IfcElementQuantity"):
			q_set=relationship.RelatingPropertyDefinition
			quantities={}
			for quantity in q_set.Quantities:
				if quantity.is_a("IfcPhysicalSimpleQuantity"):
					print("1")
					quantities[quantity.Name]=quantity[3]
					#everytime 4 element of the set is the Value
			#print(props)
			q_sets[q_set.Name]=quantities
			print(q_set.Name+" was added")

print(q_sets)

# for simple way to get q_sets, refer following code
import ifcopenshell.util.element

print(ifcopenshell.util.element.get_psets(my_beam,psets_only=False,qtos_only=True))


#To get units
project = file.by_type("IfcProject")

#print(project[0])

project=project[0]

#print(project.UnitsInContext)

#print(project.UnitsInContext.Units)

for unit in project.UnitsInContext.Units:
	print(unit)
