#PROJECT SCHOOL DB

import pandas as pd

flag=1

def show_class(x):
    print('-'*146)
    print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
    'ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM',
    'ROUTE NO.','ADDRESS'))
    print('-'*146)
    print('-'*146)
    for index, row in x.iterrows():
        print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
        row['ID'],row[' NAME'],row['CLASS'],row['ROLL NO.'],row['FATHER NAME'],row['MOTHER NAME'],row['GENDER'],row['PHONE NO.'],
        row['STREAM'],row['ROUTE NO.'],row['ADDRESS']))
        print('-'*146)

def show_teacher(x):
    print('-'*111)
    print('{0:10}{1:20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
    'ID','NAME','GENDER','DEPARTMENT','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
    print('-'*111)
    print('-'*111)
    for index, row in x.iterrows():
        print('{0:10}{1:20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
        row['ID'],row['NAME'],row['GENDER'],row['DEPARTMENT'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
        print('-'*111)


def show_other(x):
    print('-'*91)
    print('{0:10}{1:20}{2:>10}{3:>20}{4:>10}{5:>10}{6:>10}'.format(
    'ID','NAME','GENDER','CATEGORY','SALARY','ROUTE NO.','ADDRESS'))
    print('-'*91)
    print('-'*91)
    for index, row in x.iterrows():
        print('{0:10}{1:20}{2:>10}{3:>20}{4:>10}{5:>10}{6:>10}'.format(
        row['ID'],row['NAME'],row['GENDER'],row['CATEGORY'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
        print('-'*91)

def admin_menu():                                                             #TEACHER MENU
    print()
    print('ADMINS')
    print('-------')
    print()
    print('1. Admin Info')
    print('2. Appoint New')
    print()
    opp_a=input('SELECT :')
    if opp_a=='1':
        print('INFO')
    elif opp_a=='2':
        print('NEW')
    else:
        print('--- INVALID ---')
                

##################################################################################################


def other_info():                                                             #OTHER INFO MENU

    oth=pd.read_csv('NON TEACHING.csv')
    
    print()
    print('OTHER INFO')
    print('------------')
    print()
    print('1. Show All')
    print('2. Search Category')
    print('3. Search Staff')
    print()
    op_oi=input('SELECT :')
    print()
    if op_oi=='1':
        print('-'*91)
        print('{0:10}{1:20}{2:>10}{3:>20}{4:>10}{5:>10}{6:>10}'.format(
        'ID','NAME','GENDER','CATEGORY','SALARY','ROUTE NO.','ADDRESS'))
        print('-'*91)
        print('-'*91)
        for index, row in oth.iterrows():
            print('{0:10}{1:20}{2:>10}{3:>20}{4:>10}{5:>10}{6:>10}'.format(
            row['ID'],row['NAME'],row['GENDER'],row['CATEGORY'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
            print('-'*91)
        
    elif op_oi=='2':
        print()
        print("Select Category")
        print()
        print("1. Caretakers")
        print("2. Drivers")
        print("3. Security")
        print("4. Gardeners")
        print("5. Canteen")
        print()
        oop=oth.set_index(['CATEGORY'])
        op_oid=input('SELECT :')
        print()
        if op_oid=='1':
            o_loc=oop.loc["CARETAKER"]
            print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
            'CATEGORY','ID','NAME','GENDER','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*91)
            print('-'*91)
            for index, row in o_loc.iterrows():
                print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*91)
        elif op_oid=='2':
            o_loc=oop.loc["DRIVER"]
            print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
            'CATEGORY','ID','NAME','GENDER','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*91)
            print('-'*91)
            for index, row in o_loc.iterrows():
                print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*91)
        elif op_oid=='3':
            o_loc=oop.loc["SECURITY"]
            print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
            'CATEGORY','ID','NAME','GENDER','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*91)
            print('-'*91)
            for index, row in o_loc.iterrows():
                print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*91)
        elif op_oid=='4':
            o_loc=oop.loc["GARDENER"]
            print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
            'CATEGORY','ID','NAME','GENDER','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*91)
            print('-'*91)
            for index, row in o_loc.iterrows():
                print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*91)
        elif op_oid=='5':
            o_loc=oop.loc["CANTEEN"]
            print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
            'CATEGORY','ID','NAME','GENDER','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*91)
            print('-'*91)
            for index, row in o_loc.iterrows():
                print('{0:20}{1:10}{2:>20}{3:>10}{4:>10}{5:>10}{6:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*91)
        else:
            print('--- INVALID ---')
    elif op_oi=='3':
        print()
        print('SEARCH STAFF')
        print('--------------')
        print()
        print('1. Search by Name')
        print('2. Search by Staff-ID')
        print()
        op_tis=input('SELECT :')
        if op_tis=='1':
            print()
            src=input('Enter Name to Search :').upper()
            flag1=0
            for index, row in oth.iterrows():
                if row["NAME"]==src:
                    flag1=1
                else :
                    continue
            if flag1==1:
                oth=oth.set_index(['NAME'])
                print()
                print(oth.loc[src])
                print()
            else:
                print('NOT FOUND')
                    
        elif op_tis=='2':
            print()
            src=input('Enter ID to Search :').upper()
            flag1=0
            for index, row in oth.iterrows():
                if row["ID"]==src:
                    flag1=1
                else :
                    continue
            if flag1==1:
                oth=oth.set_index(['ID'])
                print()
                print(oth.loc[src])
                print()
            else:
                print('NOT FOUND')



###############################################################################
        
                                                                                #TEACHER ADD
        
def other_add():
    oth=pd.read_csv('NON TEACHING.csv')
    
    print()
    print("NON-TEACHING ADDMISSION")
    print('-------------------')
    print()
    show_other(oth)
    while True:
        print()
        print("NON-TEACHING INFORMATION")
        print()
        ID=input("Enter ID :").upper()
        NAME=input("Enter Name :").upper()
        GENDER=input("Enter Gender :").upper()
        CAT=input("Enter Category:").upper()
        dic={'ID':[ID],
             'NAME':[NAME],
             'GENDER':[GENDER],
             'CATEGORY':[CAT],
             'SALARY':None,
             'ROUTE NO.':None,
             "ADDRESS":None}
        dff=pd.DataFrame(dic,columns=['ID','NAME','GENDER','CATEGORY','SALARY','ROUTE NO.','ADDRESS'])
        dfa=pd.concat([oth,dff],ignore_index=True,sort=False)
        show_other(dfa)
        dfa.to_csv('NON TEACHING.csv')
        p=input("Do you want continue <y/n>").upper()
        if p=='N':
            break;
                
################################################################################




def teacher_info():                                                             #TEACHER INFO MENU

    tec=pd.read_csv('TEACHERS.csv')
    
    print()
    print('TEACHER INFO')
    print('------------')
    print()
    print('1. Show All Teachers')
    print('2. Search Department')
    print('3. Search Teachers')
    print()
    op_ti=input('SELECT :')
    if op_ti=='1':
        print('-'*111)
        print('{0:10}{1:20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
        'ID','NAME','GENDER','DEPARTMENT','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
        print('-'*111)
        print('-'*111)
        for index, row in tec.iterrows():
            print('{0:10}{1:20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            row['ID'],row['NAME'],row['GENDER'],row['DEPARTMENT'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
            print('-'*111)

    elif op_ti=='2':
        print()
        print("Select Department")
        print()
        print('1. Science')
        print('2. Language')
        print('3. Sports')
        print('4. Commerce')
        print('5. Fine Arts')
        print('6. IT')
        print('7. Social Science')
        print()
        top=tec.set_index(['DEPARTMENT'])
        op_tid=input('SELECT :')
        if op_tid=='1':
            t_loc=top.loc["SCIENCE"]
            print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            '','ID','NAME','GENDER','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*111)
            print('-'*111)
            for index, row in t_loc.iterrows():
                print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*111)
        elif op_tid=='2':
            t_loc=top.loc["LANGUAGE"]
            print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            '','ID','NAME','GENDER','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*111)
            print('-'*111)
            for index, row in t_loc.iterrows():
                print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*111)
        elif op_tid=='3':
            t_loc=top.loc["SPORTS"]
            print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            '','ID','NAME','GENDER','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*111)
            print('-'*111)
            for index, row in t_loc.iterrows():
                print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*111)
        elif op_tid=='4':
            t_loc=top.loc["COMMERCE"]
            print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            '','ID','NAME','GENDER','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*111)
            print('-'*111)
            for index, row in t_loc.iterrows():
                print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*111)
        elif op_tid=='5':
            t_loc=top.loc["FINE ARTS"]
            print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            '','ID','NAME','GENDER','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*111)
            print('-'*111)
            for index, row in t_loc.iterrows():
                print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*111)
        elif op_tid=='6':
            t_loc=top.loc["IT"]
            print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            '','ID','NAME','GENDER','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*111)
            print('-'*111)
            for index, row in t_loc.iterrows():
                print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*111)
        elif op_tid=='7':
            t_loc=top.loc["SOCIAL SCIENCE"]
            print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
            '','ID','NAME','GENDER','SUBJECT','SALARY','ROUTE NO.','ADDRESS'))
            print('-'*111)
            print('-'*111)
            for index, row in t_loc.iterrows():
                print('{0:>20}{1:>20}{2:>10}{3:>20}{4:>20}{5:>10}{6:>10}{7:>10}'.format(
                index,row['ID'],row['NAME'],row['GENDER'],row['SUBJECT'],row['SALARY'],row['ROUTE NO. '],row['ADDRESS']))
                print('-'*111)
        else:
            print('--- INVALID ---')

    elif op_ti=='3':
        print()
        print('SEARCH TEACHER')
        print('--------------')
        print()
        print('1. Search by Name')
        print('2. Search by Teacher-ID')
        print()
        op_tis=input('SELECT :')
        if op_tis=='1':
            print()
            t=tec
            src=input('Enter Name to Search :').upper()
            flag1=0
            for index, row in t.iterrows():
                if row["NAME"]==src:
                    flag1=1
                else :
                    continue
            if flag1==1:
                t=t.set_index(['NAME'])
                print()
                print(t.loc[src])
                print()
            else:
                print('NOT FOUND')
                    
        elif op_tis=='2':
            print()
            t=tec
            src=input('Enter ID to Search :').upper()
            flag1=0
            for index, row in t.iterrows():
                if row["ID"]==src:
                    flag1=1
                else :
                    continue
            if flag1==1:
                t=t.set_index(['ID'])
                print()
                print(t.loc[src])
                print()
            else:
                print('NOT FOUND')

        else:
            print('--- INVALID ---')
        
        



