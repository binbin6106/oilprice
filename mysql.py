import pymysql
import datetime
db = pymysql.connect("binbinss.pro","root","","sspanel" )
cursor = db.cursor()

def execmysql(sql):
	cursor.execute(sql)
	res = cursor.fetchall()
	return res
	
def class1(res):
	for i in res:
		datexpire = i[33]
		newtime = datexpire + datetime.timedelta(days = 12)
		print("old:" + str(datexpire) + " " + "new:" + str(newtime))
		
		transfer = i[9]
		newtransfer = transfer + 20*1024*1024*1024
		print("oldtr:" + str(transfer/1024/1024/1024) + " " + "newtr:" + str(newtransfer/1024/1024/1024))
	
def class6(res):
	print(type(res))

def main():

	sql1 = "SELECT * FROM `user` WHERE `reg_date` < '2019-09-28 00:00:00' AND `class` BETWEEN 1 AND 5"
	sql6 = "SELECT * FROM `user` WHERE `reg_date` < '2019-09-28 00:00:00' AND `class` BETWEEN 6 AND 8"
	res1 = execmysql(sql1)
	class1(res1)
	res6 = execmysql(sql6)
	class6(res6)
	db.close()
	
if __name__ == '__main__':
	main()
