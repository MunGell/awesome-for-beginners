from Python_Version.scraper import PriceScraper
from matplotlib import pyplot as plt
import subprocess


class Graph(object):
    def grapher(self):
        self.scraped_data = PriceScraper.Scraper(self)
        self.x = [row for row in range(0, len(self.scraped_data))]
        self.y = self.scraped_data

        class Graph_Types(object):
            self.fig = plt.figure()

            def scatter_plot(self):
                plt.ticklabel_format(style='plain', useOffset=False, axis='both')
                plt.scatter(self.x, self.y)
                plt.grid()
                # plt.show()
                self.fig.savefig('scatter.png')

            def linear_graph(self):
                plt.ticklabel_format(style='plain', useOffset=False, axis='both')
                plt.plot(self.x, self.y)
                plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
                # plt.show()
                self.fig.savefig('line.png')

            def forecast_graph(self):
                pass

        Graph_Types.scatter_plot(self)
        Graph_Types.linear_graph(self)

