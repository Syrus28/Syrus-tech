from tkinter import *
import mysql.connector

db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="test",
                     db="project2")


def disprecord():
    cur = db.cursor()
    cur.execute("Select * from player")
    answer=""
    for row in cur.fetchall():
        answer=answer+str(row[0])+" "+ row[1]+" "+str(row[2])+"\n"
    data_label.configure(text =answer)
    cur.close();
def plotdata():
    cur = db.cursor()
    cur.execute("Select * from player")
    answer=""
    x=[]
    y=[]
    for row in cur.fetchall():
        x.append(int(row[0]))
        y.append(int(row[2]))
    plt.bar(x, y) 
   
    plt.xlabel('id') 
  
    plt.ylabel('name') 
    plt.xticks(x, y, fontsize=5, rotation=30)
   
    plt.title('player Performance') 
  
  
    plt.show() 


def addrecord(r,n,m):
    cursor2 = db.cursor()
    insert_query = " insert into player values("+str(r)+",'"+n+"',"+str(m)+") "

    result = cursor2.execute(insert_query)
    db.commit()
    print("Data Inserted")
    cursor2.close()


def addF():
    if (id_txtbx.get() and name_txtbx.get()and wickets_txtbx.get() != ""):
        try:
            id = id_txtbx.get()
            name =name_txtbx.get()
            wickets=wickets_txtbx.get()
            addrecord(int(id),name,int(wickets))
            answer= id
            answer_label.configure(text =answer)
            status_label.configure(text ="successfully computed")
        except:
            status_label.configure(text ="invalid input, check your input types")
       





root = Tk()
root.geometry("500x600")
root.title("cricket")

answer_label =Label(root, text ="---")
answer_label.grid(row =0, column =0)

label1 =Label(root, text ="id")
label1.grid(row =1, column =0)

id_txtbx =Entry(root)
id_txtbx.grid(row =1, column =1)

label2 =Label(root, text ="Name")
label2.grid(row =2, column =0)

name_txtbx =Entry(root)
name_txtbx.grid(row =2, column =1)

label3 =Label(root, text ="wickets")
label3.grid(row =3, column =0)

wickets_txtbx =Entry(root)
wickets_txtbx.grid(row =3, column =1)

add_button =Button(root, text="Add player", command= addF)
add_button.grid(row =6, column =0  )

disp_button =Button(root, text="Display player", command= disprecord)
disp_button.grid(row =6, column =1)

disp2_button =Button(root, text="graph", command= plotdata)
disp2_button.grid(row =6, column =2)

data_label =Label(root, text ="---")
data_label.grid(row =8, column =0)

status_label =Label(root, height =5, width =25, bg ="black", fg ="#00FF00", text ="---", wraplength =150)
status_label.grid(row =10, column =0, columnspan =2)

root.mainloop()
