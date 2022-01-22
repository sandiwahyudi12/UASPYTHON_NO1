import requests
import mysql.connector

mydb = mysql.connector.connect(
	host ="localhost",
	user ="root",
	password="",
	database="db_akademik_0504"
	)

def write_db_api():
	url = 'https://api.abcfdab.cfd/students'
	response = requests.get(url)
	data = response.json()
	cursor = mydb.cursor()
	sql = '''INSERT INTO tbl_students_0504(id,nim,nama,jk,jurusan,alamat) VALUES (%s, %s, %s, %s, %s, %s )'''
	for i in data['data'] :
		val = (i['id'],i['nim'], i['nama'] ,i['jk'], i['jurusan'], i['alamat'])		
		cursor.execute(sql,val)
		mydb.commit()	

def tampil_data():
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM tbl_students_0504")
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

def tampil_limit():
	baris = int(input("\ntampilkan limit : "))
	mycursor = mydb.cursor()
	sql = ("SELECT * FROM tbl_students_0504 ")
	mycursor.execute(sql)
	myresult = mycursor.fetchmany(baris)
	for x in myresult:
		print(x)

def tampilkan_nim():
	petik="'"
	nim = input('Masukan NIM :')
	mycursor = mydb.cursor()
	sql = ("SELECT * FROM tbl_students_0504 WHERE nim= ")
	mycursor.execute(sql + petik + nim + petik  )
	myresult = mycursor.fetchone()
	print(myresult)

if __name__ == '__main__':
	#write_db_api()

	while True:
		print("1. Tampilkan semua data")
		print("2. Tampilkan data limit")
		print("3. Tampilkan data dari NIM")
		print("0. Exit\n")
		menu = int(input("Masukan Pilihan Menu : "))
		if menu == 1 :
			tampil_data()
		if menu == 2 :
			tampil_limit()
		if menu == 3:
			tampilkan_nim()
		if menu == 0:
			break
		else :
			print('data salah!!!')