class Stack(object):
	"""docstring for Stack"""
	def __init__(self):     #membuat stack kosong
		self.item=[]

	def isEmpty(self):      #mengembalikan nilai boolean yg menunjukkan apakah stack itu kosong
		return len(self)==0

	def __len__(self):      #mengembalikan banyaknya item di stack
		return len(self.item)

	def peek(self):         #mengembalikan nilai posisi atas tanpa menghapus dan mengembalikan nilai dari item yang paling atas tanpa menghapus
		assert not self.isEmpty(), "Stack is Empty"
		return self.item[-1]

	def pop(self):          #mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
		assert not self.isEmpty(), "Stack is Empty"
		return self.item.pop()

	def push(self, data):   #mendorong item ke stack, menambah item ke puncak stack
		self.item.append(data)

nilai=Stack()                   #menyimpan nilai stack di variable nilai
for i in range(16):             #perulangan dalam range 0-15
	if i % 3 == 0:          #jika nilai dibagi 3 memiliki sisa hasil bagi 0
		nilai.push(i)   #menambahkan nilai tersebut pada variable nilai

print(nilai.item)               #menampilkan hasil akhir pada variable nilai

#nilai 0 : sisa hasil bagi sama dengan 0 (memenuhi)
#          menambahkan nilai 0 pada variable nilai
#       >>>[0]
#nilai 1 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 2 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 3 : sisa hasil bagi sama dengan 0 (memenuhi)
#          menambahkan nilai 3 pada variable nilai
#       >>>[0,3]
#nilai 4 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 5 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 6 : sisa hasil bagi sama dengan 0 (memenuhi)
#          menambahkan nilai 6 pada variable nilai
#       >>>[0,3,6]
#nilai 7 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 8 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 9 : sisa hasil bagi sama dengan 0 (memenuhi)
#          menambahkan nilai 9 pada variable nilai
#       >>>[0,3,6,9]
#nilai 10 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 11 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 12 : sisa hasil bagi sama dengan 0 (memenuhi)
#           menambahkan nilai 12 pada variable nilai
#       >>>[0,3,6,9,12]
#nilai 13 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 14 : sisa hasil bagi tidak sama dengan 0 (tidak memenuhi)
#nilai 15 : sisa hasil bagi sama dengan 0 (memenuhi)
#           menambahkan nilai 15 pada variable nilai
#       >>>[0,3,6,9,12,15]
