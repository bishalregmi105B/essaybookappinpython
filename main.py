from cProfile import label
from tkinter import *
import essay
import tkinter
from tkinter.scrolledtext import *
import functions
root = tkinter.Tk()


# getting screen width and height of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}")
root.title("Ashlya Tech EssayBook Tutorial")
root.iconbitmap("./icon.ico")

myframe = LabelFrame(root, text='Essays List Here', bd=1, font=(
    'Arial', 14), relief=GROOVE, width=400, height=700, bg='white')
myframe.pack(side=LEFT)
canvas = Canvas(myframe)
frame = Frame(canvas)
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
# root.attributes('-fullscreen',True)

text = ScrolledText(root, state='normal', height=700,
                    width=1000, pady=2, font=('Arial', 14), padx=3, undo=True)
text.pack(side=RIGHT, fill=Y, expand=1)
text.bind('<Control-v>', lambda _: 'break')
text.bind('<Control-c>', lambda _: 'break')
text.bind('<BackSpace>', lambda _: 'break')
text.focus_set()
text.insert(0.0, '''𝒲𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝑜 𝒜𝒮𝐻𝐿𝒴𝒜 𝐸𝒮𝒮𝒜𝒴𝒮 . 𝒯𝒽𝒾𝓈 𝒾𝓈 𝒶 𝐸𝓈𝓈𝒶𝓎 𝐵𝑜𝑜𝓀 .
𝐼𝐹 𝓎𝑜𝓊 𝓌𝒶𝓃𝓉 𝓉𝑜 𝓈𝑒𝑒 𝑔𝓊𝒾𝒹𝑒 𝓊𝓈𝑒 𝒷𝓊𝓉𝓉𝑜𝓃 𝒾𝓃 𝓂𝑒𝓃𝓊𝒷𝒶𝓇.
𝒯𝒽𝒾𝓈 𝓈𝑜𝒻𝓉𝓌𝒶𝓇𝑒 𝒾𝓈 𝒹𝑒𝓋𝑒𝓁𝑜𝓅𝑒𝒹 𝐵𝓎 𝐵𝒾𝓈𝒽𝒶𝓁 𝑅𝑒𝑔𝓂𝒾 . 𝐼𝒻 𝒴𝑜𝓊 𝓌𝒶𝓃𝓉 𝓂𝑜𝓇𝑒 𝓈𝑒𝑒 𝒾𝓃 𝓂𝑒𝓃𝓊𝒷𝒶𝓇 .
''')
text.configure(state='disable')

###################################Functions #################


def computerfnc():
    text.configure(state="normal")
    text.delete(0.0, END)
    text.insert(0.0, essay.computer)
    text.configure(state="disabled")

#######################Peace ######################


def peace():
    text.configure(state='normal')
    text.insert(0.0, essay.imppeace)
    text.configure(state='disable')

#######################Prayer######################


def prayer():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.impprayer)
    text.configure(state='disable')

#######################Tolerance######################


def tolerance():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.imptolerance)
    text.configure(state='disable')

#######################Globalization ######################


def globalization():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.globalization)
    text.configure(state='disable')

#######################Patriotism######################


def patriotism():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.patriotism)
    text.configure(state='disable')

#######################Travelling######################


def travelling():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.travelling)
    text.configure(state='disable')

#######################socialmedia ######################


def socialmedia():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.socialmedia)
    text.configure(state='disable')

#######################Starvation######################


def starvation():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.starvation)
    text.configure(state='disable')

#######################mobilephone######################


def mobilephone():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.mobilephone)
    text.configure(state='disable')

#######################Peace ######################


def hinduism():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.hinduism)
    text.configure(state='disable')

#######################telivision######################


def telivision():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.telivision)
    text.configure(state='disable')

#######################Rivers in Nepal######################


def riversinnepal():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.riversinnepal)
    text.configure(state='disable')

#######################Impoftechnology ######################


def impoftechnology():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.impoftechnology)
    text.configure(state='disable')

#######################timemanagement######################


