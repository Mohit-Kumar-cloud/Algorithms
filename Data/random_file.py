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


def generate_lcs():
    with open("Data\lcs.txt","w") as f:
        for i in range(10):
            x = random_letter_generator("mohit")
            y = random_letter_generator("mohit")
            f.write(x)
            f.write("\n")
            f.write(y)
            if i != 9:
                f.write("\n")
    return


def get_lcs():
    if os.path.exists("Data\lcs.txt"):
        with open("Data\lcs.txt","r") as f:
            x=[]
            y=[]
            z=[]
            count=0
            for line in f:
                line=line.strip()
                if count %2 == 0:
                    x.append(line)
                else:
                    y.append(line)
        z=x+y
        return z
    else:
        generate_lcs()
        return get_lcs()    


def generate_scs():
    with open("Data\scs.txt","w") as f:
        for i in range(10):
            x = random_letter_generator("mohit")
            y = random_letter_generator("mohit")
            f.write(x)
            f.write("\n")
            f.write(y)
            if i != 9:
                f.write("\n")
    return


def get_scs():
    if os.path.exists("Data\scs.txt"):
        with open("Data\scs.txt","r") as f:
            x=[]
            y=[]
            z=[]
            count=0
            for line in f:
                line=line.strip()
                if count %2 == 0:
                    x.append(line)
                else:
                    y.append(line)
        z=x+y
        return z
    else:
        generate_scs()
        return get_scs()


def generate_edt():
    with open("Data\edit_distance.txt","w") as f:
        for i in range(10):
            x = random_letter_generator("mohit")
            y = random_letter_generator("mohit")
            f.write(x)
            f.write("\n")
            f.write(y)
            if i != 9:
                f.write("\n")
    return


def get_edt():
    if os.path.exists("Data\edit_distance.txt"):
        with open("Data\edit_distance.txt","r") as f:
            x=[]
            y=[]
            z=[]
            count=0
            for line in f:
                line=line.strip()
                if count %2 == 0:
                    x.append(line)
                else:
                    y.append(line)
        z=x+y
        return z
    else:
        generate_edt()
        return get_edt() 


def generate_lis():
    with open("Data\lis.txt","w") as f:
        for i in range(10):
            x = random_num_generator()
            json.dump(x,f)
            if i != 9:
                f.write("\n")
    return


def get_lis():
    if os.path.exists("Data\lis.txt"):
        lis=[]
        with open("Data\lis.txt","r") as f:
            for line in f:
                line=line.strip()
                lis.append(line)
            return lis
    else:
        generate_lis()
        return get_lis()


def generate_mcm():
    with open("Data\mcm.txt","w") as f:
        for i in range(10):
            x = random_num_generator()
            json.dump(x,f)
            if i != 9:
                f.write("\n")
    return


def get_mcm():
    if os.path.exists("Data\mcm.txt"):
        mcm=[]
        with open("Data\mcm.txt","r") as f:
            for line in f:
                line=line.strip()
                mcm.append(line)
            return mcm
    else:
        generate_mcm()
        return get_mcm()


def generate_knapsack():
    with open("Data\knapsack.txt","w") as f:
        for i in range(10):
            x = random_set_generator()
            json.dump(x,f)
            if i != 9:
                f.write("\n")
    return
def get_knapsack():
    if os.path.exists("Data\knapsack.txt"):
        knapsack=[]
        with open("Data\knapsack.txt","r") as f:
            for line in f:
                line=line.strip()
                knapsack.append(line)
            return knapsack
    else:
        generate_knapsack()
        return get_knapsack()

def generate_partition():
    with open("Data\partition.txt","w") as f:
        for i in range(10):
            x = random_num_generator()
            json.dump(x,f)
            if i != 9:
                f.write("\n")
    return


def get_partition():
    if os.path.exists("Data\partition.txt"):
        partion=[]
        with open("Data\partition.txt","r") as f:
            for line in f:
                line=line.strip()
                partion.append(line)
            return partion
    else:
        generate_partition()
        return get_partition()



def generate_rodcut():
    with open("Data\\rodcut.txt","w") as f:
        for i in range(10):
            x = random_set_generator()
            json.dump(x,f)
            if i != 9:
                f.write("\n")
    return
def get_rodcut():
    if os.path.exists("Data\\rodcut.txt"):
        rodcut=[]
        with open("Data\\rodcut.txt","r") as f:
            for line in f:
                line=line.strip()
                rodcut.append(line)
            return rodcut
    else:
        generate_rodcut()
        return get_rodcut()

def generate_coin_change():
    with open("Data\coin_change.txt","w") as f:
        for i in range(10):
            x = random_num_generator()
            json.dump(x,f)
            if i != 9:
                f.write("\n")
    return


def get_coin_change():
    if os.path.exists("Data\coin_change.txt"):
        coin_change=[]
        with open("Data\coin_change.txt","r") as f:
            for line in f:
                line=line.strip()
                coin_change.append(line)
            return coin_change
    else:
        generate_coin_change()
        return get_coin_change()



def generate_word_break():
    with open("Data\word_break.txt","w") as f:
        for i in range(10):
            x = random_string_generator()
            json.dump(x,f)
            if i != 9:
                f.write("\n")
    return


def get_word_break():
    if os.path.exists("Data\word_break.txt"):
        word_break=[]
        with open("Data\word_break.txt","r") as f:
            for line in f:
                line=line.strip()
                word_break.append(line)
            return word_break
    else:
        generate_word_break()
        return get_word_break()



if __name__ == "__main__":
  print(random_letter_generator("mohit"))
  r=random_string_generator()
  z=get_word_break()
  print(z)