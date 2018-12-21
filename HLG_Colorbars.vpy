from vapoursynth import core

import vapoursynth as vs

# Generate HLG UHD Bars
c = core.colorbars.ColorBars(format=vs.RGB30, resolution=5, hdr=1)
c = core.std.Convolution(c,mode="h",matrix=[1,2,4,2,1])
c = core.resize.Point(clip=c,format=vs.YUV422P10,matrix_s="2020ncl")


c.set_output()