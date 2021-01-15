# CramSchoolApp
***
## 分工
+ SRS:全員
+ SDD:全員
+ STD:
  + 單元測試規劃:邵安祺、呂儀安、曾清兒、梁晏慈
  + 單元測試人員:廖子權、林湘羚、謝宛蓉
  + 系統測試規劃:呂儀安、曾清兒、廖子權、邵安祺
  + 系統測試人員：林湘羚、謝宛蓉、梁晏慈
+ 廖子權:系統框架、資料庫設計、資料庫維護及復原、登入API撰寫、系統上架
+ 謝宛蓉:學生後端API撰寫、老師後端API撰寫、學生後端Models撰寫、老師後端Models撰寫、資料庫設計
+ 林湘羚:補習班後端API撰寫、補習班後端Models撰寫、資料庫設計
+ 梁晏慈:補習班_首頁頁面、補習班_課程頁面、補習班_成員列表頁面、補習班_出缺勤頁面、補習班_補課頁面、補習班_教室頁面
+ 邵安祺:登入頁面、學生_首頁頁面、學生_課程進度頁面、學生_課程作業頁面、學生_考試成績頁面、學生_出缺勤紀錄頁面、學生個人計畫頁面、學生預約補課頁面
+ 呂儀安:老師_學生頁面、老師_成績頁面、老師_出缺勤頁面
+ 曾清兒:老師_首頁頁面、老師_課程資訊頁面、老師_聯絡簿頁面、老師_各人計畫頁面
*** 
## Github & Trello
+ [Github](https://github.com/LiaozhiCheng/CramSchoolApp)
+ [Trello](https://trello.com/b/1oxtUZNC/cs%E7%AE%A1%E7%90%86%E7%B3%BB%E7%B5%B1)
***
## server網址與使用者帳號密碼
+ [server](http://140.121.197.130:55001/)
+ account
  + cram school account
    + user name:handsomeboy
    + password:beautifulgirl
  + teacher account
    + user name:110-T-001
    + password:001
    + user name:110-T-002
    + password:002
    + user name:110-T-003
    + password:003
           .
           .
           .
  + student account
    + user name:110-S-011
    + password:011
    + user name:110-S-012
    + password:012
    + user name:110-S-013
    + password:013
    + user name:110-S-014
    + password:014
    + user name:110-S-015
    + password:015
          .
          .
          .
***
## 提升流程品質或系統品質的措施
+ 開發流程
  + 使用github進行版本控管
  + 使用flask-security的MVC進行後端控管
  + 檔案命名規則遵守Google Python風格指南
+ 系統品質
  + 所有api通過flask-testing測試並達成statement coverage的白箱測試
  + 使用JMeter對系統進行壓力測試
## 系統展示影片
[展示影片](https://www.youtube.com/watch?v=30EMtj8fYA8)
