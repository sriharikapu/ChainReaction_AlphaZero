
import sys
sys.setrecursionlimit(24000)
import tkMessageBox

from Tkinter import *

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)


global count
count = 0



def check_winner():
	count_red = 0
	count_blue = 0
	for x in range(8):
		for y in range(8):
			if(arr[x][y]['bg']=="red"):
				count_red = count_red + 1
			elif(arr[x][y]['bg']=="blue"):
				count_blue = count_blue + 1
	if(count_red==0):
		tkMessageBox.showinfo( "TapDots", "Blue wins")
		sys.exit()
	elif(count_blue==0):
		tkMessageBox.showinfo( "TapDots", "Red wins")
		sys.exit()




def recurse_check():
	check_winner()
	
	for x in range(8):
		for y in range(8):
			if(((x==0) and (y==0)) or ((x==0) and (y==7)) or ((x==7) and (y==0)) or ((x==7) and (y==7))):
				if(arr[x][y]['text']>1):
					arr[x][y]['text'] = 0
					arr[x][y]['bg'] = "#d9d9d9"
					if((x==0) and (y==0)):
						arr[0][1]['text'] = arr[0][1]['text'] + 1
						arr[1][0]['text'] = arr[1][0]['text'] + 1
						arr[0][1]['bg']	= getCurrentColor(count)
						arr[1][0]['bg']	= getCurrentColor(count)
					elif((x==0) and (y==7)):
						arr[0][6]['text'] = arr[0][6]['text'] + 1
						arr[1][7]['text'] = arr[1][7]['text'] + 1
						arr[1][7]['bg']	= getCurrentColor(count)
						arr[0][6]['bg']	= getCurrentColor(count)
					elif((x==7) and (y==0)):
						arr[6][0]['text'] = arr[6][0]['text'] + 1
						arr[7][1]['text'] = arr[7][1]['text'] + 1
						arr[6][0]['bg']	= getCurrentColor(count)
						arr[7][1]['bg']	= getCurrentColor(count)
					elif((x==7) and (y==7)):
						arr[7][6]['text'] = arr[7][6]['text'] + 1
						arr[6][7]['text'] = arr[6][7]['text'] + 1
						arr[7][6]['bg']	= getCurrentColor(count)
						arr[6][7]['bg']	= getCurrentColor(count)

					recurse_check()	

			elif((x==0) or (y==7) or (x==7) or (y==0)):
				if(arr[x][y]['text']>2):
					arr[x][y]['text'] = 0
					arr[x][y]['bg'] = "#d9d9d9"
					if((x==0) and (y>0)):
						arr[x][y+1]['text'] = arr[x][y+1]['text'] + 1
						arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
						arr[x+1][y]['text'] = arr[x+1][y]['text'] + 1
						arr[x][y+1]['bg']	= getCurrentColor(count)
						arr[x][y-1]['bg']	= getCurrentColor(count)
						arr[x+1][y]['bg']   = getCurrentColor(count)
					if((x==7) and (y>0)):
						arr[x][y+1]['text'] = arr[x][y+1]['text'] + 1
						arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
						arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1
						arr[x][y+1]['bg']	= getCurrentColor(count)
						arr[x][y-1]['bg']	= getCurrentColor(count)
						arr[x-1][y]['bg']   = getCurrentColor(count)
					if((y==0) and (x>0)):
						arr[x+1][y]['text'] = arr[x+1][y]['text'] + 1
						arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1
						arr[x][y+1]['text'] = arr[x][y+1]['text'] + 1
						arr[x+1][y]['bg']	= getCurrentColor(count)
						arr[x-1][y]['bg']	= getCurrentColor(count)
						arr[x][y+1]['bg']   = getCurrentColor(count)
					if((y==7) and (x>0)):
						arr[x+1][y]['text'] = arr[x+1][y]['text'] + 1
						arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1
						arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
						arr[x+1][y]['bg']	= getCurrentColor(count)
						arr[x-1][y]['bg']	= getCurrentColor(count)
						arr[x][y-1]['bg']   = getCurrentColor(count)

					recurse_check()	
			else:
				if(arr[x][y]['text']>3):
					arr[x][y]['text'] = 0
					arr[x][y]['bg'] = "#d9d9d9"
					arr[x][y+1]['text'] = arr[x][y+1]['text'] + 1
					arr[x+1][y]['text'] = arr[x+1][y]['text'] + 1
					arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
					arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1

					arr[x][y+1]['bg'] = getCurrentColor(count)
					arr[x+1][y]['bg'] = getCurrentColor(count)
					arr[x][y-1]['bg'] = getCurrentColor(count)
					arr[x-1][y]['bg'] = getCurrentColor(count)

					recurse_check()


