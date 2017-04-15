import sys
from functools import partial
import json
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGroupBox, QLineEdit, QGridLayout, QSpinBox, QPushButton, QTabWidget, QHBoxLayout, QComboBox
from gui.components.PeakListArea import PeakListArea
from gui.components.Sidebar import SideBar
from gui.components.ValuesField import ValueField

from gui.components.ColourBox import ColourBox
from gui.components.LabelledCheckbox import LabelledCheckbox
from gui.components.LabelledCombobox import LabelledCombobox
from gui.components.LabelledSpinBox import LabelledSpinBox
from gui.components.LabelledLineEdit import LabelledLineEdit
from gui.components.LabelledDoubleSpinBox import LabelledDoubleSpinBox
from gui.popups.ExtendedBarPopup import ExtendedBarPopup
from gui.popups.CompactBarPopup import CompactBarPopup
from gui.popups.VerticalBar import VerticalBarPopup
from gui.popups.ResidueEvolution import ResidueEvolutionPopup
from gui.popups.UserMarksPopup import UserMarksPopup
from gui import gui_utils

valuesDict = {
            'x': [],
            'y': [],
            'z': []
        }


class Main(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self, parent=None)
        tab1 = Settings()
        tab2 = Interface()
        tab3 = QWidget()
        self.addTab(tab1, "Settings")
        self.addTab(tab2, "PeakList Selection")
        self.addTab(tab3, "Results")
        self.setFixedHeight(850)
        self.setFixedWidth(1300)


