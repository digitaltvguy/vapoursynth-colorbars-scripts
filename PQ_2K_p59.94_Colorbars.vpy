from vapoursynth import core

import vapoursynth as vs

# Generate PQ UHD Bars
c = core.colorbars.ColorBars(format=vs.RGB30, resolution=4, hdr=2)
c = core.std.Convolution(c,mode="h",matrix=[1,2,4,2,1])
c = core.resize.Point(clip=c,format=vs.YUV422P10,matrix_s="2020ncl")
c = c * (1 * 60000 // 1001)
c = core.std.AssumeFPS(clip=c, fpsnum=60000, fpsden=1001)


c.set_output()
