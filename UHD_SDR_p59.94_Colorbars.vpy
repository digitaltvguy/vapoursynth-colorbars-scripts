from vapoursynth import core

import vapoursynth as vs

# Generate UHD Bars with Rec.2020 primaries
c = core.colorbars.ColorBars(format=vs.YUV444P12, resolution=5, wcg=1)
c = core.std.Convolution(c,mode="h",matrix=[1,2,4,2,1])
c = core.resize.Point(clip=c,format=vs.YUV422P10)
c = core.std.AssumeFPS(clip=c, fpsnum=50, fpsden=1)

c.set_output()
