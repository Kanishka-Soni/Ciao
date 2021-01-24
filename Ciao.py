from typing import Any
from tkinter.ttk import *
from tkinter import *
import sqlite3
import random
import string
import time
import calendar
import tkinter as tk
from datetime import datetime
from datetime import date

connection = sqlite3.connect('Ciao_data.db')
cursor = connection.cursor()


def tables():
    cursor.execute('CREATE TABLE IF NOT EXISTS place (place_id TEXT PRIMARY KEY,name TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS package (pk_id TEXT PRIMARY KEY, or_id TEXT,ds_id TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS flights (flight_no TEXT PRIMARY KEY,airline TEXT, distance REAL,'
                   'dep_time TEXT,arr_time TEXT,or_id TEXT,ds_id TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS trains (train_no TEXT PRIMARY KEY,or_id TEXT,ds_id TEXT, distance REAL,'
                   'dep_time TEXT,arr_time TEXT, name TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS car (car_no INT PRIMARY KEY,model TEXT,or_id TEXT,ds_id TEXT, '
                   'distance REAL, capacity INT)')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS hotels (ht_id TEXT PRIMARY KEY, name TEXT, rating INT,tariff REAL,swim TEXT,garden TEXT,spa TEXT )')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS airbnb (airbnb_id TEXT PRIMARY KEY,tariff REAL, rooms INT,swim TEXT,park TEXT,address TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS activities (act_id INT PRIMARY KEY,place_id TEXT, cost REAL,'
                   'duration INT,start_time TEXT,end_time TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS details (it_id TEXT,or_id TEXT,ds_id TEXT,dep TEXT,arr TEXT, '
                   'no_pass INT,discount INT, senior INT,no_day INT,dep_mode TEXT,arr_mode TEXT,dep_id TEXT,'
                   'arr_id TEXT,acc_mode TEXT,acc_no TEXT,wifi TEXT,breakfast TEXT,no_rooms INT,act_id INT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS act_det (it_id TEXT, act1 INT, act2 INT, act3 INT, act4 INT, '
                   'act5 INT, act6 INT, act7 INT, act8 INT, act9 INT, act10 INT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS pays6 (it_id TEXT PRIMARY KEY, passengers INT, code TEXT, '
                   'travel_mode INT,travel_mode1 INT,acc_mode INT, dep_name TEXT,arr_name TEXT,acc_name TEXT,'
                   'dep REAL,arr REAL, tariff REAL,wifi REAL, breakfast REAL,rooms INT,'
                   'ac1 REAL,ac2 REAL,ac3 REAL,ac4 REAL,ac5 REAL,'
                   'a1 TEXT,a2 TEXT,a3 TEXT,a4 TEXT,a5 TEXT,days INT)')


def place():
    cursor.execute("INSERT INTO place VALUES ('bom', 'Mumbai')")
    cursor.execute("INSERT INTO place VALUES ('del', 'Delhi')")
    cursor.execute("INSERT INTO place VALUES ('jai', 'Jaipur')")
    cursor.execute("INSERT INTO place VALUES ('coc', 'Kochi')")


def package():
    cursor.execute("INSERT INTO package VALUES ('b00d','bom','del')")
    cursor.execute("INSERT INTO package VALUES ('b00j','bom','jai')")
    cursor.execute("INSERT INTO package VALUES ('b00k','bom','coc')")
    cursor.execute("INSERT INTO package VALUES ('d00b','del','bom')")
    cursor.execute("INSERT INTO package VALUES ('d00j','del','jai')")
    cursor.execute("INSERT INTO package VALUES ('d00k','del','coc')")


def flights():
    cursor.execute("INSERT INTO flights VALUES ('AI1001','AIR INDIA',7400,'07:00','09:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1001','SPICE JET',7488,'12:00','14:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('6E1001','INDIGO',8000,'16:00','18:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('AI1011','AIR INDIA',8052,'11:00','13:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1091','SPICE JET',8152,'15:00','17:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('6E1042','INDIGO',8200,'20:00','21:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('6E1934','INDIGO',8270,'17:00','19:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('AA1014','AIR ASIA',8490,'20:00','22:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('GA1015','GO AIR',9000,'07:00','09:00','bom','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1016','SPICE JET',10000,'09:00','11:00','bom','del')")

    cursor.execute("INSERT INTO flights VALUES ('AI1002','AIR INDIA',6700,'08:00','10:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1002','SPICE JET',6905,'12:00','14:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('6E1002','INDIGO',7000,'20:00','22:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('AI1012','AIR INDIA',7400,'18:00','20:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1012','SPICE JET',7488,'16:00','18:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('6E1012','INDIGO',8000,'12:00','14:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('AA9214','AIR ASIA',8052,'20:00','22:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('GA1115','GO AIR',8152,'23:00','01:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ7716','SPICE JET',8500,'14:00','16:00','bom','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ7616','SPICE JET',9000,'18:00','20:00','bom','jai')")

    cursor.execute("INSERT INTO flights VALUES ('AI1003','AIR INDIA',6777,'13:00','15:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1003','SPICE JET',7210,'17:00','19:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('6E1003','INDIGO',7710,'22:00','00:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('AI1013','AIR INDIA',8000,'15:00','17:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1013','SPICE JET',8000,'11:00','13:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('6E1013','INDIGO',8005,'20:00','22:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('AA9114','AIR ASIA',9000,'20:00','22:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('GA1145','GO AIR',9007,'23:00','01:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1116','SPICE JET',10000,'13:00','15:00','bom','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ6716','SPICE JET',11567,'14:00','16:00','bom','coc')")

    cursor.execute("INSERT INTO flights VALUES ('AI1005','AIR INDIA',6000,'07:00','08:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1005','SPICE JET',6434,'11:00','12:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('6E1005','INDIGO',6554,'15:00','16:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('AI1015','AIR INDIA',6700,'17:00','18:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1015','SPICE JET',6900,'09:00','10:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('6E1079','INDIGO',7000,'7:00','8:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('6E1077','INDIGO',8000,'20:00','22:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('AA0114','AIR ASIA',8500,'20:00','21:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('GA0145','GO AIR',9000,'18:00','19:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0116','SPICE JET',10000,'17:00','18:00','del','jai')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0716','SPICE JET',11709,'11:00','13:00','del','jai')")

    cursor.execute("INSERT INTO flights VALUES ('AI1004','AIR INDIA',7777,'12:30','16:00','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1004','SPICE JET',8042,'21:30','01:00','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('6E1004','INDIGO',8100,'07:00','10:30','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('AI104','AIR INDIA',8400,'14:30','18:00','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1014','SPICE JET',8800,'07:30','11:00','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('6E1014','INDIGO',9000,'12:00','15:30','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('AA3114','AIR ASIA',10000,'20:00','23:30','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('GA3145','GO AIR',11700,'11:00','14:30','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ3116','SPICE JET',12000,'11:30','14:00','del','coc')")
    cursor.execute("INSERT INTO flights VALUES ('SJ3716','SPICE JET',14500,'09:00','12:30','del','coc')")

    cursor.execute("INSERT INTO flights VALUES ('AI1006','AIR INDIA',5000,'06:00','08:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1006','SPICE JET',5678,'17:00','19:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('6E1006','INDIGO',6009,'5:00','7:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('AI1123','AIR INDIA',6100,'8:00','10:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1333','SPICE JET',6307,'12:00','14:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('6E1016','INDIGO',6400,'15:00','17:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('AA0314','AIR ASIA',6600,'20:00','22:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('GA0345','GO AIR',7000,'20:30','23:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0316','SPICE JET',8090,'14:30','17:00','del','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0313','SPICE JET',9000,'11:00','13:30','del','bom')")

    cursor.execute("INSERT INTO flights VALUES ('AI1007','AIR INDIA',8900,'06:00','08:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1007','SPICE JET',9123,'17:00','19:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('6E1007','INDIGO',9588,'05:00','07:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('AI1017','AIR INDIA',9600,'16:00','18:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1017','SPICE JET',10090,'07:00','09:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('6E1017','INDIGO',11000,'15:00','17:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('AA0169','AIR ASIA',11500,'12:00','14:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('GA0169','GO AIR',12000,'13:30','15:30','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0169','SPICE JET',14600,'11:00','13:00','jai','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0769','SPICE JET',15345,'08:00','10:30','jai','bom')")

    cursor.execute("INSERT INTO flights VALUES ('AI1008','AIR INDIA',7500,'06:00','08:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1008','SPICE JET',7763,'17:00','19:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('6E1008','INDIGO',7800,'05:00','07:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('AI1018','AIR INDIA',8000,'16:00','18:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1018','SPICE JET',8263,'07:00','09:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('6E1018','INDIGO',8463,'15:00','17:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('AA0694','AIR ASIA',8500,'20:00','22:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('GA0695','GO AIR',8700,'07:00','09:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0696','SPICE JET',8900,'05:00','07:00','coc','bom')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0611','SPICE JET',9000,'03:00','05:30','coc','bom')")

    cursor.execute("INSERT INTO flights VALUES ('AI1009','AIR INDIA',7410,'07:00','09:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1009','SPICE JET',7500,'12:00','14:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('6E1009','INDIGO',7700,'16:00','18:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('AI1019','AIR INDIA',7700,'17:00','19:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1019','SPICE JET',7900,'07:00','09:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('6E1019','INDIGO',8000,'06:00','08:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('AA6914','AIR ASIA',8300,'20:00','22:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('GA6945','GO AIR',8700,'11:00','13:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ6916','SPICE JET',9000,'12:00','14:00','jai','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ6910','SPICE JET',10000,'09:00','11:00','jai','del')")

    cursor.execute("INSERT INTO flights VALUES ('AI1010','AIR INDIA',6700,'07:00','09:00','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1010','SPICE JET',6800,'12:00','14:00','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('6E1010','INDIGO',6850,'16:00','18:00','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('AI1020','AIR INDIA',6900,'17:00','19:30','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ1020','SPICE JET',7003,'7:00','9:30','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('6E1020','INDIGO',7213,'6:00','8:30','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('AA0420','AIR ASIA',7320,'20:00','22:30','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('GA0420','GO AIR',7400,'20:30','23:00','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0423','SPICE JET',7500,'15:00','17:30','coc','del')")
    cursor.execute("INSERT INTO flights VALUES ('SJ0343','SPICE JET',8500,'15:30','18:00','coc','del')")


