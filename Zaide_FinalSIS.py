from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.ttk as ttk
import csv
import os 
import sys

class Student:
    
    def __init__ (self,root):
        self.root = root
        blank_space = ""
        self.root.title(200 * blank_space + "Student Information System")
        self.root.geometry("1400x530+0+0")
        self.root.resizable(False,False)
        self.data = dict()
        self.temp = dict()
        self.filename = "SIS.csv"
        
        StudentFirstName = StringVar()
        StudentMiddleInitial = StringVar()
        StudentLastName = StringVar()
        StudentIDNumber = StringVar()
        StudentYearLevel = StringVar()
        StudentGender = StringVar()
        StudentCourse = StringVar()
        searchbar = StringVar()
        
        if not os.path.exists('SIS.csv'):
            with open('SIS.csv', mode='w') as csv_file:
                fieldnames = ["Student ID Number", "Last Name", "First Name", "Middle Initial","Gender", "Year Level", "Course"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        
        else:
            with open('SIS.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student ID Number"]] = {'Last Name': row["Last Name"], 'First Name': row["First Name"], 'Middle Initial': row["Middle Initial"], 'Gender': row["Gender"],'Year Level': row["Year Level"], 'Course': row["Course"]}
            self.temp = self.data.copy()
        
        
         
        ##### ADD STUDENT ####
        
        def addStudent():
            with open('SIS.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentIDNumber.get()=="" or StudentFirstName.get()=="" or StudentMiddleInitial.get()=="" or StudentLastName.get()=="" or StudentYearLevel.get()=="" or StudentGender.get()=="" or StudentCourse.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Please fill in the box.")
                else:
                    studentID = StudentIDNumber.get()
                    studentID_list = []
                    for i in studentID:
                        studentID_list.append(i)
                    if "-" in studentID_list:
                        x = studentID.split("-")
                        y = x[0]
                        n = x[1]
                        if y.isdigit()==False or n.isdigit()==False:
                            tkinter.messagebox.showerror("Student Information System", "Invalid ID Number")
                        else:
                            if studentID in self.data:
                                tkinter.messagebox.showinfo("Student Information System","Student already exists")
                            else:
                                self.data[StudentIDNumber.get()] = {'Last Name': StudentLastName.get(), 'First Name': StudentFirstName.get(), 'Middle Initial': StudentMiddleInitial.get(), 'Gender': StudentGender.get(),'Year Level': StudentYearLevel.get(), 'Course': StudentCourse.get()}
                                self.saveData()
                                tkinter.messagebox.showinfo("Student Information System", "Recorded Successfully")
                                Clear()
                    else:
                        tkinter.messagebox.showerror("Student Information System", "Invalid ID Number")      
                displayData()
                    
        
        ##### CLEAR INPUT DATA BY USER ####
        
        def Clear():
            StudentIDNumber.set("")
            StudentFirstName.set("")
            StudentMiddleInitial.set("")
            StudentLastName.set("")
            StudentYearLevel.set("")
            StudentGender.set("")
            StudentCourse.set("")
        
        ##### DISPLAY DATA #####
        
        def displayData():
            tree.delete(*tree.get_children())
            with open('SIS.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    IDNumber=row['Student ID Number']
                    LastName=row['Last Name']
                    FirstName=row['First Name']
                    MiddleInitial=row['Middle Initial']
                    YearLevel=row['Year Level']
                    Course=row['Course']
                    Gender=row['Gender']
                    tree.insert("",0, values=(IDNumber, LastName, FirstName, MiddleInitial, Gender, YearLevel, Course))
                    
        ##### DELETE STUDENT #####
        
        def deleteData():
            if tree.focus()=="":
                tkinter.messagebox.showerror("Student Information System","Please select a student record from the table")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            decision = tkinter.messagebox.askquestion("Student Information System","Delete Student Record?")
            if decision == "yes":
                self.data.pop(id_no, None)
                self.saveData()
                tree.delete(tree.focus())
                tkinter.messagebox.showinfo("Student Information System","Student Record Deleted Successfully")
            else:
                pass
            
        ##### SEARCH STUDENT #####
        
        def searchData():
            s = self.searchbar.get()
            s_list = []
            for i in s:
                s_list.append(i)
   
            if "-" in s_list:
                x = s.split("-")
                y = x[0]
                n = x[1]
                if y.isdigit()==False or n.isdigit()==False:
                    tkinter.messagebox.showerror("Student Information System", "Invalid ID")
                else:
                    if s in self.data:
                        vals = list(self.data[self.searchbar.get()].values())
                        tree.delete(*tree.get_children())
                        tree.insert("",0, values=(self.searchbar.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
                    elif s == "":
                        displayData()
                    else:
                        tkinter.messagebox.showerror("Student Information System","Student not found")
                        return
            elif s == "":
                tkinter.messagebox.showerror("Student Information System","Student not found")
                return
            else:
                tkinter.messagebox.showerror("Student Information System","Student not found")
                return
            
        
        ##### SELECT STUDENT #####
        
        def editData():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a student record from the table")
                return
            values = tree.item(tree.focus(), "values")
            StudentIDNumber.set(values[0])
            StudentLastName.set(values[1])
            StudentFirstName.set(values[2])
            StudentMiddleInitial.set(values[3])
            StudentGender.set(values[4])
            StudentYearLevel.set(values[5])
            StudentCourse.set(values[6])
       
        ##### UPDATE STUDENT #####
       
        def updateData():
            with open('SIS.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentIDNumber.get()=="" or StudentFirstName.get()=="" or StudentMiddleInitial.get()=="" or StudentLastName.get()=="" or StudentYearLevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Please select a student record from the table")
                else:
                    self.data[StudentIDNumber.get()] = {'Last Name': StudentLastName.get(), 'First Name': StudentFirstName.get(), 'Middle Initial': StudentMiddleInitial.get(), 'Gender': StudentGender.get(),'Year Level': StudentYearLevel.get(), 'Course': StudentCourse.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Student Updated Successfully")
                Clear()
                displayData()     
                
#============================ DESIGN ==============================#
        ##### FRAME #####
        LeftFrame = Frame(self.root, width=250, height=800, padx=2, bg="maroon", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        topFrame = Frame(self.root, width=1350, height=30, padx=2, bg="orange", relief=RIDGE)
        topFrame.pack(side=TOP)
        
        ##### LABELS & ENTRIES #####
        
        self.lblStudentID = Label(self.root, font=('arial',12,'bold'), text="Student ID", bd=7 , anchor=W)
        self.lblStudentID.place(x=275,y=75)
        self.txtStudentID = Entry(self.root, font=('arial',12,'bold'), width=30, justify='left', textvariable = StudentIDNumber)
        self.txtStudentID.place(x=390,y=80)
        self.txtStudentID.insert(0,'YYYY-NNNN')
    
        self.lblLastName = Label(self.root, font=('arial',12,'bold'), text="Last Name", bd=7, anchor=W)
        self.lblLastName.place(x=275,y=105)
        self.txtLastName = Entry(self.root, font=('arial',12,'bold'), width=30, justify='left', textvariable = StudentLastName)
        self.txtLastName.place(x=390,y=110)
    
        self.lblFirstName = Label(self.root, font=('arial',12,'bold'), text="First Name", bd=7, anchor=W)
        self.lblFirstName.place(x=275,y=135)
        self.txtFirstName = Entry(self.root, font=('arial',12,'bold'), width=30, justify='left', textvariable = StudentFirstName)
        self.txtFirstName.place(x=390,y=140)
        
        self.lblMiddleInitial = Label(self.root, font=('arial',12,'bold'), text="Middle Initial", bd=7, anchor=W)
        self.lblMiddleInitial.place(x=275,y=165)
        self.txtMiddleInitial = Entry(self.root, font=('arial',12,'bold'), width=30, justify='left', textvariable = StudentMiddleInitial)
        self.txtMiddleInitial.place(x=390,y=170)
            
        self.lblCourse = Label(self.root, font=('arial',12,'bold'), text="Course", bd=7, anchor=W)
        self.lblCourse.place(x=275,y=195)
        self.txtCourse = Entry(self.root, font=('arial',12,'bold'), width=30, justify='left', textvariable = StudentCourse)
        self.txtCourse.place(x=390,y=200)
            
        self.lblGender = Label(self.root, font=('arial',12,'bold'), text="Gender", bd=7, anchor=W)
        self.lblGender.place(x=275,y=225)
            
        self.cboGender = ttk.Combobox(self.root, font=('arial',12,'bold'), state='readonly', width=28, textvariable = StudentGender)
        self.cboGender['values'] = ('Female', 'Male')
        self.cboGender.place(x=390,y=230)
        
        self.lblYearLevel = Label(self.root, font=('arial',12,'bold'), text="Year Level", bd=7, anchor=W)
        self.lblYearLevel.place(x=275,y=255)
            
        self.cboYearLevel = ttk.Combobox(self.root, font=('arial',12,'bold'), state='readonly', width=28, textvariable = StudentYearLevel)
        self.cboYearLevel['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year')
        self.cboYearLevel.place(x=390,y=260)
            
        self.searchbar = Entry(self.root, font=('arial',12,'bold'), textvariable = searchbar, width = 25)
        self.searchbar.place(x=680,y=45)
        self.searchbar.insert(0,'Search ID Number here')
            
        
        self.title = Label(LeftFrame, font=("Poppins", 50), bg="maroon",text="SSIS", fg="orange")
        self.title.place(x=40,y=10)    
        
        ##### BUTTONS #####
        
        
        self.btnAddNew=Button(self.root, pady=1,bd=4,font=('arial',12,'bold'), padx=24, width=10, text='Add New Student', bg="orange",command=addStudent)
        self.btnAddNew.place(x=280,y=320)
            
        self.btnClear=Button(self.root, pady=1,bd=4,font=('arial',12,'bold'), padx=24, width=10, text='Clear', bg="orange",command=Clear)
        self.btnClear.place(x=500,y=320)
                
        self.btnUpdate=Button(self.root, pady=1,bd=4,font=('arial',12,'bold'), padx=24, width=10, text='Update', bg="orange",command=updateData)
        self.btnUpdate.place(x=500,y=380)

        self.btnEdit=Button(self.root, pady=1,bd=4,font=('arial',12,'bold'), padx=24, width=10, text='Edit Student', bg="orange",command = editData)
        self.btnEdit.place(x=280,y=380)

        self.btnDelete=Button(self.root, pady=1,bd=4,font=('arial',12,'bold'), padx=24, width=10, text='Delete',bg="orange",command = deleteData)
        self.btnDelete.place(x=280,y=440)

        self.btnSearch=Button(self.root,bd=1,font=('arial',12,'bold'), width=10, text='Search', bg="orange",command = searchData)
        self.btnSearch.place(x=920,y=41)
        
        self.btnShowAll=Button(self.root,bd=1,font=('arial',12,'bold'), width=10, text='Show All', bg="orange", command = displayData)
        self.btnShowAll.place(x=1100,y=41)
        
        scroll_y=Scrollbar(self.root, orient=VERTICAL)
        #scroll_y.grid(row=1, column=1, sticky='ns')
    
        tree = ttk.Treeview(self.root, height=20, columns=("Student ID Number", "Last Name", "First Name", "Middle Initial", "Gender", "Year Level", "Course"), yscrollcommand=scroll_y.set)
    
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.place(x=1382,y=79,height=388)
        
        tree.heading("Student ID Number", text="Student ID Number")
        tree.heading("Last Name", text="Last Name")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Initial", text="Middle Initial")
        tree.heading("Gender", text="Gender")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Course", text="Course")
        tree['show'] = 'headings'
    
        tree.column("Student ID Number", width=120)
        tree.column("Last Name", width=100)
        tree.column("First Name", width=150)
        tree.column("Middle Initial", width=100)
        tree.column("Gender", width=70)
        tree.column("Year Level", width=70)
        tree.column("Course", width=90)
        scroll_y.config(command=tree.yview)
        tree.pack(fill=BOTH,expand=1)
        tree.place(x=681, y=79)
        displayData()  
        
    def saveData(self):
        temps = []
        with open('SIS.csv', "w", newline ='') as update:
            fieldnames = ["Student ID Number","Last Name","First Name","Middle Initial","Gender","Year Level","Course"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)

if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
