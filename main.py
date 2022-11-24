'''
 to startup the server 
 1. make sure that u have selected an interpreter [visible on bottom right cornor]
 2. 

'''



from website import create_app # the __init__ file inside website folder is what is making this import work
# the function defined in the __init__.py file is being imported 

app = create_app()

# this means that it will run start the server only if we run this file
# not if we import this file from some other file , just basic validation
# FOR BELOW LINE 
if __name__ == '__main__': 
    app.run(debug=True)   # this will automatically reload the server if we make any changes in the file