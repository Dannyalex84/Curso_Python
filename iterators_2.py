import time 

class Fibonacci():

    def __init__(self, max):
        self.max = max
        
    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0 
        return self
    
    def __next__(self):

        if self.counter == 0:
            self.counter += 1 
            return self.num1

        elif self.counter == 1:
            self.counter += 1
            return self.num2
        
        else:
            self.aux = self.num1 + self.num2 
            # Like a break; if the aux > nmax: stop, nmax is the limit.
            if self.aux > self.max:
                print('Finished.')
                raise StopIteration
            self.num1, self.num2 = self.num2, self.aux 
            self.counter += 1 
            return self.aux 
        
        
def run():
    try:
        max = int(input('Introduce the max limit number that can iterate this function: \n'))
        if max > 0:
            fibonacci = Fibonacci(max)
            for element in fibonacci:
                print(element)
                time.sleep(0.05)

        elif max == 0:
            print(0)

        else:
            print('Introduce a positive number.') 
            run()
            
    except ValueError as ve:
        print('Only integer and positive numbers.')
        run()
   
if __name__ == '__main__':
    run()
    
    