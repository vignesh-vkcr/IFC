import ifcopenshell
from ifcopenshell.api import run

# Create a blank model
model = ifcopenshell.file()

# All projects must have one IFC Project element
project = run("root.create_entity", model, ifc_class="IfcProject", name="My Project")

# Millimeters and square meters
length = run("unit.add_si_unit", model, unit_type="LENGTHUNIT", prefix="MILLI")
area = run("unit.add_si_unit", model, unit_type="AREAUNIT")

# Make it our default units, if we are doing a metric building
run("unit.assign_unit", model, units=[length, area])

# Geometry is optional in IFC, but because we want to use geometry in this example, let's define units
# Assigning without arguments defaults to metric units
#run("unit.assign_unit", model)

# Let's create a modeling geometry context, so we can store 3D geometry (note: IFC supports 2D too!)
context = run("context.add_context", model, context_type="Model")

# In particular, in this example we want to store the 3D "body" geometry of objects, i.e. the body shape
body = run("context.add_context", model, context_type="Model",
    context_identifier="Body", target_view="MODEL_VIEW", parent=context)

# Create a site, building, and storey. Many hierarchies are possible.
site_A = run("root.create_entity", model, ifc_class="IfcSite", name="My Site A")
building_A = run("root.create_entity", model, ifc_class="IfcBuilding", name="Building A")
storey_A = run("root.create_entity", model, ifc_class="IfcBuildingStorey", name="Ground Floor A")

# Create a site, building, and storey. Many hierarchies are possible.
site_B = run("root.create_entity", model, ifc_class="IfcSite", name="My Site B")
building_B = run("root.create_entity", model, ifc_class="IfcBuilding", name="Building B")
storey_B = run("root.create_entity", model, ifc_class="IfcBuildingStorey", name="Ground Floor B")

# Since the site is our top level location, assign it to the project
# Then place our building on the site, and our storey in the building
run("aggregate.assign_object", model, relating_object=project, product=site_A)
run("aggregate.assign_object", model, relating_object=site_A, product=building_A)
run("aggregate.assign_object", model, relating_object=building_A, product=storey_A)

# Since the site is our top level location, assign it to the project
# Then place our building on the site, and our storey in the building
run("aggregate.assign_object", model, relating_object=project, product=site_B)
run("aggregate.assign_object", model, relating_object=site_B, product=building_B)
run("aggregate.assign_object", model, relating_object=building_B, product=storey_B)

# Let's create a new wall
wall_A = run("root.create_entity", model, ifc_class="IfcWall")

# Give our wall a local origin at (0, 0, 0)
run("geometry.edit_object_placement", model, product=wall_A)

# Add a new wall-like body geometry, 5 meters long, 3 meters high, and 200mm thick
representation = run("geometry.add_wall_representation", model, context=body, length=5000, height=3000, thickness=200)
# Assign our new body geometry back to our wall
run("geometry.assign_representation", model, product=wall_A, representation=representation)

# Place our wall in the ground floor
run("spatial.assign_container", model, relating_structure=storey_A, product=wall_A)

# Let's create a new wall
wall_B = run("root.create_entity", model, ifc_class="IfcWall")

# Give our wall a local origin at (0, 0, 0)
run("geometry.edit_object_placement", model, product=wall_B)

# Add a new wall-like body geometry, 5 meters long, 3 meters high, and 200mm thick
representation = run("geometry.add_wall_representation", model, context=body, length=8000, height=2500, thickness=300)
# Assign our new body geometry back to our wall
run("geometry.assign_representation", model, product=wall_B, representation=representation)

# Place our wall in the ground floor
run("spatial.assign_container", model, relating_structure=storey_B, product=wall_B)

# Write out to a file
model.write("./model.ifc")