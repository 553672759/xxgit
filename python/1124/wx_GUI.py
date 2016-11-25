#coding:utf8
'''
Created on 2016-11-25

@author: xx
'''
#wxpython的GUI
'''
按钮Button
    文本按钮wx.Button
    位图按钮wx.BitmapButton
    开关按钮wx.toggleButton
绑定处理按钮点击的事件
菜单
    MenuBar菜单栏
    Menu菜单
    MenuItem菜单下命令
静态文本框wx.StaticText
文本框
列表
    wx.LC_ICON
单选\复选框

'''
import wx
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="hello python,wxPython")
        #创建一个容器
        panel=wx.Panel(self)
        #创建一个sizer,方向为垂直方向
        sizer=wx.BoxSizer(wx.VERTICAL)
        self.text1=wx.TextCtrl(panel,value="Hello World!",size=(200,180),style=wx.TE_MULTILINE)
        sizer.Add(self.text1,0,wx.ALIGN_TOP | wx.EXPAND)
        button=wx.Button(panel,label="Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
    def OnClick(self,text):
        self.text1.AppendText("\nHello World!")

if __name__=='__main__':
    app=wx.App()
    frame=Frame1(None)
    frame.Show(True)
    app.MainLoop()
    
'''
布局管理
    sizer灵活布局方案(窗口改变会自动改变)
    wx.BoxSizer        垂直,水平,填满窗体
    wx.FlexGridSizer   行高列宽由最大的决定
    wx.GridSizer       组件大小一直
    
    
    绝对定位
'''
        
        
        
