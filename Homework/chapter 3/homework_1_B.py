from homework_1_A import Binary as bi

class Ternary(bi):
    def __init__(self, first_num, second_num, sis=3):
        self.sis = sis
        self.__add__(first_num, second_num)
        self.__sub__(first_num, second_num)
        self.__mul__(first_num, second_num)
        self.__floordiv__(first_num, second_num)
    
if __name__ == "__main__":
    x = input().split()
    root = Ternary(int(x[0]), int(x[1]))
            
    