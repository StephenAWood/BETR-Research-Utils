# This file uses results from BETR-Research v1.0 (Python implementation) to acquire fugacities
# for various regions and output them to a file that ACC-HUMAN can accept for input.
# You should have the folder for BETR-Research added to your Python path
#

import BETRS

def run():
	write_fugacity_file()

def write_fugacity_file(chemical_name = 'PCB-153',
	filename_path = '../Output/default/pcb153 run/dyn_out.cpk',
	time_step = '0730',
	grid_cells = [77, 75, 77, 77]
	): # Modify these parameters as needed. Will write interactive file to control this one.

	# Using BETR-Research v1.0

	results = BETRS.load(filename_path) # Load the results

	if len(grid_cells) is not 4:
		raise Exception("Error, invalid number of grid_cells")

	air_region, seawater_region, soil_region, freshwater_region = grid_cells

	# Retrieve fugacities from relevant environmental media
	# Format:
	# results[compartment][units][grid_cell,:]
	# Compartment = the environmental media (lower air, upper air, seawater, etc)
	# Units - 'Pa' is fugacity - required for ACC-Human.
	# grid_cell: The grid cell from the BETR-Research globe. Remember to subtract 1 from the actual zone due to indexing starting at 0.

	air_fugacity = results[2]['Pa'][air_region - 1,:] # Lower air compartment, Fugacity (Pa), Region / grid cell from 78
	seawater_fugacity = results[5]['Pa'][seawater_region - 1,:]
	soil_fugacity = results[6]['Pa'][soil_region - 1,:]
	freshwater_fugacity = results[4]['Pa'][freshwater_region - 1,:]
	groundwater_fugacity = freshwater_fugacity # Assuming same contamination in groundwater as freshwater

	# 	Open File for Output
	#	Because ACC-Human is windows based, I must use the \r\n for End Of Line (EOL)
	with open('f' + chemical_name + '.txt', 'w+') as fugacity_file:

		#	Write first 3 lines
		fugacity_file.write(time_step + '\r\n')
		fugacity_file.write('1930\r\n') # Start year for ACC-Human
		fugacity_file.write('2100') 	# End year for ACC-Human

		# Loop through fugacities and write to file
		for f1, f2, f3, f4, f5 in zip(air_fugacity, seawater_fugacity, soil_fugacity, freshwater_fugacity, groundwater_fugacity):
			fugacity_file.write('\r\n')
			fugacity_file.write(' {:.3E}'.format(float(f1)))
			fugacity_file.write(' {:.3E}'.format(float(f2)))
			fugacity_file.write(' {:.3E}'.format(float(f3)))
			fugacity_file.write(' {:.3E}'.format(float(f4)))
			fugacity_file.write(' {:.3E}'.format(float(f5)))

######################################################

run()

######################################################