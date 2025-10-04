# Go to your design.v folder in terminal 
yosys # To open Yosys terminal for synthesis

# Phase A
read_verilog design.v   # Use your RTL design file name
hierarchy -check -top module_name   # Use the module name used in the verilog program
proc
opt -fast
techmap
opt-fast
stat
write_verilog -noattr -noexpr design_rtl.v   # You can make a directory for output file and use outputfiles/design_rtl.v (if required)
# Phase B
read_liberty -lib ~/path/to/tech.lib   # this the path to technology file beign used use the technology's tech.lib file
dfflibmap -liberty ~/path/to/tech.lib   # Use the same .lib file
abc -liberty ~/path/to/tech.lib    # Use the same .lib file
clean
stat -liberty ~/path/to/tech.lib    # Use the same .lib file
write_verilog -noattr design_synth.v   # This is the synthesised netlist (can use outputfiles/design_synth.v if required)
write_json design.json
show -format dot -prefix design_synth module_name   # creates design.dot file used to visualize
exit # To exit yosys
dot -Tsvg design.dot -o design.svg   # Make sure .dot file is the right name
open design.svg   # Now you an visualise the synthesised circuit
