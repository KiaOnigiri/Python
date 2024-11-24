import pickle
class Sohr:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    @staticmethod
    def createacc(name,number):
        global y
        global logged_acc
        if y.get(name)==None:
            y[name]=[number]
            logged_acc=name
            print(f'Аккаунт с логином "{name}" и паролем "{number}" был успешно создан')
        else:
            print('Ошибка: Аккаунт с таким именем уже существует')
    @staticmethod
    def login(name,number):
        global y
        global logged_acc
        if y.get(name)!=None and y[name][0]==number:
            logged_acc=name
            print('Вы успешно вошли в аккаунт')
        else:
            print('Ошибка: Неверное имя аккаунта или пароль')
    def __getstate__(self) -> dict:
        global y
        state=y
        return state
    def __setstate__(self, state: dict):
        global y
        y=state
y={}
with open("file.pkl", "rb") as fp:
    pickle.load(fp)
print(y)
logged_acc=None
while logged_acc==None:
    print('')
    n=input('Введите 1, если хотите создать новый аккаунт;\nВведите 2, если хотите войти в аккаунт:\n')
    print('')
    if n=='1':
        new_name=input('Введите имя для своего нового аккаунта:\n')
        new_psw1=input('Введите пароль для своего нового аккаунта:\n')
        new_psw2=input('Повторите пароль для своего нового аккаунта:\n')
        if new_psw1!=new_psw2:
            print('Пароли не совпадают, попробуйте ещё раз')
            continue
        Sohr.createacc(new_name,new_psw1)
    elif n=='2':
        old_name=input('Введите имя своего аккаунта:\n')
        old_psw=input('Введите пароль своего аккаунта:\n')
        Sohr.login(old_name,old_psw)
    else:
        print('Пожалуйста, попробуйте ещё раз')
print(y)
#state={}
with open("file.pkl", "wb") as fp:
    pickle.dump(fp)
