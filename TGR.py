from appJar import*
z=''
f = open('History.txt')
for line in f:
    line
    print(line)
    z=z+line

def press(button):
	if button == 'Начать работу':
		print('Начать работу')
	else:
		app.showSubWindow(button)
		#print('База знаний')

def knop(btv):
	print('Zvezda')

app=gui("test","350x400")
#app.setBg('red')

app.startSubWindow("База знаний", modal=True)
#app.addLabel("l2", "База знаний")
app.addMessage('Box1', z)
app.startScrollPane('z')
app.stopScrollPane()
app.stopSubWindow()


app.addLabel("l1","Разделы")
app.addCheckBox("Всемирная история")
app.addCheckBox("История России")

app.addLabelNumericEntry("Колличество вопросов")

app.addButtons(["Начать работу", "База знаний"], press)
app.addImageButton('Knopka', knop, 'book2.gif')


app.go()