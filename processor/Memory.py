from block import Block
import threading
import time

class Memory:
    #used to simulate the bus
    flag=False

    def __init__(self):
        self.block1=Block(1)
        self.block2=Block(2)
        self.block3=Block(3)
        self.block4=Block(4)
        self.block5=Block(5)
        self.block6=Block(6)
        self.block7=Block(7)
        self.block8=Block(8)
        self._lock = threading.Lock()
    


    def findInMem(self,dir):
        blocks=[self.block1, self.block2, self.block3, self.block4, self.block5, self.block6, self.block7, self.block8]
        emptyBlock=0
        for x in blocks:
            if (x.dir==dir):
                return [[x.id, x.data],emptyBlock]
        return False

    def printMem(self):
        blocks=[self.block1, self.block2, self.block3, self.block4, self.block5, self.block6, self.block7, self.block8]
        currentBlock=[]
        for x in blocks:
            currentBlock.append(x.dir)
            currentBlock.append(x.data)
            print(currentBlock)
            currentBlock=[]


    def writeMemory(self, dir, data):
        with self._lock:
            #findBlock=self.findInMem(dir)
            block=int(dir[2:],2)+1
            #if (findBlock!=False): 
                #if(findBlock[0]!=""):
            time.sleep(1)
            match block:
                case 1: self.block1.data=data; self.block1.dir=dir
                case 2: self.block2.data=data; self.block2.dir=dir
                case 3: self.block3.data=data; self.block3.dir=dir
                case 4: self.block4.data=data; self.block4.dir=dir
                case 5: self.block5.data=data; self.block5.dir=dir
                case 6: self.block6.data=data; self.block6.dir=dir
                case 7: self.block7.data=data; self.block7.dir=dir
                case 8: self.block8.data=data; self.block8.dir=dir
         


    def readMemory(self,dir):
        with self._lock:
            time.sleep(1)
            findBlock=self.findInMem(dir)
            print("FindBlock")
            print(findBlock)
            if(findBlock!=False): 
                if(findBlock[0]!=""):
                    match findBlock[0][0]:
                        case 1: return self.block1.data
                        case 2: return self.block2.data
                        case 3: return self.block3.data
                        case 4: return self.block4.data
                        case 5: return self.block5.data
                        case 6: return self.block6.data
                        case 7: return self.block7.data
                        case 8: return self.block8.data 
        
                       
