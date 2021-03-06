# Check well matched brackets.
v1 = '()'
v2 = '(())'
v3 = '()()'
v4 = '()(())()((()))'

i1 = '(()'
i2 = '))'
i3 = '(()()'
i4 = '()(()()((()))'
i5 = '()(()()((()))))))))))))'
i6 = '((((((((((()(()()((()))'

def WellMatched(input: str) -> bool:
    OpenCount = 0
    for c in input:
        if c == '(':
            OpenCount = OpenCount + 1
        else:
            OpenCount = OpenCount - 1
        if OpenCount < 0:
            print(False)
            return
    if OpenCount > 0:
        print(False)
    else:
        print(True)