def reduce():
	global count
	count = count-1	

def errorMessage(count_):
	tkMessageBox.showinfo( "TapDots", "You can't press "+getCurrentColor(count_)+" Button")	

def getCurrentColor(count_):
	if(count_%2==0):
		return "red"
	else:
		return "blue"	

def changeColor(count_ , value):
	
	if(value['bg']=="#d9d9d9"):
		if(count_%2==0):
			value['bg']	= "red"
		else:
			value['bg']	= "blue"
	
		



def action(x,y,value):
	if((value['bg']==getCurrentColor(count+1)) or (value['bg']=="#d9d9d9")):
		# global recurse_counter
		# recurse_counter = 0
		global count
		global red
		global blue
		count = count + 1
		#tkMessageBox.showinfo( "Hello Python", value['bg'])

		if(((x==1) and (y==1)) or ((x==1) and (y==8)) or ((x==8) and (y==1)) or ((x==8) and (y==8))):
			if(value['text']==1):
				value['text'] = 0
				value['bg'] = "#d9d9d9"
				if((x==1) and (y==1)):
					arr[0][1]['text'] = arr[0][1]['text'] + 1
					arr[1][0]['text'] = arr[1][0]['text'] + 1
					arr[0][1]['bg']	= getCurrentColor(count)
					arr[1][0]['bg']	= getCurrentColor(count)
				elif((x==1) and (y==8)):
					arr[0][6]['text'] = arr[0][6]['text'] + 1
					arr[1][7]['text'] = arr[1][7]['text'] + 1
					arr[1][7]['bg']	= getCurrentColor(count)
					arr[0][6]['bg']	= getCurrentColor(count)
				elif((x==8) and (y==1)):
					arr[6][0]['text'] = arr[6][0]['text'] + 1
					arr[7][1]['text'] = arr[7][1]['text'] + 1
					arr[6][0]['bg']	= getCurrentColor(count)
					arr[7][1]['bg']	= getCurrentColor(count)
				elif((x==8) and (y==8)):
					arr[7][6]['text'] = arr[7][6]['text'] + 1
					arr[6][7]['text'] = arr[6][7]['text'] + 1
					arr[7][6]['bg']	= getCurrentColor(count)
					arr[6][7]['bg']	= getCurrentColor(count)			
					
				recurse_check()	

			else:
				value['text'] = value['text'] + 1
				changeColor(count , value)	 
		elif((x==1) or (y==8) or (x==8) or (y==1)):
			if(value['text']==2):
				value['text'] = 0
				value['bg'] = "#d9d9d9"
				if((x==1) and (y>1)):
					arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1
					arr[x-1][y-2]['text'] = arr[x-1][y-2]['text'] + 1
					arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
					arr[x-1][y]['bg']	= getCurrentColor(count)
					arr[x-1][y-2]['bg']	= getCurrentColor(count)
					arr[x][y-1]['bg']   = getCurrentColor(count) 
				if((x==8) and (y>1)):
					arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1
					arr[x-1][y-2]['text'] = arr[x-1][y-2]['text'] + 1
					arr[x-2][y-1]['text'] = arr[x-2][y-1]['text'] + 1
					arr[x-1][y]['bg']	= getCurrentColor(count)
					arr[x-1][y-2]['bg']	= getCurrentColor(count)
					arr[x-2][y-1]['bg'] = getCurrentColor(count)
				if((y==1) and (x>1)):
					arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
					arr[x-2][y-1]['text'] = arr[x-2][y-1]['text'] + 1
					arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1
					arr[x][y-1]['bg']	= getCurrentColor(count)
					arr[x-2][y-1]['bg']	= getCurrentColor(count)
					arr[x-1][y]['bg']   = getCurrentColor(count)
				if((y==8) and (x>1)):
					arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
					arr[x-2][y-1]['text'] = arr[x-2][y-1]['text'] + 1
					arr[x-1][y-2]['text'] = arr[x-1][y-2]['text'] + 1
					arr[x][y-1]['bg']	= getCurrentColor(count)
					arr[x-2][y-1]['bg']	= getCurrentColor(count)
					arr[x-1][y-2]['bg'] = getCurrentColor(count)

				recurse_check()
									
			else:
				value['text'] = value['text'] + 1
				changeColor(count , value)	 
		else:
			if(value['text']==3):
				value['text'] = 0
				value['bg'] = "#d9d9d9"
				arr[x-1][y]['text'] = arr[x-1][y]['text'] + 1
				arr[x][y-1]['text'] = arr[x][y-1]['text'] + 1
				arr[x-1][y-2]['text'] = arr[x-1][y-2]['text'] + 1
				arr[x-2][y-1]['text'] = arr[x-2][y-1]['text'] + 1

				arr[x-1][y]['bg'] = getCurrentColor(count)
				arr[x][y-1]['bg'] = getCurrentColor(count)
				arr[x-1][y-2]['bg'] = getCurrentColor(count)
				arr[x-2][y-1]['bg'] = getCurrentColor(count)

				recurse_check()
				
			else:
				value['text'] = value['text'] + 1
				changeColor(count , value)



	else:
		errorMessage(count)	
		
