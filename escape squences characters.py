# ----------------
# Escape Sequences Characters 
# \b => Back Space 
# \newline => Escape New Line + \ 
# \\ => Escape Back Slash 
# \' => Escape Single Quotes 
# \" => Escape Double Quotes 
# \n => Line Feed 
# \r => Carriage Return
#\t => Horizontal Tab 
#xhh => Hexadecimal Number
# ----------------
# Back Space 
print("Hello\bWorld") # Will Remove o

# Escape New Line + Back Slash 
print("Hello\
 I Love \
Python")
# Escape Back Slash 
print("I Love Back Slash \\") 

# Escape Single Quote 
print('I Love Single Quote \'Test\' ') 

# Escape Double Quotes 
print("I Love Double Quotes \"Test\" ")

#carriage return
print("123456\rAbcd")   # Will Remove 1234 and Replace with Abcd

#horizontal tab
print("hello \tpython") # Will Add Tab Space Between hello and python

#character hex value 
print("\x4B \x49 x52 x4F") # Will Print K I R O