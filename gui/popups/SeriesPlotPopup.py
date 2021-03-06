"""
Copyright © 2017-2018 Farseer-NMR
Simon P. Skinner and João M.C. Teixeira

@ResearchGate https://goo.gl/z8dPJU
@Twitter https://twitter.com/farseer_nmr

This file is part of Farseer-NMR.

Farseer-NMR is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Farseer-NMR is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Farseer-NMR. If not, see <http://www.gnu.org/licenses/>.
"""
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QDialogButtonBox

from gui.components.LabelledCombobox import LabelledCombobox
from gui.components.LabelledCheckbox import LabelledCheckbox
from gui.components.LabelledDoubleSpinBox import LabelledDoubleSpinBox
from gui.components.LabelledSpinBox import LabelledSpinBox
from gui.components.ColourBox import ColourBox
from gui.components.FontComboBox import FontComboBox
from gui.gui_utils import font_weights, line_styles
from gui.popups.BasePopup import BasePopup


class SeriesPlotPopup(BasePopup):
    """
    A popup for setting Series Plot specific settings in the Farseer-NMR
    configuration.

    Parameters:
        parent(QWidget): parent widget for popup.

    Methods:
        .get_defaults()
        .get_values()
        .set_values()
    """
    def __init__(self, parent=None, **kw):
        BasePopup.__init__(
            self,
            parent,
            title="Series General Plot Settings",
            settings_key=["series_plot_settings"]
            )
        self.series_subtitle_groupbox = QGroupBox()
        self.series_subtitle_groupbox_layout = QVBoxLayout()
        self.series_subtitle_groupbox.setLayout(self.series_subtitle_groupbox_layout)
        self.series_subtitle_groupbox.setTitle("Subtitle Settings")
        self.series_subtitle_fn = FontComboBox(self, "Subtitle Font")
        self.series_subtitle_fs = LabelledSpinBox(
            self,
            "Subtitle Font Size",
            minimum=0,
            step=1
            )
        self.series_subtitle_pad = LabelledDoubleSpinBox(
            self,
            "Subtitle Padding",
            minimum=-100,
            maximum=100,
            step=0.1
            )
        self.series_subtitle_weight = LabelledCombobox(
            self,
            text="Subtitle "
                "Font Weight",
            items=font_weights
            )
        self.series_x_label_groupbox = QGroupBox()
        self.series_x_label_groupbox_layout = QVBoxLayout()
        self.series_x_label_groupbox.setLayout(self.series_x_label_groupbox_layout)
        self.series_x_label_groupbox.setTitle("X Label Settings")
        self.series_x_label_fn = FontComboBox(self, "X Font Label")
        self.series_x_label_fs = LabelledSpinBox(
            self,
            "X Label Font Size",
            minimum=0,
            step=1
            )
        self.series_x_label_pad = LabelledDoubleSpinBox(
            self,
            "X Label Padding",
            minimum=-100,
            maximum=100,
            step=0.1
            )
        self.series_x_label_weight = LabelledCombobox(
            self,
            text="X Label F"
                "ont Weight",
            items=font_weights
            )
        self.series_y_label_groupbox = QGroupBox()
        self.series_y_label_groupbox_layout = QVBoxLayout()
        self.series_y_label_groupbox.setLayout(self.series_y_label_groupbox_layout)
        self.series_y_label_groupbox.setTitle("Y Label Settings")
        self.series_y_tick_groupbox = QGroupBox()
        self.series_y_tick_groupbox_layout = QVBoxLayout()
        self.series_y_tick_groupbox.setLayout(self.series_y_tick_groupbox_layout)
        self.series_y_tick_groupbox.setTitle("Tick Settings")
        self.series_y_label_fn = FontComboBox(self, "Y Label Font")
        self.series_y_label_fs = LabelledSpinBox(
            self,
            "Y Label Font Size",
            minimum=0,
            step=1
            )
        self.series_y_label_pad = LabelledDoubleSpinBox(
            self,
            "Y Label Padding",
            minimum=-100,
            maximum=100,
            step=0.1
            )
        self.series_y_label_weight = LabelledCombobox(
            self,
            text="Y Label "
                "Font Weight",
            items=font_weights)
        self.series_x_ticks_pad = LabelledDoubleSpinBox(
            self,
            "X Tick Padding",
            minimum=-100,
            maximum=100,
            step=0.1
            )
        self.series_x_ticks_len = LabelledDoubleSpinBox(
            self,
            "X Tick Length",
            minimum=0,
            maximum=100,
            step=0.1
            )
        self.series_y_ticks_fn = FontComboBox(self, "Y Tick Font")
        self.series_y_ticks_fs = LabelledSpinBox(
            self,
            "Y Tick Font Size",
            minimum=0,
            step=1
            )
        self.series_y_ticks_rot = LabelledSpinBox(
            self,
            "Y Tick Rotation",
            minimum=0,
            maximum=360,
            step=1
            )
        self.series_y_ticks_pad = LabelledDoubleSpinBox(
            self,
            "Y Tick Padding",
            minimum=-100,
            maximum=100,
            step=0.1
            )
        self.series_y_ticks_weight = LabelledCombobox(
            self,
            text="Y Tick "
                "Font Weight",
            items=font_weights
            )
        self.series_y_ticks_len = LabelledDoubleSpinBox(
            self,
            "Y Tick Length",
            minimum=0,
            maximum=100,
            step=0.1
            )
        self.series_y_grid_flag = LabelledCheckbox(self, "Show Y Grid")
        self.series_y_grid_color = ColourBox(self, "Y Grid Colour")
        self.series_y_grid_linestyle = LabelledCombobox(
            self,
            text="Y Grid "
                 "Line Style",
            items=[
                '-',
                '--',
                '-.',
                ':'
               ]
            )
        self.series_y_grid_linewidth = LabelledDoubleSpinBox(
            self,
            "Y Grid Line "
            "Width"
            )
        self.series_y_grid_alpha = LabelledDoubleSpinBox(
            self,
            "Y Grid Transparency",
            minimum=0,
            maximum=1,
            step=0.1
            )
        self.series_vspace = LabelledDoubleSpinBox(
            self,
            "Plot Vertical Spacing",
            minimum=-100,
            maximum=100,
            step=0.1
            )
        self.theo_pre_groupbox = QGroupBox()
        self.theo_pre_groupbox_layout = QVBoxLayout()
        self.theo_pre_groupbox.setLayout(self.theo_pre_groupbox_layout)
        self.theo_pre_groupbox.setTitle("Dedicated PRE Settings")
        self.theo_pre_color = ColourBox(self, "Theoretical PRE Line Colour")
        self.theo_pre_lw = LabelledDoubleSpinBox(
            self,
            "Theoretical PRE Line Width",
            minimum=0,
            step=0.1
            )
        self.tag_cartoon_color = ColourBox(self, "Tag Pin Colour")
        self.tag_cartoon_lw = LabelledDoubleSpinBox(
            self,
            "Tag Pin Line Width",
            minimum=0,
            step=0.1
            )
        self.tag_cartoon_ls = LabelledCombobox(self, "Tag Pin Line Style", items=line_styles)
        self.theo_pre_groupbox.layout().addWidget(self.theo_pre_color)
        self.theo_pre_groupbox.layout().addWidget(self.theo_pre_lw)
        self.theo_pre_groupbox.layout().addWidget(self.tag_cartoon_color)
        self.theo_pre_groupbox.layout().addWidget(self.tag_cartoon_lw)
        self.theo_pre_groupbox.layout().addWidget(self.tag_cartoon_ls)
        self.series_subtitle_groupbox.layout().addWidget(self.series_subtitle_fn)
        self.series_subtitle_groupbox.layout().addWidget(self.series_subtitle_fs)
        self.series_subtitle_groupbox.layout().addWidget(self.series_subtitle_pad)
        self.series_subtitle_groupbox.layout().addWidget(self.series_subtitle_weight)
        self.series_x_label_groupbox.layout().addWidget(self.series_x_label_fn)
        self.series_x_label_groupbox.layout().addWidget(self.series_x_label_fs)
        self.series_x_label_groupbox.layout().addWidget(self.series_x_label_pad)
        self.series_x_label_groupbox.layout().addWidget(self.series_x_label_weight)
        self.layout().addWidget(self.series_subtitle_groupbox, 0, 0, 4, 1)
        self.layout().addWidget(self.series_x_label_groupbox, 0, 1, 4, 1)
        self.layout().addWidget(self.theo_pre_groupbox, 0, 2, 4, 1)
        self.series_y_label_groupbox.layout().addWidget(self.series_y_label_fn)
        self.series_y_label_groupbox.layout().addWidget(self.series_y_label_fs)
        self.series_y_label_groupbox.layout().addWidget(self.series_y_label_weight)
        self.series_y_label_groupbox.layout().addWidget(self.series_y_label_pad)
        self.layout().addWidget(self.series_y_label_groupbox, 4, 1, 4, 1)
        self.series_y_tick_groupbox.layout().addWidget(self.series_x_ticks_pad)
        self.series_y_tick_groupbox.layout().addWidget(self.series_x_ticks_len)
        self.series_y_tick_groupbox.layout().addWidget(self.series_y_ticks_fn)
        self.series_y_tick_groupbox.layout().addWidget(self.series_y_ticks_fs)
        self.series_y_tick_groupbox.layout().addWidget(self.series_y_ticks_rot)
        self.series_y_tick_groupbox.layout().addWidget(self.series_y_ticks_pad)
        self.series_y_label_groupbox.layout().addWidget(self.series_y_ticks_weight)
        self.series_y_label_groupbox.layout().addWidget(self.series_y_ticks_len)
        self.layout().addWidget(self.series_y_tick_groupbox, 4, 0, 4, 1)
        self.series_y_grid_groupbox = QGroupBox()
        self.series_y_grid_groupbox_layout = QVBoxLayout()
        self.series_y_grid_groupbox.setLayout(self.series_y_grid_groupbox_layout)
        self.series_y_grid_groupbox.setTitle("Y Grid Settings")
        self.series_y_grid_groupbox.layout().addWidget(self.series_y_grid_flag)
        self.series_y_grid_groupbox.layout().addWidget(self.series_y_grid_color)
        self.series_y_grid_groupbox.layout().addWidget(self.series_y_grid_linestyle)
        self.series_y_grid_groupbox.layout().addWidget(self.series_y_grid_linewidth)
        self.series_y_grid_groupbox.layout().addWidget(self.series_y_grid_alpha)
        self.series_y_grid_groupbox.layout().addWidget(self.series_vspace)
        self.layout().addWidget(self.series_y_grid_groupbox, 4, 2, 4, 1)
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel |
            QDialogButtonBox.RestoreDefaults
            )
        self.buttonBox.accepted.connect(self.set_values)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.get_defaults)
        self.layout().addWidget(self.buttonBox, 8, 2, 1, 1)
        self.get_values()

    def get_defaults(self):
        # dropdown
        self.series_subtitle_fn.select(self.defaults["subtitle_fn"])
        self.series_subtitle_weight.select(self.defaults["subtitle_weight"])
        self.series_x_label_fn.select(self.defaults["x_label_fn"])
        self.series_x_label_weight.select(self.defaults["x_label_weight"])
        self.series_y_label_fn.select(self.defaults["y_label_fn"])
        self.series_y_label_weight.select(self.defaults["y_label_weight"])
        self.series_y_ticks_fn.select(self.defaults["y_ticks_fn"])
        self.series_y_ticks_weight.select(self.defaults["y_ticks_weight"])
        self.series_y_grid_linestyle.select(self.defaults["y_grid_linestyle"])
        self.tag_cartoon_ls.select(self.defaults["tag_cartoon_ls"])
        # value
        self.series_subtitle_fs.setValue(self.defaults["subtitle_fs"])
        self.series_subtitle_pad.setValue(self.defaults["subtitle_pad"])
        self.series_x_label_fs.setValue(self.defaults["x_label_fs"])
        self.series_x_label_pad.setValue(self.defaults["x_label_pad"])
        self.series_y_label_fs.setValue(self.defaults["y_label_fs"])
        self.series_y_label_pad.setValue(self.defaults["y_label_pad"])
        self.series_x_ticks_pad.setValue(self.defaults["x_ticks_pad"])
        self.series_x_ticks_len.setValue(self.defaults["x_ticks_len"])
        self.series_y_ticks_fs.setValue(self.defaults["y_ticks_fs"])
        self.series_y_ticks_rot.setValue(self.defaults["y_ticks_rot"])
        self.series_y_ticks_pad.setValue(self.defaults["y_ticks_pad"])
        self.series_y_ticks_len.setValue(self.defaults["y_ticks_len"])
        self.series_y_grid_linewidth.setValue(self.defaults["y_grid_linewidth"])
        self.series_y_grid_alpha.setValue(self.defaults["y_grid_alpha"])
        self.theo_pre_lw.setValue(self.defaults["theo_pre_lw"])
        self.tag_cartoon_lw.setValue(self.defaults["tag_cartoon_lw"])
        # checked
        self.series_y_grid_flag.setChecked(self.defaults["y_grid_flag"])
        # colour
        self.series_y_grid_color.get_colour(self.defaults["y_grid_color"])
        self.theo_pre_color.get_colour(self.defaults["theo_pre_color"])
        self.tag_cartoon_color.get_colour(self.defaults["tag_cartoon_color"])

    def set_values(self):
        # dropdown
        self.local_variables["subtitle_fn"] = str(self.series_subtitle_fn.fields.currentText())
        self.local_variables["subtitle_weight"] = str(self.series_subtitle_weight.fields.currentText())
        self.local_variables["x_label_fn"] = str(self.series_x_label_fn.fields.currentText())
        self.local_variables["x_label_weight"] = str(self.series_x_label_weight.fields.currentText())
        self.local_variables["y_label_fn"] = str(self.series_y_label_fn.fields.currentText())
        self.local_variables["y_label_weight"] = str(self.series_y_label_weight.fields.currentText())
        self.local_variables["y_ticks_fn"] = str(self.series_y_ticks_fn.fields.currentText())
        self.local_variables["y_ticks_weight"] = str(self.series_y_ticks_weight.fields.currentText())
        self.local_variables["y_grid_linestyle"] = str(self.series_y_grid_linestyle.fields.currentText())
        self.local_variables["tag_cartoon_ls"] = self.tag_cartoon_ls.fields.currentText()
        # value
        self.local_variables["subtitle_fs"] = self.series_subtitle_fs.field.value()
        self.local_variables["subtitle_pad"] = self.series_subtitle_pad.field.value()
        self.local_variables["x_label_fs"] = self.series_x_label_fs.field.value()
        self.local_variables["x_label_pad"] = self.series_x_label_pad.field.value()
        self.local_variables["y_label_fs"] = self.series_y_label_fs.field.value()
        self.local_variables["y_label_pad"] = self.series_y_label_pad.field.value()
        self.local_variables["x_ticks_pad"] = self.series_x_ticks_pad.field.value()
        self.local_variables["x_ticks_len"] = self.series_x_ticks_len.field.value()
        self.local_variables["y_ticks_fs"] = self.series_y_ticks_fs.field.value()
        self.local_variables["y_ticks_rot"] = self.series_y_ticks_rot.field.value()
        self.local_variables["y_ticks_pad"] = self.series_y_ticks_pad.field.value()
        self.local_variables["y_ticks_len"] = self.series_y_ticks_len.field.value()
        self.local_variables["y_grid_linewidth"] = self.series_y_grid_linewidth.field.value()
        self.local_variables["y_grid_alpha"] = self.series_y_grid_alpha.field.value()
        self.local_variables["theo_pre_lw"] = self.theo_pre_lw.field.value()
        self.local_variables["tag_cartoon_lw"] = self.tag_cartoon_lw.field.value()
        # colours
        self.local_variables["y_grid_color"] = str(self.series_y_grid_color.fields.currentText())
        self.local_variables["theo_pre_color"] = self.theo_pre_color.fields.currentText()
        self.local_variables["tag_cartoon_color"] = self.tag_cartoon_color.fields.currentText()
        # checked
        self.local_variables["y_grid_flag"] = self.series_y_grid_flag.isChecked()
        self.accept()

    def get_values(self):
        # select
        self.series_subtitle_fn.select(self.local_variables["subtitle_fn"])
        self.series_subtitle_weight.select(self.local_variables["subtitle_weight"])
        self.series_x_label_fn.select(self.local_variables["x_label_fn"])
        self.series_x_label_weight.select(self.local_variables["x_label_weight"])
        self.series_y_label_fn.select(self.local_variables["y_label_fn"])
        self.series_y_label_weight.select(self.local_variables["y_label_weight"])
        self.series_y_ticks_fn.select(self.local_variables["y_ticks_fn"])
        self.series_y_ticks_weight.select(self.local_variables["y_ticks_weight"])
        self.series_y_grid_linestyle.select(self.local_variables["y_grid_linestyle"])
        self.tag_cartoon_ls.select(self.local_variables["tag_cartoon_ls"])
        # value
        self.series_subtitle_fs.setValue(self.local_variables["subtitle_fs"])
        self.series_subtitle_pad.setValue(self.local_variables["subtitle_pad"])
        self.series_x_label_fs.setValue(self.local_variables["x_label_fs"])
        self.series_x_label_pad.setValue(self.local_variables["x_label_pad"])
        self.series_y_label_fs.setValue(self.local_variables["y_label_fs"])
        self.series_y_label_pad.setValue(self.local_variables["y_label_pad"])
        self.series_x_ticks_pad.setValue(self.local_variables["x_ticks_pad"])
        self.series_x_ticks_len.setValue(self.local_variables["x_ticks_len"])
        self.series_y_ticks_fs.setValue(self.local_variables["y_ticks_fs"])
        self.series_y_ticks_rot.setValue(self.local_variables["y_ticks_rot"])
        self.series_y_ticks_pad.setValue(self.local_variables["y_ticks_pad"])
        self.series_y_ticks_len.setValue(self.local_variables["y_ticks_len"])
        self.series_y_grid_linewidth.setValue(self.local_variables["y_grid_linewidth"])
        self.series_y_grid_alpha.setValue(self.local_variables["y_grid_alpha"])
        self.theo_pre_lw.setValue(self.local_variables["theo_pre_lw"])
        self.tag_cartoon_lw.setValue(self.local_variables["tag_cartoon_lw"])
        # colour
        self.series_y_grid_color.get_colour(self.local_variables["y_grid_color"])
        self.theo_pre_color.get_colour(self.local_variables["theo_pre_color"])
        self.tag_cartoon_color.get_colour(self.local_variables["tag_cartoon_color"])
        # checked
        self.series_y_grid_flag.setChecked(self.local_variables["y_grid_flag"])
