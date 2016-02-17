__author__ = 'kenbrooks'

import unittest
import datetime as dt
import marketsim as m
import pandas as pd
import numpy as np

class Mc2P1Test(unittest.TestCase):
    def test_orders_short(self):

        tests = [{'filename': './orders/orders-short.csv', 'start_val':1000000, 'final_val':998035.0, 'cr':-0.001965, 'adr':-0.000178539446839, 'sdr':0.00634128215394, 'sr':-0.446948390642},
            {'filename': './orders/orders.csv', 'start_val':1000000, 'final_val':1133860.0, 'cr':0.13386, 'adr':0.000551651296638, 'sdr':0.00720514136323, 'sr':1.21540888742},
            {'filename': './orders/orders2.csv', 'start_val':1000000, 'final_val':1078752.6, 'cr':0.0787526, 'adr':0.000353426354584, 'sdr':0.00711102080156, 'sr':0.788982285751},
            {'filename': './orders/orders3.csv', 'start_val':1000000, 'final_val':1050160.0, 'cr':0.05016, 'adr':0.000365289198877, 'sdr':0.00560508094997, 'sr':1.03455887842},
            {'filename': './orders/orders-leverage-1.csv', 'start_val':1000000, 'final_val':1050160.0, 'cr':0.05016, 'adr':0.000487052265169, 'sdr':0.00647534272091, 'sr':1.19402406143},
            {'filename': './orders/orders-leverage-2.csv', 'start_val':1000000, 'final_val':1074650.0, 'cr':0.07465, 'adr':0.00202241842159, 'sdr':0.00651837064888, 'sr':4.92529481246},]

        for i, test in enumerate(tests):
            portvals = m.compute_portvals(orders_file = test['filename'], start_val = test['start_val'])
            if isinstance(portvals, pd.DataFrame):
                portvals = portvals[portvals.columns[0]] # just get the first column
            else:
                "warning, code did not return a DataFrame"

            print "portfolio_values", type(portvals)
            print portvals.shape
            cr, adr, sdr, sr = m.compute_portfolio_stats(portvals)
            np.testing.assert_almost_equal(portvals.ix[-1], test['final_val'], decimal=1)
            np.testing.assert_almost_equal(cr, test['cr'], decimal = 4)
            np.testing.assert_almost_equal(adr, test['adr'], decimal = 4)
            np.testing.assert_almost_equal(sdr, test['sdr'], decimal = 4)
            np.testing.assert_almost_equal(sr, test['sr'], decimal = 4)
            print "test", i, "passes"


if __name__ == '__main__':
    unittest.main()            