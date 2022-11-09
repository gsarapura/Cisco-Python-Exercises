"""
Nested functions:
    A function defined inside another functions.
    Their variables cannot be accessed outside their enclosing scope.

Closures:
    It's a function object that remembers values in enclosing scopes even if they are not present in memory.  
"""
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power # Without parenthesis


fsqr = make_closure(2) # Create a closure for powers of 2 
fcub = make_closure(3) # Create a closure for powers of 3

for i in range(5):
    print(i, fsqr(i), fcub(i))
