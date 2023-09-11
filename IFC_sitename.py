import ifcopenshell

# Load the IFC file
ifc_file_path = "C:\Shared_TS-models\Empire_Wind_DD\A234416-EW1-DD-WTG_1-ENV_US-Metric\IFC/10.ifc"
ifc_file = ifcopenshell.open(ifc_file_path)

# Specify the GUID or name of the IfcSite object you want to change
target_guid = "WTG Foundation"
new_site_name = "Site Updated"

# Find the IfcSite object by GUID or name
target_site = None
for site in ifc_file.by_type("IfcSite"):
    if site.Name == target_guid:
        target_site = site
        break

if target_site:
    # Update the name property
    target_site.Name = new_site_name

    # Save the changes
    new_ifc_file_path = "C:\Shared_TS-models\Empire_Wind_DD\A234416-EW1-DD-WTG_1-ENV_US-Metric\IFC/10_updt.ifc"
    ifc_file.write(new_ifc_file_path)
    print("Site name updated successfully.")
else:
    print("Site not found with the specified GUID or name.")