#example values


# arr_cor = [1,2,3,4,5,6,7,8]
red = 0
blue  = 0
#d9d9d9 = 0

b11 = Button(frame , text=0 ,command = lambda : action(1,1,b11))
b11.grid(column=1, row=1,sticky=N+S+E+W)

b12 = Button(frame , text=0 ,command = lambda : action(2,1,b12))
b12.grid(column=2, row=1,sticky=N+S+E+W)

b13 = Button(frame , text=0 ,command = lambda : action(3,1,b13))
b13.grid(column=3, row=1,sticky=N+S+E+W)

b14 = Button(frame , text=0 ,command = lambda : action(4,1,b14))
b14.grid(column=4, row=1,sticky=N+S+E+W)

b15 = Button(frame , text=0 ,command = lambda : action(5,1,b15))
b15.grid(column=5, row=1,sticky=N+S+E+W)

b16 = Button(frame , text=0 ,command = lambda : action(6,1,b16))
b16.grid(column=6, row=1,sticky=N+S+E+W)

b17 = Button(frame , text=0 ,command = lambda : action(7,1,b17))
b17.grid(column=7, row=1,sticky=N+S+E+W)

b18 = Button(frame , text=0 ,command = lambda : action(8,1,b18))
b18.grid(column=8, row=1,sticky=N+S+E+W)



b21 = Button(frame , text=0 ,command = lambda : action(1,2,b21))
b21.grid(column=1, row=2,sticky=N+S+E+W)

b22 = Button(frame , text=0 ,command = lambda : action(2,2,b22))
b22.grid(column=2, row=2,sticky=N+S+E+W)

b23 = Button(frame , text=0 ,command = lambda : action(3,2,b23))
b23.grid(column=3, row=2,sticky=N+S+E+W)

b24 = Button(frame , text=0 ,command = lambda : action(4,2,b24))
b24.grid(column=4, row=2,sticky=N+S+E+W)

b25 = Button(frame , text=0 ,command = lambda : action(5,2,b25))
b25.grid(column=5, row=2,sticky=N+S+E+W)

b26 = Button(frame , text=0 ,command = lambda : action(6,2,b26))
b26.grid(column=6, row=2,sticky=N+S+E+W)

