"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("../data/IBM.csv")
    # TODO: Your code here
    df['High'].plot()
    plt.xlabel('Price')
    plt.ylabel('Volume')
    plt.title('High price for IBM')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    #plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()

