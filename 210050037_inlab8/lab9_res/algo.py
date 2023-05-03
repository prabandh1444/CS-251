import re

##########
#### SEARCH FOR TODO and fix
# Anything following "//" is a comment until end of line
commentPat = re.compile(r'//.*')

# Grab anything within $...$. Make sure to use 
mathPat =  re.compile( r'\$.*?\$' )

#All id-like words, including optional leading '\' and 
# field access sequences 
# Examples: abc,  foo.length, \xxx
wordPat = re.compile(r'\b[_a-zA-Z][._a-zA-Z0-9]*')

#Take a set of all the unique symbols in opsToTex's keys. 
#Like this r'[<=>.]+'   etc. 
opPat = re.compile(r'\<\-|\-\>|\=\=|\<\=|\>\=|\>|\<|\!\=|\=|\.\.\.|\.\.|\+|\-')

# A line of the form "proc myfunc(a, b)".
procPat = re.compile(r'(proc)\s([-_a-zA-Z0-9]*)\(([a-zA-Z0-9\,\s]*)\)')

keywordsToTex = {
    'for'    : r'\For'        ,     'if'     : r'\If'          , 
    'end'    : r'\End'        ,     'then'   : r'\Then'        , 
    'while'  : r'\While'      ,     'do'     : r'\Do'          ,  
    'to'     : r'\To'         ,     'by'     : r'\By'          , 
    'downto' : r'\Downto'     ,     'repeat' : r'\Repeat'      , 
    'until'  : r'\Until'      ,     'elseif' : r'\Elseif'      ,
    'elsif'  : r'\Elseif'     ,     'return' : r'\Return'      , 
    'error'  : r'\Error'      ,     'nil'    : r'\const{nil}'  , 
    'true'   : r'\const{true}',     'false'  : r'\const{false}'
}

opsToTeX = {
    '<-' : r'\leftarrow' ,      '->' : r'\rightarrow',      '==' : r'\isequal' ,
    '<=' : r'\leq'       ,      '>=' : r'\geq'        ,      '>' : '>'          , 
    '<' : '<'            ,      '!=' : r'\neq'       ,      '=' : r'\eq'       , 
    '...' : r'\threedots',      '..' : r'\twodots',          '-' : '-'          ,
    '+' : '+'
}

def processLine(line):
    if(commentPat.search(line)):
        content=re.sub(commentPat,'\n',line)
        X=commentPat.findall(line)
        comment=X[0]
        return processContent(content) + processComment(comment)
    else:
        return processContent(line)


    # Split line into content part and comment part
    # Comments are always to the right, but are optional
    # return processContent(content) + processComment(comment)



def processContent(content):
    if(procPat.search(content)):
        X = procPat.findall(content)
        return processProc(X)
    else:
        return "\zi"+processOps(processWords(content))

    # Treat the entire content as if it is already in math mode
    # processProc if it matches a proc line
    # Otherwise,
    # Treat the entire content as if it is already in math mode.
    # If there are any embedded '$...$' fragments, then strip the dollar signs
    # out.
    # Prepend '\zi' to the returned line, unless content matches a proc declaration

def processProc(lineMatch):
    liner=lineMatch[0]
    func_name = liner[1]
    str = "\\Procname{\proc{"+func_name+"}("
    str1 = liner[2]
    list = str1.split(", ")
    for word in list:
        str=str+"\id{"+word+"}, "
    str=str[:-2]+")}"
    return str
    
def processMath(mathPart):
    math = mathPart.group(0)
    math=math.replace("$","")
    return processOps(processWords(math))

def processWords(fragment):
    return re.sub(wordPat, processWord, fragment)
    # call re.sub with wordPat and processWord

def processWord(wordMatch):
    word = wordMatch.group(0)
    if word[0]=="\\":
        return str
    if "." in word:
        list1=word.split(".")
        str="\\attri"
        for i in range(1,len(list1)):
            str = str + "b"
        for word1 in list1:
            str=str+"{"+word1+"}"
        return str
    if word in keywordsToTex.keys():
        str=keywordsToTex[word]
        return str
    else:
        return "\id{"+word+"}"
    #TODO
    # Handle four cases. 
    #   Word starts with '\' ... return word untouched
    #   Word has embedded '.'. Convert "abc.def.ghi" to "\attribbb{abc}{def}{ghi}"
    #            The number of 'b's following attrib should equal the number of dots
    #   Word belongs to keywords (see testalgo.py for all keywords). Replace with latex substitute
    #   Otherwise replace with "\id{word}"

def processOps(fragment):
    return re.sub(opPat, processOp, fragment)

def processOp(opMatch):
    op = opMatch.group(0)
    str="$"+opsToTeX[op]+"$"
    return str
    TODO
    # replace op with matching latex equivalent if any, and surround with '$'
    # That is, '==' becomes '$\isequal$', but '===' remains unchanged.

def processComment(comment):
    #Treat comment as if it is in text mode, but all embedded math expressions must be translated
    #by processMath
    # See testalgo.py for expected behaviur
    comment = comment.replace("//","\Comment")
    return "\zi"+re.sub(mathPat,processMath,comment)


def main(filename):
    with open(filename) as f:
        print(r'\begin{codebox}')
        for line in f:
            line = line.rstrip()
            print(processLine(line))
        print(r'\end{codebox}')

def usage():
    print("""
algo.py <file.algo>
Translates a pseudocode algorithm to LaTeX's clrscode3e environment. 
The format is a simplification of that environment, the objective being to 
not have to introduce math-mode or have special keywords like \For and \If 

Keywords: 
- Loops: for, to, by, downto, do, while, repeat, until
- Selection: if, then, else, elseif/elsif
- Jumps: return, error, goto
- Constants: nil, true, false

do/end blocks are required for indent/dedent, but do not appear in final output

Operators like <-, !=, ==, <= etc are replaced by the LaTeX equivalents.

Example:

proc insertion-sort(A, B)
   for j <- 2 to A.length do
      key <- A[j] // Insert $A[j]$ into the sorted sequence $A[1 .. j-1]$
      i <- j - 1
      while i > 0 and A[i] > key do
         A[i+1] <- A[i]
         i <- i - 1
      end
      A[i+1] <- key
   end
   if x == 3 then do
      {{Do something special}}
   end
end

""")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    main(sys.argv[1])
    
   