b27 = Button(frame , text=0 ,command = lambda : action(7,2,b27))
b27.grid(column=7, row=2,sticky=N+S+E+W)

b28 = Button(frame , text=0 ,command = lambda : action(8,2,b28))
b28.grid(column=8, row=2,sticky=N+S+E+W)



b31 = Button(frame , text=0 ,command = lambda : action(1,3,b31))
b31.grid(column=1, row=3,sticky=N+S+E+W)

b32 = Button(frame , text=0 ,command = lambda : action(2,3,b32))
b32.grid(column=2, row=3,sticky=N+S+E+W)

b33 = Button(frame , text=0 ,command = lambda : action(3,3,b33))
b33.grid(column=3, row=3,sticky=N+S+E+W)

b34 = Button(frame , text=0 ,command = lambda : action(4,3,b34))
b34.grid(column=4, row=3,sticky=N+S+E+W)

b35 = Button(frame , text=0 ,command = lambda : action(5,3,b35))
b35.grid(column=5, row=3,sticky=N+S+E+W)

b36 = Button(frame , text=0 ,command = lambda : action(6,3,b36))
b36.grid(column=6, row=3,sticky=N+S+E+W)

b37 = Button(frame , text=0 ,command = lambda : action(7,3,b37))
b37.grid(column=7, row=3,sticky=N+S+E+W)

b38 = Button(frame , text=0 ,command = lambda : action(8,3,b38))
b38.grid(column=8, row=3,sticky=N+S+E+W)



b41 = Button(frame , text=0 ,command = lambda : action(1,4,b41))
b41.grid(column=1, row=4,sticky=N+S+E+W)

b42 = Button(frame , text=0 ,command = lambda : action(2,4,b42))
b42.grid(column=2, row=4,sticky=N+S+E+W)

b43 = Button(frame , text=0 ,command = lambda : action(3,4,b43))
b43.grid(column=3, row=4,sticky=N+S+E+W)

b44 = Button(frame , text=0 ,command = lambda : action(4,4,b44))
b44.grid(column=4, row=4,sticky=N+S+E+W)

b45 = Button(frame , text=0 ,command = lambda : action(5,4,b45))
b45.grid(column=5, row=4,sticky=N+S+E+W)

b46 = Button(frame , text=0 ,command = lambda : action(6,4,b46))
b46.grid(column=6, row=4,sticky=N+S+E+W)

b47 = Button(frame , text=0 ,command = lambda : action(7,4,b47))
b47.grid(column=7, row=4,sticky=N+S+E+W)

b48 = Button(frame , text=0 ,command = lambda : action(8,4,b48))
b48.grid(column=8, row=4,sticky=N+S+E+W)



b51 = Button(frame , text=0 ,command = lambda : action(1,5,b51))
b51.grid(column=1, row=5,sticky=N+S+E+W)

b52 = Button(frame , text=0 ,command = lambda : action(2,5,b52))
b52.grid(column=2, row=5,sticky=N+S+E+W)

b53 = Button(frame , text=0 ,command = lambda : action(3,5,b53))
b53.grid(column=3, row=5,sticky=N+S+E+W)

b54 = Button(frame , text=0 ,command = lambda : action(4,5,b54))
b54.grid(column=4, row=5,sticky=N+S+E+W)

b55 = Button(frame , text=0 ,command = lambda : action(5,5,b55))
b55.grid(column=5, row=5,sticky=N+S+E+W)

b56 = Button(frame , text=0 ,command = lambda : action(6,5,b56))
b56.grid(column=6, row=5,sticky=N+S+E+W)

b57 = Button(frame , text=0 ,command = lambda : action(7,5,b57))
b57.grid(column=7, row=5,sticky=N+S+E+W)

b58 = Button(frame , text=0 ,command = lambda : action(8,5,b58))
b58.grid(column=8, row=5,sticky=N+S+E+W)



b61 = Button(frame , text=0 ,command = lambda : action(1,6,b61))
b61.grid(column=1, row=6,sticky=N+S+E+W)

