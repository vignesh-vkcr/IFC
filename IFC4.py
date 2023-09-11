import ifcopenshell
import ifcopenshell.util.element as Element

file=ifcopenshell.open('C:\Shared_TS-models\Empire_Wind_DD\A234416-EW1-DD-WTG_1-ENV_US-Metric\IFC\Airtight Platform.ifc')

my_beam=file.by_type("IfcBeam")[0]

# Express ID
print(my_beam.id())

# Global ID
print(my_beam.GlobalId)

# Class
print(my_beam.is_a())

# Predefined Type
print(Element.get_predefined_type(my_beam))

#Name
print(my_beam.Name)

#Level
print(Element.get_container(my_beam))

#Level
print(Element.get_container(my_beam).Name if Element.get_container(my_beam) else "")

#Type
print(Element.get_type(my_beam).Name if Element.get_type(my_beam) else "")

# Quantity Sets
print(Element.get_psets(my_beam,qtos_only=True))

# Property Sets
print(Element.get_psets(my_beam,psets_only=True))