def car():
    cursor.execute("INSERT INTO car VALUES (4000,'HYUNDAI i10','bom','del','3422',4)")
    cursor.execute("INSERT INTO car VALUES (8000,'HYUNDAI i10','bom','jai','3422',4)")
    cursor.execute("INSERT INTO car VALUES (1003,'HYUNDAI i10','bom','coc','3422',4)")
    cursor.execute("INSERT INTO car VALUES (5005,'HYUNDAI i10','del','jai','3422',4)")
    cursor.execute("INSERT INTO car VALUES (7007,'HYUNDAI i10','del','coc','3422',4)")
    cursor.execute("INSERT INTO car VALUES (6901,'HYUNDAI i10','del','bom','3422',4)")

    cursor.execute("INSERT INTO car VALUES (4719,'HYUNDAI i20','bom','del','3777',4)")
    cursor.execute("INSERT INTO car VALUES (8719,'HYUNDAI i20','bom','jai','3777',4)")
    cursor.execute("INSERT INTO car VALUES (1619,'HYUNDAI i20','bom','coc','3777',4)")
    cursor.execute("INSERT INTO car VALUES (5619,'HYUNDAI i20','del','jai','3777',4)")
    cursor.execute("INSERT INTO car VALUES (7719,'HYUNDAI i20','del','coc','3777',4)")
    cursor.execute("INSERT INTO car VALUES (1219,'HYUNDAI i20','del','bom','3777',4)")

    cursor.execute("INSERT INTO car VALUES (4209,'HONDA AMAZE','bom','del','3990',5)")
    cursor.execute("INSERT INTO car VALUES (4259,'HONDA AMAZE','bom','jai','3990',5)")
    cursor.execute("INSERT INTO car VALUES (4559,'HONDA AMAZE','bom','coc','3990',5)")
    cursor.execute("INSERT INTO car VALUES (4869,'HONDA AMAZE','del','jai','3990',5)")
    cursor.execute("INSERT INTO car VALUES (4889,'HONDA AMAZE','del','coc','3990',5)")
    cursor.execute("INSERT INTO car VALUES (4009,'HONDA AMAZE','del','bom','3990',5)")

    cursor.execute("INSERT INTO car VALUES (3687,'MARUTI ERTIGA','bom','del','4300',8)")
    cursor.execute("INSERT INTO car VALUES (1089,'MARUTI ERTIGA','bom','jai','4300',8)")
    cursor.execute("INSERT INTO car VALUES (0986,'MARUTI ERTIGA','bom','coc','4300',8)")
    cursor.execute("INSERT INTO car VALUES (1349,'MARUTI ERTIGA','del','jai','4300',8)")
    cursor.execute("INSERT INTO car VALUES (3824,'MARUTI ERTIGA','del','coc','4300',8)")
    cursor.execute("INSERT INTO car VALUES (1908,'MARUTI ERTIGA','del','bom','4300',8)")

    cursor.execute("INSERT INTO car VALUES (7019,'NISSAN ALTIMA','bom','del','4600',7)")
    cursor.execute("INSERT INTO car VALUES (3730,'NISSAN ALTIMA','bom','jai','4600',7)")
    cursor.execute("INSERT INTO car VALUES (0566,'NISSAN ALTIMA','bom','coc','4600',7)")
    cursor.execute("INSERT INTO car VALUES (6798,'NISSAN ALTIMA','del','jai','4600',7)")
    cursor.execute("INSERT INTO car VALUES (2133,'NISSAN ALTIMA','del','coc','4600',7)")
    cursor.execute("INSERT INTO car VALUES (2453,'NISSAN ALTIMA','del','bom','4600',7)")

    cursor.execute("INSERT INTO car VALUES (3681,'FORD FOCUS','bom','del','4750',5)")
    cursor.execute("INSERT INTO car VALUES (1081,'FORD FOCUS','bom','jai','4750',5)")
    cursor.execute("INSERT INTO car VALUES (0981,'FORD FOCUS','bom','coc','4750',5)")
    cursor.execute("INSERT INTO car VALUES (1341,'FORD FOCUS','del','jai','4750',5)")
    cursor.execute("INSERT INTO car VALUES (3821,'FORD FOCUS','del','coc','4750',5)")
    cursor.execute("INSERT INTO car VALUES (1901,'FORD FOCUS','del','bom','4750',5)")

    cursor.execute("INSERT INTO car VALUES (7011,'FORD MUSTANG','bom','del','4950',5)")
    cursor.execute("INSERT INTO car VALUES (3731,'FORD MUSTANG','bom','jai','4950',5)")
    cursor.execute("INSERT INTO car VALUES (0561,'FORD MUSTANG','bom','coc','4950',5)")
    cursor.execute("INSERT INTO car VALUES (6791,'FORD MUSTANG','del','jai','4950',5)")
    cursor.execute("INSERT INTO car VALUES (2131,'FORD MUSTANG','del','coc','4950',5)")
    cursor.execute("INSERT INTO car VALUES (2451,'FORD MUSTANG','del','bom','4950',5)")

    cursor.execute("INSERT INTO car VALUES (9220,'TATA NEXON','bom','del','5125',5)")
    cursor.execute("INSERT INTO car VALUES (4200,'TATA NEXON','bom','jai','5125',5)")
    cursor.execute("INSERT INTO car VALUES (4203,'TATA NEXON','bom','coc','5125',5)")
    cursor.execute("INSERT INTO car VALUES (9101,'TATA NEXON','del','jai','5125',5)")
    cursor.execute("INSERT INTO car VALUES (9200,'TATA NEXON','del','coc','5125',5)")
    cursor.execute("INSERT INTO car VALUES (9201,'TATA NEXON','del','bom','5125',5)")

    cursor.execute("INSERT INTO car VALUES (4720,'FIAT PALIO','bom','del','5125',5)")
    cursor.execute("INSERT INTO car VALUES (8770,'FIAT PALIO','bom','jai','5125',5)")
    cursor.execute("INSERT INTO car VALUES (1603,'FIAT PALIO','bom','coc','5125',5)")
    cursor.execute("INSERT INTO car VALUES (5645,'FIAT PALIO','del','jai','5125',5)")
    cursor.execute("INSERT INTO car VALUES (7777,'FIAT PALIO','del','coc','5125',5)")
    cursor.execute("INSERT INTO car VALUES (1231,'FIAT PALIO','del','bom','5125',5)")

    cursor.execute("INSERT INTO car VALUES (3333,'FIAT PUNTO','bom','del','5300',5)")
    cursor.execute("INSERT INTO car VALUES (5887,'FIAT PUNTO','bom','jai','5300',5)")
    cursor.execute("INSERT INTO car VALUES (1254,'FIAT PUNTO','bom','coc','5300',5)")
    cursor.execute("INSERT INTO car VALUES (3255,'FIAT PUNTO','del','jai','5300',5)")
    cursor.execute("INSERT INTO car VALUES (4562,'FIAT PUNTO','del','coc','5300',5)")
    cursor.execute("INSERT INTO car VALUES (6799,'FIAT PUNTO','del','bom','5300',5)")

    cursor.execute("INSERT INTO car VALUES (1120,'SWIFT DZIRE','bom','del','5300',5)")
    cursor.execute("INSERT INTO car VALUES (1170,'SWIFT DZIRE','bom','jai','5300',5)")
    cursor.execute("INSERT INTO car VALUES (1103,'SWIFT DZIRE','bom','coc','5300',5)")
    cursor.execute("INSERT INTO car VALUES (1145,'SWIFT DZIRE','del','jai','5300',5)")
    cursor.execute("INSERT INTO car VALUES (1177,'SWIFT DZIRE','del','coc','5300',5)")
    cursor.execute("INSERT INTO car VALUES (1131,'SWIFT DZIRE','del','bom','5300',5)")

    cursor.execute("INSERT INTO car VALUES (6969,'CHRYSLER 300','bom','del','6056',7)")
    cursor.execute("INSERT INTO car VALUES (1001,'CHRYSLER 300','bom','jai','6056',7)")
    cursor.execute("INSERT INTO car VALUES (2993,'CHRYSLER 300','bom','coc','6056',7)")
    cursor.execute("INSERT INTO car VALUES (2941,'CHRYSLER 300','del','jai','6056',7)")
    cursor.execute("INSERT INTO car VALUES (2920,'CHRYSLER 300','del','coc','6056',7)")
    cursor.execute("INSERT INTO car VALUES (2111,'CHRYSLER 300','del','bom','6056',7)")

    cursor.execute("INSERT INTO car VALUES (4269,'TATA HARRIER','bom','del','6690',8)")
    cursor.execute("INSERT INTO car VALUES (4201,'TATA HARRIER','bom','jai','6690',8)")
    cursor.execute("INSERT INTO car VALUES (4293,'TATA HARRIER','bom','coc','6690',8)")
    cursor.execute("INSERT INTO car VALUES (4241,'TATA HARRIER','del','jai','6690',8)")
    cursor.execute("INSERT INTO car VALUES (4220,'TATA HARRIER','del','coc','6690',8)")
    cursor.execute("INSERT INTO car VALUES (4211,'TATA HARRIER','del','bom','6690',8)")

    cursor.execute("INSERT INTO car VALUES (2340,'TOYOTA INNOVA','bom','del','7320',8)")
    cursor.execute("INSERT INTO car VALUES (3565,'TOYOTA INNOVA','bom','jai','7320',8)")
    cursor.execute("INSERT INTO car VALUES (5734,'TOYOTA INNOVA','bom','coc','7320',8)")
    cursor.execute("INSERT INTO car VALUES (4392,'TOYOTA INNOVA','del','jai','7320',8)")
    cursor.execute("INSERT INTO car VALUES (5342,'TOYOTA INNOVA','del','coc','7320',8)")
    cursor.execute("INSERT INTO car VALUES (4643,'TOYOTA INNOVA','del','bom','7320',8)")

    cursor.execute("INSERT INTO car VALUES (2341,'XUV 500','bom','del','7777',8)")
    cursor.execute("INSERT INTO car VALUES (3561,'XUV 500','bom','jai','7777',8)")
    cursor.execute("INSERT INTO car VALUES (5731,'XUV 500','bom','coc','7777',8)")
    cursor.execute("INSERT INTO car VALUES (4391,'XUV 500','del','jai','7777',8)")
    cursor.execute("INSERT INTO car VALUES (5341,'XUV 500','del','coc','7777',8)")
    cursor.execute("INSERT INTO car VALUES (4641,'XUV 500','del','bom','7777',8)")

    cursor.execute("INSERT INTO car VALUES (1320,'MG HECTOR','bom','del','8232',5)")
    cursor.execute("INSERT INTO car VALUES (1370,'MG HECTOR','bom','jai','8232',5)")
    cursor.execute("INSERT INTO car VALUES (1303,'MG HECTOR','bom','coc','8232',5)")
    cursor.execute("INSERT INTO car VALUES (1345,'MG HECTOR','del','jai','8232',5)")
    cursor.execute("INSERT INTO car VALUES (1377,'MG HECTOR','del','coc','8232',5)")
    cursor.execute("INSERT INTO car VALUES (1331,'MG HECTOR','del','bom','8232',5)")


def trains():
    cursor.execute("INSERT INTO trains VALUES('MD001','bom','del',3443,'21:00','11:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('MJ002','bom','jai',3443,'22:00','09:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('MK003','bom','coc',3443,'10:00','18:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('DM004','del','bom',3443,'20:00','11:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('DJ005','del','jai',3443,'19:00','23:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('DK006','del','coc',3443,'12:00','00:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('JD007','jai','del',3443,'03:00','15:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('KD008','coc','del',3443,'09:00','21:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('JM009','jai','bom',3443,'23:00','11:00', 'DURONTO')")
    cursor.execute("INSERT INTO trains VALUES('KM010','coc','bom',3443,'20:00','08:00', 'DURONTO')")

    cursor.execute("INSERT INTO trains VALUES('MD011','bom','del',3777,'19:00','09:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('MJ012','bom','jai',3777,'20:00','07:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('MK013','bom','coc',3777,'08:00','16:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('DM014','del','bom',3777,'18:00','09:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('DJ015','del','jai',3777,'19:00','07:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('DK016','del','coc',3777,'10:00','20:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('JD017','jai','del',3777,'10:00','00:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('KD018','coc','del',3777,'19:00','09:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('JM019','jai','bom',3777,'18:00','08:00', 'AKAL TAKHT')")
    cursor.execute("INSERT INTO trains VALUES('KM020','coc','bom',3777,'18:30','10:00', 'AKAL TAKHT')")

    cursor.execute("INSERT INTO trains VALUES('MD021','bom','del',3945,'23:00','13:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('MJ022','bom','jai',3945,'00:00','11:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('MK023','bom','coc',3945,'12:00','20:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('DM024','del','bom',3945,'22:00','13:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('DJ025','del','jai',3945,'21:00','09:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('DK026','del','coc',3945,'14:00','04:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('JD027','jai','del',3945,'14:00','07:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('KD028','coc','del',3945,'23:00','13:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('JM029','jai','bom',3945,'22:00','13:00', 'RAJDHANI')")
    cursor.execute("INSERT INTO trains VALUES('KM030','coc','bom',3945,'19:00','08:00', 'RAJDHANI')")

    cursor.execute("INSERT INTO trains VALUES('MD041','bom','del',4010,'20:00','07:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('MJ042','bom','jai',4010,'00:00','09:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('MK043','bom','coc',4010,'06:00','14:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('DM044','del','bom',4010,'16:00','07:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('DJ045','del','jai',4010,'09:00','19:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('DK046','del','coc',4010,'20:00','00:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('JD047','jai','del',4010,'23:00','11:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('KD048','coc','del',4010,'18:00','07:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('JM049','jai','bom',4010,'13:00','00:00', 'AGNIVEENA')")
    cursor.execute("INSERT INTO trains VALUES('KM050','coc','bom',4010,'16:00','07:00', 'AGNIVEENA')")

    cursor.execute("INSERT INTO trains VALUES('MD441','bom','del',4333,'16:00','06:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('MJ442','bom','jai',4333,'21:00','05:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('MK443','bom','coc',4333,'18:00','08:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('DM444','del','bom',4333,'18:30','09:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('DJ445','del','jai',4333,'11:00','20:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('DK446','del','coc',4333,'00:00','08:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('JD447','jai','del',4333,'08:00','21:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('KD448','coc','del',4333,'07:00','17:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('JM449','jai','bom',4333,'16:00','07:00', 'AHIMSA')")
    cursor.execute("INSERT INTO trains VALUES('KM450','coc','bom',4333,'15:00','09:00', 'AHIMSA')")

    cursor.execute("INSERT INTO trains VALUES('MD641','bom','del',4556,'18:00','05:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('MJ642','bom','jai',4556,'18:00','05:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('MK643','bom','coc',4556,'02:00','13:30', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('DM644','del','bom',4556,'04:00','09:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('DJ645','del','jai',4556,'06:00','03:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('DK646','del','coc',4556,'08:00','20:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('JD647','jai','del',4556,'08:00','19:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('KD648','coc','del',4556,'07:00','17:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('JM649','jai','bom',4556,'12:00','00:00', 'AMRAVATI')")
    cursor.execute("INSERT INTO trains VALUES('KM650','coc','bom',4556,'00:00','12:00', 'AMRAVATI')")

    cursor.execute("INSERT INTO trains VALUES('MD669','bom','del',4714,'06:00','20:00', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('MJ669','bom','jai',4714,'20:00','05:00', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('MK669','bom','coc',4714,'21:50','04:35', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('DM669','del','bom',4714,'06:50','23:35', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('DJ669','del','jai',4714,'04:50','19:35', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('DK669','del','coc',4714,'23:50','08:35', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('JD669','jai','del',4714,'12:00','00:00', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('KD669','coc','del',4714,'07:00','17:00', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('JM669','jai','bom',4714,'15:00','02:00', 'DHAULI')")
    cursor.execute("INSERT INTO trains VALUES('KM659','coc','bom',4714,'11:00','23:00', 'DHAULI')")

    cursor.execute("INSERT INTO trains VALUES('MD600','bom','del',4999,'17:00','07:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('MJ600','bom','jai',4999,'19:00','07:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('MK600','bom','coc',4999,'06:00','14:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('DM660','del','bom',4999,'16:00','07:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('DJ600','del','jai',4999,'15:00','23:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('DK600','del','coc',4999,'08:00','20:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('JD600','jai','del',4999,'08:00','19:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('KD600','coc','del',4999,'17:00','07:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('JM600','jai','bom',4999,'16:00','03:00', 'EKTA')")
    cursor.execute("INSERT INTO trains VALUES('KM600','coc','bom',4999,'14:00','05:00', 'EKTA')")

    cursor.execute("INSERT INTO trains VALUES('MD900','bom','del',5223,'03:00','21:00', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('MJ900','bom','jai',5223,'18:00','06:00', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('MK900','bom','coc',5223,'07:25','15:35', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('DM960','del','bom',5223,'16:25','09:35', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('DJ900','del','jai',5223,'04:25','20:35', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('DK900','del','coc',5223,'09:25','20:35', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('JD900','jai','del',5223,'19:25','08:35', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('KD900','coc','del',5223,'12:00','23:00', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('JM900','jai','bom',5223,'10:00','21:00', 'FRONTIER')")
    cursor.execute("INSERT INTO trains VALUES('KM900','coc','bom',5223,'11:00','20:00', 'FRONTIER')")

    cursor.execute("INSERT INTO trains VALUES('MD420','bom','del',5555,'04:00','18:00', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('MJ420','bom','jai',5555,'18:00','05:00', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('MK420','bom','coc',5555,'07:15','15:20', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('DM420','del','bom',5555,'08:15','21:40', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('DJ420','del','jai',5555,'09:15','17:15', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('DK420','del','coc',5555,'08:40','18:30', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('JD420','jai','del',5555,'08:00','16:00', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('KD420','coc','del',5555,'17:00','06:00', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('JM420','jai','bom',5555,'00:00','07:00', 'GAJANAN')")
    cursor.execute("INSERT INTO trains VALUES('KM420','coc','bom',5555,'02:00','14:00', 'GAJANAN')")


