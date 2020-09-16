
student1 = {"Name": "Bui Dang Phong", "age": "30", "work": "TTKTKV1"}
student2 = {"Name": "Bui Dang B", "age": "25", "work": "TTKTKV2"}
student3 = {"Name": "Bui Dang C", "age": "20", "work": "TTKTKV3"}

students = (student1, student2, student3)

for a in students:
	print("-----------------")
	print("Ten: " + a["Name"])
	print("Tuoi: " + a["age"])
	print("Don vi: " + a["work"])
