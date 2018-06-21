from __future__ import print_function
from datetime import date, datetime, timedelta
from faker import Faker
import random
from random import randint
import mysql.connector
from collections import Counter
import json

fake = Faker()
fake.seed_instance()

noD = 5500

noE = 6000
noB = 0


add_dep = ("INSERT INTO Department "
               "(Name, Email, phone) "
               "VALUES (%s, %s, %s)")

add_emp = ("INSERT INTO Employee "
               "(SSN, Name, Mobile, Birthdate, DepartmentID) "
               "VALUES (%s, %s, %s, %s, %s)")

add_bonus = ("INSERT INTO EmployeeBonus "
               "(EmployeeSSN, Reason, BonusDate, Value) "
               "VALUES (%s, %s, %s, %s)")



with open('config.json') as data_file:
    config = json.loads(data_file.read())
dbconfig = config["mydb"]
cnx = mysql.connector.connect(**dbconfig)
cursor = cnx.cursor()

bench  = int(config["bench"])
print ("Connected, Bench = " + str(bench))

'''
Minimal Example for the article
'''

if (bench == 1):



    for _ in range(noD):
        data_dep = (fake.name(), fake.ascii_safe_email(), fake.phone_number())
        cursor.execute(add_dep, data_dep)
    cnx.commit()

    print('Departments Added')


    cursor.execute("SELECT id FROM Department;")
    depsIds = cursor.fetchall()
    depsIds = list(sum(depsIds , ()))
    depsIds.append(0)
    # print(depsIds)
    cursor.execute("SELECT SSN FROM Employee;")
    print('fetching ssns')
    ssns = cursor.fetchall()
    print('ssns fetched')
    print('convert ssns to list')
    # ssns = list(sum(ssns , ()))
    #ssns = list(cursor)
    #print(ssns)
    ssns = [item[0] for item in ssns]
    print('convert ssns to dictionary')
    #ssns = Counter(ssns)
    ssns = dict((s,1) for s in ssns)
    dp = 0
    added = 0
    print('will begin adding employees')
    for _ in range(noE):
        depId = random.choice(depsIds)
        if(depId == 0):
            depId = None
        ssn = fake.ssn()
        while ssn in ssns:
            ssn = fake.ssn()
            dp = dp +1
            print(dp)
        # ssns.append(ssn)
        ssns[ssn] = 1
        added = added+1

        if (added % 10000 ==0):
            cnx.commit()
            print('added',added)
        data_emp = (ssn,fake.name(),fake.phone_number(), fake.date(), depId)
        #print(data_emp)
        cursor.execute(add_emp, data_emp)
    cnx.commit()


    print('Employees Added')

    cursor.execute("SELECT SSN FROM Employee;")
    ssns = cursor.fetchall()


    ssns = [item[0].encode('ascii', 'ignore') for item in ssns]



    # for i,s in enumerate(ssns):
    #     ssns[i] = s.encode('ascii', 'ignore')
    added = 0
    for _ in range(noB):
        ssn = random.choice(ssns)
        data_bonus= (ssn,fake.text(),fake.date(), randint(100, 1000))
        cursor.execute(add_bonus, data_bonus)
        added = added+1
        if (added % 10000 ==0):
            cnx.commit()
            print('added',added)
        
    cnx.commit()

    print('Bonuses Added')

else:


    data_dep = ('IT','it@example.com','(005)-555 5555')
    cursor.execute(add_dep, data_dep)
    data_dep = ('Sales','sales@example.com','(005)-555 5556')
    cursor.execute(add_dep, data_dep)
    cnx.commit()
    
    data_emp = ('001-01-1933','Bob','(005)-015 4567', '1981-08-21', 1)
    cursor.execute(add_emp, data_emp)

    data_emp = ('004-02-1543','Alice','(005)-013 5678', '1972-01-01', None)
    cursor.execute(add_emp, data_emp)

    data_emp = ('009-02-1422','Dan','(005)-014 9876', '1993-03-27', 2)
    cursor.execute(add_emp, data_emp)

    data_bonus= ('001-01-1933','Over time','2017-05-05', 100)
    cursor.execute(add_bonus, data_bonus)
    data_bonus= ('001-01-1933','Early delivery','2017-05-07', 150)
    cursor.execute(add_bonus, data_bonus)
    data_bonus= ('004-02-1543','Travelling','2017-05-08', 500)
    cursor.execute(add_bonus, data_bonus)


    cnx.commit()

cursor.close()
cnx.close()
