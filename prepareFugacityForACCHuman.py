# This file uses results from BETR-Research v1.0 (Python implementation) to acquire fugacities
# for various regions and output them to a file that ACC-HUMAN can accept for input.

import BETRS


def write_fugacity_file():

	#data = fugacityReader.openFile("BETR-Global Output/PCB-153 BETR-Global Fugacities Temp Fix.csv")

	#acquireFugacityForRegionAndCompartment(region, compartment, data)

	chemicalName = "PCB-153"

	# Using BETR-Research v1.0

	results = BETRS.load('Output/default/pcb153 run/dyn_out.cpk')

	air = results[2]['Pa'][77,:]
	seawater = results[5]['Pa'][75,:]
	soil = results[6]['Pa'][77,:]
	freshwater = results[4]['Pa'][77,:]
	groundwater = freshwater


	# 	Open File for Output
	#	Because ACC-Human is windows based, I must use the \r\n for End Of Line (EOL)
	fugacityFile = open(chemicalName + '.txt', 'w+')

	#	Write first 3 lines
	fugacityFile.write('0730\r\n')
	fugacityFile.write('1930\r\n')
	fugacityFile.write('2100')

	# Loop through Fugacities and write to file
	for f1, f2, f3, f4, f5 in zip(air, seawater, soil, freshwater, groundwater):
		fugacityFile.write('\r\n')
		fugacityFile.write(' ')
		fugacityFile.write('{:.3E}'.format(float(f1)))

		fugacityFile.write(' ')
		fugacityFile.write('{:.3E}'.format(float(f2)))

		fugacityFile.write(' ')
		fugacityFile.write('{:.3E}'.format(float(f3)))

		fugacityFile.write(' ')
		fugacityFile.write('{:.3E}'.format(float(f4)))

		fugacityFile.write(' ')
		fugacityFile.write('{:.3E}'.format(float(f5)))

	fugacityFile.close()

######################################################

writeFugacityFile()

######################################################