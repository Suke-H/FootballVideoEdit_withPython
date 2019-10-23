import wx

class FileDropTarget(wx.FileDropTarget):
    """ Drag & Drop Class """
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, files):
        print(y, files)
        if y <= 100:
            print("wide")
        else:
            print("verch")

        return 0


class App(wx.Frame):
    """ GUI """
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(400, 400), style=wx.DEFAULT_FRAME_STYLE)

        # パネル
        DDPanel = wx.Panel(self, -1)
        DDPanel.SetBackgroundColour("green")
        EditPanel = wx.Panel(self, -1)
        EditPanel.SetBackgroundColour("red")

        # パネルのレイアウト
        PanelLayout = wx.BoxSizer(wx.VERTICAL)
        PanelLayout.Add(DDPanel, proportion=1, flag=wx.EXPAND)
        PanelLayout.Add(EditPanel, proportion=1, flag=wx.EXPAND)
        self.SetSizer(PanelLayout)

        ###DDpanel###############################################

        # ラベル
        wideLabel = wx.StaticText(DDPanel, -1, 'wideのフォルダをドラッグ＆ドロップ', style=wx.SIMPLE_BORDER | wx.TE_CENTER)
        wideLabel.SetBackgroundColour("#e0ffff")
        verchLabel = wx.StaticText(DDPanel, -1, 'verchのフォルダをドラッグ＆ドロップ', style=wx.SIMPLE_BORDER | wx.TE_CENTER)
        verchLabel.SetBackgroundColour("#e0ffff")

        # DDpanelをドロップ対象に設定
        DDPanel.SetDropTarget(FileDropTarget(self))

        # DDpanelの中身をレイアウト
        DDLayout = wx.BoxSizer(wx.HORIZONTAL)
        DDLayout.Add(wideLabel, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        DDLayout.Add(verchLabel, proportion=1, flag=wx.EXPAND | wx.LEFT, border=5)
        DDPanel.SetSizer(DDLayout)

        ##############################################################
        
        self.Show()

app = wx.App()
App(None, -1, 'タイトル')
app.MainLoop()