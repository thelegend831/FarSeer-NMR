import sys
import unittest
import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import os

from gui.popups.SeriesPlotPopup import SeriesPlotPopup
from gui.gui_utils import default_path as default_config


app = QApplication(sys.argv)

from current.fslibs.Variables import Variables

class Test_BarPlotPopup(unittest.TestCase):

    def setUp(self):
        ''' Create the popup'''

        Variables().read(default_config)
        fin = open(default_config, 'r')
        self.popup = SeriesPlotPopup()
        self.defaults = json.load(fin)["series_plot_settings"]
        fin.close()
        self.variable_keys = tuple(self.popup.variables.keys())
        self.local_variable_keys = tuple(self.popup.local_variables.keys())
        print(self.local_variable_keys)


    def test_defaults(self):
        """Test popup reads and sets default variables"""

        pass

    def test_set_values(self):
        self.popup.set_values()
        self.assertEqual(tuple(self.popup.local_variables.keys()), self.local_variable_keys)
        self.assertEqual(tuple(self.popup.variables.keys()), self.variable_keys)


if __name__ == "__main__":
    unittest.main()