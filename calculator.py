import tkinter as tk

disValue = 0    # 현재 표시될 값
operator = {'+':1, '-':2, '/':3, '*':4, 'C':5, '=':6}
stoValue = 0    # 계산하는 값
opPre = 0   # 이전에 눌린 연산자 저장

def number_click(value):    # 숫자를 눌렀을 때
    global disValue
    disValue = (disValue*10) + value
    str_value.set(disValue)

def clear():
    global disValue, stoValue, opPre
    stoValue = 0
    opPre = 0
    disValue = 0
    str_value.set(disValue)

def operator_click(value):  # 연산자를 눌렀을 때
    global disValue, operator, stoValue, opPre
    op = operator[value]
    if op == 5: # C
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(disValue)
    elif op == 6: # =
        if opPre == 1:
            disValue = stoValue + disValue
        if opPre == 2:
            disValue = stoValue - disValue
        if opPre == 3:
            disValue = stoValue / disValue
        if opPre == 4:
            disValue = stoValue * disValue
        
        str_value.set(str(disValue))
        disValue = 0
        stoValue = 0
        opPre = 0
    else:   # 오류
        clear()   

def button_click(value):
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)

win = tk.Tk()
win.title('계산기')

str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable=str_value, justify='right', bg = 'white', fg='red')
dis.grid(column=0, row=0, columnspan=4, ipadx=80, ipady=30)

calItem = [['1','2','3','4'],
           ['5','6','7','8'],
           ['9','0','+','-'],
           ['/','*','C','=']]

for i, items in enumerate(calItem):
    for k, item in enumerate(items):

        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'

        bt = tk.Button(win,
            text=item,
            width=10,
            height=5,
            bg = color,
            fg = 'white',
            command = lambda cmd=item: button_click(cmd)
            )
        bt.grid(column=k, row=(i+1))

win.mainloop()