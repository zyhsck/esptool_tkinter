#项目建于2024/1/31
# 作者：bilibili 秃头程序园嘛
#搬运请标出 出处：https://github.com/zyhsck/esptool_tkinter
#本程序开源免费





import tkinter as tk
import os
import tkinter.filedialog



root = tk.Tk()
root.title("EspTool")
root.geometry('300x500')
#-----------------------------
com_t = tk.Label(root,text="COM");com_t.place(x=0,y=0)
com_entry = tk.Entry(root,width=5);com_entry.place(x=40,y=0)
#-----------------------------
except_text=""
def get_id():
    global except_text
    exportation.delete(1.0,"end")
    except_text=os.popen("python -m esptool -p COM"+com_entry.get()+" flash_id")
    
    exportation.insert("end",str(except_text.read()))
get_id_b =tk.Button(root,text="获取esp信息",command=get_id); get_id_b.place(x=90,y=0)
#---------------------------------
def get_file():
    global file_path
    file_path = tkinter.filedialog.askopenfilename(title="选择bin文件")
    
def flash_file():
    global file_path
    if file_path !="":
        exportation.delete(1.0,"end")
        os.system("esptool --port COM"+com_entry.get()+" erase_flash")
        except_text=os.popen("esptool --port COM"+com_entry.get()+" --baud 115200 write_flash -z --flash_mode dio --flash_freq 80m --flash_size 8MB 0x0 "+str(file_path))
        except_text=except_text.read()
        with open("console.txt","w") as f:
            f.write(except_text)
        exportation.insert("end",except_text[-1:-500]+"\n省略\n结束")
get_file_b =tk.Button(root,text="选择BIN文件",command=get_file); get_file_b.place(x=0,y=35)
flash_file_b = tk.Button(root,text="烧录",command=flash_file); flash_file_b.place(x=85,y=35)
#---------------------------------
def get_bin():
    exportation.delete(1.0,"end")
    except_text=os.popen("python -m esptool --port COM"+com_entry.get()+" -b 115200 read_flash 0x0 0x400000 py.bin")
    except_text=except_text.read()
    with open("console.txt","w") as f:
            f.write(except_text)
    exportation.insert("end",except_text[-1:-500]+"\n省略\n结束")

get_bin_b = tk.Button(root,text="提取BIN文件",command=get_bin);get_bin_b.place(x=125,y=35)

#----------------------------------

tips_l = tk.Label(root,text="By 秃头程序园嘛~\nversion:1.1");tips_l.place(x=90,y=450)





exportation = tk.Text(root,width=42);exportation.place(x=0,y=100)
exportation.insert("end",'''
提醒：
1.如果按下按钮后显示程序未响应,这是正常的
2.如果按下按钮后完成时间过短,可以打开console.txt,查看完整输出,查看是否报错
3.请在设备管理器里查看端口号(COM)进行填写
4.请确保没有其它软件占用端口
5.对于个别esp,在烧录请同时按下boot和reset键进行手动复位
                                   ''')


root.mainloop()