def hotel():
    cursor.execute("INSERT INTO hotels VALUES('h201','PENINSULA',0,18590,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h202','FOUR SEASONS',0,19670,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h203','ACQUALINA',0,18000,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h204','ASTRO RESORT',0,17390,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h205','SUNRISE POINT RESORT',0,16700,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h206','COUNTY RESTORT',0,17300,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h207','LIME WOOD RESORT',0,16000,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h208','PARADISE RESORT',0,19070,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h209','PEACOCK RESORT',0,14070,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h200','FABBEL',0,18070,'yes','yes','yes')")

    cursor.execute("INSERT INTO hotels VALUES('h101','TAJ',5,14050,'yes','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h102','SAHARA STAR',5,12670,'yes','no','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h103','JW MARRIOT',5,13000,'no','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h104','NOVATEL',5,11390,'yes','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h105','LALIT',5,13700,'yes','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h106','INTERCONTINENTAL',5,14300,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h107','SOFITEL',5,15000,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h108','THE FEERN',5,13070,'yes','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h109','MARINES BAY',5,13070,'yes','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h100','THE PALACE',5,13070,'yes','yes','no')")

    cursor.execute("INSERT INTO hotels VALUES('h301','PRUPLE ORCHID',4,8590,'yes','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h302','SPRING BROOK',4,7670,'yes','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h303','WHITE SEASON',4,5000,'yes','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h304','KNIGHTS INN',4,7390,'yes','yes','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h305','GARDEN HOUSE',4,6700,'yes','no','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h306','AIRPORT HOTEL',4,7300,'no','no','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h307','CANDLEWOOD',4,9000,'yes','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h308','BLOOMING DAY',4,6070,'no','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h309','ORANGE ROADS',4,6070,'yes','no','yes')")
    cursor.execute("INSERT INTO hotels VALUES('h300','AIRPORT STAY',4,5070,'no','no','no')")

    cursor.execute("INSERT INTO hotels VALUES('h401','WELCOME',3,3590,'no','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h402','HOTEL SANDY',3,3670,'no','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h403','HAPPY STAY',3,2000,'no','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h404','RELAX INN',3,2390,'no','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h405','ON THE ROADS',3,4700,'no','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h406','ORIENTAL',3,4300,'no','yes','no')")
    cursor.execute("INSERT INTO hotels VALUES('h407','VENTURE',3,3900,'no','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h408','THE SLEEP INN',3,2456,'yes','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h409','FANCY ROOMS',3,3456,'no','no','no')")
    cursor.execute("INSERT INTO hotels VALUES('h400','FLOWER WAYS',3,2690,'yes','no','no')")


def airbnb():
    cursor.execute("INSERT INTO airbnb VALUES('ab101',4045,1,'yes','yes','OLD CITY ROAD,4000-32')")
    cursor.execute("INSERT INTO airbnb VALUES('ab102',6678,2,'yes','no','OLD CITY ROAD,4000-32')")
    cursor.execute("INSERT INTO airbnb VALUES('ab103',8046,3,'yes','yes','OLD CITY ROAD,4000-32')")
    cursor.execute("INSERT INTO airbnb VALUES('ab104',10550,4,'yes','no','OLD CITY ROAD,4000-32')")
    cursor.execute("INSERT INTO airbnb VALUES('ab201',3056,1,'no','no','OLD CITY ROAD,4000-32')")
    cursor.execute("INSERT INTO airbnb VALUES('ab202',5033,2,'no','yes','OLD CITY ROAD,4000-32')")
    cursor.execute("INSERT INTO airbnb VALUES('ab203',7045,3,'no','yes','OLD CITY ROAD,4000-32')")
    cursor.execute("INSERT INTO airbnb VALUES('ab204',9067,4,'no','no','OLD CITY ROAD,4000-32')")

    cursor.execute("INSERT INTO airbnb VALUES('ab111',5078,1,'yes','yes','AIRPORT ROAD,4000-67')")
    cursor.execute("INSERT INTO airbnb VALUES('ab112',7065,2,'yes','yes','AIRPORT ROAD,4000-67')")
    cursor.execute("INSERT INTO airbnb VALUES('ab113',9073,3,'yes','yes','AIRPORT ROAD,4000-67')")
    cursor.execute("INSERT INTO airbnb VALUES('ab114',11054,4,'yes','no','AIRPORT ROAD,4000-67')")
    cursor.execute("INSERT INTO airbnb VALUES('ab211',4024,1,'no','no','AIRPORT ROAD,4000-67')")
    cursor.execute("INSERT INTO airbnb VALUES('ab212',6134,2,'no','yes','AIRPORT ROAD,4000-67')")
    cursor.execute("INSERT INTO airbnb VALUES('ab213',8436,3,'no','yes','AIRPORT ROAD,4000-67')")
    cursor.execute("INSERT INTO airbnb VALUES('ab214',10356,4,'no','no','AIRPORT ROAD,4000-67')")

    cursor.execute("INSERT INTO airbnb VALUES('ab121',6024,1,'yes','yes','NEW CITY,4000-89')")
    cursor.execute("INSERT INTO airbnb VALUES('ab122',8024,2,'yes','no','NEW CITY,4000-89')")
    cursor.execute("INSERT INTO airbnb VALUES('ab123',10024,3,'yes','yes','NEW CITY ,4000-89')")
    cursor.execute("INSERT INTO airbnb VALUES('ab124',10024,4,'yes','no','NEW CITY,4000-89')")
    cursor.execute("INSERT INTO airbnb VALUES('ab221',5024,1,'no','no','NEW CITY,4000-89')")
    cursor.execute("INSERT INTO airbnb VALUES('ab222',7021,2,'no','yes','NEW CITY,4000-89')")
    cursor.execute("INSERT INTO airbnb VALUES('ab223',9056,3,'no','yes','NEW CITY,4000-89')")
    cursor.execute("INSERT INTO airbnb VALUES('ab224',11460,4,'no','no','NEW CITY,4000-89')")

    cursor.execute("INSERT INTO airbnb VALUES('ab131',7024,1,'yes','yes','GARDEN LANE,4000-28')")
    cursor.execute("INSERT INTO airbnb VALUES('ab132',9013,2,'yes','no','GARDEN LANE,4000-28')")
    cursor.execute("INSERT INTO airbnb VALUES('ab133',11450,3,'yes','no','GARDEN LANE,4000-28')")
    cursor.execute("INSERT INTO airbnb VALUES('ab134',13780,4,'yes','yes','GARDEN LANE,4000-28')")
    cursor.execute("INSERT INTO airbnb VALUES('ab231',6035,1,'no','no','GARDEN LANE,4000-28')")
    cursor.execute("INSERT INTO airbnb VALUES('ab232',8045,2,'no','no','GARDEN LANE,4000-28')")
    cursor.execute("INSERT INTO airbnb VALUES('ab233',10240,3,'no','yes','GARDEN LANE,4000-28')")
    cursor.execute("INSERT INTO airbnb VALUES('ab234',11230,4,'no','yes','GARDEN LANE,4000-28')")

    cursor.execute("INSERT INTO airbnb VALUES('ab141',8013,1,'yes','no','MALL ROAD,4000-24')")
    cursor.execute("INSERT INTO airbnb VALUES('ab142',9046,2,'yes','no','MALL ROAD,4000-24')")
    cursor.execute("INSERT INTO airbnb VALUES('ab143',10360,3,'yes','yes','MALL ROAD,4000-24')")
    cursor.execute("INSERT INTO airbnb VALUES('ab144',110360,4,'yes','no','MALL ROAD,4000-24')")
    cursor.execute("INSERT INTO airbnb VALUES('ab241',7004,1,'no','yes','MALL ROAD,4000-24')")
    cursor.execute("INSERT INTO airbnb VALUES('ab242',8002,2,'no','yes','MALL ROAD,4000-24')")
    cursor.execute("INSERT INTO airbnb VALUES('ab243',9025,3,'no','no','MALL ROAD,4000-24')")
    cursor.execute("INSERT INTO airbnb VALUES('ab244',10350,4,'no','no','MALL ROAD,4000-24')")

    cursor.execute("INSERT INTO airbnb VALUES('ab151',4600,1,'yes','yes','AERO CITY,4000-81')")
    cursor.execute("INSERT INTO airbnb VALUES('ab152',5680,2,'yes','yes','AERO CITY,4000-81')")
    cursor.execute("INSERT INTO airbnb VALUES('ab153',6360,3,'yes','no','AERO CITY ,4000-81')")
    cursor.execute("INSERT INTO airbnb VALUES('ab154',7050,4,'yes','yes','AERO CITY,4000-81')")
    cursor.execute("INSERT INTO airbnb VALUES('ab251',3240,1,'no','yes','AERO CITY,4000-81')")
    cursor.execute("INSERT INTO airbnb VALUES('ab252',4035,2,'no','no','AERO CITY,4000-81')")
    cursor.execute("INSERT INTO airbnb VALUES('ab253',5025,3,'no','yes','AERO CITY,4000-81')")
    cursor.execute("INSERT INTO airbnb VALUES('ab254',6256,4,'no','no','AERO CITY,4000-81')")

    cursor.execute("INSERT INTO airbnb VALUES('ab161',3600,1,'yes','yes','PALACE TOWN ,4000-12')")
    cursor.execute("INSERT INTO airbnb VALUES('ab162',4680,2,'yes','yes','PALACE TOWN ,4000-12')")
    cursor.execute("INSERT INTO airbnb VALUES('ab163',5360,3,'yes','yes','PALACE TOWN ,4000-12')")
    cursor.execute("INSERT INTO airbnb VALUES('ab164',6050,4,'yes','no','PALACE TOWN ,4000-12')")
    cursor.execute("INSERT INTO airbnb VALUES('ab261',2240,1,'no','yes','PALACE TOWN ,4000-12')")
    cursor.execute("INSERT INTO airbnb VALUES('ab262',3035,2,'no','no','PALACE TOWN ,4000-12')")
    cursor.execute("INSERT INTO airbnb VALUES('ab263',4025,3,'no','yes','PALACE TOWN ,4000-12')")
    cursor.execute("INSERT INTO airbnb VALUES('ab264',5256,4,'no','no','PALACE TOWN ,4000-12')")


def activities():
    cursor.execute("INSERT INTO activities VALUES(01,'CITY TOUR',1000,480,'8:00','16:00')")
    cursor.execute("INSERT INTO activities VALUES(02,'NIGHT TOUR',1500,480,'00:00','8:00')")
    cursor.execute("INSERT INTO activities VALUES(03,'CYCLING TOUR',1800,120,'17:00','19:00')")
    cursor.execute("INSERT INTO activities VALUES(04,'WALKING TOUR',500,180,'7:00','10:00')")
    cursor.execute("INSERT INTO activities VALUES(05,'HERITAGE WALK',700,180,'8:00','11:00')")
    cursor.execute("INSERT INTO activities VALUES(06,'FILMCITY TOUR',2000,240,'12:00','16:00')")
    cursor.execute("INSERT INTO activities VALUES(07,'ADVENTUROUS TOUR',3000,720,'8:00','20:00')")
    cursor.execute("INSERT INTO activities VALUES(08,'OPEN BUS TOUR',1200,150,'10:00','12:30')")
    cursor.execute("INSERT INTO activities VALUES(09,'CLOSE TO THE NATURE',1800,240,'8:00','12:00')")
    cursor.execute("INSERT INTO activities VALUES(10,'CULTURAL TOUR',1900,360,'10:00','16:00')")