################################################################################
                


def student_info():                                                             #STUDENT INFO MENU (COMPLETED..!!!!)

    cl_8=pd.read_csv('CLASS VIII.csv')
    cl_9=pd.read_csv('CLASS IX.csv')
    cl_10=pd.read_csv('CLASS X.csv')
    cl_11=pd.read_csv('CLASS XI.csv')
    cl_12=pd.read_csv('CLASS XII.csv')
    cl=pd.concat([cl_8,cl_9,cl_10,cl_11,cl_12],ignore_index=True,axis=0,sort=False)
    
    print()
    print('STUDENT INFO')
    print('------------')
    print()
    print('1. Show All Students')
    print('2. Search Class')      
    print('3. Search Student')  
    print()
    op_si=input('SELECT :')
    if op_si=='1':
        print('-'*146)
        print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
        'ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM',
        'ROUTE NO.','ADDRESS'))
        print('-'*146)
        print('-'*146)
        for index, row in cl.iterrows():
            print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
            row['ID'],row[' NAME'],row['CLASS'],row['ROLL NO.'],row['FATHER NAME'],row['MOTHER NAME'],row['GENDER'],row['PHONE NO.'],
            row['STREAM'],row['ROUTE NO.'],row['ADDRESS']))
            print('-'*146)
          
    
    elif op_si=='2':
        print()
        print("Enter Class to Search (8-12)")
        print()
        op_sic=input('ENTER :')
        if op_sic=='8' or op_sic.upper()=='VIII':

            print('-'*146)
            print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
            'ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM',
            'ROUTE NO.','ADDRESS'))
            print('-'*146)
            print('-'*146)
            for index, row in cl_8.iterrows():
                print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
                row['ID'],row[' NAME'],row['CLASS'],row['ROLL NO.'],row['FATHER NAME'],row['MOTHER NAME'],row['GENDER'],row['PHONE NO.'],
                row['STREAM'],row['ROUTE NO.'],row['ADDRESS']))
                print('-'*146)
                                            
        elif op_sic =='9' or op_sic.upper()=='IX':
            
            print('-'*146)
            print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
            'ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM',
            'ROUTE NO.','ADDRESS'))
            print('-'*146)
            print('-'*146)
            for index, row in cl_9.iterrows():
                print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
                row['ID'],row[' NAME'],row['CLASS'],row['ROLL NO.'],row['FATHER NAME'],row['MOTHER NAME'],row['GENDER'],row['PHONE NO.'],
                row['STREAM'],row['ROUTE NO.'],row['ADDRESS']))
                print('-'*146)
            
        elif op_sic=='10' or op_sic.upper()=='X':
            
            print('-'*146)
            print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
            'ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM',
            'ROUTE NO.','ADDRESS'))
            print('-'*146)
            print('-'*146)
            for index, row in cl_10.iterrows():
                print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
                row['ID'],row[' NAME'],row['CLASS'],row['ROLL NO.'],row['FATHER NAME'],row['MOTHER NAME'],row['GENDER'],row['PHONE NO.'],
                row['STREAM'],row['ROUTE NO.'],row['ADDRESS']))
                print('-'*146)
                
        elif op_sic=='11' or op_sic.upper()=='XI':

            print('-'*146)
            print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
            'ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM',
            'ROUTE NO.','ADDRESS'))
            print('-'*146)
            print('-'*146)
            for index, row in cl_11.iterrows():
                print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
                row['ID'],row[' NAME'],row['CLASS'],row['ROLL NO.'],row['FATHER NAME'],row['MOTHER NAME'],row['GENDER'],row['PHONE NO.'],
                row['STREAM'],row['ROUTE NO.'],row['ADDRESS']))
                print('-'*146)
                
        elif op_sic=='12' or op_sic.upper()=='XII':

            print('-'*146)
            print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
            'ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM',
            'ROUTE NO.','ADDRESS'))
            print('-'*146)
            print('-'*146)
            for index, row in cl_12.iterrows():
                print('{0:10}{1:20}{2:>10}{3:>10}{4:>20}{5:>20}{6:>10}{7:>15}{8:>10}{9:>10}{10:>10}'.format(
                row['ID'],row[' NAME'],row['CLASS'],row['ROLL NO.'],row['FATHER NAME'],row['MOTHER NAME'],row['GENDER'],row['PHONE NO.'],
                row['STREAM'],row['ROUTE NO.'],row['ADDRESS']))
                print('-'*146)
                
        else:
            print('--- INVALID ---')
                    
    elif op_si=='3':
        print()
        print('SEARCH STUDENT')
        print('--------------')
        print()
        print('1. Search by Name')
        print('2. Search by Student-ID')
        print()
        op_sis=input('SELECT :')
        if op_sis=='1':
            print()
            t=cl
            src=input('Enter Name to Search :').upper()
            flag1=0
            for index, row in t.iterrows():
                if row[" NAME"]==src:
                    flag1=1
                else :
                    continue
            if flag1==1:
                t=t.set_index([' NAME'])
                print()
                print(t.loc[src])
                print()
            else:
                print('NOT FOUND')
                    
        elif op_sis=='2':
            print()
            t=cl
            src=input('Enter ID to Search :').upper()
            for index, row in t.iterrows():
                if row["ID"]==src:
                    flag1=1
                else :
                    continue
            if flag1==1:
                t=t.set_index(['ID'])
                print()
                print(t.loc[src])
                print()
            else:
                print('NOT FOUND')
        else:
            print('--- INVALID ---')

