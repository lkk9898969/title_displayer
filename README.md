Title displayer  
可顯示任意視窗上的標題  
針對 **VLC** 及 **edge的youtube分頁** 有做優化

*以下為舊版介紹 :  
chrome-edge_title_displayer  
針對edge youtube做的。主要功能為顯示Youtube影片標題。  
支援Edge及Chrome瀏覽器。  
要觸發必須開啟Youtube分頁才能啟動顯示功能，  
顯示功能啟動後則可顯示任意網頁的標題。*

## 2024/1/26更新:
主程式所有window controller重構、所有UI.py重構  
新增物件detectelement，作為偵測視窗的主物件  
新增"自行選擇視窗"功能，可選擇有標題的視窗進行顯示。

## 2023/12/16更新:
更新啟動後介面 : 需先選擇要偵測的視窗標題樣式。  
追加支援 VLC media player。  
UI架構重新建構。將UI介面分開為單一py檔案。

### **注意事項 :**
1.~~不支援相同視窗標題樣式但顯示不同實例的標題。(ex:可能無法正確偵測兩個(或以上)不同的VLC media player)~~(2024/1/26更新後)使用"自行選擇視窗"可指定特定視窗  
2.Chrome瀏覽器可能不支援(2023/12/16更新後)