#I used backtracking algorithm for this
a = [
    ["t", "z", "x", "c","d"],
    ["s", "h", "a", "z","x"],
    ["h", "w", "l", "o","m"],
    ["o", "r", "n", "t","n"],
    ["a", "b", "r", "i","n"]] #letters
b = [
    [0, 0, 0, 0,0],
    [0, 0, 0, 0,0],
    [0, 0, 0, 0,0],
    [0, 0, 0, 0,0],
    [0, 0, 0, 0,0]] #answer matrix
def printAnswer(arr): #Print a two dimensional array
    allZero = True
    for i in arr:
        for j in i:
            if j != 0:
                allZero = False
    if not allZero:
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()
def solve(x,y,b,counter,a,search,z=0):
    """if z = 0 than it searches for the first letter of the word, and if it doesnt find it, it goes one to the right/
        if z = 1 that it checks one square, if it doesn't have the next letter in the word, it returns back to the function that called it,
        and if it does find it that it continues to search from there, and if it finds a dead end it backtracks until z = 0
    """
    if z:
        if y <0 or y>4 or x<0 or x>4: #if out of array bounds
            return counter,b
    try:
        if counter <= len(search)-1 and a[y][x]==search[counter] and b[y][x] == 0: #check if the spot is free and is the letter that were looking for and we haven't reached the end of the word yet
            counter += 1 #we found one letter, so we are looking for the next letter
            b[y][x] =counter #we set the path
            counter,b = solve(x,y - 1, b,counter,a,search,1) #we search in z = 1 if there is any correct letter next to our x,y, and than we update our counter and b to match it
            counter,b = solve(x,y + 1, b,counter,a,search,1)
            counter,b = solve(x + 1,y, b,counter,a,search,1)
            counter,b = solve(x - 1,y, b,counter,a,search,1)
            if counter > len(search)-1: #if the counter reached the end f the word than we found the word, and we return
                return counter,b
            counter -=1 #we didn't find the next letter if were here, so we start backtracking
            b[y][x]= 0
        else:
            if z:
                return counter,b #This means that there is no correct letter here, so we return
    except:
        print("No number")
        counter = 10000 #Increase counter to skip to end
        return counter,b
    if not z: #Regulear search, Search for the first letter, if it reaches out of array bounds it goes to the next line
        if y>len(a)-1:
            return counter,b
        if x<len(a)-1:
            counter,b= solve(x+1, y,b,counter,a,search)
        else:
            counter,b = solve(0,y+1,b,counter,a,search)
    return counter,b



printAnswer(solve(0,0,b,0,a,'shalom')[1])