def timemanagement():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.timemanagement)
    text.configure(state='disable')

#######################poverty######################


def poverty():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.poverty)
    text.configure(state='disable')

#######################pleasureofreading######################


def pleasureofreading():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.pleasureofreading)
    text.configure(state='disable')

#######################honesty######################


def honesty():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.honesty)
    text.configure(state='disable')

#######################knowledgeispower######################


def knowledgeispower():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.knowledgeispower)
    text.configure(state='disable')

#######################impofhealtheducation######################


def impofhealtheducation():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.impofhealtheducation)
    text.configure(state='disable')

#######################missuseofscience######################


def missuseofscience():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.missuseofscience)
    text.configure(state='disable')

#######################cybercrime######################


def cybercrime():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.cybercrime)
    text.configure(state='disable')

#######################corruption######################


def corruption():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.corruption)
    text.configure(state='disable')

#######################lustforwealth######################


def lustforwealth():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.lustforwealth)
    text.configure(state='disable')

#######################facetofacecommunication######################


def facetofacecommunication():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.facetofacecommunication)
    text.configure(state='disable')

#######################discipline######################


def discipline():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.lustforwealth)
    text.configure(state='disable')

#######################hobby######################


def hobby():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.hobby)
    text.configure(state='disable')

####################### myfamily######################


def myfamily():
    text.configure(state='normal')
    text.insert(0.0, essay.myfamily)
    text.configure(state='disable')

#######################femaleeducation######################


def femaleeducation():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.femaleeducation)
    text.configure(state='disable')

#######################valueoftime######################


def valueoftime():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.valueoftime)
    text.configure(state='disable')

#######################Dashain######################


def Dashain():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.Dashain)
    text.configure(state='disable')

#######################humannature######################


def humannature():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.humannature)
    text.configure(state='disable')

#######################florencenightangle######################


def florencenightangle():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.florencenightangle)
    text.configure(state='disable')

#######################worldwarI######################


def worldwarI():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.worldwarI)
    text.configure(state='disable')

#######################internet######################


def internet():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.internet)
    text.configure(state='disable')

#######################myschool######################


def myschool():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.myschool)
    text.configure(state='disable')
#######################nepal######################


def nepal():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.nepal)
    text.configure(state='disable')

#######################computer######################


def computer():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.computer)
    text.configure(state='disable')

#######################myvillage######################


def myvillage():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.myvillage)
    text.configure(state='disable')

#######################environment######################


def environment():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.environment)
    text.configure(state='disable')

#######################Impoftechnology ######################


def impoftechnology():
    text.configure(state='normal')
    text.insert(0.0, essay.impoftechnology)
    text.configure(state='disable')

#######################impeducation######################


def impeducation():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.impeducation)
    text.configure(state='disable')

#######################dowry######################


def dowry():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.dowry)
    text.configure(state='disable')

#######################superstation######################


def superstation():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.superstation)
    text.configure(state='disable')

#######################politics######################


def politics():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.politics)
    text.configure(state='disable')

#######################Socialservics######################


def Socialservics():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.Socialservics)
    text.configure(state='disable')

#######################Gautambuddha######################


def Gautambuddha():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.Gautambuddha)
    text.configure(state='disable')

#######################fashain######################


def fashain():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.fashain)
    text.configure(state='disable')

#######################tourisminnepal######################


def tourisminnepal():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.tourisminnepal)
    text.configure(state='disable')

#######################Thecow######################


def Thecow():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.Thecow)
    text.configure(state='disable')

#######################Healthiswealth######################


def Healthiswealth():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.Healthiswealth)
    text.configure(state='disable')

#######################game######################


def game():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.game)
    text.configure(state='disable')

#######################newspaper######################


def newspaper():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.newspaper)
    text.configure(state='disable')

########################Covid##################
def covidfnc():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.covid19)
    text.configure(state='disable')

#######################love######################


def love():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.love)
    text.configure(state='disable')

#######################globalwarming######################


