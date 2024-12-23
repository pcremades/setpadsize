import pcbnew
import wx
import os

def set_pad_size(pcb, diameter, padTypes):
    for footprint in pcb.GetFootprints():
        for pad in footprint.Pads():
            if pad.GetShape() in padTypes:
                pad.SetSize(pcbnew.VECTOR2I_MM(diameter, diameter))
                # print(pad.GetShape())
            # print(f"Set pad diameter of pad {pad.GetPadName()} to {diameter}mm")

class DiameterDialog(wx.Dialog):
    def __init__(self, parent, title):
        super(DiameterDialog, self).__init__(parent, title=title, size=(250, 250))
        self.init_ui()
        self.SetSizeHints(250, 250, 250, 250)
        self.Centre()
        self.padTypes = []

    def init_ui(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Pad Diameter (mm)')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(self, value="1.6")
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.VERTICAL)
        st2 = wx.StaticText(self, label='Pad Shape')
        self.checkCircle = wx.CheckBox(self, label='Circle', )
        self.checkCircle.SetValue(True)
        self.checkRect = wx.CheckBox(self, label='Rectalgular')
        self.checkOval = wx.CheckBox(self, label='Oval')
        hbox2.Add(st2, flag=wx.LEFT, border=8)
        hbox2.Add(self.checkCircle)
        hbox2.Add(self.checkRect)
        hbox2.Add(self.checkOval)
        vbox.Add(hbox2, flag=wx.ALIGN_LEFT|wx.TOP|wx.BOTTOM, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox3.Add(okButton)
        hbox3.Add(closeButton, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox3, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.on_ok)
        closeButton.Bind(wx.EVT_BUTTON, self.on_close)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_close(self, event):
        self.EndModal(wx.ID_CANCEL)

    def get_diameter(self):
        return float(self.tc.GetValue())

    def get_pad_types(self):
        if self.checkCircle.IsChecked():
            self.padTypes.append(pcbnew.PAD_SHAPE_CIRCLE)
        if self.checkRect.IsChecked():
            self.padTypes.append(pcbnew.PAD_SHAPE_RECT)
        if self.checkOval.IsChecked():
            self.padTypes.append(pcbnew.PAD_SHAPE_OVAL)
        return self.padTypes

class SetPadSizePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Set Pad Diameter"
        self.category = "Modify PCB"
        self.description = "Sets the pad diameter of all pads in the PCB."
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.dark_icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        pcb = pcbnew.GetBoard()

        # Create an instance of wx.App if it doesn't already exist
        if not wx.GetApp():
            app = wx.App(False)
        else:
            app = wx.GetApp()

        dialog = DiameterDialog(None, title="Set Pad Size")
        if dialog.ShowModal() == wx.ID_OK:
            diameter = dialog.get_diameter()
            padTypes = dialog.get_pad_types()
            print(f"Setting pad size to {diameter}mm")
            set_pad_size(pcb, diameter, padTypes)
            pcbnew.Refresh()
            print("Pad size setting completed.")
            print(f'Pads: {padTypes}')
        dialog.Destroy()

SetPadSizePlugin().register()
