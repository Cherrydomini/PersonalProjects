import numpy
import re
import decimal



print("Welcome to the financial garden! \nLet's get budgetting!")

inc = (float(input("Let's start with your income! how much do you get paid a month?: ")))
exp = (float(input("Nice! and how about your expenses? Those are things you pay monthly like phone bill, rent, etc.?: ")))
paydebt = input("Are you already paying your debts?")
paydebt = paydebt.lower()
if paydebt == 'yes':
    mdebt = (float(input("How much are you paying a month?")))
if paydebt == 'no':
    debt = (float(input("What is your total debt? school loan, hospital bill, etc?: ")))
    pt = (float(input("Ok let's look at the debt some more \nin how many months do you want to pay it back?: ")))
    mdebt = debt/pt
    mdebt = float("{0:.2f}".format(mdebt))
print("Ok! that puts your debt payments at", mdebt, " a month! (doesn't seem so bad anymore right? )")
inv = (float(input("Ok! you're doing great! now the fun part! You have to pay yourself. did you know that? how much money do you want to put away a month for the future you?: ")))
emg = (float(input("I bet future you will be happy about that! now how about future you that may be in a bit of trouble?: ")))
fun = (float(input("ok so you're budgeting but you still gotta have fun! life can't be all saving you know? "
                   "\n so how much do you think you can spend on fun a month? "
                   "\njust think how much you spend per week on unneccesarries and how much you want to spend, \n"
                   "then multiply that by 4!:  ")))
more = False
newpot = input("Would you like to add an extra pot?: ")
newpot = newpot.lower()
if newpot == "yes":
    more = True
if newpot == "no":
    more = False

if more == True:
    name = input("What do you want to name this new pot?")
    print("how much do you want to put into", name)
    opt = (float(input("?: ")))

#convert the inputs to percentages
print("ok thanks for that! you put in alot of numbers for me, so let me put out some numbers for you! \n this is the precentage break down of what you pay per month in each category!")
mdebt = (mdebt/inc)*100
exp = (exp/inc)*100
inv = (inv/inc)*100
emg = (emg/inc)*100
fun = (fun/inc)*100
if more == True:
    opt = (opt/inc)*100
print("income: ", inc, "%\ndebt: ", mdebt,"%\nexpenses: ", exp, "%\ninvestment: ", inv,"%\nEmergency: ", emg, "%\nFun: ", fun)
if more == True:
    print(name,": ",opt)
percentage = (mdebt+ exp+inv+emg+fun)
if more == True:
    percentage = percentage+opt
change = False
#If the budget comes out perfectly
if percentage == 100:
    print("income allocation: ", percentage,"%")
    print("Hey this is great! what you're trying to do fits perfectly inside you budget!\nstill if you fill there is need for improvement we can work on it!")
    improve = input("Do you still want to make changed?")
    improve.lower()
    if improve == "yes":
        change = True
    if improve == "no":
        change = False
    if change == True:
        print("great! ok let\'s get started!")
        mdebt = (float(input("What percent would you like to allocate to monthly debts?: ")))
        inv = (float(input("What percent would you like to allocate to investments?: ")))
        emg = (float(input("What percent would you like to allocate to emergencies?: ")))
        exp = (float(input("What percent would you like to allocate to expenses?: ")))
        fun = (float(input("What percent would you like to allocate to fun?: ")))
        if more == True:
            print("What percent would you like to allocate to", name,)
            opt = (float(input("?: ")))
    else:
        print("All right i'll be seeing you around! Keep up the good work!")
#to compute changes to the budget in case of over budgetting
if percentage > 100:
    print("income allocation: ", percentage, "%")
    print("uh oh!, looks like what you want to do doesn't fit within you budget. ")
    improve = input("What do you want to change?(i.e. debt, investment, expenses, emergencys, etc?: ")
    if improve == "yes":
        change = True
    if improve == "no":
        change = False
    if change == True:
        print("great! ok let\'s get started!")
        lack =  percentage - 100
        allot = (lack/100)* inc
        print("You have to get rid of ", lack, "% in some area, where do you think can you decrease this amount")
        reduction = input("debts, investments, expenses, emergency, fun?: ")
        if reduction == "debt":
            mdebt = mdebt*100 - allot
            print("That comes out to ", mdebt)
            mdebt = mdebt/100
        elif reduction == "investment":
            inv = inv*100 - allot
            print("That comes out to ",inv)
            inv = inv/100
        elif reduction == "expenses":
            exp = exp*100 - allot
            print("That comes out to ", exp)
            exp = exp/100
        elif reduction == "emergency":
            emg = emg*100 - allot
            print("That comes out to ", emg)
            emg = emg/100
        elif reduction == "fun":
            fun = fun*100 - allot
            print("That comes out to ", fun)
            fun = fun/100
        else:
            opt = opt*100 - allot
            print("That comes out to ", opt)
            opt = opt/100
        print("All right! here\'s the final allocation!\n income: ", inc, "\ndebt: ", mdebt,"\nexpenses: ", exp, "\ninvestment: ", inv,"\nEmergency: ", emg, "\nFun: ", fun)
    else:
        print("All right i'll be seeing you around! Just keep trying your best!")
#to compute changes to the budget in case of under budgetting
if percentage < 100:
    print("income allocation: ", percentage, "%")
    print("Great news! looks like you have some extra to allocate somewhere else! ")
    improve = input("woud you like to re-allocate this money?")
    if improve == "yes":
        change = True
    if improve == "no":
        change = False
    if change == True:
        print("great! ok let\'s get started!")
        excess =  100 - percentage
        allot = (excess/100)* inc
        print("You have to get add ", excess, "% in some area, where do you think can you increase this amount?")
        reduction = input("debts, investments, expenses, etc?: ")
        if reduction == "debt":
            mdebt = mdebt*100 + allot
            print("That comes out to ", mdebt)
            mdebt = mdebt/100
        elif reduction == "investment":
            inv = inv*100 + allot
            print("That comes out to ", inv)
            inv = inv/100
        elif reduction == "expenses":
            exp = exp*100 + allot
            print("That comes out to ", exp)
            exp = exp/100
        elif reduction == "emergency":
            emg = emg*100 + allot
            print("That comes out to ", emg)
            emg = emg/100
        elif reduction == "fun":
            fun = fun*100 + allot
            print("That comes out to ",fun)
            fun = fun/100
        else:
            opt = opt*100 + allot
            print("That comes out to ",opt)
            opt = opt/100
        print("All right! here\'s the final allocation!\n income: ", inc, "\ndebt: ", mdebt,"\nexpenses: ", exp, "\ninvestment: ", inv,"\nEmergency: ", emg, "\nFun: ", fun)
    else:
        print("All right i'll be seeing you around! Don't spend all that extra money in fun now!")
