# Save docs to a file called "builtins"
f = open('builtins','w')

for x in dir(__builtins__):
    if x and getattr(__builtins__,x).__doc__:
        f.write('%s:\  n' % x)
        f.write(getattr(__builtins__,x).__doc__)
        f.write('\  n\  n')

