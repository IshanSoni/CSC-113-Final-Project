''' Final Project
    Ishan Soni
    Csc 113 - Afternoon section '''

from tkinter import *
from turtle import *

' Implementation of the interface '
#---------------------------------------------------------------------

' initializes an interface and sets the size '
interface = Tk()
interface.resizable(width = False, height = False)
interface.geometry('{}x{}'.format(250, 250))

''' adds the required widgets to the interface 
    like about and instruction texts, buttons 
    and entry box '''
about_string = "About: Python program that draws a \n pie chart of the n most frequent \n letters in \"Words.txt\" file"
about = Label(interface, text =about_string)
about.grid(row=0, column=0, padx=(25), pady=(10, 10))
instruction = Label(interface, text ="Enter n below:\n(0 <= n <= max # of characters used)")
instruction.grid(row=1, column=0, padx=(25), pady=(10, 10))
entry = Entry(interface, bd = 5)
entry.grid(row=2, column=0, padx=(25), pady=(10, 10))

n = 0

''' function that is called after the submit button is pressed.
    assigns n to the value entered by user and destroys
    the interface so the script can proceed to calculation '''
def assign_n():
    global n
    n = int(entry.get())
    interface.destroy()

button = Button(interface, text ="Draw pie chart", command = assign_n)
button.grid(row=3, column=0, padx=(25), pady=(10, 10))
created_by_string = "Created by: Ishan Soni"
credit = Label(interface, text =created_by_string)
credit.grid(row=4, column=0, padx=(25), pady=(10, 10))
interface.mainloop()
#---------------------------------------------------------------------

' Calculation of probablities '
#---------------------------------------------------------------------

''' function that converts a dictionary into a 2d list with
    letter occurences sorted in descending order '''
def sort_dict_by_occurence(unsorted_dict):
    sorted_dict = sorted(unsorted_dict.items(), key = lambda t: t[1], reverse = True)
    return sorted_dict

''' reads the txt file line by line, word to word and
    adds characters as keys and value as their occurence
    in a dictionary '''
acceptable_lower_chars = "abcdefghijklmnopqrstuvwxyz" 
acceptable_upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_counts = {}

with open("Words.txt", 'r') as f:
    word_list = f.readlines()
    
for line in word_list:  # goes through every line in the file
    for c in line:      # then goes through every character in the string line
      # if the character is a lower case or upper case alphabet,
      # the character is lower cased and its value is incremented
      # in the dictionary
        if c == ' ' or c == '\n' or c == '\t': #Anything but space, newline, and tab
            continue                           #will be counted up for occurences
        if c in acceptable_lower_chars or c in acceptable_upper_chars:
            c = c.lower()
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1

''' sorts dictionary by letter occurences (high to low)
    converted into a 2d array, where 2dlist[i][0] is character
    and 2dlist[i][1] is its occurence. Example: [("a",3),("b",2),...] '''
letter_counts = sort_dict_by_occurence(letter_counts)

''' sums up the frequencies of all character occurences
    which will be used later to calculate probability of letters '''
sum_of_freq = 0
for key in letter_counts:
    sum_of_freq += key[1]

''' counts probability of top n characters with highest freqs.
    puts probability and letter in a dictionary (key = letter, value = prob)
    calculates "All other letters" freqs as well by subtracting
    n probabilites from 1 '''
n_freqs = {}
other_prob = 1
for i in range(n):
    probability = letter_counts[i][1]/sum_of_freq
    other_prob -= probability
    n_freqs[letter_counts[i][0]] = probability

' converts the dictionary into 2d list again by "sorting" it '
n_freqs = sort_dict_by_occurence(n_freqs)
#---------------------------------------------------------------------

' Construction of pie chart '
#---------------------------------------------------------------------
' radius of the pie chart circle and color choices for 26 letters '
r = 130
colors = ["peachpuff", "aquamarine", "lightgoldenrodyellow",
          "pink", "yellow", "sandybrown", "cornflowerblue", "lightgreen",
          "greenyellow", "lightcoral", "mediumpurple", "steelblue",
          "khaki", "powderblue", "lightsalmon", "lime", "hotpink",
          "burlywood", "violet", "skyblue", "tan", "palegreen",
          "silver", "coral", "beige", "palegoldenrod"]

# draws the initial circle
penup()
goto(0,-r)
pendown()
circle(r)
penup()
up()
goto(0,0)
pendown()

''' if n greater is than or equal to 1 it will draw the first segment
    and setup the drawing to make it easier for next segements to be
    drawn easily.
    else n is 0 and the pie chart is labeled "All other characters, 1" '''
if n >= 1: #segment drawing for n = 1 
    fillcolor(colors[0])
    begin_fill()
    fd(r)
    left(90)
  # calculation of arc length is divided by 2 to
  # label the segment in the center of the arc '''
    # half arc is drawn
    circle(r, n_freqs[0][1]*360/2)
    # segment labeled at that point
    if xcor() > 0:
        write(n_freqs[0][0]+", "+str(n_freqs[0][1]), align="left", font=("Arial", 11, "bold"))
    else:
        write(n_freqs[0][0]+", "+str(n_freqs[0][1]), align="right", font=("Arial", 11, "bold"))
    # second half of arc is drawn
    circle(r, n_freqs[0][1]*360/2)
    position = pos()
    goto(0,0)
    end_fill()
    if n > 1: #segment drawings for n > 1
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
    # drawing of "All other characters" segment
    if other_prob != 0:
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
        
else: #construction of pie chart if n = 0
    penup()
    fd(r)
    left(90)
    pendown()
    fillcolor('lightgrey')
    begin_fill()
    circle(r)
    write("All other letters, "+str(other_prob), align="left", font=("Arial", 11, "bold"))

#ends the drawing of final segment
end_fill()
done()
#---------------------------------------------------------------------
