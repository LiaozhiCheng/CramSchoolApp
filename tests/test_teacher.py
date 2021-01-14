from . import SettingBase
from flask import url_for,jsonify
import json

class CheckTeacherAPI(SettingBase):
    def test_personal_info(self):
        self.user_id = '110-T-008'
        self.password = '008'
        self.signin()
        response = self.client.get(url_for('teacher_api.user_personal_info') + "?student_id=110-S-098")
        expected_output = {"user_id": "110-S-098",
                           "name": "西莉雅‧坎圖",
                           "phone": "0934283790",
                           "email": "S098@gmail.com.tw",
                           "role": "student"}
        self.assertEquals(response.json, expected_output)
        self.logout()
    def test_course_communication_book(self):
        self.user_id = '110-T-007'
        self.password = '007'
        self.signin()
        response = self.client.get(url_for('teacher_api.course_communication_book') + "?course_id=C-009")
        expected_output = [
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-000", 
                                "lesson_time": "2020-09-01", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-001", 
                                "lesson_time": "2020-09-08", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-002", 
                                "lesson_time": "2020-09-15", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-003", 
                                "lesson_time": "2020-09-22", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-004", 
                                "lesson_time": "2020-09-29", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-005", 
                                "lesson_time": "2020-10-06", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-006", 
                                "lesson_time": "2020-10-13", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-007", 
                                "lesson_time": "2020-10-20", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-008", 
                                "lesson_time": "2020-10-27", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-009", 
                                "lesson_time": "2020-11-03", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-010", 
                                "lesson_time": "2020-11-10", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-011", 
                                "lesson_time": "2020-11-17", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-012", 
                                "lesson_time": "2020-11-24", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-013", 
                                "lesson_time": "2020-12-01", 
                                "progress": ""
                              }, 
                              {
                                "context": "", 
                                "deadline": "2021-02-01", 
                                "lesson_id": "L-009-014", 
                                "lesson_time": "2020-12-08", 
                                "progress": ""
                              }
                            ]
        self.assertEquals(list(response.json), expected_output)

    def test_edit_course_communication_book(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        input_data = {
                        "lesson_id" : "L-013-000",
                        "lesson_time" : "2020-09-01",
                        "progress" : "英文第一課",
                        "deadline" : "2021-01-13",
                        "context": "Workbook p2~p5,單字本1~10"
                    }
        response = self.client.post(url_for('teacher_api.edit_course_communication_book') ,data = json.dumps(input_data), content_type="application/json")
        expected_output = {"homework":{
                                    "context" : "Workbook p2~p5,單字本1~10",
                                    "deadline" : "Wed, 13 Jan 2021 00:00:00 GMT" },
                          "progress":"英文第一課"}
        self.assertEquals(response.json, expected_output)
        self.logout()
        
    def test_edit_course_communication_book_2(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        input_data = {
                        "lesson_id" : "L-013-000",
                        "lesson_time" : "2020-09-01",
                        "progress" : "",
                        "deadline" : "2021-01-13",
                        "context": ""
                    }
        response = self.client.post(url_for('teacher_api.edit_course_communication_book') ,data = json.dumps(input_data), content_type="application/json")
        expected_output = { "message": "資料不得為空" }
        self.assertEquals(response.json, expected_output)
        self.logout()
        
    def test_delete_course_communication_book(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        response = self.client.post(url_for('teacher_api.delete_course_communication_book') + "?lesson_id=L-013-000")
        expected_output = {
                            "homework":{
                            "context": "",
                            "deadline":""},
                            "progress":""}
        self.assertEquals(response.json, expected_output)
        self.logout()
    def test_course_personal_plan(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        response = self.client.post(url_for('teacher_api.course_personal_plan') + "?course_id=C-013&student_id=110-S-100")
        expected_output = []
        self.assertEquals(list(response.json), expected_output)
        self.logout()
        
    def test_teacher_no_plan_lesson_time(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        response = self.client.post(url_for('teacher_api.teacher_no_plan_lesson_time') + "?course_id=C-005&student_id=110-S-086")
        expected_output = [{
                              "lesson_id": "L-005-000", 
                              "lesson_time": "2020-09-01"
                            }, 
                            {
                              "lesson_id": "L-005-001", 
                              "lesson_time": "2020-09-08"
                            }, 
                            {
                              "lesson_id": "L-005-002", 
                              "lesson_time": "2020-09-15"
                            }, 
                            {
                              "lesson_id": "L-005-003", 
                              "lesson_time": "2020-09-22"
                            }, 
                            {
                              "lesson_id": "L-005-004", 
                              "lesson_time": "2020-09-29"
                            }, 
                            {
                              "lesson_id": "L-005-005", 
                              "lesson_time": "2020-10-06"
                            }, 
                            {
                              "lesson_id": "L-005-006", 
                              "lesson_time": "2020-10-13"
                            }, 
                            {
                              "lesson_id": "L-005-007", 
                              "lesson_time": "2020-10-20"
                            }, 
                            {
                              "lesson_id": "L-005-008", 
                              "lesson_time": "2020-10-27"
                            }, 
                            {
                              "lesson_id": "L-005-009", 
                              "lesson_time": "2020-11-03"
                            }, 
                            {
                              "lesson_id": "L-005-010", 
                              "lesson_time": "2020-11-10"
                            }, 
                            {
                              "lesson_id": "L-005-011", 
                              "lesson_time": "2020-11-17"
                            }, 
                            {
                              "lesson_id": "L-005-012", 
                              "lesson_time": "2020-11-24"
                            }, 
                            {
                              "lesson_id": "L-005-013", 
                              "lesson_time": "2020-12-01"
                            }, 
                            {
                              "lesson_id": "L-005-014", 
                              "lesson_time": "2020-12-08"
                            }]
        self.assertEquals(list(response.json), expected_output)
        self.logout()
        
    def test_edit_course_personal_plan(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        input_data = {
                        "lesson_id" : "L-013-000",
                        "student_id" : "110-S-098",
                        "deadline" : "2021-01-13",
                        "context": "單字考不及格，罰寫單字1~10五遍"
                    }
        response = self.client.post(url_for('teacher_api.edit_course_personal_plan') ,data = json.dumps(input_data), content_type="application/json")
        expected_output = {"context": "單字考不及格，罰寫單字1~10五遍",
                           "deadline": "2021-01-13", 
                           "lesson_id": "L-013-000"}
        self.assertEquals(response.json, expected_output)
        self.logout()
        
    def test_edit_course_personal_plan_2(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        input_data = {
                        "lesson_id" : "L-013-000",
                        "student_id" : "110-S-098",
                        "deadline" : "2021-01-20",
                        "context": "上課不認真，回去抄五遍課文"
                    }
        response = self.client.post(url_for('teacher_api.edit_course_personal_plan') ,data = json.dumps(input_data), content_type="application/json")
        expected_output = {"context": "上課不認真，回去抄五遍課文",
                           "deadline": "2021-01-20", 
                           "lesson_id": "L-013-000"}
        self.assertEquals(response.json, expected_output)
        self.logout()
    def test_edit_course_personal_plan_3(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        input_data = {
                        "lesson_id" : "L-013-000",
                        "student_id" : "110-S-098",
                        "deadline" : "2021-01-20",
                        "context": ""
                    }
        response = self.client.post(url_for('teacher_api.edit_course_personal_plan') ,data = json.dumps(input_data), content_type="application/json")
        expected_output = { "message": "資料不得為空"}
        self.assertEquals(response.json, expected_output)
        self.logout()
        
    def test_delete_course_personal_plan(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        input_data = {
                        "lesson_id" : "L-013-000",
                        "student_id" : "110-S-098",
                        "deadline" : "2021-01-20",
                        "context": "上課不認真，回去抄五遍課文"
                    }
        response = self.client.post(url_for('teacher_api.delete_course_personal_plan') ,data = json.dumps(input_data), content_type="application/json")
        expected_output = {"context": "上課不認真，回去抄五遍課文",
                           "deadline": "2021-01-20", 
                           "lesson_id": "L-013-000"}
        self.assertEquals(response.json, expected_output)
        self.logout()
    def test_course_student_list(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        response = self.client.get(url_for('teacher_api.course_student_list') + "?course_id=C-016")
        expected_output = [
          {
            "email": "S014@gmail.com.tw", 
            "phone": "0980977455", 
            "student_id": "110-S-014", 
            "student_name": "德斯蒙德‧科爾"
          }, 
          {
            "email": "S031@gmail.com.tw", 
            "phone": "0979528457", 
            "student_id": "110-S-031", 
            "student_name": "毛理斯‧該隱"
          }, 
          {
            "email": "S042@gmail.com.tw", 
            "phone": "0924304431", 
            "student_id": "110-S-042", 
            "student_name": "卡萊布‧沃森"
          }, 
          {
            "email": "S053@gmail.com.tw", 
            "phone": "0926309558", 
            "student_id": "110-S-053", 
            "student_name": "查理‧唐納森"
          }, 
          {
            "email": "S036@gmail.com.tw", 
            "phone": "0968924440", 
            "student_id": "110-S-036", 
            "student_name": "彭妮‧赫爾"
          }, 
          {
            "email": "S056@gmail.com.tw", 
            "phone": "0973533295", 
            "student_id": "110-S-056", 
            "student_name": "科恩‧巴克斯特"
          }, 
          {
            "email": "S027@gmail.com.tw", 
            "phone": "0997089161", 
            "student_id": "110-S-027", 
            "student_name": "艾登‧美世"
          }, 
          {
            "email": "S043@gmail.com.tw", 
            "phone": "0953273522", 
            "student_id": "110-S-043", 
            "student_name": "福雷斯特‧居伊"
          }, 
          {
            "email": "S065@gmail.com.tw", 
            "phone": "0945596148", 
            "student_id": "110-S-065", 
            "student_name": "福斯特‧弗羅斯特"
          }, 
          {
            "email": "S017@gmail.com.tw", 
            "phone": "0911177203", 
            "student_id": "110-S-017", 
            "student_name": "埃絲特‧羅薩裡奧"
          }, 
          {
            "email": "S087@gmail.com.tw", 
            "phone": "0930336796", 
            "student_id": "110-S-087", 
            "student_name": "伊芙琳‧布萊克"
          }, 
          {
            "email": "S098@gmail.com.tw", 
            "phone": "0934283790", 
            "student_id": "110-S-098", 
            "student_name": "西莉雅‧坎圖"
          }, 
          {
            "email": "S094@gmail.com.tw", 
            "phone": "0954571847", 
            "student_id": "110-S-094", 
            "student_name": "賈希敏‧特雷爾"
          }, 
          {
            "email": "S024@gmail.com.tw", 
            "phone": "0947555381", 
            "student_id": "110-S-024", 
            "student_name": "茱莉安娜‧基"
          }, 
          {
            "email": "S077@gmail.com.tw", 
            "phone": "0977981879", 
            "student_id": "110-S-077", 
            "student_name": "撒迦利亞‧尼貝爾"
          }, 
          {
            "email": "S012@gmail.com.tw", 
            "phone": "0974192616", 
            "student_id": "110-S-012", 
            "student_name": "戴倫‧裴斯"
          }, 
          {
            "email": "S016@gmail.com.tw", 
            "phone": "0933788878", 
            "student_id": "110-S-016", 
            "student_name": "魯迪‧米勒"
          }, 
          {
            "email": "S044@gmail.com.tw", 
            "phone": "0931974326", 
            "student_id": "110-S-044", 
            "student_name": "艾爾弗雷德‧伯吉斯"
          }, 
          {
            "email": "S100@gmail.com.tw", 
            "phone": "0930483068", 
            "student_id": "110-S-100", 
            "student_name": "魯思‧惠特克"
          }, 
          {
            "email": "S019@gmail.com.tw", 
            "phone": "0970534585", 
            "student_id": "110-S-019", 
            "student_name": "佩內洛普‧傑克遜"
          }, 
          {
            "email": "S039@gmail.com.tw", 
            "phone": "0984936035", 
            "student_id": "110-S-039", 
            "student_name": "布蘭森‧佩雷斯"
          }, 
          {
            "email": "S091@gmail.com.tw", 
            "phone": "0950370398", 
            "student_id": "110-S-091", 
            "student_name": "克萊德‧格洛弗"
          }, 
          {
            "email": "S055@gmail.com.tw", 
            "phone": "0967404060", 
            "student_id": "110-S-055", 
            "student_name": "傑克遜‧查韋斯"
          }, 
          {
            "email": "S072@gmail.com.tw", 
            "phone": "0962350407", 
            "student_id": "110-S-072", 
            "student_name": "喬丹‧莫雷諾"
          }, 
          {
            "email": "S085@gmail.com.tw", 
            "phone": "0950890657", 
            "student_id": "110-S-085", 
            "student_name": "麗賈娜‧信斯"
          }, 
          {
            "email": "S020@gmail.com.tw", 
            "phone": "0994177911", 
            "student_id": "110-S-020", 
            "student_name": "帕特理克‧考夫曼"
          }
        ]
        self.assertEquals(list(response.json), expected_output)
        self.logout()
        
    def test_course_attendence(self):
        self.user_id = "110-T-003"
        self.password = "003"
        response = self.client.get(url_for('teacher_api.course_attendence') + "?course_id=C-001")
        expected_output = [
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-09-01"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-09-08"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-09-15"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-09-22"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-09-29"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-10-06"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-10-13"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-10-20"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-10-27"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-11-03"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-11-10"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-11-17"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-11-24"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-12-01"
  }, 
  {
    "attendence_list": [
      {
        "email": "S014@gmail.com.tw", 
        "phone": "0980977455", 
        "state": True, 
        "student_id": "110-S-014", 
        "student_name": "德斯蒙德‧科爾"
      }, 
      {
        "email": "S031@gmail.com.tw", 
        "phone": "0979528457", 
        "state": True, 
        "student_id": "110-S-031", 
        "student_name": "毛理斯‧該隱"
      }, 
      {
        "email": "S042@gmail.com.tw", 
        "phone": "0924304431", 
        "state": True, 
        "student_id": "110-S-042", 
        "student_name": "卡萊布‧沃森"
      }, 
      {
        "email": "S053@gmail.com.tw", 
        "phone": "0926309558", 
        "state": True, 
        "student_id": "110-S-053", 
        "student_name": "查理‧唐納森"
      }, 
      {
        "email": "S036@gmail.com.tw", 
        "phone": "0968924440", 
        "state": True, 
        "student_id": "110-S-036", 
        "student_name": "彭妮‧赫爾"
      }, 
      {
        "email": "S056@gmail.com.tw", 
        "phone": "0973533295", 
        "state": True, 
        "student_id": "110-S-056", 
        "student_name": "科恩‧巴克斯特"
      }, 
      {
        "email": "S027@gmail.com.tw", 
        "phone": "0997089161", 
        "state": True, 
        "student_id": "110-S-027", 
        "student_name": "艾登‧美世"
      }, 
      {
        "email": "S043@gmail.com.tw", 
        "phone": "0953273522", 
        "state": True, 
        "student_id": "110-S-043", 
        "student_name": "福雷斯特‧居伊"
      }, 
      {
        "email": "S065@gmail.com.tw", 
        "phone": "0945596148", 
        "state": True, 
        "student_id": "110-S-065", 
        "student_name": "福斯特‧弗羅斯特"
      }, 
      {
        "email": "S017@gmail.com.tw", 
        "phone": "0911177203", 
        "state": True, 
        "student_id": "110-S-017", 
        "student_name": "埃絲特‧羅薩裡奧"
      }, 
      {
        "email": "S087@gmail.com.tw", 
        "phone": "0930336796", 
        "state": True, 
        "student_id": "110-S-087", 
        "student_name": "伊芙琳‧布萊克"
      }, 
      {
        "email": "S098@gmail.com.tw", 
        "phone": "0934283790", 
        "state": True, 
        "student_id": "110-S-098", 
        "student_name": "西莉雅‧坎圖"
      }, 
      {
        "email": "S094@gmail.com.tw", 
        "phone": "0954571847", 
        "state": True, 
        "student_id": "110-S-094", 
        "student_name": "賈希敏‧特雷爾"
      }, 
      {
        "email": "S024@gmail.com.tw", 
        "phone": "0947555381", 
        "state": True, 
        "student_id": "110-S-024", 
        "student_name": "茱莉安娜‧基"
      }, 
      {
        "email": "S077@gmail.com.tw", 
        "phone": "0977981879", 
        "state": True, 
        "student_id": "110-S-077", 
        "student_name": "撒迦利亞‧尼貝爾"
      }, 
      {
        "email": "S012@gmail.com.tw", 
        "phone": "0974192616", 
        "state": True, 
        "student_id": "110-S-012", 
        "student_name": "戴倫‧裴斯"
      }, 
      {
        "email": "S016@gmail.com.tw", 
        "phone": "0933788878", 
        "state": True, 
        "student_id": "110-S-016", 
        "student_name": "魯迪‧米勒"
      }, 
      {
        "email": "S044@gmail.com.tw", 
        "phone": "0931974326", 
        "state": True, 
        "student_id": "110-S-044", 
        "student_name": "艾爾弗雷德‧伯吉斯"
      }, 
      {
        "email": "S100@gmail.com.tw", 
        "phone": "0930483068", 
        "state": True, 
        "student_id": "110-S-100", 
        "student_name": "魯思‧惠特克"
      }, 
      {
        "email": "S019@gmail.com.tw", 
        "phone": "0970534585", 
        "state": True, 
        "student_id": "110-S-019", 
        "student_name": "佩內洛普‧傑克遜"
      }, 
      {
        "email": "S039@gmail.com.tw", 
        "phone": "0984936035", 
        "state": True, 
        "student_id": "110-S-039", 
        "student_name": "布蘭森‧佩雷斯"
      }, 
      {
        "email": "S091@gmail.com.tw", 
        "phone": "0950370398", 
        "state": True, 
        "student_id": "110-S-091", 
        "student_name": "克萊德‧格洛弗"
      }, 
      {
        "email": "S055@gmail.com.tw", 
        "phone": "0967404060", 
        "state": True, 
        "student_id": "110-S-055", 
        "student_name": "傑克遜‧查韋斯"
      }, 
      {
        "email": "S072@gmail.com.tw", 
        "phone": "0962350407", 
        "state": True, 
        "student_id": "110-S-072", 
        "student_name": "喬丹‧莫雷諾"
      }, 
      {
        "email": "S085@gmail.com.tw", 
        "phone": "0950890657", 
        "state": True, 
        "student_id": "110-S-085", 
        "student_name": "麗賈娜‧信斯"
      }, 
      {
        "email": "S020@gmail.com.tw", 
        "phone": "0994177911", 
        "state": True, 
        "student_id": "110-S-020", 
        "student_name": "帕特理克‧考夫曼"
      }
    ], 
    "lesson_time": "2020-12-08"
  }
]
        
        self.assertEquals(response.json, expected_output)
        self.signin()
    
    def test_course_grade(self):
        self.user_id = "110-T-008"
        self.password = "008"
        self.signin()
        response = self.client.get(url_for('teacher_api.course_grade') + "?course_id=C-016")
        expected_output = [
              {
                "grade_list": [
                  {
                    "student_grade": 5, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 10, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 15, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 20, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 25, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 30, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 35, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 40, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 45, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 50, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 55, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 90, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 95, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-091"
                  }
                ], 
                "lesson_id": "L-016-000", 
                "lesson_time": "2020-09-01", 
                "quiz_name": "test0"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 95, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 62, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 91, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 67, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 61, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 91, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 76, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 62, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 61, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 90, 
                    "student_name": "110-S-039"
                  }
                ], 
                "lesson_id": "L-016-001", 
                "lesson_time": "2020-09-08", 
                "quiz_name": "test1"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 62, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 64, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 91, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 88, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 90, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 98, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 64, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 78, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 94, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-077"
                  }
                ], 
                "lesson_id": "L-016-002", 
                "lesson_time": "2020-09-15", 
                "quiz_name": "test2"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 67, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 72, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 97, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 91, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 89, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 92, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 74, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 93, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-031"
                  }
                ], 
                "lesson_id": "L-016-003", 
                "lesson_time": "2020-09-22", 
                "quiz_name": "test3"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 89, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 78, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 67, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 74, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 72, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 78, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 74, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-100"
                  }
                ], 
                "lesson_id": "L-016-004", 
                "lesson_time": "2020-09-29", 
                "quiz_name": "test4"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 97, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 89, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 76, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 78, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 88, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 92, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 64, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-014"
                  }
                ], 
                "lesson_id": "L-016-005", 
                "lesson_time": "2020-10-06", 
                "quiz_name": "test5"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 93, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 89, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 91, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 98, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 72, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 78, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 98, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 64, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 93, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 61, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 62, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 90, 
                    "student_name": "110-S-087"
                  }
                ], 
                "lesson_id": "L-016-006", 
                "lesson_time": "2020-10-13", 
                "quiz_name": "test6"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 93, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 72, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 92, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 95, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 78, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-031"
                  }
                ], 
                "lesson_id": "L-016-007", 
                "lesson_time": "2020-10-20", 
                "quiz_name": "test7"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 76, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 88, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 97, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 97, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-094"
                  }
                ], 
                "lesson_id": "L-016-008", 
                "lesson_time": "2020-10-27", 
                "quiz_name": "test8"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 95, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 62, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 97, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 74, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 76, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-016"
                  }
                ], 
                "lesson_id": "L-016-009", 
                "lesson_time": "2020-11-03", 
                "quiz_name": "test9"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 98, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 64, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 95, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 65, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 61, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 94, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 74, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 64, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 82, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 97, 
                    "student_name": "110-S-024"
                  }
                ], 
                "lesson_id": "L-016-010", 
                "lesson_time": "2020-11-10", 
                "quiz_name": "test10"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 63, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 89, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 72, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 91, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 97, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 61, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 94, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 99, 
                    "student_name": "110-S-065"
                  }
                ], 
                "lesson_id": "L-016-011", 
                "lesson_time": "2020-11-17", 
                "quiz_name": "test11"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 89, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 62, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 95, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 86, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 76, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 79, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 84, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 60, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 90, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 77, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 66, 
                    "student_name": "110-S-087"
                  }
                ], 
                "lesson_id": "L-016-012", 
                "lesson_time": "2020-11-24", 
                "quiz_name": "test12"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 75, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 93, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 100, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 81, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 61, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 61, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 70, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 83, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 68, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 88, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 89, 
                    "student_name": "110-S-091"
                  }, 
                  {
                    "student_grade": 69, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 88, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 96, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 80, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 87, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 73, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 92, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 85, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 71, 
                    "student_name": "110-S-100"
                  }
                ], 
                "lesson_id": "L-016-013", 
                "lesson_time": "2020-12-01", 
                "quiz_name": "test13"
              }, 
              {
                "grade_list": [
                  {
                    "student_grade": 0, 
                    "student_name": "110-S-044"
                  }, 
                  {
                    "student_grade": 1, 
                    "student_name": "110-S-039"
                  }, 
                  {
                    "student_grade": 2, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": 3, 
                    "student_name": "110-S-014"
                  }, 
                  {
                    "student_grade": 4, 
                    "student_name": "110-S-100"
                  }, 
                  {
                    "student_grade": 5, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": 6, 
                    "student_name": "110-S-042"
                  }, 
                  {
                    "student_grade": 7, 
                    "student_name": "110-S-094"
                  }, 
                  {
                    "student_grade": 8, 
                    "student_name": "110-S-027"
                  }, 
                  {
                    "student_grade": 9, 
                    "student_name": "110-S-036"
                  }, 
                  {
                    "student_grade": 10, 
                    "student_name": "110-S-031"
                  }, 
                  {
                    "student_grade": 11, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": 12, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": 13, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": 14, 
                    "student_name": "110-S-087"
                  }, 
                  {
                    "student_grade": 15, 
                    "student_name": "110-S-019"
                  }, 
                  {
                    "student_grade": 16, 
                    "student_name": "110-S-072"
                  }, 
                  {
                    "student_grade": 17, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": 18, 
                    "student_name": "110-S-056"
                  }, 
                  {
                    "student_grade": 19, 
                    "student_name": "110-S-065"
                  }, 
                  {
                    "student_grade": 20, 
                    "student_name": "110-S-053"
                  }, 
                  {
                    "student_grade": 21, 
                    "student_name": "110-S-024"
                  }, 
                  {
                    "student_grade": 22, 
                    "student_name": "110-S-017"
                  }, 
                  {
                    "student_grade": 23, 
                    "student_name": "110-S-020"
                  }, 
                  {
                    "student_grade": 24, 
                    "student_name": "110-S-043"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-091"
                  }
                ], 
                "lesson_id": "L-016-014", 
                "lesson_time": "2020-12-08", 
                "quiz_name": "test14"
              }
            ]
        self.assertEquals(list(response.json), expected_output)
        self.logout()
        
    def test_delete_course_grade(self):
        self.user_id = "110-T-007"
        self.password = "007"
        self.signin()
        response = self.client.get(url_for('teacher_api.delete_course_grade') + "?lesson_id=L-004-000")
        expected_output = {
                "grade_list": [
                  {
                    "student_grade": None, 
                    "student_name": "110-S-064"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-032"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-082"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-029"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-093"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-097"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-063"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-085"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-023"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-045"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-073"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-055"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-061"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-089"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-077"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-084"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-012"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-086"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-054"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-028"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-088"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-099"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-016"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-098"
                  }, 
                  {
                    "student_grade": None, 
                    "student_name": "110-S-047"
                  }
                ], 
                "lesson_id": "L-004-000", 
                "lesson_time": "2020-09-01", 
                "quiz_name": "test0"
              }
        self.assertEquals(response.json, expected_output)
        self.logout()
    
    def test_edit_course_grade(self):
        self.user_id = "110-T-006"
        self.password = "006"
        self.signin()
        input_data = {
              "grade_list": [
                {
                  "student_grade": 20, 
                  "student_name": "110-S-061"
                }, 
                {
                  "student_grade": 95, 
                  "student_name": "110-S-087"
                }, 
                {
                  "student_grade": 95, 
                  "student_name": "110-S-023"
                }, 
                {
                  "student_grade": 86, 
                  "student_name": "110-S-047"
                }, 
                {
                  "student_grade": 89, 
                  "student_name": "110-S-068"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-094"
                }, 
                {
                  "student_grade": 74, 
                  "student_name": "110-S-052"
                }, 
                {
                  "student_grade": 82, 
                  "student_name": "110-S-073"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-058"
                }, 
                {
                  "student_grade": 85, 
                  "student_name": "110-S-069"
                }, 
                {
                  "student_grade": 63, 
                  "student_name": "110-S-045"
                }, 
                {
                  "student_grade": 81, 
                  "student_name": "110-S-017"
                }, 
                {
                  "student_grade": 99, 
                  "student_name": "110-S-021"
                }, 
                {
                  "student_grade": 83, 
                  "student_name": "110-S-032"
                }, 
                {
                  "student_grade": 75, 
                  "student_name": "110-S-098"
                }, 
                {
                  "student_grade": 87, 
                  "student_name": "110-S-011"
                }, 
                {
                  "student_grade": 79, 
                  "student_name": "110-S-095"
                }, 
                {
                  "student_grade": 86, 
                  "student_name": "110-S-036"
                }, 
                {
                  "student_grade": 81, 
                  "student_name": "110-S-019"
                }, 
                {
                  "student_grade": 78, 
                  "student_name": "110-S-038"
                }, 
                {
                  "student_grade": 61, 
                  "student_name": "110-S-088"
                }, 
                {
                  "student_grade": 82, 
                  "student_name": "110-S-077"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-020"
                }, 
                {
                  "student_grade": 93, 
                  "student_name": "110-S-016"
                }, 
                {
                  "student_grade": 78, 
                  "student_name": "110-S-018"
                }
              ], 
              "lesson_id": "L-010-000", 
              "lesson_time": "2020-09-01", 
              "quiz_name": "第一章"
            }
        response = self.client.post(url_for('teacher_api.edit_course_grade')  ,data = json.dumps(input_data), content_type="application/json")
        expected_output = {
              "grade_list": [
                {
                  "student_grade": 20, 
                  "student_name": "110-S-061"
                }, 
                {
                  "student_grade": 95, 
                  "student_name": "110-S-087"
                }, 
                {
                  "student_grade": 95, 
                  "student_name": "110-S-023"
                }, 
                {
                  "student_grade": 86, 
                  "student_name": "110-S-047"
                }, 
                {
                  "student_grade": 89, 
                  "student_name": "110-S-068"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-094"
                }, 
                {
                  "student_grade": 74, 
                  "student_name": "110-S-052"
                }, 
                {
                  "student_grade": 82, 
                  "student_name": "110-S-073"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-058"
                }, 
                {
                  "student_grade": 85, 
                  "student_name": "110-S-069"
                }, 
                {
                  "student_grade": 63, 
                  "student_name": "110-S-045"
                }, 
                {
                  "student_grade": 81, 
                  "student_name": "110-S-017"
                }, 
                {
                  "student_grade": 99, 
                  "student_name": "110-S-021"
                }, 
                {
                  "student_grade": 83, 
                  "student_name": "110-S-032"
                }, 
                {
                  "student_grade": 75, 
                  "student_name": "110-S-098"
                }, 
                {
                  "student_grade": 87, 
                  "student_name": "110-S-011"
                }, 
                {
                  "student_grade": 79, 
                  "student_name": "110-S-095"
                }, 
                {
                  "student_grade": 86, 
                  "student_name": "110-S-036"
                }, 
                {
                  "student_grade": 81, 
                  "student_name": "110-S-019"
                }, 
                {
                  "student_grade": 78, 
                  "student_name": "110-S-038"
                }, 
                {
                  "student_grade": 61, 
                  "student_name": "110-S-088"
                }, 
                {
                  "student_grade": 82, 
                  "student_name": "110-S-077"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-020"
                }, 
                {
                  "student_grade": 93, 
                  "student_name": "110-S-016"
                }, 
                {
                  "student_grade": 78, 
                  "student_name": "110-S-018"
                }
              ], 
              "lesson_id": "L-010-000", 
              "lesson_time": "2020-09-01", 
              "quiz_name": "第一章"
            }
        self.assertEquals(response.json, expected_output)
        self.logout()
        
    def test_edit_course_grade_2(self):
        self.user_id = "110-T-006"
        self.password = "006"
        self.signin()
        input_data = {
              "grade_list": [
                {
                  "student_grade": 20, 
                  "student_name": "110-S-061"
                }, 
                {
                  "student_grade": 95, 
                  "student_name": "110-S-087"
                }, 
                {
                  "student_grade": 95, 
                  "student_name": "110-S-023"
                }, 
                {
                  "student_grade": 86, 
                  "student_name": "110-S-047"
                }, 
                {
                  "student_grade": 89, 
                  "student_name": "110-S-068"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-094"
                }, 
                {
                  "student_grade": 74, 
                  "student_name": "110-S-052"
                }, 
                {
                  "student_grade": 82, 
                  "student_name": "110-S-073"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-058"
                }, 
                {
                  "student_grade": 85, 
                  "student_name": "110-S-069"
                }, 
                {
                  "student_grade": 63, 
                  "student_name": "110-S-045"
                }, 
                {
                  "student_grade": 81, 
                  "student_name": "110-S-017"
                }, 
                {
                  "student_grade": 99, 
                  "student_name": "110-S-021"
                }, 
                {
                  "student_grade": 83, 
                  "student_name": "110-S-032"
                }, 
                {
                  "student_grade": 75, 
                  "student_name": "110-S-098"
                }, 
                {
                  "student_grade": 87, 
                  "student_name": "110-S-011"
                }, 
                {
                  "student_grade": 79, 
                  "student_name": "110-S-095"
                }, 
                {
                  "student_grade": 86, 
                  "student_name": "110-S-036"
                }, 
                {
                  "student_grade": 81, 
                  "student_name": "110-S-019"
                }, 
                {
                  "student_grade": 78, 
                  "student_name": "110-S-038"
                }, 
                {
                  "student_grade": 61, 
                  "student_name": "110-S-088"
                }, 
                {
                  "student_grade": 82, 
                  "student_name": "110-S-077"
                }, 
                {
                  "student_grade": 80, 
                  "student_name": "110-S-020"
                }, 
                {
                  "student_grade": 93, 
                  "student_name": "110-S-016"
                }, 
                {
                  "student_grade": 78, 
                  "student_name": "110-S-018"
                }
              ], 
              "lesson_id": "L-010-000", 
              "lesson_time": "2020-09-01", 
              "quiz_name": ""
            }
        response = self.client.post(url_for('teacher_api.edit_course_grade')  ,data = json.dumps(input_data), content_type="application/json")
        expected_output = {"message": "資料不得為空"}
        self.assertEquals(response.json, expected_output)
        self.logout()