class movie:
    def _init_(self):
        pass

    def upd(self, var1):
        count = 0
        moviearray = []
        while (count < var1):
            var3 = input('Enter movie name ')
            moviearray.append(var3)
            count += 1
        print(moviearray)

    def rem(self, var1, var4):
        count = 0
        while (count < var1):
            var3 = int(input('Enter movie sr. no. you want to remove '))
            var4 = np.delete(var4, var3)
            print(var4)
            count += 1
        print(var4)


class moviecount(movie):
    def __init__(self):
        movie.__init__(self)
        pass

loop = 0
while loop == 0:
    print('What do you want to do\n1. Update watched list')
    print('2. Remove from watched list\n3. End program\n')
    var2 = int(input())
    m = movie()
    if var2 == 1:
        var1 = int(input('Number of movies you want to update in list '))
        m.upd(var1)
    if var2 == 2:
        var1 = int(input('Number of movies you want to remove from the list '))
        var4 = np.array(moviearray)
        m.upd(var1, var4)
    if var2 == 3:
        break