import ifcopenshell
import ifcopenshell.util.element as Element

file=ifcopenshell.open('C:\Shared_TS-models\Empire_Wind_DD\A234416-EW1-DD-WTG_1-ENV_US-Metric\IFC\Airtight Platform.ifc')

beams=file.by_type("IfcBeam")

objects_data = {}

for beam in beams:
	object_id=beam.id()
	objects_data[object_id]={
	"ExpresslD": beam.id(),
	"Global ld": beam.GlobalId,
	"Class": beam.is_a(),
	"PredefinedType": Element .get_predefined_type(beam),
	"Name": beam.Name,
	"Level": Element.get_container(beam).Name if Element.get_container(beam) else "",
	"ObjectType": Element.get_type(beam).Name if Element.get_type(beam) else "",
	"Quantitysets":Element.get_psets(beam,qtos_only=True),
	"Propertysets":Element.get_psets(beam,psets_only=True),
	}

import pprint

pp=pprint.PrettyPrinter()

pp.pprint(objects_data)