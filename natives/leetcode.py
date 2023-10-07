s = "/../"

def makeGood( s: str) -> str:
    stack= []
    sp = s.split('/')
    

    for c in sp:
        if c == '.'or c == '':
            
            continue

        if c == '..':
            if not stack:
                continue
                
            stack.pop()
        else: 
            stack.append(c)
        
    return "/"+"/".join(stack)

        
            
            
        
    
    


print(makeGood(s))
    