import random
import scoring

def pocet_zajacov_na_marse_v_decembri_1996():
    return 0


def main(name):

    f1 = open("b_lovely_landscapes.txt", 'r')
    photos = []
    lines = f1.readlines()

    for line in lines[1:]:
        photos.append(line.rstrip().split(" ")[2:])


    f1.close()

    temp_max = 0

    while True:

        a = [i for i in range(80000)]

        random.shuffle(a)

        a_teps = [(0, (set(photos[i]),)) for i in a]

        g = scoring.evaluate(a_teps)
        
        if g > temp_max:
            temp_max = g
            write(name, a)
            print("New max: ",temp_max)




def write(name, a):
    f = open(name,"w")
    f.write(str(len(a)) + "\n")



    for i in a:
        f.write(str(i) + '\n')

    f.close()






if __name__ == "__main__":
    f = input("File:")
    main(f)