################################################################################

                                                                                #STUDENT ADMISSIONS
def student_add():
    cl_8=pd.read_csv('CLASS VIII.csv')
    cl_9=pd.read_csv('CLASS IX.csv')
    cl_10=pd.read_csv('CLASS X.csv')
    cl_11=pd.read_csv('CLASS XI.csv')
    cl_12=pd.read_csv('CLASS XII.csv')
    print()
    print('STUDENT ADMISSIONS')
    print('------------------')
    print()
    op_sa=input('SELECT CLASS :')
    if op_sa=='8':        
        show_class(cl_8)
        while True:
            print()
            print("Enter information")
            print()
            ID=input("Enter ID of student :").upper()
            NAME=input("Enter Name of student :").upper()
            CLASS='VIII'
            ROLL=input("Enter valid Roll No. of student :").upper()
            GENDER=input("Enter gender of student :").upper()
            F_NAME=input("Enter Father Name of student :").upper()
            M_NAME=input("Enter Mother Name of student :").upper()
            PH_NO=input("Enter Phone NO. of student/Guardian :").upper()
            STREAM='N/A'
            std={"ID":ID,
                 "NAME":[NAME],
                 "CLASS":[CLASS],
                 "ROLL NO.":[ROLL],
                 "FATHER NAME":[F_NAME],
                 "MOTHER NAME":[M_NAME],
                 "GENDER":[GENDER],
                 "PHONE NO.":[PH_NO],
                 "STREAM":None,
                 "ROUTE NO.":None,
                 "ADDRESS":None}
            dff=pd.DataFrame(std,columns=['ID','NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM','ROUTE NO.','ADDRESS'])
            dfa=pd.concat([cl_8,dff],ignore_index=True,sort=False)
            show_class(dfa)
            dfa.to_csv('CLASS VIII.csv')
            p=input("Do you want continue <y/n>").upper()
            if p=='N':
                break;
        
    elif op_sa=='9':
        while True:
            show_class(cl_9)
            print()
            print("Enter information")
            print()
            ID=input("Enter ID of student :").upper()
            NAME=input("Enter Name of student :").upper()
            CLASS='IX'
            ROLL=input("Enter valid Roll No. of student :").upper()
            GENDER=input("Enter gender of student :").upper()
            F_NAME=input("Enter Father Name of student :").upper()
            M_NAME=input("Enter Mother Name of student :").upper()
            PH_NO=input("Enter Phone NO. of student/Guardian :").upper()
            STREAM='N/A'
            std={"ID":ID,
                 " NAME":[NAME],
                 "CLASS":[CLASS],
                 "ROLL NO.":[ROLL],
                 "FATHER NAME":[F_NAME],
                 "MOTHER NAME":[M_NAME],
                 "GENDER":[GENDER],
                 "PHONE NO.":[PH_NO],
                 "STREAM":None,
                 "ROUTE NO.":None,
                 "ADDRESS":None}
            dff=pd.DataFrame(std,columns=['ID',' NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM','ROUTE NO.','ADDRESS'])
            dfa=pd.concat([cl_9,dff],ignore_index=True,sort=False)
            show_class(dfa)
            dfa.to_csv('CLASS IX.csv')
            p=input("Do you want continue <y/n>").upper()
            if p=='N':
                break;
                
    elif op_sa=='10':
        show_class(cl_10)
        while True:
            print()
            print("Enter information")
            print()
            ID=input("Enter ID of student :").upper()
            NAME=input("Enter Name of student :").upper()
            CLASS='X'
            ROLL=input("Enter valid Roll No. of student :").upper()
            GENDER=input("Enter gender of student :").upper()
            F_NAME=input("Enter Father Name of student :").upper()
            M_NAME=input("Enter Mother Name of student :").upper()
            PH_NO=input("Enter Phone NO. of student/Guardian :").upper()
            STREAM='N/A'
            std={"ID":ID,
                 " NAME":[NAME],
                 "CLASS":[CLASS],
                 "ROLL NO.":[ROLL],
                 "FATHER NAME":[F_NAME],
                 "MOTHER NAME":[M_NAME],
                 "GENDER":[GENDER],
                 "PHONE NO.":[PH_NO],
                 "STREAM":None,
                 "ROUTE NO.":None,
                 "ADDRESS":None}
            dff=pd.DataFrame(std,columns=['ID',' NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM','ROUTE NO.','ADDRESS'])
            dfa=pd.concat([cl_10,dff],ignore_index=True,sort=False)
            show_class(dfa)
            dfa.to_csv('CLASS X.csv')
            p=input("Do you want continue <y/n>").upper()
            if p=='N':
                break;        
        
    elif op_sa=='11':
        while True:
            show_class(Cl_11)
            print()
            print("Enter information")
            print()
            ID=input("Enter ID of student :").upper()
            NAME=input("Enter Name of student :").upper()
            CLASS='XI'
            ROLL=input("Enter valid Roll No. of student :").upper()
            GENDER=input("Enter gender of student :").upper()
            F_NAME=input("Enter Father Name of student :").upper()
            M_NAME=input("Enter Mother Name of student :").upper()
            PH_NO=input("Enter Phone NO. of student/Guardian :").upper()
            STREAM=input("Enter Stream of student :").upper()
            std={"ID":ID,
                 " NAME":[NAME],
                 "CLASS":[CLASS],
                 "ROLL NO.":[ROLL],
                 "FATHER NAME":[F_NAME],
                 "MOTHER NAME":[M_NAME],
                 "GENDER":[GENDER],
                 "PHONE NO.":[PH_NO],
                 "STREAM":[STREAM],
                 "ROUTE NO.":None,
                 "ADDRESS":None}
            dff=pd.DataFrame(std,columns=['ID',' NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM','ROUTE NO.','ADDRESS'])
            dfa=pd.concat([cl_11,dff],ignore_index=True,sort=False)
            show_class(dfa)
            dfa.to_csv('CLASS XI.csv')
            p=input("Do you want continue <y/n>").upper()
            if p=='N':
                break;
                
    elif op_sa=='12':
        while True:
            show_class(cl_12)
            print()
            print("Enter information")
            print()
            ID=input("Enter ID of student :").upper()
            NAME=input("Enter Name of student :").upper()
            CLASS='XII'
            ROLL=input("Enter valid Roll No. of student :").upper()
            GENDER=input("Enter gender of student :").upper()
            F_NAME=input("Enter Father Name of student :").upper()
            M_NAME=input("Enter Mother Name of student :").upper()
            PH_NO=input("Enter Phone NO. of student/Guardian :").upper()
            STREAM=input("Enter Stream of student :").upper()
            std={"ID":ID,
                 " NAME":[NAME],
                 "CLASS":[CLASS],
                 "ROLL NO.":[ROLL],
                 "FATHER NAME":[F_NAME],
                 "MOTHER NAME":[M_NAME],
                 "GENDER":[GENDER],
                 "PHONE NO.":[PH_NO],
                 "STREAM":[STREAM],
                 "ROUTE NO.":None,
                 "ADDRESS":None}
            dff=pd.DataFrame(std,columns=['ID',' NAME','CLASS','ROLL NO.','FATHER NAME','MOTHER NAME','GENDER','PHONE NO.','STREAM','ROUTE NO.','ADDRESS'])
            dfa=pd.concat([cl_12,dff],ignore_index=True,sort=False)
            show_class(dfa)
            dfa.to_csv('CLASS XII.csv')
            p=input("Do you want continue <y/n>").upper()
            if p=='N':
                break;
                
    else:
        print('--- INVALID ---') 
        

        
