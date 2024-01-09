import pandas as Pmessi
import streamlit as stmessi
import matplotlib.pyplot as plt
stmessi.title("Qatar world cup 2022")
stmessi.write("Book for the last dance \" France vs Argentina \" ")
stmessi.sidebar.title(" Qatar 2022 ")
upload_National = stmessi.sidebar.file_uploader("Upload your National ID")
action = stmessi.sidebar.radio("what you want ", ("Home", "data", "stat", "sample", 'chart1' , 'chart2'))


def display_home(x):
    if x is not None:
        stmessi.title(" Choose Action to begin  ")
    else:
        stmessi.title(" Upload file to start   ")


def display_sample():
    stmessi.header(" Data Sample  ")
    sample_date = WC2024.head(11)
    stmessi.write(sample_date)


def display_stat():
    stmessi.header(" Stat")
    wc_stat = WC2024.describe()
    stmessi.write(wc_stat)


def display_data():
    stmessi.header(" All Data ")

    stmessi.write(WC2024)  # WC204
def display_chart1():
    stmessi.header(" Chart 1 ")

    pos_team_1 = WC2024["possession team1"]
    pos_team_2 = WC2024["possession team2"]
    goal_team_1 = WC2024["number of goals team1"]
    goal_team_2 = WC2024["number of goals team2"]

    # figure A
    fig = plt.figure("World Cup")
    plt.subplot(121)
    plt.title(" Team 1 ")
    plt.scatter(goal_team_1, pos_team_1)
    plt.xlabel(" Team 1 Goals")
    plt.ylabel(" Team 1 Posestion")
    plt.subplot(122)
    plt.title(" Team 2 ")
    plt.bar(goal_team_2, pos_team_2)
    plt.xlabel(" Team 2 Goals")
    plt.ylabel(" Team 2 Posestion")
    #plt.show()
    stmessi.pyplot(fig)

def display_chart2():
    stmessi.header(" Chart 2 ")
    years = ['2010', '2014', '2018', '2022']
    Ticket = [25, 50, 100, 200]
    Win_up_prize = [17, 18, 30, 50]
    fig = plt.figure(" WC 2022")  # we will see in next part

    plt.subplot(221)  # first number one raws second 2 columes third location
    plt.plot(years, Ticket, marker="*", linestyle="--")
    plt.plot(years, Win_up_prize, marker="+", linestyle="-")
    plt.legend(['Tickests', 'First price'])
    plt.title(" World Cup Prizes  plots")
    plt.xlabel(" Years ")
    plt.ylabel(" prices ")

    plt.subplot(222)
    plt.scatter(years, Ticket)
    plt.scatter(years, Win_up_prize)
    plt.title(" World Cup Prizes Scatter")
    plt.xlabel(" Years ")
    plt.ylabel(" prices ")

    plt.subplot(223)
    plt.bar(years, Ticket)
    plt.bar(years, Win_up_prize)
    plt.title(" World Cup Prizes bar")
    plt.xlabel(" Years ")
    plt.ylabel(" prices ")

    plt.subplot(224)
    plt.hist(years)
    plt.hist(Win_up_prize)
    plt.title(" World Cup Prizes hostogram")
    plt.xlabel(" prices ")
    plt.ylabel(" Frequancy ")
    stmessi.pyplot(fig)


if upload_National is not None:
    WC2024 = Pmessi.read_csv(upload_National)
if action == "Home":
    display_home(upload_National)
elif action == "stat":
    display_stat()
elif action == "data":
    display_data()
elif action == "sample":
    display_sample()
elif action == "chart1":
    display_chart1()
elif action == "chart2":
    display_chart2()
