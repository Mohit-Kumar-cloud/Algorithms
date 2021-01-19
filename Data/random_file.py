import random
import string
import os.path
import json
def random_letter_generator(x="mohit"):
    len_r = random.choice(range(30,100))
    r="".join(random.choice(x) for i in range(len_r))
    return r
def random_num_generator():
    len_r = random.choice(range(30,100))
    r=[random.choice(range(0,100)) for i in range(len_r)]

    return r
def random_set_generator():
    len_r = random.choice(range(30,100))
    r=[(random.choice(range(0,100)),random.choice(range(0,100))) for i in range(len_r)]
    return r


def random_string_generator():
    letters=string.ascii_lowercase
    n = random.choice(range(1,26))
    dictionary=[]
    for i in range(n):
        len_r = random.choice(range(1,26))
        r=''.join(random.choice(letters) for j in range(len_r))
        dictionary.append(r)  
    return dictionary


def generate_file(string):
    for i in range(10):
        with open("Data\\"+str(string)+"\\"+str(i)+".txt","w") as f:
            x = random_letter_generator("mohit")
            y = random_letter_generator("mohit")
            f.write(x)
            f.write("\n")
            f.write(y)
    return


def get_file(string,i):
    x=[]
    y=[]
    z=[]
    if os.path.exists("Data\\"+str(string)):

        if os.path.exists("Data\\"+str(string)+"\\"+str(i)+".txt"):
            with open("Data\\"+str(string)+"\\"+str(i)+".txt","r") as f:
                for line in f:
                    line=line.strip()
                    x.append(line)     
        else:
            generate_file(string)
            return get_file(string,i)
    else:
        os.mkdir("Data\\"+str(string))
        return get_file(string)
    return x     



def generate_file_1(string):
    for i in range(10):
        with open("Data\\"+str(string)+"\\"+str(i)+".txt","w") as f:
            x = random_num_generator()
            json.dump(x,f)
    return


def get_file_1(string,i):
    if os.path.exists("Data\\"+str(string)):

        if os.path.exists("Data\\"+str(string)+"\\"+str(i)+".txt"):
                with open("Data\\"+str(string)+"\\"+str(i)+".txt","r") as f:
                    for line in f:
                        line=line.strip()
                    return line
        else:
            generate_file_1(string)
            return get_file_1(string,i)
    else:
        os.mkdir("Data\\"+str(string))
        return get_file(string)

def generate_file_2(string):
    for i in range(10):
        with open("Data\\"+str(string)+"\\"+str(i)+".txt","w") as f:
            f.write("160\n")
            x = random_set_generator()
            json.dump(x,f)
    return
def get_file_2(string,i):
    if os.path.exists("Data\\"+str(string)):
        lis=[]
        if os.path.exists("Data\\"+str(string)+"\\"+str(i)+".txt"):
            with open("Data\\"+str(string)+"\\"+str(i)+".txt","r") as f:
                for line in f:
                    line=line.strip()
                    lis.append(line)
                return lis
        else:
            generate_file_2(string)
            return get_file_2(string,i)
    else:
        os.mkdir("Data\\"+str(string))
        return get_file_2(string)



def generate_file_3(string):
    if os.path.exists("Data\\"+str(string)):
        for i in range(10):
            with open("Data\\"+str(string)+"\\"+str(i)+".txt","w") as f:
                x = random_string_generator()
                json.dump(x,f)
        return
    else:
        os.mkdir("Data\\"+str(string))
        return generate_file_3(string)


def get_file_3(string,i):
    if os.path.exists("Data\\"+str(string)):
        if os.path.exists("Data\\"+str(string)+"\\"+str(i)+".txt"):
            with open("Data\\"+str(string)+"\\"+str(i)+".txt","r") as f:
                for line in f:
                    line=line.strip()
            return line
        else:
            generate_file_3(string)
            return get_file_3(string,i)
    else:
        os.mkdir("Data\\"+str(string))
        return get_file_3(string)

if __name__ == "__main__":
  #print(random_letter_generator("mohit"))
  r=get_file_1("coin_change",0)
  z=get_file("edit_distance",0)
  y=get_file_2("rodcut",0)
  x=get_file_3("word_break",0)
  print(x)