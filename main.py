def lnot(a,b):
	if (a==True and b==True):
		return False
	elif (a==True and b==False):
		return False
	elif (a==False and b==True):
		return True
	elif (a==False and b==False):
		return True

def land(a,b):
	if (a==True and b==True):
		return True
	elif (a==True and b==False):
		return False
	elif (a==False and b==True):
		return False
	elif (a==False and b==False):
		return False

def lor(a,b):
	if (a==True and b==True):
		return True
	elif (a==True and b==False):
		return True
	elif (a==False and b==True):
		return True
	elif (a==False and b==False):
		return False

def limp(a,b):
	if (a==True and b==True):
		return True
	elif (a==True and b==False):
		return False
	elif (a==False and b==True):
		return True
	elif (a==False and b==False):
		return True

def lequ(a,b):
	if (a==True and b==True):
		return True
	elif (a==True and b==False):
		return False
	elif (a==False and b==True):
		return False
	elif (a==False and b==False):
		return True

def lxor(a,b):
	if (a==True and b==True):
		return False
	elif (a==True and b==False):
		return True
	elif (a==False and b==True):
		return True
	elif (a==False and b==False):
		return False



		