b62 = Button(frame , text=0 ,command = lambda : action(2,6,b62))
b62.grid(column=2, row=6,sticky=N+S+E+W)

b63 = Button(frame , text=0 ,command = lambda : action(3,6,b63))
b63.grid(column=3, row=6,sticky=N+S+E+W)

b64 = Button(frame , text=0 ,command = lambda : action(4,6,b64))
b64.grid(column=4, row=6,sticky=N+S+E+W)

b65 = Button(frame , text=0 ,command = lambda : action(5,6,b65))
b65.grid(column=5, row=6,sticky=N+S+E+W)

b66 = Button(frame , text=0 ,command = lambda : action(6,6,b66))
b66.grid(column=6, row=6,sticky=N+S+E+W)

b67 = Button(frame , text=0 ,command = lambda : action(7,6,b67))
b67.grid(column=7, row=6,sticky=N+S+E+W)

b68 = Button(frame , text=0 ,command = lambda : action(8,6,b68))
b68.grid(column=8, row=6,sticky=N+S+E+W)



b71 = Button(frame , text=0 ,command = lambda : action(1,7,b71))
b71.grid(column=1, row=7,sticky=N+S+E+W)

b72 = Button(frame , text=0 ,command = lambda : action(2,7,b72))
b72.grid(column=2, row=7,sticky=N+S+E+W)

b73 = Button(frame , text=0 ,command = lambda : action(3,7,b73))
b73.grid(column=3, row=7,sticky=N+S+E+W)

b74 = Button(frame , text=0 ,command = lambda : action(4,7,b74))
b74.grid(column=4, row=7,sticky=N+S+E+W)

b75 = Button(frame , text=0 ,command = lambda : action(5,7,b75))
b75.grid(column=5, row=7,sticky=N+S+E+W)

b76 = Button(frame , text=0 ,command = lambda : action(6,7,b76))
b76.grid(column=6, row=7,sticky=N+S+E+W)

b77 = Button(frame , text=0 ,command = lambda : action(7,7,b77))
b77.grid(column=7, row=7,sticky=N+S+E+W)

b78 = Button(frame , text=0 ,command = lambda : action(8,7,b78))
b78.grid(column=8, row=7,sticky=N+S+E+W)



b81 = Button(frame , text=0 ,command = lambda : action(1,8,b81))
b81.grid(column=1, row=8,sticky=N+S+E+W)

b82 = Button(frame , text=0 ,command = lambda : action(2,8,b82))
b82.grid(column=2, row=8,sticky=N+S+E+W)

b83 = Button(frame , text=0 ,command = lambda : action(3,8,b83))
b83.grid(column=3, row=8,sticky=N+S+E+W)

b84 = Button(frame , text=0 ,command = lambda : action(4,8,b84))
b84.grid(column=4, row=8,sticky=N+S+E+W)

b85 = Button(frame , text=0 ,command = lambda : action(5,8,b85))
b85.grid(column=5, row=8,sticky=N+S+E+W)

b86 = Button(frame , text=0 ,command = lambda : action(6,8,b86))
b86.grid(column=6, row=8,sticky=N+S+E+W)

b87 = Button(frame , text=0 ,command = lambda : action(7,8,b87))
b87.grid(column=7, row=8,sticky=N+S+E+W)

b88 = Button(frame , text=0 ,command = lambda : action(8,8,b88))
b88.grid(column=8, row=8,sticky=N+S+E+W)

arr =   [[b11,b21,b31,b41,b51,b61,b71,b81],
    	[b12,b22,b32,b42,b52,b62,b72,b82],
    	[b13,b23,b33,b43,b53,b63,b73,b83],
    	[b14,b24,b34,b44,b54,b64,b74,b84],
    	[b15,b25,b35,b45,b55,b65,b75,b85],
    	[b16,b26,b36,b46,b56,b66,b76,b86],
    	[b17,b27,b37,b47,b57,b67,b77,b87],
    	[b18,b28,b38,b48,b58,b68,b78,b88],
    	]


for x in range(8):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(8):
  Grid.rowconfigure(frame, y, weight=1)

root.mainloop()