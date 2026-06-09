# merge.py  --  build a complete GDS from a routed DEF + technology cell GDS

# Run from the folder that contains .def .

import pya

# ---- inputs (edit only if your paths change) ----
tech_lef = "/path/to/.lef"                  #  Use the tech.lef file of the Technology you are using
cell_lef = "path/to/std_cell.lef"           # Use the cell.lef file of the Technology you are using
cell_gds = "path/to/technology.gds"         # Use the .gds file of the Technology you are using
in_def   = "path/to/.def"`                  # Use the .def file created from Step 4
out_gds  = "design.gds"
# -------------------------------------------------

layout = pya.Layout()

# 1) Load the standard-cell geometry first, so every cell exists with real polygons.
layout.read(cell_gds)

# 2) Configure the LEF/DEF reader.
opt = pya.LoadLayoutOptions()
cfg = opt.lefdef_config
cfg.lef_files = [tech_lef, cell_lef]
# 0 = automatic: use the cell's loaded GDS geometry when it exists (it does),
#     fall back to the LEF abstract only for anything missing.
# If cells come out hollow, change this to 2 (force external geometry).
cfg.macro_resolution_mode = 0

# 3) Read the routed DEF into the SAME layout -> merges routing + real cells.
layout.read(in_def, opt)

# 4) Write the merged GDS.
layout.write(out_gds)
print("Wrote " + out_gds)
