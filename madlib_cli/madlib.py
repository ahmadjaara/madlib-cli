import re

def read_template(path):
    try:
        textfile = open(path)
        textcontent = textfile.read()
        textfile.close()
        return(textcontent)
    except FileNotFoundError:
        raise(FileNotFoundError)
   
def parse_template(text):
    actual_parts=tuple(re.findall(r'\{(.*?)\}',text))
    actual_stripped=re.sub(r'\{(.*?)\}', "{}", text)
    return (actual_stripped,actual_parts)
    
def merge(actual_stripped,actual_parts):
    result=actual_stripped.format(*actual_parts)
    return result
    

# textfile = open('assests/dark_and_stormy_night_template.txt')
# textcontent = textfile.read()
# textfile.close()
# print(textcontent)
read_template('assets/dark_and_stormy_night_template.txt')

print(""" 
*****Welcome to madlib*****
before we start lets me descripe the game for you in this game you will enter 
deffirent world which have a different types "noun,adjective ,name...etc"
at each time the game will ask you for a specific type of input 

when you finish your answers you will read a paragragh I promise you it will be the most 
funny paragragh you will read it in your life 
are you ready ?  ....lets start 
""")
madlib_text_content=read_template('assets/template.txt')
# print(madlib_text_content)
actual_stripped,actual_parts=parse_template(madlib_text_content)
print(actual_parts)
print(actual_stripped)
user_input=[]
for elem in actual_parts:
    user_input+=[input(f"Enter {elem}:")]

print(tuple(user_input))