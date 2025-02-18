#Write your code here >:-(
import tkinter as tk #เรียกใช้โมดูล tkinter

window = tk.Tk() #กำหนดหน้าต่างโปรแกรม
window.title("คำนวณค่า BMI") #ชื่อหน้าต่างโปรแกรม
window.geometry("450x140") #ขนาดหน้าต่างโปรแกรม

#
weight = tk.DoubleVar() #สร้างตัวแปรเก็บค่าน้ำหนัก
label1=tk.Label(window,text='น้ำหนัก (กก.)',font=30) #สร้าง Label แสดงข้อความ  
label1.grid(row=0,column=0,sticky='W') #กำหนดตำแหน่งของ Lebel
etweight=tk.Entry(window,font=30,width=30,textvariable=weight,bg='yellow',fg='black')
#สร้าง Entry รับข้อมูลจากคีย์บอร์ด
etweight.grid(row=0,column=1) #กำหนดตำแหน่ง Entry

height = tk.DoubleVar()
label2=tk.Label(text='Height (cm.)',font=30)
label2.grid(row=1,column=0,sticky='W')
ethight=tk.Entry(font=30,width=30,textvariable=height,bg='yellow',fg='black')
ethight.grid(row=1,column=1)
#END Input

#Output
label3=tk.Label(text='BMI value',font=30)
label3.grid(row=2,column=0,sticky='W')
etbmi=tk.Entry(font=30,width=30)
etbmi.grid(row=2,column=1)

label4=tk.Label(text='Result',font=30)
label4.grid(row=3,column=0,sticky='W')
ettext=tk.Entry(font=30,width=30)
ettext.grid(row=3,column=1)
#END Output

def deleteText():
    etweight.delete(0,'end')
    ethight.delete(0,'end')
    etbmi.delete(0,'end')
    ettext.delete(0,'end')

#Process
def calculate():
    weightGet=weight.get()
    heightGet=height.get()
    #bmi=weightGet/((heightGet/100)*(heightGet/100)) ตัวอย่างการเขียนแบบที่ 1
    bmi=weightGet/(heightGet/100)**2 #ตัวอย่างการเขียนแบบที่ 2
    if bmi<18.5: #เงื่อนไขการตัดสินใจ
        etbmi.delete(0,'end') #ลบข้อมูลเดิม
        ettext.delete(0,'end') #ลบข้อมูลเดิม
        result=bmi
        result = "{: .2f}".format(float(bmi)) #กำหนดค่าแสดงผลทศนิยม 2 ตำแหน่ง
        result2='Thin'
        etbmi.insert(0,result) #แสดงผลลไปที่ Entry etbmi
        ettext.insert(0,result2) #แสดงผลลไปที่ Entry ettext
    elif bmi>=18.5 and bmi<=23:
        etbmi.delete(0,'end')
        ettext.delete(0,'end')
        result=bmi
        result = "{: .2f}".format(float(bmi))
        result2='Normal'
        etbmi.insert(0,result)
        ettext.insert(0,result2)
    elif bmi>23 and bmi<=24.9:
        etbmi.delete(0,'end')
        ettext.delete(0,'end')
        result=bmi
        result = "{: .2f}".format(float(bmi))
        result2='Fat'
        etbmi.insert(0,result)
        ettext.insert(0,result2)
    elif bmi>=25 and bmi<=29.9:
        etbmi.delete(0,'end')
        ettext.delete(0,'end')
        result=bmi
        result = "{: .2f}".format(float(bmi))
        result2='Over Fat'
        etbmi.insert(0,result)
        ettext.insert(0,result2)
    elif bmi>=30:
        etbmi.delete(0,'end')
        ettext.delete(0,'end')
        result=bmi
        result = "{: .2f}".format(float(bmi))
        result2='Dangerous Fat'
        etbmi.insert(0,result)
        ettext.insert(0,result2)

    print('ค่าดัชนีมวลกาย=',result)
    print('แปลงผลค่าดัชนีมวลกาย=',result2)      

buttonReset=tk.Button(text='Delete',font=30,width=15,command=deleteText)
buttonReset.grid(row=4,column=0)
buttonCal=tk.Button(text='Calculate',font=30,width=15,command=calculate)
buttonCal.grid(row=4,column=1)

tk.mainloop()
