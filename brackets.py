# Check well matched brackets.
v1 = '()'
v2 = '(())'
v3 = '()()'
v4 = '()(())()((()))'

i1 = '(()'
i2 = '))'
i3 = '(()()'
i4 = '()(()()((()))'

def WellMatched(input: str) -> bool:
    for c in input:
        if c == '(':
            count = count + 1