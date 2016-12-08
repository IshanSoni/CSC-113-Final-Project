from tkinter import *
from turtle import *

interface = Tk()

instruction = Label(interface, text ="Enter n")
instruction.pack(side = TOP)
entry = Entry(interface, bd = 5)
entry.pack(side = TOP)

n = 0
'''function that converts dictionary into a 2d list with
   letter occurences sorted in descending order '''
def sort_dict_by_occurence(unsorted_dict):
    sorted_dict = sorted(unsorted_dict.items(), key = lambda t: t[1], reverse = True)
    return sorted_dict

acceptable_lower_chars = "abcdefghijklmnopqrstuvwxyz"
acceptable_upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("Words.txt", 'r') as f:
    word_list = f.readlines()

letter_counts = {}
for line in word_list:
    for c in line:
        if c in acceptable_lower_chars or c in acceptable_upper_chars:
            c = c.lower()
            if c in letter_counts:
                letter_counts[c] += 1
            else:
                letter_counts[c] = 1

# sorts dictionary by letter occurences
letter_counts = sort_dict_by_occurence(letter_counts)

# sums up the frequencies of all character occurences
# this will be used later to calculate probability of letter
sum_of_freq = 0
for key in letter_counts:
    sum_of_freq += key[1]

def assign_n():
    global n
    n = int(entry.get())
    # counts probability of top n characters with highest freqs
    # puts probability and letter in a dictionary (key = letter, value = prob)
    # calculates "All other letters" freqs as well
    n_freqs = {}
    other_prob = 1
    for i in range(n):
        probability = letter_counts[i][1]/sum_of_freq
        other_prob -= probability
        n_freqs[letter_counts[i][0]] = probability

    # sorts the dictionary by letter probabailities 
    n_freqs = sort_dict_by_occurence(n_freqs)

    # construction of pie chart
    r = 130
    colors = ["peachpuff", "aquamarine", "lightgoldenrodyellow",
              "pink", "cyan", "yellow", "cornflowerblue", "lightgreen",
              "greenyellow", "lightcoral", "mediumpurple", "lemonchiffon",
              "khaki", "powderblue", "linen", "gold", "hotpink",
              "burlywood", "chartreuse", "skyblue", "tan", "lightcyan",
              "silver", "coral", "slateblue", "antiquewhite"]
    penup()
    goto(0,-r)
    pendown()
    circle(r)
    penup()
    up()
    goto(0,0)
    pendown()

    if n >= 1:
        fillcolor(colors[0])
        begin_fill()
        fd(r)
        left(90)
        circle(r, n_freqs[0][1]*360/2)
        if xcor() > 0:
            write(n_freqs[0][0]+", "+str(n_freqs[0][1]), align="left", font=("Arial", 11, "bold"))
        else:
            write(n_freqs[0][0]+", "+str(n_freqs[0][1]), align="right", font=("Arial", 11, "bold"))
        circle(r, n_freqs[0][1]*360/2)
        position = pos()
        goto(0,0)
        end_fill()
        if n > 1:
            for i in range(1, n):
                fillcolor(colors[i])
                begin_fill()
                goto(position)
                circle(r, n_freqs[i][1]*360/2)
                if xcor() > 0:
                    write(n_freqs[i][0]+", "+str(n_freqs[i][1]), align="left", font=("Arial", 11, "bold"))
                else:
                    write(n_freqs[i][0]+", "+str(n_freqs[i][1]), align="right", font=("Arial", 11, "bold"))
                circle(r, n_freqs[i][1]*360/2)
                position = pos()
                goto(0,0)
                end_fill()
        fillcolor('lightgrey')
        begin_fill()
        goto(position)
        circle(r, other_prob*360/2)
        if xcor() > 0:
            write("All other letters, "+str(other_prob), align="left", font=("Arial", 11, "bold"))
        else:
            write("All other letters, "+str(other_prob), align="right", font=("Arial", 11, "bold"))
        circle(r, other_prob*360/2)
        position = pos()
        goto(0,0)
        
    else:
        fillcolor('lightgrey')
        begin_fill()
        write("All other letters, "+str(other_prob), align="right", font=("Arial", 11, "bold"))
        
    end_fill()
    done()

button = Button(interface, text ="OK", command = assign_n)
button.pack(side = BOTTOM)
interface.mainloop() 


