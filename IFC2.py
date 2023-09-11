import ifcopenshell
import ifcopenshell.util.element

file=ifcopenshell.open('C:\Shared_TS-models\Empire_Wind_DD\A234416-EW1-DD-WTG_1-ENV_US-Metric\IFC\Airtight Platform.ifc')

my_beam=file.by_type("IfcBeam")[0]

print(ifcopenshell.util.element.get_psets(my_beam,psets_only=True))