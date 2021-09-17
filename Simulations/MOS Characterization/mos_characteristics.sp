* MOS Characteristic Curves
* LPA 8/13/2019

******************************
* Include model files
******************************
.include ./45nm_LP.pm

******************************
* Additional options
******************************
.option TEMP=27C

******************************
* Circuit netlist
******************************

vd		drain gnd	dc 1
vg		gate gnd 	dc 1

mn0		drain gate gnd gnd 	nmos	W=1u L=45n

******************************
* Control section
******************************

.control 
dc vd 0 1 0.01

.endc


******************************
* End of file
******************************
.end


