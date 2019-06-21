import numpy as np
from scipy.interpolate import interp1d

from get_aw import get_aw


def giop(wl, rrs, chl=0.2,
         gopt=dict(fq=[0.0949, 0.0794],
                   aw=np.NaN, bbw=np.NaN,
                   aph='bricaud', aphs=np.NaN,
                   bbps=np.NaN, adgs=np.NaN,
                   g0=np.NaN, g1=np.NaN,
                   Sf=0.5, inv='fmin', qc=np.NaN,
                   eta=np.NaN, sdg=np.NaN,
                   solz=np.NaN, senz=np.NaN)
         ):
    """
    GIOP ocean color reflectance inversion model.
    gopt: dict, inversion parameters, including
            aw, bbw
    """

    mapg = -999;
    maph = -999;
    madg = -999;
    mbbp = -999;
    mrrs = -999;

    rrs_indigo = np.NaN
    rrs_blue = np.NaN
    rrs_green = np.NaN
    for wli, rrsi in zip(wl, rrs):
        if wli in np.arange(411, 416):
            rrs_indigo = rrs
        elif wli in np.arange(443, 446):
            rrs_blue = rrs
        elif wli in np.arange(546, 558):
            rrs_green = rrs

    if gopt['fq'] == 'morel':
        if np.isnan(gopt['senz']) and np.isnan(gopt['relaz']):
            f, q = morel_fq_appb(chl, gopt['solz'])