class Settings(QWidget):
    def __init__(self):
        QWidget.__init__(self, parent=None)
        grid = QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(grid)
        grid.setSpacing(3)
        vars = json.load(open("/Users/fbssps/PycharmProjects/FarSeer-NMR/current/default_config.json", 'r'))
        # label1 = QLabel("General Settings", self)


        paths_group_box = QGroupBox()
        paths_groupbox_layout = QVBoxLayout()
        paths_groupbox_layout.setSpacing(5)
        paths_group_box.setLayout(paths_groupbox_layout)

        self.spectrum_path = LabelledLineEdit(self, "Spectrum Path")
        self.logfile_path = LabelledLineEdit(self, "Log file Path")

        paths_group_box.layout().addWidget(self.spectrum_path)
        paths_group_box.layout().addWidget(self.logfile_path)

        self.ext_bar_checkbox = LabelledCheckbox(self, "Extended Bar")
        self.comp_bar_checkbox = LabelledCheckbox(self, "Compact Bar")
        self.vert_bar_checkbox = LabelledCheckbox(self, "Vertical Bar")
        self.res_evo_checkbox = LabelledCheckbox(self, "Residue Evolution")
        self.user_details_checkbox = LabelledCheckbox(self, "User Details")
        self.scatter_checkbox = LabelledCheckbox(self, "CS Scatter")
        self.dpre_checkbox = LabelledCheckbox(self, "DPre")
        self.heat_map_checkbox = LabelledCheckbox(self, "PRE Heat Map")

        self.ext_bar_button = QPushButton("Settings", self)
        self.ext_bar_button.clicked.connect(partial(self.show_popup, ExtendedBarPopup, vars))

        self.comp_bar_button = QPushButton("Settings", self)
        self.comp_bar_button.clicked.connect(partial(self.show_popup, CompactBarPopup, vars))
        self.vert_bar_button = QPushButton("Settings", self)
        self.vert_bar_button.clicked.connect(partial(self.show_popup, VerticalBarPopup, vars))

        self.res_evo_button = QPushButton("Settings", self)
        self.res_evo_button.clicked.connect(partial(self.show_popup, ResidueEvolutionPopup, vars))

        self.user_details_button = QPushButton("Settings", self)
        self.user_details_button.clicked.connect(partial(self.show_popup, UserMarksPopup, vars))

        self.scatter_button = QPushButton("Settings", self)
        self.scatter_button.clicked.connect(partial(self.show_popup, UserMarksPopup, vars))

        self.heat_map_button = QPushButton("Settings", self)
        self.heat_map_button.clicked.connect(partial(self.show_popup, UserMarksPopup, vars))

        self.dpre_button = QPushButton("Settings", self)
        self.dpre_button.clicked.connect(partial(self.show_popup, UserMarksPopup, vars))



        self.has_sidechains_checkbox = LabelledCheckbox(self, "Sidechain Peaks?")
        self.use_sidechains_checkbox = LabelledCheckbox(self, "Analyse Sidechains?")
        self.perform_controls_checkbox = LabelledCheckbox(self, "Perform Controls?")
        self.apply_fasta_checkbox = LabelledCheckbox(self, "Apply FASTA?")
        self.fasta_start = LabelledSpinBox(self, "Fasta start")

        # self.res_evo_fitting = LabelledCheckbox(self, "Fit Parameter Evolution?")
        # self.res_evo_fit_line_colour = ColourBox(self, text="Fit Line Colour")
        # self.res_evo_fit_line_width = LabelledSpinBox(self, "Fit Line Width")

        self.expand_lost_yy = LabelledCheckbox(self, "Analyse Lost Y Residues?")
        self.expand_lost_zz = LabelledCheckbox(self, "Analyse Lost Z Residues?")

        self.figure_width = LabelledDoubleSpinBox(self, "Figure Width")
        self.figure_height = LabelledDoubleSpinBox(self, "Figure Height")
        self.figure_dpi = LabelledDoubleSpinBox(self, "Figure DPI")
        self.figure_format = LabelledCombobox(self, "Figure Format", items=['pdf', 'png', 'ps', 'svg'])

        grid.layout().addWidget(paths_group_box, 0, 0, 4, 20)


        general_groupbox = QGroupBox()
        general_groupbox_layout = QHBoxLayout()
        general_groupbox_layout.setSpacing(10)
        general_groupbox.setLayout(general_groupbox_layout)

        general_groupbox.layout().addWidget(self.has_sidechains_checkbox)
        general_groupbox.layout().addWidget(self.use_sidechains_checkbox)
        general_groupbox.layout().addWidget(self.perform_controls_checkbox)
        general_groupbox.layout().addWidget(self.expand_lost_yy)
        general_groupbox.layout().addWidget(self.expand_lost_zz)

        figure_groupbox = QGroupBox()
        figure_groupbox_layout = QHBoxLayout()
        figure_groupbox_layout.setSpacing(10)
        figure_groupbox.setLayout(figure_groupbox_layout)

        figure_groupbox.layout().addWidget(self.figure_width)
        figure_groupbox.layout().addWidget(self.figure_height)
        figure_groupbox.layout().addWidget(self.figure_dpi)
        figure_groupbox.layout().addWidget(self.figure_format)


        grid.layout().addWidget(general_groupbox, 5, 0, 2, 20)
        grid.layout().addWidget(figure_groupbox, 7, 0, 2, 20)

        # res_evo_groupbox = QGroupBox()
        # res_evo_groupbox_layout = QHBoxLayout()
        # res_evo_groupbox.setLayout(res_evo_groupbox_layout)
        #
        # res_evo_groupbox.layout().addWidget(self.res_evo_fitting)
        # res_evo_groupbox.layout().addWidget(self.res_evo_fit_line_colour)
        # res_evo_groupbox.layout().addWidget(self.res_evo_fit_line_width)

        # grid.layout().addWidget(res_evo_groupbox, 4, 0, 1, 3)

        fasta_groupbox = QGroupBox()
        fasta_groupbox_layout = QHBoxLayout()
        fasta_groupbox.setLayout(fasta_groupbox_layout)

        fasta_groupbox.layout().addWidget(self.apply_fasta_checkbox)
        fasta_groupbox.layout().addWidget(self.fasta_start)
        grid.layout().addWidget(fasta_groupbox, 9, 14, 2, 6)



        self.cs_correction = LabelledCheckbox(self, "CS Correction?")
        self.cs_correction_res_ref = LabelledLineEdit(self, text="Correction Residue")
        self.csp_alpha = LabelledLineEdit(self, text="CSP Alpha")
        self.csp_lost = LabelledCombobox(self, text="CSP Lost Mode", items=['prev', 'full'])
        self.csp_exceptions = QPushButton("CSP Exceptions", self)

        cs_groupbox = QGroupBox()
        cs_groupbox_layout = QHBoxLayout()
        cs_groupbox.setLayout(cs_groupbox_layout)


        cs_groupbox.layout().addWidget(self.cs_correction)
        cs_groupbox.layout().addWidget(self.cs_correction_res_ref)
        cs_groupbox.layout().addWidget(self.csp_alpha)
        cs_groupbox.layout().addWidget(self.csp_lost)
        cs_groupbox.layout().addWidget(self.csp_exceptions)

        grid.layout().addWidget(cs_groupbox, 9, 0, 2, 14)

        self.plot_F1_data = LabelledCheckbox(self, text="Plot F1 data")
        self.plot_F2_data = LabelledCheckbox(self, text="Plot F2 data")
        self.plot_CSP = LabelledCheckbox(self, text="Plot CSPs")
        self.plot_height_ratio = LabelledCheckbox(self, text="Plot Height Ratio")
        self.plot_volume_ratio = LabelledCheckbox(self, text="Plot Volume Ratio")

        self.plot_F1_y_label = LabelledLineEdit(self, text="Y Axis Label")
        self.plot_F2_y_label = LabelledLineEdit(self, text="Y Axis Label")
        self.plot_CSP_y_label = LabelledLineEdit(self, text="Y Axis Label")
        self.plot_height_y_label = LabelledLineEdit(self, text="Y Axis Label")
        self.plot_volume_y_label = LabelledLineEdit(self, text="Y Axis Label")

        self.plot_F1_calccol = LabelledLineEdit(self, text="Data Column")
        self.plot_F2_calccol = LabelledLineEdit(self, text="Data Column")
        self.plot_CSP_calccol = LabelledLineEdit(self, text="Data Column")
        self.plot_height_calccol = LabelledLineEdit(self, text="Data Column")
        self.plot_volume_calccol = LabelledLineEdit(self, text="Data Column")

        self.plot_F1_y_scale = LabelledDoubleSpinBox(self, text="Y Axis Scale")
        self.plot_F2_y_scale = LabelledDoubleSpinBox(self, text="Y Axis Scale")
        self.plot_CSP_y_scale = LabelledDoubleSpinBox(self, text="Y Axis Scale")
        self.plot_height_y_scale = LabelledDoubleSpinBox(self, text="Y Axis Scale")
        self.plot_volume_y_scale = LabelledDoubleSpinBox(self, text="Y Axis Scale")

        plot_F1_group_box = QGroupBox(self)
        plot_F2_group_box = QGroupBox(self)
        plot_csp_group_box = QGroupBox(self)
        plot_height_group_box = QGroupBox(self)
        plot_volume_group_box = QGroupBox(self)

        plot_F1_layout = QVBoxLayout()
        plot_F2_layout = QVBoxLayout()
        plot_csp_layout = QVBoxLayout()
        plot_height_layout = QVBoxLayout()
        plot_volume_layout = QVBoxLayout()

        plot_F1_group_box.setLayout(plot_F1_layout)
        plot_F2_group_box.setLayout(plot_F2_layout)
        plot_csp_group_box.setLayout(plot_csp_layout)
        plot_height_group_box.setLayout(plot_height_layout)
        plot_volume_group_box.setLayout(plot_volume_layout)

        plot_F1_layout.setSpacing(5)
        plot_F2_layout.setSpacing(5)
        plot_csp_layout.setSpacing(5)
        plot_height_layout.setSpacing(5)
        plot_volume_layout.setSpacing(5)


        plot_F1_group_box.layout().addWidget(self.plot_F1_data)
        plot_F1_group_box.layout().addWidget(self.plot_F1_y_label)
        plot_F1_group_box.layout().addWidget(self.plot_F1_calccol)
        plot_F1_group_box.layout().addWidget(self.plot_F1_y_scale)

        plot_F2_group_box.layout().addWidget(self.plot_F2_data)
        plot_F2_group_box.layout().addWidget(self.plot_F2_y_label)
        plot_F2_group_box.layout().addWidget(self.plot_F2_calccol)
        plot_F2_group_box.layout().addWidget(self.plot_F2_y_scale)

        plot_csp_group_box.layout().addWidget(self.plot_CSP)
        plot_csp_group_box.layout().addWidget(self.plot_CSP_y_label)
        plot_csp_group_box.layout().addWidget(self.plot_CSP_calccol)
        plot_csp_group_box.layout().addWidget(self.plot_CSP_y_scale)

        plot_height_group_box.layout().addWidget(self.plot_height_ratio)
        plot_height_group_box.layout().addWidget(self.plot_height_y_label)
        plot_height_group_box.layout().addWidget(self.plot_height_calccol)
        plot_height_group_box.layout().addWidget(self.plot_height_y_scale)

        plot_volume_group_box.layout().addWidget(self.plot_volume_ratio)
        plot_volume_group_box.layout().addWidget(self.plot_volume_y_label)
        plot_volume_group_box.layout().addWidget(self.plot_volume_calccol)
        plot_volume_group_box.layout().addWidget(self.plot_volume_y_scale)

        # plots_widget = QWidget()
        # plot_layout = QGridLayout()
        # plots_widget.setLayout(plot_layout)

        grid.layout().addWidget(plot_F1_group_box, 11, 0, 5, 4)
        grid.layout().addWidget(plot_F2_group_box, 11, 4, 5, 4)
        grid.layout().addWidget(plot_csp_group_box, 11, 8, 5, 4)
        grid.layout().addWidget(plot_height_group_box, 11, 12, 5, 4)
        grid.layout().addWidget(plot_volume_group_box, 11, 16, 5, 4)

        # grid.layout().addWidget(plots_widget, 6, 0, 3, 5)

        ext_bar_group_box = QGroupBox(self)
        comp_bar_group_box = QGroupBox(self)
        vert_bar_group_box = QGroupBox(self)
        res_evo_plot_group_box = QGroupBox(self)
        user_details_group_box = QGroupBox(self)
        heat_map_group_box = QGroupBox(self)
        scatter_group_box = QGroupBox(self)
        dpre_group_box = QGroupBox(self)

        ext_bar_group_box_layout = QHBoxLayout()
        comp_bar_group_box_layout = QHBoxLayout()
        vert_bar_group_box_layout = QHBoxLayout()
        res_evo_plot_group_box_layout = QHBoxLayout()
        user_details_group_box_layout = QHBoxLayout()
        heat_map_group_box_layout = QHBoxLayout()
        scatter_group_box_layout = QHBoxLayout()
        dpre_group_box_layout = QHBoxLayout()

        ext_bar_group_box.setLayout(ext_bar_group_box_layout)
        comp_bar_group_box.setLayout(comp_bar_group_box_layout)
        vert_bar_group_box.setLayout(vert_bar_group_box_layout)
        res_evo_plot_group_box.setLayout(res_evo_plot_group_box_layout)
        user_details_group_box.setLayout(user_details_group_box_layout)
        heat_map_group_box.setLayout(heat_map_group_box_layout)
        scatter_group_box.setLayout(scatter_group_box_layout)
        dpre_group_box.setLayout(dpre_group_box_layout)

        ext_bar_group_box.layout().addWidget(self.ext_bar_checkbox)
        comp_bar_group_box.layout().addWidget(self.comp_bar_checkbox)
        vert_bar_group_box.layout().addWidget(self.vert_bar_checkbox)
        res_evo_plot_group_box.layout().addWidget(self.res_evo_checkbox)
        user_details_group_box.layout().addWidget(self.user_details_checkbox)
        heat_map_group_box.layout().addWidget(self.heat_map_checkbox)
        scatter_group_box.layout().addWidget(self.scatter_checkbox)
        dpre_group_box.layout().addWidget(self.dpre_checkbox)

        ext_bar_group_box.layout().addWidget(self.ext_bar_button)
        comp_bar_group_box.layout().addWidget(self.comp_bar_button)
        vert_bar_group_box.layout().addWidget(self.vert_bar_button)
        res_evo_plot_group_box.layout().addWidget(self.res_evo_button)
        user_details_group_box.layout().addWidget(self.user_details_button)
        heat_map_group_box.layout().addWidget(self.heat_map_button)
        scatter_group_box.layout().addWidget(self.scatter_button)
        dpre_group_box.layout().addWidget(self.dpre_button)

        grid.layout().addWidget(ext_bar_group_box, 16, 0, 2, 5)
        grid.layout().addWidget(comp_bar_group_box, 16, 5, 2, 5)
        grid.layout().addWidget(vert_bar_group_box, 16, 10, 2, 5)
        grid.layout().addWidget(res_evo_plot_group_box, 16, 15, 2, 5)
        grid.layout().addWidget(scatter_group_box, 18, 0, 2, 5)
        grid.layout().addWidget(heat_map_group_box, 18, 5, 2, 5)
        grid.layout().addWidget(dpre_group_box, 18, 10, 2, 5)
        grid.layout().addWidget(user_details_group_box, 18, 15, 2, 5)

        buttons_groupbox = QGroupBox()
        buttons_groupbox_layout = QHBoxLayout()
        buttons_groupbox.setLayout(buttons_groupbox_layout)

        self.load_config_button = QPushButton("Load Configuration", self)
        self.save_config_button = QPushButton("Save Configuration", self)
        self.run_farseer_button = QPushButton("Run FarSeer-NMR", self)
        buttons_groupbox.layout().addWidget(self.load_config_button)
        buttons_groupbox.layout().addWidget(self.save_config_button)
        buttons_groupbox.layout().addWidget(self.run_farseer_button)

        grid.layout().addWidget(buttons_groupbox, 20, 0, 1, 20)


    def set_variables(self, vars):
        vars["general"]["spectrum_path"] = self.spectra_path.text()
        vars["general"]["logfile_name"] = self.logfile_path.text()
        vars["general"]["has_sidechains"] = self.has_sidechains_checkbox.isChecked()
        vars["general"]["use_sidechains"] = self.use_sidechains_checkbox.isChecked()


    def load_config(self, vars):
        pass

    def save_config(self, vars):
        pass

    def show_popup(self, popup, vars):
        p = popup(vars=vars)
        p.exec()
        p.raise_()
        print(vars["compact_bar_settings"])


    def show_compact_bar_popup(self):
        popup = CompactBarPopup()
        popup.exec()
        popup.raise_()


