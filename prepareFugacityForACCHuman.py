# This file uses results from BETR-Research v1.0 (Python implementation) to acquire fugacities
# for various regions and output them to a file that ACC-HUMAN can accept for input.

import BETRS


def write_fugacity_file():

	chemical_name = "PCB-153"
	filename_path = '../Output/default/pcb153 run/dyn_out.cpk'

	# Using BETR-Research v1.0

	results = BETRS.load(filename_path)

	# Retrieve fugacities from relevant environmental media
	# Format:
	# results[compartment][units][grid_cell,:]
	# Compartment = the environmental media (lower air, upper air, seawater, etc)
	# Units - 'Pa' is fugacity - required for ACC-Human.
	# grid_cell: The grid cell from the BETR-Research globe. Remember to subtract 1 from the actual zone due to indexing starting at 0.

	air = results[2]['Pa'][77,:] # Lower air compartment, Fugacity (Pa), Region / grid cell from 78
	seawater = results[5]['Pa'][75,:]
	soil = results[6]['Pa'][77,:]
	freshwater = results[4]['Pa'][77,:]
	groundwater = freshwater # Assuming same contamination in groundwater as freshwater

	# 	Open File for Output
	#	Because ACC-Human is windows based, I must use the \r\n for End Of Line (EOL)
	fugacity_file = open(chemicalName + '.txt', 'w+')

	#	Write first 3 lines
	fugacity_file.write('0730\r\n')
	fugacity_file.write('1930\r\n')
	fugacity_file.write('2100')

	# Loop through Fugacities and write to file
	for f1, f2, f3, f4, f5 in zip(air, seawater, soil, freshwater, groundwater):
		fugacity_file.write('\r\n')
		fugacity_file.write(' ')
		fugacity_file.write('{:.3E}'.format(float(f1)))

		fugacity_file.write(' ')
		fugacity_file.write('{:.3E}'.format(float(f2)))

		fugacity_file.write(' ')
		fugacity_file.write('{:.3E}'.format(float(f3)))

		fugacity_file.write(' ')
		fugacity_file.write('{:.3E}'.format(float(f4)))

		fugacity_file.write(' ')
		fugacity_file.write('{:.3E}'.format(float(f5)))

	fugacity_file.close()

######################################################

write_fugacity_file()

######################################################