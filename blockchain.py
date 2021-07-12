from hashlib import sha256
import datetime

def updateHash(*args):
	hashData=""
	for arg in (args):
		hashData += str(arg)
	hashVal=sha256(hashData.encode('utf-8'))
	return(hashVal.hexdigest())


class block():
	previousHash="0"*64
	data=None
	nonce=0
	"""docstring for block_chain"""
	def __init__(self,data,number):
		self.chain = []
		self.data=data
		self.number=number
		date=datetime.datetime.now()
		self.hash=updateHash(self.data,self.number,self.nonce,self.previousHash,date)
		
		#print(self.data,"\n",self.number,"\n",self.nonce,"\n",self.previousHash,"\n",hash,"\n",date)
	 
class blockChain(block):
	"""docstring for blockChain"""
	def __init__(self,chain=[]):
		self.chain = chain
	def add(self,block):
		self.chain.append({'hash':block.hash,'data':block.data,'number':block.number,'previousHash':block.previousHash})
		
		return(self.chain)
#block call
obj=block('12qwer3423wsdfwq12',1000000)
#block chain Call
chainObj=blockChain()
print(chainObj.add(obj))

#print('\nPublic Key:',obj.data,'\nAmount:',obj.number,'\nHash:',obj.hash,'\nPrevious Hash:',obj.previousHash)

		