###############################################################################
        
                                                                                #TEACHER ADD
        
def teacher_add():
    tec=pd.read_csv('TEACHERS.csv')
    print()
    print("TEACHERS ADDMISSION")
    print('-------------------')
    print()
    show_teacher(tec)
    while True:
        print()
        print("TEACHER INFORMATION")
        print()
        ID=input("Enter Teacher ID :").upper()
        NAME=input("Enter Teacher Name :").upper()
        GENDER=input("Enter Gender of Teacher :").upper()
        DEPT=input("Enter Department of Teacher :").upper()
        SUBJECT=input("Enter Subject of Teacher :").upper()
        dic={'ID':[ID],
             'NAME':[NAME],
             'GENDER':[GENDER],
             'DEPARTMENT':[DEPT],
             'SUBJECT':[SUBJECT],
             'SALARY':None,
             'ROUTE NO.':None,
             "ADDRESS":None}
        dff=pd.DataFrame(dic,columns=['ID','NAME','GENDER','DEPARTMENT','SUBJECT','SALARY','ROUTE NO.','ADDRESS'])
        dfa=pd.concat([tec,dff],ignore_index=True,sort=False)
        show_teacher(dfa)
        dfa.to_csv('TEACHERS.csv')
        p=input("Do you want continue <y/n>").upper()
        if p=='N':
            break;
        
        
        