def pay2():
    t = Tk()
    t.config(bg='#ADEBBE')
    t.title('www.ciao.com')
    t.geometry('530x680+420+0')

    global gross
    cursor.execute("insert into pays6 (it_id) values (?)", (it_no,))
    cursor.execute("select * from details where it_id=? ", (it_no,))
    a = cursor.fetchall()
    a = a[0]
    cursor.execute("update pays6 set days=? where it_id=?", (a[8], it_no,))

    Label(t, text="ciao", font=("Glasgow Script", 80), bg='#ADEBBE').pack()
    Label(t, text="", bg='#ADEBBE').pack()
    Label(t, text="ITINERARY", font=("Montserrat", 30), bg='#ADEBBE').pack()
    Label(t, text="", bg='#ADEBBE').pack()

    def p2():
        t2 = Tk()
        t2.title("www.ciao.com")
        t2.config(bg='#ADEBBE')
        t2.geometry('1000x650+200+150')
        cursor.execute("select * from pays6 where it_id=?", (it_no,))
        z = cursor.fetchall()
        z = z[0]
        print(z)

        def p4():
            t2.destroy()
            t3 = Tk()
            t3.title("www.ciao.com")
            t3.config(bg='#ADEBBE')
            t3.geometry('450x350+500+150')

            Label(t3, text="Your payment was SUCCESSFULLY PROCESSED!\nThank you for booking with us"
                           "\n Have a safe travel. \n CIAO!", font=("Montserrat", 15), bg='#ADEBBE').pack()
            t3.mainloop()

        def p3():
            Button(t2, text="Gpay", command=p4, font=("Montserrat", 10)).grid(row=x, column=2, pady=20)
            Button(t2, text="PayTM", command=p4, font=("Montserrat", 10)).grid(row=x, column=3)

        gross = 0
        Label(t2, text='Particulars', font=('Courier New', 15), bg='#ADEBBE').grid(row=0, column=1)
        Label(t2, text='Cost', font=('Courier New', 15), bg='#ADEBBE').grid(row=0, column=2)
        Label(t2, text='Quantity', font=('Courier New', 15), bg='#ADEBBE').grid(row=0, column=3)
        Label(t2, text='Total', font=('Courier New', 15), bg='#ADEBBE').grid(row=0, column=4)

        Label(t2, text='1', font=('Courier New', 12), bg='#ADEBBE').grid(row=1, column=0)
        Label(t2, text=z[6], font=('Courier New', 12), bg='#ADEBBE').grid(row=1, column=1)
        Label(t2, text=z[9], bg='#ADEBBE', font=('Courier New', 12)).grid(row=1, column=2)
        if z[3] == 1:
            Label(t2, text=z[1], bg='#ADEBBE', font=('Courier New', 12)).grid(row=1, column=3)
            t = z[1] * z[9]
        else:
            Label(t2, text='1', bg='#ADEBBE', font=('Courier New', 12)).grid(row=1, column=3)
            t = z[9]
        Label(t2, text=t, bg='#ADEBBE', font=('Courier New', 12)).grid(row=1, column=4)
        gross+=t

        Label(t2, text='2', bg='#ADEBBE', font=('Courier New', 12)).grid(row=2, column=0)
        Label(t2, text=z[7], bg='#ADEBBE', font=('Courier New', 12)).grid(row=2, column=1)
        Label(t2, text=z[10], bg='#ADEBBE', font=('Courier New', 12)).grid(row=2, column=2)
        if z[4] == 1:
            Label(t2, text=z[1], bg='#ADEBBE',font=('Courier New', 12)).grid(row=2, column=3)
            t = z[1] * z[10]
        else:
            Label(t2, text='1', bg='#ADEBBE',font=('Courier New', 12)).grid(row=2, column=3)
            t = z[10]
        Label(t2, text=t, bg='#ADEBBE',font=('Courier New', 12)).grid(row=2, column=4)
        gross+=t

        Label(t2, text='3', bg='#ADEBBE', font=('Courier New', 12)).grid(row=3, column=0)
        Label(t2, text=z[8], bg='#ADEBBE', font=('Courier New', 12)).grid(row=3, column=1)
        Label(t2, text=z[11], bg='#ADEBBE', font=('Courier New', 12)).grid(row=3, column=2)
        if z[5] == 1:
            Label(t2, text=str(z[14])+'x'+str(z[25]), bg='#ADEBBE', font=('Courier New', 12)).grid(row=3, column=3)
            t = z[14] * z[11] * z[25]
        else:
            Label(t2, text='1x'+str(z[25]), bg='#ADEBBE', font=('Courier New', 12)).grid(row=3, column=3)
            t = z[11]*z[25]
        Label(t2, text=t, bg='#ADEBBE', font=('Courier New', 12)).grid(row=3, column=4)
        gross+=t

        if a[15] == 'yes':

            Label(t2, text="   WiFi", bg='#ADEBBE', font=('Courier New', 12)).grid(row=4, column=1)
            Label(t2, text=z[12], bg='#ADEBBE', font=('Courier New', 12)).grid(row=4, column=2)
            Label(t2, text='1', bg='#ADEBBE', font=('Courier New', 12)).grid(row=4, column=3)
            Label(t2, text=z[12], bg='#ADEBBE', font=('Courier New', 12)).grid(row=4, column=4)
            gross+=z[12]

        if a[16] == 'yes':
            Label(t2, text="  Breakfast", bg='#ADEBBE', font=('Courier New', 12)).grid(row=5, column=1)
            Label(t2, text=z[13], bg='#ADEBBE', font=('Courier New', 12)).grid(row=5, column=2)
            Label(t2, text=str(z[1])+'x'+str(z[25]), bg='#ADEBBE', font=('Courier New', 12)).grid(row=5, column=3)
            t = z[1]*z[13]*z[25]
            Label(t2, text=t, font=('Courier New', 12), bg='#ADEBBE').grid(row=5, column=4)
            gross+=t

        Label(t2, text='4', font=('Courier New', 12), bg='#ADEBBE').grid(row=6, column=0)
        Label(t2, text='Activities', font=('Courier New', 12), bg='#ADEBBE').grid(row=6, column=1)
        y = 1
        x = 7
        for i in range(15,19):
            if z[i] != None:
                Label(t2, text=z[i+5], font=('Courier New', 12), bg='#ADEBBE').grid(row=x, column=y)
                y += 1
                Label(t2, text=z[i], font=('Courier New', 12), bg='#ADEBBE').grid(row=x, column=y)
                y += 1
                Label(t2, text=z[1], bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=y)
                y += 1
                t = z[i]*z[1]
                Label(t2, text=t, bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=y)
                gross += t
                y = 1
                x += 1

        Label(t2, text="__________________", bg='#ADEBBE').grid(row=x, column=0)
        Label(t2, text="_______________________________", bg='#ADEBBE').grid(row=x, column=1)
        Label(t2, text="___________", bg='#ADEBBE').grid(row=x, column=2)
        Label(t2, text="___________", bg='#ADEBBE').grid(row=x, column=3)
        Label(t2, text="________________", bg='#ADEBBE').grid(row=x, column=4)
        x += 1

        Label(t2, text="GROSS TOTAL = ", bg='#ADEBBE', font=('Courier New', 15)).grid(row=x, column=3)
        Label(t2, text=gross, bg='#ADEBBE', font=('Courier New', 15)).grid(row=x, column=4)
        x += 1

        if z[2] == 'AB1973' or z[2]=='QWD12' or z[2]=='HOT67':
            Label(t2, text='DISCOUNT=', bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=3)
            Label(t2, text='1000.0', bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=4)
            gross -= 1000
            x += 1

        cursor.execute("select discount,senior from details where it_id=?", (it_no,))
        d = cursor.fetchall()
        d = d[0]
        print(d)
        if d[0] != 0:
            Label(t2, text="STUDENT DISCOUNT=", bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=3)
            Label(t2, text="1500.0", bg='#ADEBBE', font=('Courier New', 8)).grid(row=x, column=4)
            gross -= 1500
            x += 1

        if d[1]!= 0:
            Label(t2, text="SENIOR CITIZEN DISCOUNT=", bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=3)
            Label(t2, text="1500.0", bg='#ADEBBE', font=('Courier New', 8)).grid(row=x, column=4)
            gross -= 1500
            x += 1


        Label(t2, text="CGST (9%)=", bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=3)
        t = 9*gross/100
        Label(t2, text=t, bg='#ADEBBE', font=('Courier New',12)).grid(row=x, column=4)
        gross += t
        x += 1

        Label(t2, text="SGST (9%)=", bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=3)
        Label(t2, text=t, bg='#ADEBBE', font=('Courier New', 12)).grid(row=x, column=4)
        gross += t
        x += 1

        Label(t2, text='TOTAL COST=', bg='#ADEBBE', font=('Courier New', 15)).grid(row=x, column=3)

        Label(t2, text=round(gross, 2), bg='#ADEBBE', font=('Courier New', 15)).grid(row=x, column=4)
        x += 1
        Button(t2, text="PAY", bg='#ADEBBE', command=p3).grid(row=x, column=4)
        x += 1

    def p1():
        t1 = Tk()
        t1.title("www.ciao.com")
        t1.config(bg='#ADEBBE')
        t1.geometry('350x350+500+150')

        def p11():
            x = no_pass.get()
            x = int(x)
            y = code.get()
            cursor.execute("update pays6 set passengers=?,code=? where it_id=?", (x, y, it_no))
            t1.destroy()
            p2()

        Label(t1, text="", bg='#ADEBBE').pack()
        Label(t1, text="", bg='#ADEBBE').pack()
        Label(t1, text="Enter Number of Passengers:", bg='#ADEBBE', font=("Latinia", 12)).pack()
        no_pass = Entry(t1)
        no_pass.pack()
        Label(t1, text="", bg='#ADEBBE').pack()
        Label(t1, text="Enter Discount Code (If Applicable):", bg='#ADEBBE', font=("Latinia", 12)).pack()
        code = Entry(t1)
        code.insert(0, '')
        code.pack()
        Label(t1, text="", bg='#ADEBBE').pack()
        Label(t1, text="", bg='#ADEBBE').pack()
        Label(t1, text="", bg='#ADEBBE').pack()
        Label(t1, text="", bg='#ADEBBE').pack()
        Button(t1, text="NEXT", command=p11, font=("Montserrat", 12)).pack()
        t1.mainloop()

    def travels1():
        f1 = Tk()
        f1.title("www.ciao.com")
        f1.config(bg='#ADEBBE')
        f1.geometry('350x400+500+150')
        x = a[9]
        y = a[11]
        if x == '1':
            cursor.execute("select airline,dep_time,arr_time,distance from flights where flight_no=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute("update pays6 set travel_mode=1,dep=?,dep_name=? where it_id=?", (z[3], z[0], it_no,))
            cursor.execute("")

            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="FLIGHT", width=27, font=("Latinia", 20), bg='#ADEBBE').pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Flight No.", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f1, text=y, font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Airline", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f1, text=z[0], font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Departure Time", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f1, text=z[1], font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Arrival Time", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f1, text=z[2], font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
        elif x == '2':
            cursor.execute("select name,dep_time,arr_time,distance from trains where train_no=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute("update pays6 set travel_mode=1,dep=?,dep_name=? where it_id=?", (z[3], z[0], it_no,))

            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="TRAIN", width=27, font=("Latinia", 20), bg='#ADEBBE').pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Train No.", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f1, text=y, font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Name", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f1, text=z[0], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Departure Time", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f1, text=z[1], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Arrival Time", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f1, text=z[2], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
        else:
            cursor.execute("select model,capacity,distance from car where car_no=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute("update pays6 set travel_mode=0,dep=?,dep_name=? where it_id=?", (z[2], z[0], it_no,))

            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="CAR", width=27, bg='#ADEBBE', font=("Latinia", 20)).pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Car No.", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f1, text=y, bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Company", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f1, text=z[0], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f1, text="", bg='#ADEBBE').pack()
            Label(f1, text="Capacity", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f1, text=z[1], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()

    def travels2():
        f2 = Tk()
        f2.title("www.ciao.com")
        f2.config(bg='#ADEBBE')
        f2.geometry('350x400+500+150')
        x = a[10]
        y = a[12]
        if x == '1':
            cursor.execute("select airline,dep_time,arr_time,distance from flights where flight_no=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute("update pays6 set travel_mode1=1,arr=? ,arr_name=? where it_id=?", (z[3], z[0], it_no,))
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="FLIGHT", width=27, font=("Latinia", 20), bg='#ADEBBE').pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Flight No.", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f2, text=y, font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Airline", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f2, text=z[0], font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Departure Time", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f2, text=z[1], font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Arrival Time", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f2, text=z[2], font=("Caviar Dreams", 15), bg='#ADEBBE').pack()

        elif x == '2':
            cursor.execute("select name,dep_time,arr_time,distance from trains where train_no=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute("update pays6 set travel_mode1=1,arr=?,arr_name=? where it_id=?", (z[3], z[0], it_no,))

            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="TRAIN", width=27, font=("Latinia", 20), bg='#ADEBBE').pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Train No.", font=("Latinia", 12), bg='#ADEBBE').pack()
            Label(f2, text=y, font=("Caviar Dreams", 15), bg='#ADEBBE').pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Name", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f2, text=z[0], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Departure Time", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f2, text=z[1], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Arrival Time", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f2, text=z[2], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
        else:
            cursor.execute("select model,capacity,distance from car where car_no=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute("update pays6 set travel_mode1=0,arr=?,arr_name=? where it_id=?", (z[2], z[0], it_no,))

            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="CAR", width=27, bg='#ADEBBE', font=("Latinia", 20)).pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Car No.", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f2, text=y, bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Company", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f2, text=z[0], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f2, text="", bg='#ADEBBE').pack()
            Label(f2, text="Capacity", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f2, text=z[1], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()

    def acc():
        f3 = Tk()
        f3.title("www.ciao.com")
        f3.config(bg='#ADEBBE')
        f3.geometry('350x550+500+150')
        x = a[13]
        y = a[14]
        w = a[15]
        b = a[16]
        n = a[17]
        if x == '1':
            cursor.execute("select name,swim,garden,spa,tariff from hotels where ht_id=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute("update pays6 set acc_mode=1,acc_name=?,tariff=?,wifi=1000,breakfast=500,rooms=? "
                           "where it_id=? ", (z[0], z[4], n, it_no,))
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="HOTELS", width=20, bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Name", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=z[0], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Pool", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=z[1], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Garden", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=z[2], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Spa", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=z[3], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="WiFi:", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=w, bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Breakfast:", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=b, bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()

        else:
            cursor.execute("select address,swim,park,tariff from airbnb where airbnb_id=?", (y,))
            z = cursor.fetchall()
            z = z[0]
            cursor.execute(
                "update pays6 set acc_mode=0,acc_name='AIR BnB',tariff=?,wifi=1000,breakfast=500,rooms=? where it_id=? ",
                (z[3], n, it_no,))
            print(z)

            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="AIR BnB", bg='#ADEBBE', width=10, font=("Latinia", 20)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Address", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=z[0], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Pool", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=z[1], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Car Park", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=z[2], bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="WiFi:", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=w, bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()
            Label(f3, text="", bg='#ADEBBE').pack()
            Label(f3, text="Breakfast", bg='#ADEBBE', font=("Latinia", 12)).pack()
            Label(f3, text=b, bg='#ADEBBE', font=("Caviar Dreams", 15)).pack()

    def act():
        f4 = Tk()
        f4.title("www.ciao.com")
        f4.config(bg='#ADEBBE')
        f4.geometry('350x550+500+150')
        cursor.execute("select act1,act2,act3,act4,act5,act6,act7,act8,act9,act10 from act_det where it_id=?", (it_no,))
        x = cursor.fetchall()
        x = x[0]
        print(x)
        cursor.execute("select place_id,start_time,end_time,cost from activities")
        y = cursor.fetchall()
        print(y)
        k = 2
        Label(f4, text="", bg="#ADEBBE").pack()
        for i in range(0, 10):
            if x[i] == 1:
                Label(f4, text=y[i][0], font=("Latinia", 16), bg='#ADEBBE', width=20).pack()
                Label(f4, text=y[i][1], width=20, font=("Caviar Dreams", 14), bg='#ADEBBE').pack()
                Label(f4, text=y[i][2], width=20, font=("Caviar Dreams", 14), bg='#ADEBBE').pack()
                k += 1
                if k == 3:
                    cursor.execute("update pays6 set a1=?,ac1=? where it_id=?", (y[i][0], y[i][3], it_no,))
                elif k == 4:
                    cursor.execute("update pays6 set a2=?,ac2=? where it_id=?", (y[i][0], y[i][3], it_no,))
                elif k == 5:
                    cursor.execute("update pays6 set a3=?,ac3=? where it_id=?", (y[i][0], y[i][3], it_no,))
                elif k == 6:
                    cursor.execute("update pays6 set a4=?,ac4=? where it_id=?", (y[i][0], y[i][3], it_no,))
                elif k == 7:
                    cursor.execute("update pays6 set a5=?,ac5=? where it_id=?", (y[i][0], y[i][3], it_no,))
                else:
                    break

    Label(t, text="", height=3, bg='#ADEBBE').pack()
    b1 = Button(t, text="Origin to Destination", font=("Caviar Dreams", 15), width=35, command=travels1)
    b1.pack()
    Label(t, text="", bg='#ADEBBE').pack()
    b2 = Button(t, text="Destination to Origin", font=("Caviar Dreams", 15), width=35, command=travels2)
    b2.pack()
    Label(t, text="", bg='#ADEBBE').pack()
    b3 = Button(t, text="Accommodation", font=("Caviar Dreams", 15), command=acc, width=35)
    b3.pack()
    Label(t, text="", bg='#ADEBBE').pack()
    b4 = Button(t, text="Activities", font=("Caviar Dreams", 15), command=act, width=35)
    b4.pack()

    Label(t, text="", height=5, bg='#ADEBBE').pack()
    Button(t, text="Payment", command=p1, font=("Caviar Dreams", 18), bg='#EEF3AD').pack()
    t.mainloop()


def acts1():
    root1 = Tk()
    root1.config(bg='#74BEC1')
    root1.title('www.ciao.com')
    l0 = IntVar()
    l1 = IntVar()
    l2 = IntVar()
    l3 = IntVar()
    l4 = IntVar()
    l5 = IntVar()
    l6 = IntVar()
    l7 = IntVar()
    l8 = IntVar()
    l9 = IntVar()
    ch = StringVar()
    f1 = Frame(root1, width=200, height=750, bg="#EEF3AD")
    f2 = Frame(root1, width=800, height=750, bg="#ADEBBE")

    root1.configure(width=1450, height=750)

    def go_d():
        a0 = l0.get()
        a1 = l1.get()
        a2 = l2.get()
        a3 = l3.get()
        a4 = l4.get()
        a5 = l5.get()
        a6 = l6.get()
        a7 = l7.get()
        a8 = l8.get()
        a9 = l9.get()
        print(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
        cursor.execute(
            'UPDATE act_det SET act1=?,act2=?,act3=?,act4=?,act5=?,act6=?,act7=?,act8=?,act9=?,act10=? WHERE it_id=?',
            (a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, it_no))
        root1.destroy()
        pay2()

    def act():
        x = ch.get()
        c1 = Checkbutton(f2, text="", height=3, variable=l0, bg="#ADEBBE")
        c1.grid(row=1, column=0)
        c2 = Checkbutton(f2, text="", height=3, variable=l1, bg="#ADEBBE")
        c2.grid(row=2, column=0)
        c3 = Checkbutton(f2, text="", height=3, variable=l2, bg="#ADEBBE")
        c3.grid(row=3, column=0)
        c4 = Checkbutton(f2, text="", height=3, variable=l3, bg="#ADEBBE")
        c4.grid(row=4, column=0)
        c5 = Checkbutton(f2, text="", height=3, variable=l4, bg="#ADEBBE")
        c5.grid(row=5, column=0)
        c6 = Checkbutton(f2, text="", height=3, variable=l5, bg="#ADEBBE")
        c6.grid(row=6, column=0)
        c7 = Checkbutton(f2, text="", height=3, variable=l6, bg="#ADEBBE")
        c7.grid(row=7, column=0)
        c8 = Checkbutton(f2, text="", height=3, variable=l7, bg="#ADEBBE")
        c8.grid(row=8, column=0)
        c9 = Checkbutton(f2, text="", height=3, variable=l8, bg="#ADEBBE")
        c9.grid(row=9, column=0)
        c10 = Checkbutton(f2, text="", height=3, variable=l9, bg="#ADEBBE")
        c10.grid(row=10, column=0)
        Label(f2, text="ACTIVITY", font=("Latinia", 17), bg="#ADEBBE", width=12).grid(row=0, column=1)
        Label(f2, text="COST", font=("Latinia", 17), bg="#ADEBBE", width=10).grid(row=0, column=2)
        Label(f2, text="DURATION\n(in minutes)", font=("Latinia", 17), bg="#ADEBBE", width=12).grid(
            row=0, column=3)
        Label(f2, text="START\nTIME", font=("Latinia", 17), bg="#ADEBBE", width=10).grid(row=0, column=4)
        Label(f2, text="END\nTIME", font=("Latinia", 17), bg="#ADEBBE", width=10).grid(row=0, column=5)
        if x == 'Price-Low to High':
            cursor.execute(
                "select act_id, place_id , cost,duration ,start_time ,end_time from activities order by cost")
            y = cursor.fetchall()
        elif x == 'Duration-High to Low':
            cursor.execute(
                "select act_id, place_id , cost,duration ,start_time ,end_time from activities order by duration desc")
            y = cursor.fetchall()
        elif x == 'Duration-Low to High':
            cursor.execute(
                "select act_id, place_id , cost,duration ,start_time ,end_time from activities order by duration")
            y = cursor.fetchall()
        elif x == 'Price-High to Low':
            cursor.execute(
                "select act_id, place_id , cost,duration ,start_time ,end_time from activities order by cost desc")
            y = cursor.fetchall()
        else:
            cursor.execute("select act_id, place_id , cost,duration ,start_time ,end_time from activities")
            y = cursor.fetchall()
        j = 1
        k = 1
        for i in y:
            for x in range(1, len(i)):
                Label(f2, text=i[x], font=("Adobe Caslon Pro", 15), bg="#ADEBBE").grid(row=j, column=k)
                k += 1
            j += 1
            k = 1

    Button(root1, text="NEXT", command=go_d, font=("Montserrat", 15)).place(x=1250, y=600)
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Label(f1, text="Activities", font=("Caviar Dreams", 27), bg='#EEF3AD').grid()
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Label(f1, text="  Please select upto \n 5 Activities", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    r5 = Combobox(f1, textvariable=ch, font=("Caviar Dreams", 13))
    r5['values'] = ('Popular', 'Price-High to Low', 'Price-Low to High',
                    'Duration-High to Low', 'Duration-Low to High', '            SORT BY')
    r5.current(5)
    r5.grid(padx=37)
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Label(f1, text="", font=("Caviar Dreams", 20), bg='#EEF3AD').grid()
    Button(f1, text="GO", font=("Montserrat", 14), command=act).grid()
    f1.place(x=0, y=0, width=300, height=750)
    f2.place(x=300, y=0, width=920, height=750)
    root1.mainloop()


def hotel1():
    root = Tk()
    root.config(bg='#74BEC1')
    root.title('www.ciao.com')
    m1 = IntVar(root, 0)  # star/capacity
    m2 = IntVar(root, 0)  # acc_mode
    m3 = StringVar(root, 0)  # acc_id
    m4 = StringVar(root, 0)  # wifi
    m5 = StringVar(root, 0)  # breakfast
    m6 = StringVar(root, 0)  # pool
    root.configure(width=1450, height=750)
    s1 = 'yes'
    s2 = 'no'
    f1 = Frame(root, width=200, height=750, bg="#EEF3AD")
    f2 = Frame(root, width=800, height=750, bg="#ADEBBE")
    f3 = Frame(f1, width=200, height=750, bg="#EEF3AD")
    f4 = Frame(f1, width=200, height=750, bg="#EEF3AD")
    room = Scale(f3, from_=1, to=4, orient=HORIZONTAL)
    st = StringVar()

    def go_c():
        a = room.get()
        b = m3.get()
        c = m4.get()
        d = m5.get()
        e = m2.get()
        cursor.execute("update details set wifi=?,breakfast=?,acc_mode=?,acc_no=?,no_rooms=? where it_id=? ",
                       (c, d, e, b, a, it_no,))
        root.destroy()
        acts1()

    def hot():
        x = m1.get()
        s = st.get()
        Label(f2, text="ID", font=("Latinia", 17), bg='#ADEBBE', width=5).grid(row=0, column=1)
        Label(f2, text="NAME", font=("Latinia", 17), bg='#ADEBBE', width=10).grid(row=0, column=2)
        Label(f2, text="SPA", font=("Latinia", 17), bg='#ADEBBE', width=5).grid(row=0, column=3)
        Label(f2, text="POOL", font=("Latinia", 17), bg='#ADEBBE', width=5).grid(row=0, column=4)
        Label(f2, text="GARDEN", font=("Latinia", 17), bg='#ADEBBE', width=10).grid(row=0, column=5)
        Label(f2, text="TARIFF", font=("Latinia", 17), bg='#ADEBBE', width=10).grid(row=0, column=6)
        if s == 'Price-High to Low':
            cursor.execute("SELECT ht_id,name,spa,swim,garden,tariff FROM hotels WHERE rating=? order by tariff desc",
                           (x,))
            y = cursor.fetchall()
        elif s == 'Price-Low to High':
            cursor.execute("SELECT ht_id,name,spa,swim,garden,tariff FROM hotels WHERE rating=? order by tariff ",
                           (x,))
            y = cursor.fetchall()
        else:
            cursor.execute("SELECT ht_id,name,spa,swim,garden,tariff FROM hotels WHERE rating=? ",
                           (x,))
            y = cursor.fetchall()
        j = 1
        for i in y:
            Radiobutton(f2, text="", variable=m3, value=i[0], bg="#ADEBBE", height=3).grid(row=j, column=0)
            y = 1
            for a in i:
                Label(f2, text=a, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=j, column=y, pady=1)
                y += 1
            j += 1

    def bnb():
        z = m6.get()
        x = room.get()
        s = st.get()
        Label(f2, text="ID", font=("Latinia", 17), bg='#ADEBBE', width=5).grid(row=0, column=1)
        Label(f2, text="CAR PARK", font=("Latinia", 17), bg='#ADEBBE', width=10).grid(row=0, column=2)
        Label(f2, text="ADDRESS", font=("Latinia", 17), bg='#ADEBBE', width=10).grid(row=0, column=3)
        Label(f2, text="POOL", font=("Latinia", 17), bg='#ADEBBE', width=5).grid(row=0, column=4)
        Label(f2, text="TARIFF", font=("Latinia", 17), bg='#ADEBBE', width=10).grid(row=0, column=5)
        if s == 'Price-High to Low':
            cursor.execute(
                "select airbnb_id, park,address, swim, tariff from airbnb where rooms=? and swim=? order by tariff desc",
                (x, z,))
            y = cursor.fetchall()
        elif s == 'Price-Low to High':
            cursor.execute(
                "select airbnb_id, park,address, swim, tariff from airbnb where rooms=? and swim=? order by tariff ",
                (x, z,))
            y = cursor.fetchall()
        else:
            cursor.execute(
                "select airbnb_id, park,address, swim, tariff from airbnb where rooms=? and swim=? ", (x, z,))
            y = cursor.fetchall()
        j = 1
        for i in y:
            Radiobutton(f2, text="", variable=m3, value=i[0], bg="#ADEBBE", height=3).grid(row=j, column=0)
            y = 1
            for a in i:
                Label(f2, text=a, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=j, column=y, pady=2)
                y += 1
            j += 1

    def rate(): # hotel option
        Label(f4, text="", bg='#EEF3AD').grid(row=0, column=0)
        Label(f4, text="RATING:", bg='#EEF3AD', font=("Caviar Dreams", 15)).grid(row=1, column=0)
        r10 = Radiobutton(f4, text="RESORTS", variable=m1, height=1, value=0, bg="#EEF3AD", font=("Caviar Dreams", 12))
        r10.grid(row=2, column=0)
        r11 = Radiobutton(f4, text="5 STAR", variable=m1, height=1, value=5, bg="#EEF3AD", font=("Caviar Dreams", 12))
        r11.grid(row=3, column=0)
        r12 = Radiobutton(f4, text="4 STAR", variable=m1, height=1, value=4, bg="#EEF3AD", font=("Caviar Dreams", 12))
        r12.grid(row=4, column=0)
        r13 = Radiobutton(f4, text="3 STAR", variable=m1, height=1, value=3, bg="#EEF3AD", font=("Caviar Dreams", 12))
        r13.grid(row=5, column=0, padx=0)
        Label(f4, text="", bg='#EEF3AD').grid(row=6, column=0)
        Label(f4, text="NUMBER OF\nROOMS", bg='#EEF3AD', font=("Caviar Dreams", 12)).grid(row=7, column=0)
        room = Entry(f4)
        room.grid(row=9, column=0)
        Label(f4, text="", bg='#EEF3AD').grid(row=10, column=0)
        Label(f4, text="WiFi", bg="#EEF3AD", font=("Caviar Dreams", 12)).grid(row=11, column=0)
        op = OptionMenu(f4, m4, s1, s2)
        op.grid(row=12, column=0)
        Label(f4, text="", bg='#EEF3AD').grid(row=13, column=0)
        LL5 = Label(f4, text="Breakfast",
                    bg="#EEF3AD", height=2, font=("Caviar Dreams", 12))
        LL5.grid(row=14, column=0)
        op = OptionMenu(f4, m5, s1, s2)
        op.grid(row=15, column=0)
        Label(f4, text="", bg='#EEF3AD').grid(row=16, column=0)
        cob3 = Combobox(f4, textvariable=st, font=("caviar Dreams", 12))
        cob3['values'] = ('Price-Low to High', 'Price-High to Low', 'Popular', 'SORT BY')
        cob3.current(3)
        cob3.grid(row=17, column=0)
        Label(f4, text="", bg='#EEF3AD').grid(row=18, column=0)
        b = Button(f4, text="GO", command=hot, font=("Montserrat", 15))
        b.grid(row=19, column=0)
        f4.place(x=30, y=150)

    def capacity(): # airbnb option
        Label(f3, text="", bg='#EEF3AD').grid(row=0, column=0)
        Label(f3, text="NUMBER OF ROOMS", bg='#EEF3AD', font=("Caviar Dreams", 13)).grid(row=1, column=0)
        room.grid(row=2, column=0)
        Label(f3, text="", bg='#EEF3AD').grid(row=3, column=0)
        Label(f3, text="WiFi", font=('Caviar Dreams', 13), bg="#EEF3AD").grid(row=4, column=0)
        op = OptionMenu(f3, m4, s1, s2)
        op.grid(row=5, column=0)
        Label(f3, text="", bg='#EEF3AD').grid(row=6, column=0)
        LL5 = Label(f3, text="Breakfast", font=('Caviar Dreams', 13), bg="#EEF3AD")
        LL5.grid(row=7, column=0)
        op = OptionMenu(f3, m5, s1, s2)
        op.grid(row=8, column=0)
        Label(f3, text="", bg='#EEF3AD').grid(row=9, column=0)
        Label(f3, text="SWIMMING POOL", bg='#EEF3AD', font=("Caviar Dreams", 13)).grid(row=10, column=0)
        op = OptionMenu(f3, m6, s1, s2)
        op.grid(row=11, column=0)
        Label(f3, text="", bg='#EEF3AD').grid(row=12, column=0)
        cob3 = Combobox(f3, textvariable=st, font=("Caviar Dreams", 11))
        cob3['values'] = ('Price-Low to High', 'Price-High to Low', 'Popular', 'SORT BY')
        cob3.current(3)
        cob3.grid(row=13, column=0)
        Label(f3, text="", bg='#EEF3AD').grid(row=14, column=0)
        Label(f3, text="", bg='#EEF3AD').grid(row=15, column=0)
        b = Button(f3, text="GO", command=bnb, font=("Montserrat", 13))
        b.grid(row=16, column=0)
        f3.place(x=40, y=150) #

    def s():
        x = m2.get()
        print(x)
        if x == 1:
            rate()
        elif x == 2:
            capacity()
        else:
            initial()

    Label(f1, text="", bg='#EEF3AD', width=15).pack()
    Label(f1, text="", bg='#EEF3AD', width=15).pack()
    r8 = Radiobutton(f1, text='HOTELS', variable=m2, value=1, bg="#EEF3AD", font=("Caviar Dreams", 13))
    r8.pack()
    r9 = Radiobutton(f1, text='AIR BNB', variable=m2, value=2, bg="#EEF3AD", font=("Caviar Dreams", 13))
    r9.pack()
    Button(f1, text="GO", command=s, font=("Montserrat", 12)).pack()
    Button(root, text="NEXT", command=go_c, font=("Montserrat", 15)).place(x=1250, y=600)

    f1.place(x=0, y=0, width=280, height=750)
    f2.place(x=280, y=0, width=940, height=750)
    root.mainloop()


def fro():
    t2 = Tk()
    t2.title("www.ciao.com")
    t2.config(width=1450, height=750, bg='#74BEC1')
    f6 = Frame(t2, bg='#ADEBBE')
    f5 = Frame(t2, bg='#EEF3AD')
    v2 = IntVar(t2, 0)
    v3 = StringVar(t2, 0)
    st = StringVar()

    def go_b():
        temp = v2.get()
        temp1 = v3.get()
        cursor.execute("update details set arr_mode=?,arr_id=? where it_id=?", (temp, temp1, it_no,))
        print(temp1)
        t2.destroy()
        hotel1()

    def go1():
        print("hi")
        x = v2.get()
        sort = st.get()

        if x == 1:
            Label(f6, text="FROM", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=1)
            Label(f6, text="TO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=2)
            Label(f6, text="  FLIGHT NO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=3)
            Label(f6, text="  DEPARTURE", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=4)
            Label(f6, text="  ARRIVAL", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=5)
            Label(f6, text="  AIRLINE", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=6)
            Label(f6, text="  COST", font=("Latinia", 18), bg='#ADEBBE').grid(row=0, column=7)

            if sort == 'Price-High to Low':
                cursor.execute("select distinct f.ds_id, f.or_id, flight_no,dep_time,arr_time, airline, distance "
                               "from flights f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance desc ", (it_no,))
                y = cursor.fetchall()
            elif sort == 'Price-Low to High':
                cursor.execute("select distinct f.ds_id, f.or_id, flight_no,dep_time,arr_time, airline, distance "
                               "from flights f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance  ", (it_no,))
                y = cursor.fetchall()

            else:
                cursor.execute("select distinct f.ds_id, f.or_id, flight_no,dep_time,arr_time, airline, distance "
                               "from flights f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? ",
                               (it_no,))
                y = cursor.fetchall()

            for c in range(0, len(y)):
                Radiobutton(f6, text="", variable=v3, value=y[c][2], font=("Adobe Caslon Pro", 20,),
                            bg='#ADEBBE').grid(row=c + 1, column=0)
                k = 1
                for r in y[c]:
                    Label(f6, text=r, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=c + 1, column=k)
                    k += 1
            f6.place(x=270, y=0, width=930, height=750)

        if x == 2:
            f7 = Frame(t2, bg='#ADEBBE')
            Label(f7, text="FROM", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=1)
            Label(f7, text="   TO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=2)
            Label(f7, text="   TRAIN NO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=3)
            Label(f7, text="   NAME", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=4)
            Label(f7, text="   DEPARTURE", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=5)
            Label(f7, text="   ARRIVAL", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=6)
            Label(f7, text="   COST", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=7)

            if sort == 'Price-High to Low':
                cursor.execute("select distinct f.ds_id, f.or_id, train_no, name, dep_time,arr_time, distance "
                               "from trains f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance desc ", (it_no,))
                y = cursor.fetchall()
            elif sort == 'Price-Low to High':
                cursor.execute("select distinct f.ds_id, f.or_id, train_no, name, dep_time,arr_time, distance "
                               "from trains f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance  ", (it_no,))
                y = cursor.fetchall()

            else:
                cursor.execute("select distinct f.ds_id, f.or_id, train_no, name, dep_time,arr_time, distance "
                               "from trains f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? ",
                               (it_no,))
                y = cursor.fetchall()

            for c in range(0, len(y)):
                Radiobutton(f7, text="", variable=v3, value=y[c][2], font=("Adobe Caslon Pro", 20),
                            bg='#ADEBBE').grid(row=c + 1, column=0)
                k = 1
                for r in y[c]:
                    Label(f7, text=r, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=c + 1, column=k)
                    k += 1
            f7.place(x=270, y=0, width=930, height=750)

        if x == 3:
            f8 = Frame(t2, bg='#ADEBBE')
            Label(f8, text="PICKUP", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=1)
            Label(f8, text="DROP", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=2)
            Label(f8, text="   CAR NO  ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=3)
            Label(f8, text="   MODEL    ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=4)
            Label(f8, text="   CAPACITY   ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=5)
            Label(f8, text="   COST  ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=6)

            if sort == 'Price-High to Low':
                cursor.execute("select distinct f.ds_id, f.or_id, car_no, model, capacity, distance "
                               "from car f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance desc ", (it_no,))
                y = cursor.fetchall()
            elif sort == 'Price-Low to High':
                cursor.execute("select distinct f.ds_id, f.or_id, car_no, model, capacity, distance "
                               "from car f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance  ", (it_no,))
                y = cursor.fetchall()

            else:
                cursor.execute("select distinct f.ds_id, f.or_id, car_no, model, capacity, distance "
                               "from car f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? ",
                               (it_no,))
                y = cursor.fetchall()

            for c in range(0, len(y)):
                Radiobutton(f8, text="", variable=v3, value=y[c][2], bg='#ADEBBE').grid(row=c + 1, column=0)
                k = 1
                for r in y[c]:
                    Label(f8, text=r, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=c + 1, column=k)
                    k += 1
            f8.place(x=270, y=0, width=930, height=750)

    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=1, column=0)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=2, column=0)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=3, column=0)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=4, column=0)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=5, column=0)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=6, column=0)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=7, column=0)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=8, column=0)
    Radiobutton(f5, text="FLIGHTS", variable=v2, value=1, font=("Caviar Dreams", 18), bg='#EEF3AD').grid(row=9,
                                                                                                           column=0)
    Radiobutton(f5, text="TRAINS", variable=v2, value=2, font=("Caviar Dreams", 18), bg='#EEF3AD').grid(row=10,
                                                                                                          column=0)
    Radiobutton(f5, text="CAR", variable=v2, value=3, font=("Caviar Dreams", 18), bg='#EEF3AD').grid(row=11, column=0)
    cob3 = Combobox(f5, textvariable=st, font=("Caviar Dreams", 11))
    cob3['values'] = ('Price-Low to High', 'Price-High to Low', 'Popular', '             SORT BY')
    cob3.current(3)
    labs1 = Label(f5, text="", bg='#EEF3AD').grid(row=12, column=0)
    cob3.grid(row=13, column=0, padx=30)
    Label(f5, text="", bg='#EEF3AD').grid(row=14, column=0)
    Label(f5, text="", bg='#EEF3AD').grid(row=15, column=0)
    Button(f5, text="GO", command=go1, font=("Montserrat", 14)).grid(row=16, column=0, padx=10)
    f5.place(x=0, y=0, width=270, height=750)

    Button(t2, text="NEXT", command=go_b, font=("Montserrat", 15)).place(x=1250, y=600)

    t2.mainloop()


def to():
    t1 = Tk()
    t1.title("www.ciao.com")
    t1.config(width=1450, height=750, bg='#74BEC1') # behind all
    f2 = Frame(t1, bg='#ADEBBE') # behind flights
    f1 = Frame(t1, bg='#EEF3AD') # behind sorting
    v = IntVar(t1, 0)
    v1 = StringVar(t1, 0)
    st = StringVar()

    def go_a():
        temp = v1.get()
        temp1 = v.get()
        cursor.execute("update details set dep_mode=?,dep_id=? where it_id=?", (temp1, temp, it_no,))
        print(temp)
        t1.destroy()
        fro()

    def go():
        x = v.get()
        sort = st.get()
        if x == 1:
            print(it_no)            # latinia, caviar dreams
            Label(f2, text="FROM", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=1)
            Label(f2, text="  TO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=2)
            Label(f2, text="  FLIGHT NO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=3)
            Label(f2, text="  DEPARTURE", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=4)
            Label(f2, text="  ARRIVAL", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=5)
            Label(f2, text="  AIRLINE", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=6)
            Label(f2, text="  COST", font=("Latinia", 18), bg='#ADEBBE').grid(row=0, column=7)

            if sort == 'Price-High to Low':
                cursor.execute("select distinct f.or_id, f.ds_id, flight_no,dep_time,arr_time, airline, distance "
                               "from flights f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance desc ", (it_no,))
                y = cursor.fetchall()
            elif sort == 'Price-Low to High':
                cursor.execute("select distinct f.or_id, f.ds_id, flight_no,dep_time,arr_time, airline, distance "
                               "from flights f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance  ", (it_no,))
                y = cursor.fetchall()

            else:
                cursor.execute("select distinct f.or_id, f.ds_id, flight_no,dep_time,arr_time, airline, distance "
                               "from flights f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and "
                               "i.it_id=? ", (it_no,))
                y = cursor.fetchall()
            for c in range(0, len(y)):
                Radiobutton(f2, text="", variable=v1, value=y[c][2], font=("Adobe Caslon Pro", 20,),
                            bg='#ADEBBE').grid(row=c + 1, column=0)
                k = 1
                for r in y[c]:
                    Label(f2, text=r, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=c + 1, column=k)
                    k += 1
            f2.place(x=270, y=0, width=930, height=750)

        if x == 2:
            f3 = Frame(t1, bg='#ADEBBE')
            Label(f3, text="FROM", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=1)
            Label(f3, text="   TO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=2)
            Label(f3, text="   TRAIN NO", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=3)
            Label(f3, text="   NAME", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=4)
            Label(f3, text="   DEPART TIME", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=5)
            Label(f3, text="   ARRIVAL TIME", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=6)
            Label(f3, text="   COST", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=7)

            if sort == 'Price-High to Low':
                cursor.execute("select distinct f.or_id, f.ds_id, train_no, name, dep_time,arr_time, distance "
                               "from trains f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance desc ", (it_no,))
                y = cursor.fetchall()
            elif sort == 'Price-Low to High':
                cursor.execute("select distinct f.or_id, f.ds_id, train_no, name, dep_time,arr_time, distance "
                               "from trains f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance  ", (it_no,))
                y = cursor.fetchall()

            else:
                cursor.execute("select distinct f.or_id, f.ds_id, train_no, name, dep_time,arr_time, distance "
                               "from trains f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? ",
                               (it_no,))
                y = cursor.fetchall()

            for c in range(0, len(y)):
                Radiobutton(f3, text="", variable=v1, value=y[c][2], font=("Adobe Caslon Pro", 20),
                            bg='#ADEBBE').grid(row=c + 1, column=0)
                k = 1
                for r in y[c]:
                    Label(f3, text=r, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=c + 1, column=k)
                    k += 1
            f3.place(x=270, y=0, width=930, height=750)

        if x == 3:
            f4 = Frame(t1, bg='#ADEBBE')
            Label(f4, text="PICKUP", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=1)
            Label(f4, text=" DROP", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=2)
            Label(f4, text="   CAR NO  ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=3)
            Label(f4, text="   MODEL    ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=4)
            Label(f4, text="   CAPACITY   ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=5)
            Label(f4, text="   COST   ", font=("Latinia", 17), bg='#ADEBBE').grid(row=0, column=6)

            if sort == 'Price-High to Low':
                cursor.execute("select distinct f.or_id, f.ds_id, car_no, model, capacity, distance "
                               "from car f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance desc ", (it_no,))
                y = cursor.fetchall()
            elif sort == 'Price-Low to High':
                cursor.execute("select distinct f.or_id, f.ds_id, car_no, model, capacity, distance "
                               "from car f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? "
                               "order by distance  ", (it_no,))
                y = cursor.fetchall()

            else:
                cursor.execute("select distinct f.or_id, f.ds_id, car_no, model, capacity, distance "
                               "from car f,details i where f.or_id==i.or_id and f.ds_id=i.ds_id and i.it_id=? ",
                               (it_no,))
                y = cursor.fetchall()

            for c in range(0, len(y)):
                Radiobutton(f4, text="", variable=v1, value=y[c][2], bg='#ADEBBE').grid(row=c + 1, column=0)
                k = 1
                for r in y[c]:
                    Label(f4, text=r, font=("Adobe Caslon Pro", 15), bg='#ADEBBE').grid(row=c + 1, column=k)
                    k += 1
            f4.place(x=270, y=0, width=930, height=750)

    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=1, column=0)
    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=2, column=0)
    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=3, column=0)
    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=4, column=0)
    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=5, column=0)
    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=6, column=0)
    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=7, column=0)
    labs1 = Label(f1, text="", bg='#EEF3AD').grid(row=8, column=0)
    Radiobutton(f1, text="FLIGHTS", variable=v, value=1, font=("Caviar Dreams", 18), bg='#EEF3AD').grid(row=9, column=0)
    Radiobutton(f1, text="TRAINS", variable=v, value=2, font=("Caviar Dreams", 18), bg='#EEF3AD').grid(row=10, column=0)
    Radiobutton(f1, text="CAR", variable=v, value=3, font=("Caviar Dreams", 18), bg='#EEF3AD').grid(row=11, column=0)
    cob3 = Combobox(f1, textvariable=st, font=("Caviar Dreams", 11))
    cob3['values'] = ('Price-Low to High', 'Price-High to Low', 'Popular', '             SORT BY')
    cob3.current(3)
    Label(f1, text="", bg='#EEF3AD').grid(row=12, column=0)
    cob3.grid(row=13, column=0, padx=30)
    Label(f1, text="", bg='#EEF3AD').grid(row=14, column=0)
    Label(f1, text="", bg='#EEF3AD').grid(row=15, column=0)
    Button(f1, text="GO", command=go, font=("Montserrat", 14)).grid(row=16, column=0, padx=10)
    f1.place(x=0, y=0, width=270, height=750)

    Button(t1, text="NEXT", command=go_a, font=("Montserrat", 15)).place(x=1250, y=600)

    # menus()
    t1.mainloop()


def home1():
    from tkinter import messagebox
    import calendar

    t = Tk()
    t.config(bg='#ADEBBE')
    v = IntVar()
    var = IntVar()
    var2 = IntVar()
    fr = Frame(t, bg='#ADEBBE')
    dep1 = StringVar()
    arr1 = StringVar()
    dep2 = StringVar()
    arr2 = StringVar()
    t.geometry('1352x675+0+0')

    global arrdate
    arrdate = ""

    global depdate
    depdate = ""

    global d1, m1, y1, d2, m2, y2


    def radiosel():
        print("Departure Date:", depdate)
        print("Arrival Date:", arrdate)

        global sel1
        sel1 = var2.get()  # student concession
        print(sel1)

        global sel2  # senior citizen
        sel2 = var.get()
        print(sel2)

        global sel3
        dep = date(y1, m1, d1)
        arr = date(y2, m2, d2)
        no = arr-dep
        sel3 = no.days
        print(no.days)

        global departure  # or_id
        departure = dep1.get()
        print(departure)

        global arrival  # des_id
        arrival = arr1.get()
        print(arrival)

        sel9 = 1  # no_pass

        global it_no
        it_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

        # global sc
        # sc = w.get()
        # print(sc)

        print(it_no)
        cursor.execute("INSERT INTO details(it_id, or_id, ds_id, dep, arr, no_pass, discount, "
                       "senior,no_day ) VALUES(?,?,?,?,?,?,?,?,?)",
                       (it_no, departure, arrival, depdate,arrdate, sel9, sel1, sel2,sel3,))
        cursor.execute("INSERT INTO act_det(it_id) VALUES(?)", (it_no,))
        t.destroy()
        to()

    def placea1():
        messagebox.showinfo('MUMBAI DISCOUNT', 'Mumbai is that city of Dreams. The one that never sleeps. '
                                               'The one that never stops.\n\nDIVE IN THE CITY THAT NEVER STOPS!!'
                                               '\n\n\nAdd code AB1973 during checkout to avail special discount.'
                                               '\n\n\n*TnC Applied')

    def placea2():
        messagebox.showinfo('HOTEL DISCOUNT', 'Check out the resorts and other high end hotels listed on our website.'
                                              '\n\nAdd code HOT67 during checkout to avail special discount.'
                                              '\n\n\n*TnC applied')

    def placea3():
        messagebox.showinfo('JAIPUR DISCOUNT', 'Roam the city of Maharajas with style and glamour.'
                                               '\n\nAdd code QWD12 during checkout to avail special discount.'
                                               '\n\n\n*TnC applied')

    def placea4():
        messagebox.showinfo('GIFT CARDS', 'Going out with loved ones? \nMaybe the first time?\n\nCheck out our gift '
                                          'card options in our menu to make your trip one that you will never forget'
                                      '\n\n\n*TnC applied')

    t.title("www.ciao.com")

    def visa():
        t1 = Tk()
        t1.title("www.ciao.com")
        t1.config(bg='#EEF3AD')
        t1.geometry('350x350+500+150')

        l1 = Label(t1, text="\nApplicants may fill the online application form by \ngoing to the tab placed below.\n\n "
                            "Once the form is filled and submitted, applicant must print \nthe completed application "
                            "form and sign and submit \nthe physical copy along with the supporting documents \nand "
                            "the Passport to the concerned Indian Visa \nApplication Center (IVAC) or directly at the "
                            "Indian \nMission on the scheduled appointed date. \n\nThe instructions for filling the "
                            "form \nand scheduling the appointment \ncan be seen at Instructions for Regular Visa "
                            "Application.\n\nThe status of Visa Application \ncan be seen on the link for Visa "
                            "Enquiry.\n\nThe applicants are also requested to visit website \nof the "
                            "Indian Mission concerned for detailed \ninformation about "
                            "Indian visa.",bg='#EEF3AD').pack()

        b1 = Button(t1, text="Form", font="Latinia, 11")
        # b1.pack()

    def passport():
        t1 = Tk()
        t1.title("www.ciao.com")
        t1.config(bg='#EEF3AD')
        t1.geometry('350x300+500+150')
        l1 = Label(t1, text="\nApplicants are advised to visit their jurisdictional passport \noffice's home page "
                            "under Passport Office Page to know \nabout additional documents required, if any. "
                            "\n\nApplicants are required to furnish original documents along \nwith one set of "
                            "self-attested photocopies of the same \nat the Passport Seva "
                            "Kendra (PSK) for processing.", bg='#EEF3AD')

        l2 = Label(t1, text="\nMinor", font="Latinia, 11", bg='#EEF3AD')
        l3 = Label(t1, text="For minor applicants, present address proof document\n "
                            "in the name of parent(s).\n\nIt is advised to carry "
                            "original and self-attested copies \nof parents passport to Passport "
                            "Seva Kendra (PSK), \nin case parents possess passport. \n\nFor minor applicants, "
                            "documents can be attested by parents.", bg='#EEF3AD')
        b1 = Button(t1, text="Form", font="Latinia, 11")

        l1.pack()
        l2.pack()
        l3.pack()
        # b1.pack()

    def giftcards():
        t1 = Tk()
        t1.title("www.ciao.com")
        t1.config(bg='#EEF3AD')
        t1.geometry('380x420+480+70')
        l1 = Label(t1, text="Gift Cards", font=("Latinia", 20), bg='#EEF3AD')
        l2 = Label(t1, text="\nGift Memories", font=("Latinia", 13), bg='#EEF3AD')
        l3 = Label(t1, text="There is no better gift than a gift of beautiful "
                            "memories. \nA dream holiday for your loved ones makes "
                            "for a perfect gift! \nGift them memories to cherish for a lifetime."
                   , font=("", 9), bg='#EEF3AD')
        l4 = Label(t1, text="\nFreedom To Choose", font=("Latinia", 13), bg='#EEF3AD')
        l5 = Label(t1, text="Personal or corporate, we offer holiday gift \nvouchers to suit everyone's "
                            "tastes & needs. \nPick from the many denominations available with us!"
                   , font=("", 9), bg='#EEF3AD')

        l6 = Label(t1, text="\nPersonalize Your Message", font=("Latinia", 13), bg='#EEF3AD')
        l7 = Label(t1, text="Personalize your Ciao gift vouchers. \n"
                            "Say how much you care in your own words and style. ", font=("", 9), bg='#EEF3AD')
        l8 = Label(t1, text="\n\nEmail us to know more", font=("Latinia", 11), bg='#EEF3AD')
        l9 = Label(t1, text="giftsforall@ciao.org", font=("Latinia", 12), bg='#EEF3AD')

        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        l6.pack()
        l7.pack()
        l8.pack()
        l9.pack()

    def faq():
        t1 = Tk()
        t1.title("www.ciao.com")
        t1.config(bg = '#EEF3AD')
        t1.geometry('480x500+420+50')
        l1 = Label(t1, text="FAQ", font=("Latinia", 18), bg='#EEF3AD')
        l2 = Label(t1, text="\n1. What is the benefit of working with Ciao?", font=("Latinia", 12), bg='#EEF3AD')
        l3 = Label(t1, text="Strongest OTA with 50% market share.", bg='#EEF3AD')
        l4 = Label(t1, text="Online Products (Domestic flights/ Hotels/ Train/ Cars)", bg='#EEF3AD')
        l5 = Label(t1, text="Widest selling hotel inventory in the country with attractive "
                            "commission structure", bg='#EEF3AD')
        l6 = Label(t1, text="Customer Support from Monday - Sunday (24X7)", bg='#EEF3AD')
        l7 = Label(t1, text="2. What is the process to change a date with your portal?",
                   font=("Latinia", 12), bg='#EEF3AD')
        l8 = Label(t1, text=" You just need to drop an email with original PNR to our "
                            "\nhelp desk team (helpdesk@ciao.com). \nThey will do the needful "
                            "and send you the new ticket.", bg='#EEF3AD')
        l9 = Label(t1, text="3. How much time will it take in case of refunds?", font=("Latinia", 12), bg='#EEF3AD')
        l10 = Label(t1, text="It is processed immediately after the confirmation of the "
                             "cancellation\n and goes directly to the respective booking account", bg='#EEF3AD')
        l11 = Label(t1, text="4. Do you also sell coupons for different airline?", font=("Latinia", 12), bg='#EEF3AD')
        l12 = Label(t1, text="Yes, it depends on the availability of coupons in the market. We do sell \ncoupons "
                             "for Jet, Kingfisher, Air India and other airlines as well.", bg='#EEF3AD')
        l13 = Label(t1, text="5. What is your credit policy?", font=("Latinia", 12), bg='#EEF3AD')
        l14 = Label(t1, text="Ciao does not promote any credit because we work on advance "
                             "deposit \nmodel to provide best deal to our partners. ", bg='#EEF3AD')
        l15 = Label(t1, text="Customer Care", font=("Latinia", 12), bg='#EEF3AD')
        l16 = Label(t1, text="Dweej Vyas                  +91 9326007743", font=("", 12), bg='#EEF3AD')
        l17 = Label(t1, text="Vidhi Vazirani              +91 7021946521", font=("", 12), bg='#EEF3AD')

        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()
        l6.pack()
        l7.pack()
        l8.pack()
        l9.pack()
        l10.pack()
        l11.pack()
        l12.pack()
        l13.pack()
        l14.pack()
        l15.pack()
        l16.pack()
        l17.pack()

    def vision():
        t1 = Tk()
        t1.config(bg='#EEF3AD')
        t1.title("www.ciao.com")
        t1.geometry('780x300+285+150')
        l1 = Label(t1, text="Vision", font=("Latinia", 15), bg='#EEF3AD')
        l2 = Label(t1, text="\nNurtured from the seed of a single great idea - to empower the traveller - "
                            "Ciao is a pioneer in India’s online travel industry. \nFounded in the year "
                            "2015, Ciao came to life to empower the Indian traveller with instant bookings "
                            "and comprehensive choices. \nThe company initiated its journey serving the "
                            "domestic India travel market offering a range of best-value \nproducts and "
                            "services powered by technology and round-the-clock customer support. "
                            "\n\nAfter consolidating its position in the market as a brand recognised "
                            "for its reliability and \ntransparency, Ciao launched its India operations in "
                            "2019. \nWith more and more Indians initiating to transact online with IRCTC "
                            "and new opportunities with the advent of low cost carriers, \nCiao offered "
                            "travellers the convenience of booking travel online with a few clicks. "
                            "\n\nCiao's rise has been led by the vision and the spirit of each one of its "
                            "employees, for whom no idea was too big and no problem too difficult. "
                            "\nWith untiring determination, Ciao has proactively diversified its product "
                            "offering, adding a variety of online and offline products and services. "
                            "\nCiao has stayed ahead of the curve by continually evolving its technology to "
                            "meet the ever-changing demands of the rapidly \ndeveloping global travel market, "
                            "steadily establishing itself as India’s leading online travel company.", bg='#EEF3AD')
        l1.pack()
        l2.pack()

    def customercare():
        t1 = Tk()
        t1.title("www.ciao.com")
        t1.config(bg='#EEF3AD')
        t1.geometry('330x260+500+150')
        l1 = Label(t1, text="\n\nCustomer Care", font=("Latinia", 15), bg='#EEF3AD')
        l2 = Label(t1, text="\nDweej Vyas                  +91 9326007743", font=("Latinia", 12), bg='#EEF3AD')
        l3 = Label(t1, text="Vidhi Vazirani              +91 7021946521", font=("Latinia", 12), bg='#EEF3AD')
        l4 = Label(t1, text="\nFor any other queries, please email us at -", font=("Latinia", 12), bg='#EEF3AD')
        l5 = Label(t1, text="onlyqueries@ciao.org", font=("Latinia", 12), bg='#EEF3AD')
        l1.pack()
        l2.pack()
        l3.pack()
        l4.pack()
        l5.pack()

    def team():
        t1 = Tk()
        t1.title("www.ciao.com")
        t1.geometry('350x350+500+150')
        l1 = Label(t1, text="Vidhi Vazirani\tN052")
        l1.pack()

        l2 = Label(t1, text="Vaishnavi Singh Suroth - 48")
        l2.pack()

        l3 = Label(t1, text="Dweej Vyas - 56")
        l3.pack()

        l4 = Label(t1, text="Kanishka Soni - 45")
        l4.pack()

    def menus():
        menu1 = Menu(t)
        t.config(menu=menu1)
        sm1 = Menu(menu1)
        menu1.add_cascade(label="Travel Documents", menu=sm1, font=("Latinia", 10))
        sm1.add_command(label="Passport", command=passport, font=("Latinia", 10))
        sm1.add_command(label="Visa", command=visa, font=("Latinia", 10))
        sm2 = Menu(menu1)
        menu1.add_cascade(label="Gift Cards", menu=sm2, font=("Latinia", 10))
        sm2.add_command(label="Gift Cards", command=giftcards, font=("Latinia", 10))
        sm3 = Menu(menu1)
        menu1.add_cascade(label="Help", menu=sm3, font=("Latinia", 10))
        sm3.add_command(label="FAQ's", command=faq, font=("Latinia", 10))
        sm4 = Menu(menu1)
        menu1.add_cascade(label="About Us", menu=sm4, font=("Latinia", 10))
        sm4.add_command(label="Vision", command=vision, font=("Latinia", 10))
        sm4.add_command(label="Customer Care", command=customercare, font=("Latinia", 10))
        sm4.add_separator()
        sm4.add_command(label="Our Team", command=team, font=("Latinia", 10))

    menus()
    lab1 = Label(fr, text="ciao", font=("Glasgow Script", 85), bg='#ADEBBE').grid(row=0, column=2)
    img = PhotoImage(file="mum3.png")
    img = img.zoom(8)
    img = img.subsample(27)
    img2 = PhotoImage(file="hot.png")
    img2 = img2.zoom(6)
    img2 = img2.subsample(20)
    img3 = PhotoImage(file="del2.png")
    img3 = img3.zoom(14)
    img3 = img3.subsample(32)
    img4 = PhotoImage(file="trav.png")
    img4 = img4.zoom(8)
    img4 = img4.subsample(25)

    but1 = Button(fr, command=placea1, image=img, height=150, width=250, relief='ridge')
    but2 = Button(fr, command=placea2, image=img2, height=150, width=250, relief='ridge')
    but3 = Button(fr, command=placea3, image=img3, height=150, width=250, relief='ridge')
    but4 = Button(fr, command=placea4, image=img4, height=150, width=250, relief='ridge')
    but1.grid(row=1, column=1, padx=5, pady=10)
    but2.grid(row=2, column=0, padx=5, pady=10)
    but3.grid(row=1, column=3, pady=10, padx=5)
    but4.grid(row=2, column=4, pady=10, padx=5)

    f = Frame(fr, bg='#ADEBBE')

    f.grid(row=3, column=2)

    f2 = Frame(fr, bg='#ADEBBE')
    cob1 = Combobox(f2, textvariable=dep1, font=("Latinia", 14))
    cob1['values'] = ('bom', 'del', "From")
    cob1.current(2)
    cob1.pack()

    cob2 = Combobox(f2, textvariable=arr1, font=("Latinia", 14))
    cob2['values'] = ('bom', 'del', 'coc', 'jai', "To")
    cob2.current(4)
    cob2.pack()
    f2.grid(row=2, column=2)

    Label(f2, text="", bg='#ADEBBE').pack()

    class MyDatePicker(tk.Toplevel):
        def __init__(self, widget=None, format_str=None):
            super().__init__()
            self.widget = widget
            self.str_format = format_str

            self.title("Date Picker")
            self.resizable(0, 0)
            self.geometry("+630+390")

            self.init_frames()
            self.init_needed_vars()
            self.init_month_year_labels()
            self.init_buttons()
            self.space_between_widgets()
            self.fill_days()
            self.make_calendar()

        def init_frames(self):
            self.frame1 = tk.Frame(self)
            self.frame1.pack()

            self.frame_days = tk.Frame(self)
            self.frame_days.pack()

        def init_needed_vars(self):
            self.month_names = tuple(calendar.month_name)
            self.day_names = tuple(calendar.day_abbr)
            self.year = time.strftime("%Y")
            self.month = time.strftime("%B")

        def init_month_year_labels(self):
            self.year_str_var = tk.StringVar()
            self.month_str_var = tk.StringVar()

            self.year_str_var.set(self.year)
            self.year_lbl = tk.Label(self.frame1, textvariable=self.year_str_var,
                                     width=3)
            self.year_lbl.grid(row=0, column=5)

            self.month_str_var.set(self.month)
            self.month_lbl = tk.Label(self.frame1, textvariable=self.month_str_var,
                                      width=8)
            self.month_lbl.grid(row=0, column=1)

        def init_buttons(self):
            self.left_yr = ttk.Button(self.frame1, text="←", width=5,
                                      command=self.prev_year)
            self.left_yr.grid(row=0, column=4)

            self.right_yr = ttk.Button(self.frame1, text="→", width=5,
                                       command=self.next_year)
            self.right_yr.grid(row=0, column=6)

            self.left_mon = ttk.Button(self.frame1, text="←", width=5,
                                       command=self.prev_month)
            self.left_mon.grid(row=0, column=0)

            self.right_mon = ttk.Button(self.frame1, text="→", width=5,
                                        command=self.next_month)
            self.right_mon.grid(row=0, column=2)

        def space_between_widgets(self):
            self.frame1.grid_columnconfigure(3, minsize=40)

        def prev_year(self):
            self.prev_yr = int(self.year_str_var.get()) - 1
            self.year_str_var.set(self.prev_yr)

            self.make_calendar()

        def next_year(self):
            self.next_yr = int(self.year_str_var.get()) + 1
            self.year_str_var.set(self.next_yr)

            self.make_calendar()

        def prev_month(self):
            index_current_month = self.month_names.index(self.month_str_var.get())
            index_prev_month = index_current_month - 1

            #  index 0 is empty string, use index 12 instead,
            # which is index of December.
            if index_prev_month == 0:
                self.month_str_var.set(self.month_names[12])
            else:
                self.month_str_var.set(self.month_names[index_current_month - 1])

            self.make_calendar()

        def next_month(self):
            index_current_month = self.month_names.index(self.month_str_var.get())

            try:
                self.month_str_var.set(self.month_names[index_current_month + 1])
            except IndexError:
                #  index 13 does not exist, use index 1 instead, which is January.
                self.month_str_var.set(self.month_names[1])

            self.make_calendar()

        def fill_days(self):
            col = 0
            #  Creates days label
            for day in self.day_names:
                self.lbl_day = tk.Label(self.frame_days, text=day)
                self.lbl_day.grid(row=0, column=col)
                col += 1

        def make_calendar(self):
            #  Delete date buttons if already present.
            #  Each button must have its own instance attribute for this to work.
            try:
                for dates in self.m_cal:
                    for date in dates:
                        if date == 0:
                            continue

                        self.delete_buttons(date)

            except AttributeError:
                pass

            year = int(self.year_str_var.get())
            month = self.month_names.index(self.month_str_var.get())
            self.m_cal = calendar.monthcalendar(year, month)

            #  build dates buttons.
            for dates in self.m_cal:
                row = self.m_cal.index(dates) + 1
                for date in dates:
                    col = dates.index(date)

                    if date == 0:
                        continue

                    self.make_button(str(date), str(row), str(col))

        def make_button(self, date, row, column):

            exec(
                "self.btn_" + date + " = ttk.Button(self.frame_days, text=" + date
                + ", width=5)\n"
                  "self.btn_" + date + ".grid(row=" + row + " , column=" + column
                + ")\n"
                  "self.btn_" + date + ".bind(\"<Button-1>\", self.get_date)"
            )

        def delete_buttons(self, date):

            exec(
                "self.btn_" + str(date) + ".destroy()"
            )

        def get_date(self, clicked=None):
            global y2,d2,m2
            clicked_button = clicked.widget
            year = self.year_str_var.get()
            y2=int(year)
            month = self.month_str_var.get()
            long_month_name = month
            datetime_object = datetime.strptime(long_month_name, "%B")
            m2 = datetime_object.month
            date = clicked_button['text']
            d2=int(date)

            self.full_date = self.str_format % (date, month, year)
            global arrdate
            arrdate = self.full_date
            print(arrdate)

            #  Replace with parent 'widget' of your choice.
            try:
                self.widget.delete(0, f2.END)
                self.widget.insert(0, self.full_date)
            except AttributeError:
                pass

    if __name__ == '__main__':
        def application():
            MyDatePicker2(format_str='%02d-%s-%s')

        btn = Button(f2, text="Departure Date", command=application, relief='groove',
                     width=21, height=2, font=("Latinia", 11))
        btn.pack()

    class MyDatePicker2(tk.Toplevel):
        def __init__(self, widget=None, format_str=None):
            super().__init__()
            self.widget = widget
            self.str_format = format_str

            self.title("Date Picker")
            self.resizable(0, 0)
            self.geometry("+630+390")

            self.init_frames()
            self.init_needed_vars()
            self.init_month_year_labels()
            self.init_buttons()
            self.space_between_widgets()
            self.fill_days()
            self.make_calendar()

        def init_frames(self):
            self.frame1 = tk.Frame(self)
            self.frame1.pack()

            self.frame_days = tk.Frame(self)
            self.frame_days.pack()

        def init_needed_vars(self):
            self.month_names = tuple(calendar.month_name)
            self.day_names = tuple(calendar.day_abbr)
            self.year = time.strftime("%Y")
            self.month = time.strftime("%B")

        def init_month_year_labels(self):
            self.year_str_var = tk.StringVar()
            self.month_str_var = tk.StringVar()

            self.year_str_var.set(self.year)
            self.year_lbl = tk.Label(self.frame1, textvariable=self.year_str_var,
                                     width=3)
            self.year_lbl.grid(row=0, column=5)

            self.month_str_var.set(self.month)
            self.month_lbl = tk.Label(self.frame1, textvariable=self.month_str_var,
                                      width=8)
            self.month_lbl.grid(row=0, column=1)

        def init_buttons(self):
            self.left_yr = ttk.Button(self.frame1, text="←", width=5,
                                      command=self.prev_year)
            self.left_yr.grid(row=0, column=4)

            self.right_yr = ttk.Button(self.frame1, text="→", width=5,
                                       command=self.next_year)
            self.right_yr.grid(row=0, column=6)

            self.left_mon = ttk.Button(self.frame1, text="←", width=5,
                                       command=self.prev_month)
            self.left_mon.grid(row=0, column=0)

            self.right_mon = ttk.Button(self.frame1, text="→", width=5,
                                        command=self.next_month)
            self.right_mon.grid(row=0, column=2)

        def space_between_widgets(self):
            self.frame1.grid_columnconfigure(3, minsize=40)

        def prev_year(self):
            self.prev_yr = int(self.year_str_var.get()) - 1
            self.year_str_var.set(self.prev_yr)

            self.make_calendar()

        def next_year(self):
            self.next_yr = int(self.year_str_var.get()) + 1
            self.year_str_var.set(self.next_yr)

            self.make_calendar()

        def prev_month(self):
            index_current_month = self.month_names.index(self.month_str_var.get())
            index_prev_month = index_current_month - 1

            #  index 0 is empty string, use index 12 instead,
            # which is index of December.
            if index_prev_month == 0:
                self.month_str_var.set(self.month_names[12])
            else:
                self.month_str_var.set(self.month_names[index_current_month - 1])

            self.make_calendar()

        def next_month(self):
            index_current_month = self.month_names.index(self.month_str_var.get())

            try:
                self.month_str_var.set(self.month_names[index_current_month + 1])
            except IndexError:
                #  index 13 does not exist, use index 1 instead, which is January.
                self.month_str_var.set(self.month_names[1])

            self.make_calendar()

        def fill_days(self):
            col = 0
            #  Creates days label
            for day in self.day_names:
                self.lbl_day = tk.Label(self.frame_days, text=day)
                self.lbl_day.grid(row=0, column=col)
                col += 1

        def make_calendar(self):
            #  Delete date buttons if already present.
            #  Each button must have its own instance attribute for this to work.
            try:
                for dates in self.m_cal:
                    for date in dates:
                        if date == 0:
                            continue

                        self.delete_buttons(date)

            except AttributeError:
                pass

            year = int(self.year_str_var.get())
            month = self.month_names.index(self.month_str_var.get())
            self.m_cal = calendar.monthcalendar(year, month)

            #  build dates buttons.
            for dates in self.m_cal:
                row = self.m_cal.index(dates) + 1
                for date in dates:
                    col = dates.index(date)

                    if date == 0:
                        continue

                    self.make_button(str(date), str(row), str(col))

        def make_button(self, date, row, column):

            exec(
                "self.btn_" + date + " = ttk.Button(self.frame_days, text=" + date
                + ", width=5)\n"
                  "self.btn_" + date + ".grid(row=" + row + " , column=" + column
                + ")\n"
                  "self.btn_" + date + ".bind(\"<Button-1>\", self.get_date)"
            )

        def delete_buttons(self, date):

            exec(
                "self.btn_" + str(date) + ".destroy()"
            )

        def get_date(self, clicked=None):
            global d1
            global y1
            global m1
            clicked_button = clicked.widget
            year = self.year_str_var.get()
            y1=int(year)
            month = self.month_str_var.get()
            long_month_name = month
            datetime_object = datetime.strptime(long_month_name, "%B")
            m1 = datetime_object.month
            date = clicked_button['text']
            d1=int(date)

            self.full_date = self.str_format % (date, month, year)
            global depdate
            depdate = self.full_date
            print(depdate)
            #  Replace with parent 'widget' of your choice.
            try:
                self.widget.delete(0, tk.END)
                self.widget.insert(0, self.full_date)
            except AttributeError:
                pass

    if __name__ == '__main__':
        def application():
            MyDatePicker(format_str='%02d-%s-%s')

        butn = Button(f2, text="Arrival Date", command=application, relief='groove',
                      width=21, height=2, font=("Latinia", 11))
        butn.pack()

    print(arrdate)
    Label(f2, text="", bg='#ADEBBE').pack()
    chk1 = Checkbutton(f2, text="Senior Citizen Concession", font=("Caviar Dreams", 15), variable=var, bg='#ADEBBE')
    chk1.pack()
    chk2 = Checkbutton(f2, text="Student Concession", font=("Caviar Dreams", 15), variable=var2, bg='#ADEBBE')
    chk2.pack()
    fr.pack()
    but5 = Button(f2, text="SEARCH", bg='#74BEC1', font=("Latinia", 15), command=radiosel)
    Label(f2, text="", bg='#ADEBBE').pack()
    but5.pack()
    t.mainloop()


def db():
    tables()
    place()
    flights()
    car()
    trains()
    hotel()
    airbnb()
    activities()


# db()
tables()
home1()
connection.commit()
cursor.close()
connection.close()