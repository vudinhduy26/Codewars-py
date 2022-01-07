class Pell(object):
    def __init__(self,arr = [0,1]):# khai bao thuoc tinh cua lop
        self.arr = arr

    def get(self, n):
        for i in range(0,n-1):
            try:
                k = self.arr[i]+2*self.arr[i+1]
                self.arr.append(k)
            except:
                break
        
        return self.arr[len(self.arr)-1]


a = Pell()
print(a.get(6))