import os.path

from prepareFugacityForACCHuman import write_fugacity_file

chemical_name = str(raw_input("What is the name of the chemical? "))

filename_path = str(raw_input("What is the path & filename of the BETR-Global output? "))

while not os.path.isfile(filename_path):
	filename_path = str(raw_input("%s was not found. Enter again: " %(filename_path)))

time_step = str(raw_input("Timestep of the results? (Leave blank for default) "))

if len(time_step) == 3:
	time_step = '0' + time_step

if len(time_step) == 0:
	time_step = '0730'

grid_cells = []

regions = ['air', 'seawater', 'soil', 'freshwater']

for region in regions:
	grid_cells.append(int(raw_input("Enter region number for %s: " % (region))))

print "Thank you. Now creating f%s.txt file for ACC-HUMAN." %(chemical_name)

write_fugacity_file(chemical_name, filename_path, time_step, grid_cells)