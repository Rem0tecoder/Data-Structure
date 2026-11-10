
count = 0
def func():
    global count
    if count == 4:
        return
    print('Animal')
    count +=1
    func()

func() 

count = 0
def func():
    global count
    if count == 4:
        return
    count+=1
    func()
    print('Animal')

func()