from .linspace import *
from .FrameCtrl import *


def sample_animation(num_samples, sampleFcn, *args, **kwargs):
    ctrl = FrameCtrl()
    c = ctrl.current
    for frame in ctrl.sample(num_samples):
        ctrl.current = frame
        sampleFcn(frame, *args, **kwargs)
    ctrl.current = c
