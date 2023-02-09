class Custome_range :
    def __init__(self , *data_list) :
        lenght = len(data_list)
        if lenght == 0  : raise TypeError("range expected 1 argument, got 0")
        elif lenght > 3 : raise TypeError(f"range expected at most 3 arguments, got {lenght}")

        elif lenght == 3 : 
            self.start = data_list[0]
            self.end = data_list[1]
            self.step = data_list[2]
            
        elif lenght == 2 : 
            self.start = data_list[0]
            self.end = data_list[1]
            self.step = 1
            
        else : 
            self.start = 0
            self.end = data_list[0]
            self.step = 1
        
        self.count = self.start
        
    def __iter__(self) :
        return self
    
    def __next__(self) :    
        if self.step < 0 :
            if self.end >= self.start : raise StopIteration 
            if self.count <= self.end : raise StopIteration 
            return_value = self.count
            self.count += self.step
            return return_value
        else :
            if self.end <= self.start : raise StopIteration 
            if self.count >= self.end : raise StopIteration 
            return_value = self.count
            self.count += self.step
            return return_value