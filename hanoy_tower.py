import os
import time

class hanoi():
    column = {1:'one_column', 2: 'two_column', 3: 'tree_column'}
    def __init__(self, i=8):
        self.one_column = [k for k in range(1, i+1)]
        self.two_column = [0 for k in range(i)]
        self.tree_column = [0 for k in range(i)]


    def show(self):
        print("""                ###############################################
                #                                             #"""
           
        )

        [print(f'                #      |-{one}-|         |-{two}-|         |-{tree}-|      #') for one, two, tree in zip(self.one_column, self.two_column, self.tree_column)]

        print("""                #                                             #
                ###############################################""")

        return None

    def permutation_hanoy(self, a=1, b=3):
        eval(f'self.{self.column[a]}')[hanoi().stack(eval(f'self.{self.column[a]}'))], eval(f'self.{self.column[b]}')[hanoi().stack(eval(f'self.{self.column[b]}'))-1] = eval(f'self.{self.column[b]}')[hanoi().stack(eval(f'self.{self.column[b]}'))-1], eval(f'self.{self.column[a]}')[hanoi().stack(eval(f'self.{self.column[a]}'))]
 

    def stack(self, lst):
        for i in range(len(lst)):
            if lst[i] !=0:
                return i
        return i+1

    def hanoi_def(self,mode=0, k=None, a=1, b=3,):
        if k is None:
            k=len(self.one_column)

        if mode:
            pass
        else:
            if k==1:
                hanoi.permutation_hanoy(self, a, b)

                self.show()
                time.sleep(1)
                os.system("clear")

                return None

            hanoi.hanoi_def(self, k=k-1,a=a, b=6-a-b)

            hanoi.permutation_hanoy(self, a, b)

            self.show()
            time.sleep(1)
            os.system("clear")            

            hanoi.hanoi_def(self, k=k-1, a=6-a-b, b=b)          

    def run(self, mode=0):
        if mode:
            pass
        else:
            self.hanoi_def(mode=mode)
            self.show()
        

        

app = hanoi()
app.run()


