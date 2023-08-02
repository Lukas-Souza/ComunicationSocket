#
# |@.1.0
# |autor: Limae
#
def inicialização(username, Data):

    Texto = ' BEM VINDO AO FCHAT '
    nickename = " ", username, " "
    print("\033[1;33m")
    print("=====".center(70,"="))
    print("\033[36m")
    print(Texto.center(70, " "))
    print("\033[1;33m")
    print(f' {username} '.center(70, ">"))
    print("\033[0;32m")
    print(f' {Data} '.center(70, "-"))
    print("\033[m")
    print("\033[0;35mPara sair baste digitar o comenado [::exit]\033[m\n")