def globalwarming():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.globalwarming)
    text.configure(state='disable')

#######################population######################


def population():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.population)
    text.configure(state='disable')

#######################democracy######################


def democracy():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.democracy)
    text.configure(state='disable')

#######################Religion######################


def Religion():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.Religion)
    text.configure(state='disable')

#######################game######################


def deforestation():
    text.configure(state='normal')
    text.delete(0.0, END)
    text.insert(0.0, essay.game)
    text.configure(state='disable')


def data():

    for i in range(1):
        Label(frame, text="Essays List", bd=0, font=('Arial', 16)).grid(row=1, column=2)
        Button(frame,text="Peace",bd=0,font=('Arial',16),command= peace).grid(row=2,column=2)
        Button(frame,text="Importance of Tolerance",bd=0,font=('Arial',16),command= tolerance).grid(row=3,column=2)
        Button(frame,text="Patriotism",bd=0,font=('Arial',16),command= patriotism).grid(row=4,column=2)
        Button(frame,text="Globalization",bd=0,font=('Arial',16),command= globalization).grid(row=4,column=2)
        Button(frame,text="Travelling",bd=0,font=('Arial',16),command= travelling).grid(row=5,column=2)
        Button(frame,text="Use And Missuse of Social media",bd=0,font=('Arial',16),command= socialmedia).grid(row=6,column=2)
        Button(frame,text="Starvation",bd=0,font=('Arial',16),command= starvation).grid(row=7,column=2)
        Button(frame,text="Mobile Phone",bd=0,font=('Arial',16),command= mobilephone).grid(row=8,column=2)
        Button(frame,text="Hinduism",bd=0,font=('Arial',16),command= hinduism).grid(row=9,column=2)
        Button(frame,text="Merits and Demerits of Television",bd=0,font=('Arial',16),command= telivision).grid(row=10,column=2)
        Button(frame,text="Rivers in Nepal",bd=0,font=('Arial',16),command= riversinnepal).grid(row=11,column=2)
        Button(frame,text="Technology",bd=0,font=('Arial',16),command= impoftechnology).grid(row=12,column=2)
        Button(frame,text="Time management",bd=0,font=('Arial',16),command= timemanagement).grid(row=13,column=2)
        Button(frame,text="Poverty",bd=0,font=('Arial',16),command= poverty).grid(row=14,column=2)
        Button(frame,text="Pleasure of reading",bd=0,font=('Arial',16),command= pleasureofreading).grid(row=15,column=2)
        Button(frame,text="Honesty",bd=0,font=('Arial',16),command= honesty).grid(row=16,column=2)
        Button(frame,text="Knowledge is power",bd=0,font=('Arial',16),command= knowledgeispower).grid(row=17,column=2)
        Button(frame,text="Health Education",bd=0,font=('Arial',16),command= impofhealtheducation).grid(row=18,column=2)
        Button(frame,text="Science",bd=0,font=('Arial',16),command= missuseofscience).grid(row=19,column=2)
        Button(frame,text="Cyber Crime",bd=0,font=('Arial',16),command= cybercrime).grid(row=20,column=2)
        Button(frame,text="Corruption",bd=0,font=('Arial',16),command= corruption).grid(row=21,column=2)
        Button(frame,text="Lust for wealth",bd=0,font=('Arial',16),command= lustforwealth).grid(row=22,column=2)
        Button(frame,text="Face to Face Communication",bd=0,font=('Arial',16),command= facetofacecommunication).grid(row=23,column=2)
        Button(frame,text="Discipline",bd=0,font=('Arial',16),command= discipline).grid(row=24,column=2)
        Button(frame,text="My Hobby",bd=0,font=('Arial',16),command= hobby).grid(row=25,column=2)
        Button(frame,text="My Family",bd=0,font=('Arial',16),command= myfamily).grid(row=26,column=2)
        Button(frame,text="Female Education",bd=0,font=('Arial',16),command= femaleeducation).grid(row=27,column=2)
        Button(frame,text="Value of Time",bd=0,font=('Arial',16),command= valueoftime).grid(row=28,column=2)
        Button(frame,text="Dashain",bd=0,font=('Arial',16),command= Dashain).grid(row=29,column=2)
        Button(frame,text="Human Nature",bd=0,font=('Arial',16),command= humannature).grid(row=30,column=2)
        Button(frame,text="My school",bd=0,font=('Arial',16),command= myschool).grid(row=31,column=2)
        Button(frame,text="Florence Nightangle",bd=0,font=('Arial',16),command= florencenightangle).grid(row=32,column=2)
        Button(frame,text="World War I",bd=0,font=('Arial',16),command= worldwarI).grid(row=33,column=2)
        Button(frame,text="Internet",bd=0,font=('Arial',16),command= internet).grid(row=34,column=2)
        Button(frame,text="My Country Nepal",bd=0,font=('Arial',16),command= nepal).grid(row=35,column=2)
        Button(frame,text="Computer",bd=0,font=('Arial',16),command= computer).grid(row=36,column=2)
        Button(frame,text="My village",bd=0,font=('Arial',16),command= myvillage).grid(row=37,column=2)
        Button(frame,text="Enironment",bd=0,font=('Arial',16),command= environment).grid(row=38,column=2)
        Button(frame,text="Importance of Education",bd=0,font=('Arial',16),command= impeducation).grid(row=39,column=2)
        Button(frame,text="Dowry System",bd=0,font=('Arial',16),command= dowry).grid(row=40,column=2)
        Button(frame,text="Superstation",bd=0,font=('Arial',16),command= superstation).grid(row=41,column=2)
        Button(frame,text="politics",bd=0,font=('Arial',16),command= politics).grid(row=42,column=2)
        Button(frame,text="Social Services",bd=0,font=('Arial',16),command= Socialservics).grid(row=43,column=2)
        Button(frame,text="Gautam Buddha",bd=0,font=('Arial',16),command= Gautambuddha).grid(row=44,column=2)
        Button(frame,text="Fashoin",bd=0,font=('Arial',16),command= fashain).grid(row=45,column=2)
        Button(frame,text="Tourism in Nepal",bd=0,font=('Arial',16),command= tourisminnepal).grid(row=46,column=2)
        Button(frame,text="The Cow",bd=0,font=('Arial',16),command= Thecow).grid(row=47,column=2)
        Button(frame,text="Health is Wealth",bd=0,font=('Arial',16),command= Healthiswealth).grid(row=50,column=2)
        Button(frame,text="Game",bd=0,font=('Arial',16),command= game).grid(row=51,column=2)
        Button(frame,text="The News-paper",bd=0,font=('Arial',16),command= newspaper).grid(row=52,column=2)
        Button(frame,text="covid19",bd=0,font=('Arial',16),command= covidfnc).grid(row=53,column=2)
        Button(frame,text="Love",bd=0,font=('Arial',16),command= love).grid(row=54,column=2)
        Button(frame,text="Global warming",bd=0,font=('Arial',16),command= globalwarming).grid(row=56,column=2)
        Button(frame,text="population",bd=0,font=('Arial',16),command= population).grid(row=61,column=2)
        Button(frame,text="Democracy",bd=0,font=('Arial',16),command= democracy).grid(row=62,column=2)
        Button(frame,text="Religion",bd=0,font=('Arial',16),command= Religion).grid(row=63,column=2)
        Button(frame,text="Deforstation",bd=0,font=('Arial',16),command= deforestation).grid(row=64,column=2)
        Button(frame,text="The Power and Importance of Prayer",bd=0,font=('Arial',16),command=prayer).grid(row=65,column=2)

        
       
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=700)
#####################################Essays#########
def test ():
    print("Btn Clicked")
##################################Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=test)
filemenu.add_command(label="Open", command=test)
filemenu.add_command(label="Save", command=test)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=test)
helpmenu.add_command(label="About...", command=test)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
#############################End Menu Bar###################
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data()
root.mainloop()