################################################################################
                


def teacher_menu():                                                             #TEACHER MENU
    print()
    print('TEACHERS')
    print('-------')
    print()
    print('1. Teacher Info')
    print('2. Appoint New Teacher')
    print()
    opp_t=input('SELECT :')
    if opp_t=='1':
        teacher_info()
    elif opp_t=='2':
        teacher_add()
    else:
        print('--- INVALID ---')    


################################################################################
        

    
def other_menu():                                                               #OTHER MENU
    print()
    print('NON_TEACHING STAFF')
    print('-----------')
    print()
    print('1. Staff Info')
    print('2. Appoint New Staff')
    print()
    op_o=input('SELECT :')
    if op_o=='1':
        other_info()
    elif op_o=='2':
        other_add()
    else:
        print('--- INVALID ---') 
           
    

################################################################################
        


def staff_menu():                                                               #STAFF MENU
    print()
    print('STAFF')
    print('----------')
    print()
    print("Select Category :")
    print("1. Teachers")
    print("2. Non-Teaching Staff")
    print()
    op_ss=input("SELECT :")      
    if op_ss=='1' :
        teacher_menu()
    elif op_ss=='2' :
        other_menu()
        
        

#################################################################################
        


def student_menu():                                                             #STUDENT MENU
        print()
        print('STUDENTS')
        print('-------')
        print()
        print('1. Student Info')
        print('2. Student Admission')
        print()
        op_s=input('SELECT :')
        if op_s=='1':
            student_info()
        elif op_s=='2':
            student_add()
        else:
            print('--- INVALID ---')
            
            

#################################################################################
                
                                                                                  #MAIN MENU
print()
print('S C H O O L    D A T A B A S E')
print('------------------------------')
print('------------------------------')

while flag==1:
    print()
    print("MAIN MENU")
    print('---------')
    print()
    print("1. Students")
    print("2. Admins")
    print("3. Staff")
    op_m=input("SELECT :")
    if op_m=='1':
        student_menu()
    elif op_m=='2':
          admin_menu()
    elif op_m=='3':
        staff_menu()
    print()    
    print("Do you want to go again")
    cont=input(" Y/N :").upper()
    if cont=="Y":
        flag=1
    else:
        flag=0
