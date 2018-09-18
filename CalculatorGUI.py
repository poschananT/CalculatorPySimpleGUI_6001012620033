# Poschanan Thongsri 6001012620033
# My Block : http://poschanan.blogspot.com/
# referent : https://pysimplegui.readthedocs.io/en/latest/cookbook/#keypad-touchscreen-entry-input-element-update

import PySimpleGUI as sg

layout = [[sg.Input(size=(45,1), do_not_clear=True, justification='left', key='input')],
            [sg.ReadFormButton('C', button_color=('white', 'gray')), sg.ReadFormButton('<--', button_color=('white', 'gray')), sg.ReadFormButton('/', button_color=('white', 'red')), sg.ReadFormButton('*', button_color=('white', 'red'))],
            [sg.ReadFormButton('7', button_color=('white', 'black')), sg.ReadFormButton('8', button_color=('white', 'black')), sg.ReadFormButton('9', button_color=('white', 'black')), sg.ReadFormButton('-', button_color=('white', 'red'))],
            [sg.ReadFormButton('4', button_color=('white', 'black')), sg.ReadFormButton('5', button_color=('white', 'black')), sg.ReadFormButton('6', button_color=('white', 'black')), sg.ReadFormButton('+', button_color=('white', 'red'))],
            [sg.ReadFormButton('1', button_color=('white', 'black')), sg.ReadFormButton('2', button_color=('white', 'black')), sg.ReadFormButton('3', button_color=('white', 'black')), sg.ReadFormButton('=', button_color=('white', 'red'))],
            [sg.ReadFormButton('.', button_color=('white', 'black')), sg.ReadFormButton('0', button_color=('white', 'black')), sg.ReadFormButton('(', button_color=('white', 'red')), sg.ReadFormButton(')', button_color=('white', 'red'))]]
    #เป็นการสร้างปุ่มกดขึ้นมาโดยการกำหนดค่าตัวเลขและสีของแต่ละปุ่ม และสร้างช่อง input

form = sg.FlexForm('Calculator', default_button_element_size=(8,5), auto_size_buttons=False, grab_anywhere=False,background_color=('gray8'))
form.Layout(layout)
# เป็นขั้นตอนของการตั้งค่าหน้าต่างที่ใช้แสดงผล

number = ''   # เก็บสมการที่ input เข้ามา
countnum = 0  # ไว้คอยนับจำนวนตัวเลขเพื่อจำกัดขอบเขต
while True:
    button = form.Read()[0]
    if button is 'C':
        number = ''
        # เป็นการลบข้อมูลทั้งหมด
    elif button is '<--':
        number = number[:-1]
        # เป็นการลบเลขออกโดยจะทำการลบแค่ตัวสุดท้าย
    elif button in '1234567890.+-*/()':
        if button in '1234567890.':
            if 7 > countnum >= 0:    # จำกัดขอบเขตของตัวเลขไว้เเค่ 7 ตำแหน่ง
                number += button
                countnum += 1
        else:
            number += button
            countnum = 0
        # เป็นการใส่ค่าของตัวที่กดลงในช่อง input
    elif button in '=':
        if ')' not in number and '(' in number:
            number = ''
            number += 'ERROR'

        elif '(' not in number and ')' in number:
            number = ''
            number += 'ERROR'

        elif number[-1] == '+' or number[-1] == '-' or number[-1] == '*' or number[-1] == '/':
            number = ''
            number += 'ERROR'

        elif number[-1] == '0' and number[-2] == '/':
            number = ''
            number += 'ERROR'
        # เป็นการตรวจสอบว่าสมการที่กรอกเข้ามานั้นผิดไหม ถ้าผิดมันจะเข้าไปตาม if elif ข้างบนเเล้วแสดง ERROR

        else:
            equals = eval(''.join(number))
            number = ''
            number += str(equals)
        # คิดคำตอบของสมการ โดยการใช้ eval() แล้วแสดงค่าไที่ช่อง input

    form.FindElement('input').Update(number)    # ทำการ update ค่าที่ช่อง input
            
           
"""
  Test Case
34 + 78 = 112
(22.1 + 15) - 3 = 34.1
543 / 0 = ERROR
92 / = ERROR
(54 * 2) + (42 / 2) = 129.0
(12 + 9  - 45 = ERROR
674 * 53 = 35722
-34 - 45 = -79
39 - (56 * 3) = -129
34 / 2 = 17.0
"""
