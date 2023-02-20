from tabulate import tabulate

while (True):
    print("""
            ============================================================================
                                    1 WELCOME TO COVID CENTER
            ============================================================================
    """)
    import mysql.connector as sql

    mysql = sql.connect(host="localhost", user="root", passwd="MKsadam2002@")
    mycursor = mysql.cursor()
    mycursor.execute("use project")

    while (True):
        print("""
                                        1.Administration
                                        2.Patient(Details)
                                        3.Sign Out


                                                                    """)
        a = int(input("ENTER YOUR CHOICE:"))
        if a == 1:
            print("""
                    1. Display Doctor's Details
                    2. Update Appointmet Status
                    3. Update Patient's Medical History
                    4. Update Vaccine detail
                    5 Show vaccine detail
                    6. Exit
                                             """)
            while (True):
                b = int(input("Enter your Choice:"))
                if b == 1:
                    mycursor.execute("select * from doctor")
                    record = mycursor.fetchall()
                    print()
                    print(tabulate(record,
                                   headers=['Doc_name', 'Qualification', 'Phone_No', 'Age', 'Registration No',
                                            'Doctor ID',
                                            'fees'], tablefmt='psql'))
                    break
                elif b == 2:
                    print("""    
                            Enter patient's Aadhar No. whose status to be updated : 

                                                                 """)
                    aadhar_no = int(input("Enter your aadhar no"))
                    if (len(str(aadhar_no)) != 12):
                        print("Invalid format")
                        break
                    sql = "update appointment set app_status = 1 where aadhar_no = %s"
                    mycursor.execute("update appointment set app_status = 1 where aadhar_no = %s" % (aadhar_no))
                    mysql.commit()

                    break

                elif b == 3:
                    d = int(input("""Enter patient's Aadhar No. whose patient_medical to be updated 
                            Press 1 To enter general details
                            Press 2 to enter chronic dieases: """))
                    if (d == 1):
                        aadhar_no = int(input("enter your aadhar_no"))
                        if (len(str(aadhar_no)) != 12):
                            print("Invalid format")
                            break
                        weight = int(input("enter weight of the patient"))
                        height = int(input("enter height of the patient"))
                        blood_grp = input("enter the blood Grp:")

                        sql = "INSERT into patient_history values (%s,%s,%s,%s)"
                        mycursor.execute(sql, (weight, height, blood_grp, aadhar_no))
                        mysql.commit()
                    else:
                        aadhar_no = int(input("enter your aadhar_no"))
                        if (len(str(aadhar_no)) != 12):
                            print("Invalid format")
                            break
                        n = int(input("how many disease does the patient have"))
                        while (n):
                            diease = input("Enter disease:")
                            sql = "INSERT INTO patient_diease values(%s,%s)"
                            mycursor.execute(sql, (aadhar_no, diease))
                            mysql.commit()
                            n = n - 1
                    break
                elif b == 4:
                    aadhar_no = input("enter your aadhar no")
                    if (len(str(aadhar_no)) != 12):
                        print("Invalid format")
                        break
                    no_of_dose = input("enter no doses")
                    mycursor.execute(
                        "update vaccine set no_of_dose = %s where aadhar_no = %s" % (no_of_dose, aadhar_no))
                    mysql.commit()
                    break
                elif b == 5:
                    sql = "select * from vaccine"
                    mycursor.execute(sql)
                    rec = mycursor.fetchall()
                    print()
                    print(tabulate(rec,
                                   headers=['Aadhar No', 'Number of Doses', 'Vaccine Name'
                                            ], tablefmt='psql'))
                    break
                elif b == 6:
                    break

        elif a == 2:
            print("""
                                    1. APPOINTMENT
                                    2. BILLING
                                    3. PERSONAL INFO
                                    4. Enter vaccine details
                                    5.See you vaccine status
                                    6.Exit
                                                        """)
            while (True):
                c = int(input("Enter your Choice:"))
                if c == 1:
                    app_date = input("Enter date of appointment ")
                    doc_id = input("enter doctor id ")
                    aadhar_no = input("enter your aadhar number ")
                    if (len(str(aadhar_no)) != 12):
                        print("Invalid format")
                        break
                    pat_name = input("enter your name ")
                    phn_no = input("enter your phone number")
                    if (len(str(phn_no)) != 10):
                        print("Invalid format")
                        break
                    age = input("enter your age")
                    app_status = 0
                    sql = "INSERT INTO appointment (app_date,doc_id,aadhar_no,pat_name,phn_no,age,app_status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    sql2 = "INSERT INTO billing (aadhar_no,doc_id,pat_name,age) VALUES (%s,%s,%s,%s)"

                    mycursor.execute(sql, (app_date, doc_id, aadhar_no, pat_name, phn_no, age, app_status))
                    mysql.commit()
                    mycursor.execute(sql2, (aadhar_no, doc_id, pat_name, age))
                    mysql.commit()
                    up = ''' update appointment,doctor
                             set appointment.fees = doctor.fees 
                             where appointment.doc_id = doctor.doc_id'''
                    up1 = '''update billing,doctor
                             set billing.fees = doctor.fees 
                             where billing.doc_id = doctor.doc_id'''
                    mycursor.execute(up)
                    mycursor.execute(up1)
                    mysql.commit()

                elif c == 2:
                    aadhar_no = int(input("enter your aadhar number to show your bill : "))
                    if (len(str(aadhar_no)) != 12):
                        print("Invalid format")
                        break
                    sql = "SELECT * from appointment where aadhar_no = %s"
                    mycursor.execute(sql, (aadhar_no,))
                    record = mycursor.fetchone()
                    if (record[6] == 0):
                        print("Your appointment is due")
                    elif (record[6] == 1):
                        sql = "select * from billing where aadhar_no = %s"
                        mycursor.execute(sql, (aadhar_no,))
                        rec = mycursor.fetchall()
                        print()
                        print(tabulate(rec,
                                       headers=['Aadhar No', 'Doctor Id', 'Name',
                                                'Age', 'fees'], tablefmt='psql'))


                    break


                elif c == 3:
                    aadhar_no = input("enter your aadhar number to show your detail : ")
                    if (len(str(aadhar_no)) != 12):
                        print("Invalid format")
                        break
                    sql = "SELECT weight,height,blood_grp from patient_history where aadhar_no = %s"
                    mycursor.execute(sql, (aadhar_no,))
                    record = mycursor.fetchall()
                    print(tabulate(record,
                                   headers=['Weight', 'Height', 'Blood Group'
                                            ], tablefmt='psql'))

                    sql = "SELECT * from patient_diease where aadhar_no = %s"
                    mycursor.execute(sql, (aadhar_no,))
                    record = mycursor.fetchall()
                    print(tabulate(record,
                                   headers=['Aadhar No', 'Disease'], tablefmt='psql'))
                    break


                elif c == 4:
                    aadhar_no = input("enter your aadhar no")
                    if (len(str(aadhar_no)) != 12):
                        print("Invalid format")
                        break
                    no_of_dose = (input("enter no of vaccine dose"))
                    name_of_vaccine = input("enter name of vaccine")
                    sql2 = "INSERT INTO vaccine (aadhar_no,no_of_dose,name_of_vaccine) VALUES (%s,%s,%s)"
                    mycursor.execute(sql2, (aadhar_no, no_of_dose, name_of_vaccine))
                    mysql.commit()
                    break
                elif c == 5:
                    aadhar_no = input("enter your aadhar no")
                    if (len(str(aadhar_no)) != 12):
                        print("Invalid format")
                        break
                    sql = "select * from vaccine where aadhar_no = %s"
                    mycursor.execute(sql, (aadhar_no,))
                    rec = mycursor.fetchall()
                    print()
                    print(tabulate(rec,
                                   headers=['Aadhar No', 'Number of Doses', 'Vaccine Name'
                                            ], tablefmt='psql'))
                    break
                elif c == 6:
                    break

        if a == 3:
            break
    break