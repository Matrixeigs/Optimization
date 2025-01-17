# Copyright (c) 2017-2018. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Power flow data for 33 bus, 1 generator case.
"""



def case33_modified():
    """Power flow data for 33 bus, 6 generator case.
    Please see L{caseformat} for details on the case file format.
    Based on data from ...
    Alsac, O. & Stott, B., I{"Optimal Load Flow with Steady State Security"},
    IEEE Transactions on Power Apparatus and Systems, Vol. PAS 93, No. 3,
    1974, pp. 745-751.
    ... with branch parameters rounded to nearest 0.01, shunt values divided
    by 100 and shunt on bus 10 moved to bus 5, load at bus 5 zeroed out.
    Generator locations, costs and limits and bus areas were taken from ...
    Ferrero, R.W., Shahidehpour, S.M., Ramesh, V.C., I{"Transaction analysis
    in deregulated power systems using game theory"}, IEEE Transactions on
    Power Systems, Vol. 12, No. 3, Aug 1997, pp. 1340-1347.
    Generator Q limits were derived from Alsac & Stott, using their Pmax
    capacities. V limits and line |S| limits taken from Alsac & Stott.
    @return: Power flow data for 30 bus, 6 generator case.
    @see: U{http://www.pserc.cornell.edu/matpower/}
    """
    from numpy import array, ix_
    from pypower.idx_bus import BASE_KV, BUS_I, PQ, PV, REF, BUS_TYPE
    from pypower.idx_brch import BR_R, BR_X, F_BUS, T_BUS
    from pypower.idx_gen import GEN_BUS
    ppc = {"version": '2'}

    ##-----  Power Flow Data  -----##
    ## system MVA base
    ppc["baseMVA"] = 100.0

    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([
        [1, 3, 0, 0, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [2, 1, 0.1, 0.06, 0, 0, 1, 1, 0, 12.66, 1, 1.1, 0.95],
        [3, 1, 0.09, 0.04, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [4, 1, 0.12, 0.08, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [5, 1, 0.06, 0.03, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [6, 1, 0.06, 0.02, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [7, 1, 0.2, 0.1, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [8, 1, 0.2, 0.1, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [9, 1, 0.06, 0.02, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [10, 1, 0.06, 0.02, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [11, 1, 0.045, 0.03, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [12, 1, 0.06, 0.035, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [13, 1, 0.06, 0.035, 0, 0, 2, 1, 0, 12.66, 1, 1.1, 0.95],
        [14, 1, 0.12, 0.08, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [15, 1, 0.06, 0.01, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [16, 1, 0.06, 0.02, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [17, 1, 0.06, 0.02, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [18, 1, 0.09, 0.04, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [19, 1, 0.09, 0.04, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [20, 1, 0.09, 0.04, 0, 0, 2, 1, 0, 12.66, 1, 1.05, 0.95],
        [21, 3, 0.09, 0.04, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [22, 1, 0.09, 0.04, 0, 0, 3, 1, 0, 12.66, 1, 1.1, 0.95],
        [23, 1, 0.09, 0.05, 0, 0, 2, 1, 0, 12.66, 1, 1.1, 0.95],
        [24, 1, 0.42, 0.20, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [25, 1, 0.42, 0.2, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [26, 1, 0.06, 0.025, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [27, 1, 0.06, 0.025, 0, 0, 3, 1, 0, 12.66, 1, 1.1, 0.95],
        [28, 1, 0.06, 0.02, 0, 0, 1, 1, 0, 12.66, 1, 1.05, 0.95],
        [29, 1, 0.12, 0.07, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [30, 1, 0.2, 0.6, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [31, 1, 0.15, 0.07, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [32, 1, 0.21, 0.1, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
        [33, 1, 0.06, 0.04, 0, 0, 3, 1, 0, 12.66, 1, 1.05, 0.95],
    ])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    ppc["gen"] = array([
        [14, 0, 0, 0.20, -0.2, 1, 100, 1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [21, 0, 0, 0.35, -0.35, 1, 100, 1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [25, 0, 0, 0.30, -0.30, 1, 100, 1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    ])

    ## branch data
    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    # Note that r, x, b are nominal value here and will later be converted to per unit value.
    ppc["branch"] = array([
        [1, 2, 0.0922, 0.0470, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [2, 3, 0.4930, 0.2511, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [3, 4, 0.3660, 0.1864, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [4, 5, 0.3811, 0.1941, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [5, 6, 0.8190, 0.7070, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [6, 7, 0.1872, 0.6188, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [7, 8, 0.7114, 0.2351, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [8, 9, 1.0300, 0.7400, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [9, 10, 1.0440, 0.7400, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [10, 11, 0.1966, 0.0650, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [11, 12, 0.3744, 0.1238, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [12, 13, 1.4680, 1.1550, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [13, 14, 0.5416, 0.7129, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [14, 15, 0.5910, 0.5260, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [15, 16, 0.7463, 0.5450, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [16, 17, 1.2890, 1.7210, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [17, 18, 0.7320, 0.5740, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [2, 19, 0.1640, 0.1565, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [19, 20, 1.5042, 1.3554, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [20, 21, 0.4095, 0.4784, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [21, 22, 0.7089, 0.9373, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [3, 23, 0.4512, 0.3083, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [23, 24, 0.8980, 0.7091, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [24, 25, 0.8960, 0.7011, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [6, 26, 0.2030, 0.1034, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [26, 27, 0.2842, 0.1447, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [27, 28, 1.0590, 0.9337, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [28, 29, 0.8042, 0.7006, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [29, 30, 0.5075, 0.2585, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [30, 31, 0.9744, 0.9630, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [31, 32, 0.3105, 0.3619, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        [32, 33, 0.3410, 0.5302, 0, 250, 250, 250, 0, 0, 1, -360, 360],
        # tie lines
        [8, 21, 2.0000, 2.0000, 0, 250, 250, 250, 0, 0, 0, -360, 360],
        [9, 15, 2.0000, 2.0000, 0, 250, 250, 250, 0, 0, 0, -360, 360],
        [12, 22, 2.0000, 2.0000, 0, 250, 250, 250, 0, 0, 0, -360, 360],
        [18, 33, 0.5000, 0.5000, 0, 250, 250, 250, 0, 0, 0, -360, 360],
        [25, 29, 0.5000, 0.5000, 0, 250, 250, 250, 0, 0, 0, -360, 360],
    ])

    ##-----  OPF Data  -----##
    ## area data
    # area refbus
    ppc["areas"] = array([
        [1, 8],
        [2, 23],
        [3, 26],
    ])

    ## generator cost data
    # 1 startup shutdown n x1 y1 ... xn yn
    # 2 startup shutdown n c(n-1) ... c0
    ppc["gencost"] = array([
        [2, 0, 0, 3, 0, 20, 0],
        [2, 0, 0, 3, 0, 20, 0],
        [2, 0, 0, 3, 0, 20, 0]
    ])

    # Unit conversion
    vbase = ppc['bus'][0, BASE_KV] * 1e3
    sbase = ppc['baseMVA'] * 1e6
    ppc['branch'][:, [BR_R, BR_X]] = ppc['branch'][:, [BR_R, BR_X]] / (vbase**2 / sbase)

    # Index conversion to zero-base, if input of bus ID is one-based
    # For bus
    ppc['bus'][:, BUS_I] -= 1
    # For branch
    ppc['branch'][:, [F_BUS, T_BUS]] -= 1
    # For gen
    ppc['gen'][:, GEN_BUS] -= 1

    # Set generator bus type to type 3 (REF bus) for use in pandapower
    # Only for use in pandapower
    # Set all bus type to PQ bus
    ppc['bus'][:, BUS_TYPE] = PQ
    # Set generator bus to REF bus
    ppc['bus'][ppc['gen'][:, GEN_BUS].astype(int), BUS_TYPE] = REF

    # Check if gen is matched with gencost

    return ppc

