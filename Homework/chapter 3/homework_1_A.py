class Binary:
    def __init__(self, first_num, second_num, sis=2):
        self.sis = sis
        self.__add__(first_num, second_num)
        self.__sub__(first_num, second_num)
        self.__mul__(first_num, second_num)
        self.__floordiv__(first_num, second_num)
    
    def __changer__(self):
        alphabet = "0123456789"
        b = alphabet[self.value % self.sis]
        while self.value >= self.sis:
            self.value = self.value // self.sis 
            b += alphabet[self.value % self.sis]
        print(b[::-1])        
        
                
    def __add__(self, first_num, second_num):
        self.value = int(f"{first_num}", self.sis) + int(f"{second_num}", self.sis)
        self.__changer__()
        
    def __sub__(self, first_num, second_num):
        self.value = int(f"{first_num}", self.sis) - int(f"{second_num}", self.sis)
        self.__changer__()
    
    def __mul__(self, first_num, second_num):
        self.value = int(f"{first_num}", self.sis) * int(f"{second_num}", self.sis)
        self.__changer__()
    
    def __floordiv__(self, first_num, second_num):
        self.value = int(f"{first_num}", self.sis) // int(f"{second_num}", self.sis)
        self.__changer__()


if __name__ == "__main__":
    y = input().split()
    root = Binary(int(y[0]), int(y[1]))