class Interface(QWidget):
 
    def __init__(self):
        QWidget.__init__(self, parent=None)

        self.initUI()

    def initUI(self):
        self.peakListArea = PeakListArea(self, valuesDict=valuesDict)
        grid = QGridLayout()
        grid1 = QGridLayout()
        grid2 = QGridLayout()
        grid.setVerticalSpacing(0)
        grid.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(grid)


        widget1 = QWidget(self)
        widget1.setLayout(grid1)
        self.widget2 = QWidget(self)
        self.widget2.setLayout(grid2)
        axes_label = QLabel("Use axes", self)
        self.x_checkbox = LabelledCheckbox(self, "x", fixed=True)
        self.y_checkbox = LabelledCheckbox(self, "y", fixed=True)
        self.z_checkbox = LabelledCheckbox(self, "z", fixed=True)
        self.widget2.layout().addWidget(axes_label, 0, 0, 1, 1)
        self.widget2.layout().addWidget(self.x_checkbox, 3, 0)
        self.widget2.layout().addWidget(self.y_checkbox, 2, 0)
        self.widget2.layout().addWidget(self.z_checkbox, 1, 0)

        self.sideBar = SideBar(self)

        self.layout().addWidget(self.sideBar, 0, 0, 4, 1)

        num_points_label = QLabel("Number of Points", self)

        grid2.layout().addWidget(num_points_label, 0, 1)

        self.z_combobox = QSpinBox(self)
        self.y_combobox = QSpinBox(self)
        self.x_combobox = QSpinBox(self)

        self.x_combobox.valueChanged.connect(partial(self.update_condition_boxes, 3, 'x'))
        self.y_combobox.valueChanged.connect(partial(self.update_condition_boxes, 2, 'y'))
        self.z_combobox.valueChanged.connect(partial(self.update_condition_boxes, 1, 'z'))

        self.z_combobox.setFixedWidth(100)
        self.y_combobox.setFixedWidth(100)
        self.x_combobox.setFixedWidth(100)

        grid2.layout().addWidget(self.x_combobox, 3, 1, 1, 1)
        grid2.layout().addWidget(self.y_combobox, 2, 1, 1, 1)
        grid2.layout().addWidget(self.z_combobox, 1, 1, 1, 1)

        self.z_combobox.setValue(1)
        self.y_combobox.setValue(1)
        self.x_combobox.setValue(1)

        self.layout().addWidget(self.widget2, 1, 1)

        self.showTreeButton = QPushButton('Show Parameter Tree', self)

        self.layout().addWidget(self.showTreeButton, 2, 1, 1, 3)
        self.layout().addWidget(self.peakListArea, 3, 1, 1, 3)
        self.showTreeButton.clicked.connect(self.peakListArea.updateTree)
        # self.peakListArea.hide()
        


    def update_condition_boxes(self, row, dim, value):

        self.x, self.y, self.z = self.x_combobox.value(), self.y_combobox.value(), self.z_combobox.value()
        layout = self.widget2.layout()
        colCount = layout.columnCount()
        for m in range(2, colCount):
            item = layout.itemAtPosition(row, m)
            if item:
                if item.widget():
                    item.widget().hide()
            layout.removeItem(item)
        if len(valuesDict[dim]) < value:
            [valuesDict[dim].append(0) for x in range(value-len(valuesDict[dim]))]
        if len(valuesDict[dim]) > value:
            valuesDict[dim] = valuesDict[dim][:value]
        for x in range(value):
            text_box = ValueField(self, x, dim, valuesDict)
            text_box.setFixedWidth(50)
            text_box.setText(str(valuesDict[dim][x]))
            layout.addWidget(text_box, row, x+2, 1, 1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    ex.raise_()
    sys.exit(app.exec_())
