def solve(PUZZLE,WORDS,reverse=False):
	def calc_end(PUZZLE,sx,sy,w,data):
		if (len(w)<2):return data
		d=None
		ex=0
		ey=0
		for dr in [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]:
			if (0<=sx+dr[0]<len(PUZZLE[0]) and 0<=sy+dr[1]<len(PUZZLE) and PUZZLE[sy+dr[1]][sx+dr[0]]==w[1]):
				ex=sx+dr[0]
				ey=sy+dr[1]
				d=dr
				break
		if (d==None):return data
		for i in range(2,len(w),1):
			ex+=dr[0]
			ey+=dr[1]
			if (not(0<=ex<len(PUZZLE[0]) and 0<=ey<len(PUZZLE))):return data
			if (PUZZLE[ey][ex]!=w[i]):return data
		data.append([w,(sx+1,sy+1),(ex+1,ey+1)])
		return data
	if (reverse==True):
		s="^".join(WORDS).split("^")
		for w in s:
			nw=""
			for ci in range(len(w)-1,-1,-1):
				nw+=w[ci]
			WORDS.append(nw)
	dt=[]
	x=0
	y=0
	for row in PUZZLE:
		for c in row:
			for w in WORDS:
				if (c==w[0]):
					dt=calc_end(PUZZLE,x,y,w,dt)
			x+=1
		y+=1
		x=0
	return dt
def printCrossword(PUZZLE):
	s=""
	for row in PUZZLE:
		for c in row:
			s+=c+" "
		s=s[:len(s)-1]+"\n"
	print(s)
def crossword(s):
	d=[]
	for row in s.split(";"):
		r=""
		for c in row:
			r+=c.lower()
		d.append(r)
	return d



PUZZLE=crossword("abc;def;ghi")
printCrossword(PUZZLE)
print(solve(PUZZLE,["aei"],reverse=True))