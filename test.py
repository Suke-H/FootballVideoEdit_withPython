ループさせるimport wx

# ボタンのクリックイベント
def click(event):
    input_text = None

    #テキストがキーボード入力されるまでループさせる
    while not input_text:
        # テキスト入力ダイアログ
        dlg = wx.TextEntryDialog(None, u'テキストを入力してください', u'タイトル部分')
        dlg.ShowModal()

        # 入力値を取得
        input_text = dlg.GetValue()
        print(input_text)

        if not input_text:
            # メッセージボックスを表示
            wx.MessageBox(u'1文字以上入力してください', u'入力エラー')

    # 入力値をステータスバーに表示する
    frame.SetStatusText(input_text)


app = wx.App()

frame = wx.Frame(None, -1, u'タイトル', size=(200, 200))
frame.CreateStatusBar()
p = wx.Panel(frame, -1)

button = wx.Button(p, -1, u'ボタン')
button.Bind(wx.EVT_BUTTON, click)

frame.Show()
app.MainLoop()