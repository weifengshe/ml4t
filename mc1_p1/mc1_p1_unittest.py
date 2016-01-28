import unittest
import datetime as dt
import analysis as a


class Mc1P1Test(unittest.TestCase):
    def test_example1(self):
        start_date = dt.datetime(2010, 1, 1)
        end_date = dt.datetime(2010, 12, 31)
        symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
        allocations = [0.2, 0.3, 0.4, 0.1]
        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252

        # Assess the portfolio
        cr, adr, sddr, sr, ev = a.assess_portfolio(sd=start_date, ed=end_date,
                                                   syms=symbols,
                                                   allocs=allocations,
                                                   sv=start_val,
                                                   gen_plot=False)

        self.assertAlmostEqual(0.255646784534, cr, 3, "Cumulative Return {} is incorrect".format(cr), delta=None)
        self.assertAlmostEqual(1.51819243641, sr, 3, "Sharpe Ratio {} is incorrect".format(sr), delta=None)
        self.assertAlmostEqual(0.000957366234238, adr, 5, "Avg Daily Return {} is incorrect".format(adr), delta=None)
        self.assertAlmostEqual(0.0100104028, sddr, 5,
                               "Volatility (stdev of daily returns) {} is incorrect".format(sddr), delta=None)

    def test_example2(self):
        start_date = dt.datetime(2010, 1, 1)
        end_date = dt.datetime(2010, 12, 31)
        symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']
        allocations = [0.0, 0.0, 0.0, 1.0]
        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252

        # Assess the portfolio
        cr, adr, sddr, sr, ev = a.assess_portfolio(sd=start_date, ed=end_date,
                                                   syms=symbols,
                                                   allocs=allocations,
                                                   sv=start_val,
                                                   gen_plot=False)

        self.assertAlmostEqual(0.198105963655, cr, 3, "Cumulative Return {} is incorrect".format(cr), delta=None)
        self.assertAlmostEqual(1.30798398744, sr, 3, "Sharpe Ratio {} is incorrect".format(sr), delta=None)
        self.assertAlmostEqual(0.000763106152672, adr, 5, "Avg Daily Return {} is incorrect".format(adr), delta=None)
        self.assertAlmostEqual(0.00926153128768, sddr, 5,
                               "Volatility (stdev of daily returns) {} is incorrect".format(sddr), delta=None)

    def test_example3(self):
        start_date = dt.datetime(2010, 6, 1)
        end_date = dt.datetime(2010, 12, 31)
        symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
        allocations = [0.2, 0.3, 0.4, 0.1]
        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252

        # Assess the portfolio
        cr, adr, sddr, sr, ev = a.assess_portfolio(sd=start_date, ed=end_date,
                                                   syms=symbols,
                                                   allocs=allocations,
                                                   sv=start_val,
                                                   gen_plot=False)

        self.assertAlmostEqual(0.205113938792, cr, 3, "Cumulative Return {} is incorrect".format(cr), delta=None)
        self.assertAlmostEqual(2.21259766672, sr, 3, "Sharpe Ratio {} is incorrect".format(sr), delta=None)
        self.assertAlmostEqual(0.00129586924366, adr, 5, "Avg Daily Return {} is incorrect".format(adr), delta=None)
        self.assertAlmostEqual(0.00929734619707, sddr, 5,
                               "Volatility (stdev of daily returns) {} is incorrect".format(sddr), delta=None)


if __name__ == '__main__':
    unittest.main()