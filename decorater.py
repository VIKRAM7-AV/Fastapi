def Owndecorater(fun):
    def Inner():
        print("This is my own decorator")
        fun();
        print("This is the end of my own decorator")
    return Inner

@Owndecorater
def MyFunction():
    print("This is my function")

MyFunction()