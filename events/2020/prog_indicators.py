#from __future__ import unicode_literals

class Bar():
    def __init__(self, iterations, fill='#', empty='-', prefix='|', suffix='|', display_iter=False, display_percent=True, width=100):
        self.iterations = iterations
        self.fill = fill
        self.empty = empty
        self.prefix = prefix
        self.suffix = suffix
        self.display_iter = display_iter
        self.display_percent = display_percent
        self.width = width
        self.current_iter = 0
    
    def update(self):
        if not self.current_iter > self.iterations:
            self.current_iter += 1

        filled = int(self.width * self.current_iter // self.iterations)
        bar = (self.fill * filled) + (self.empty * (self.width - filled))
        percent = self.display_percent * f' {100 * self.current_iter/self.iterations:.1f}%'
        iter_count = self.display_iter * f' {self.current_iter}/{self.iterations}'

        if self.display_iter and self.display_percent:
            print(self.prefix + bar + self.suffix + percent +' |'+ iter_count, end='\r')
        else:
            print(self.prefix + bar + self.suffix + percent + iter_count, end='\r')
        
        if self.current_iter == self.iterations:
            print()