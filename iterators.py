from select import select
import time
from typing_extensions import Self

class FiboIter():
    
    def __init__(self, max=None):
        self.max = max
    
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
                     
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            #  self.n1 = self.n2
            #  self.n2 = self.aux
            if self.aux > self.max:
                print('Finished.')
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux           
                        
# def run():
if __name__ == '__main__':
        max = int(input('Numero maximo:'))
        fibonacci = FiboIter(max)
        for element in fibonacci:
            print(element)
            time.sleep(0.05)
      
# if __name__ == '__main__':
    # run()


        
#if __name__ == '__main__':
#    fibonacci = FiboIter()
    
#    for element in fibonacci:
#        print(element)
#        time.sleep(0.05)