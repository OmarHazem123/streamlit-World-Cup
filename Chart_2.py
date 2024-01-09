import matplotlib.pyplot as plt


years= ['2010' , '2014' , '2018' , '2022' ]
Ticket= [ 25 , 50 , 100 , 200 ]
Win_up_prize=[17 , 18 , 30 , 50]

fig = plt.figure(" WC 2022") #we will see in next part

plt.subplot(221)  # first number one raws second 2 columes third location
plt.plot(years,Ticket , marker="*" , linestyle = "--")
plt.plot(years,Win_up_prize , marker="+" , linestyle = "-")
plt.legend([ 'Tickests' , 'First price'])
plt.title (" World Cup Prizes  plots")
plt.xlabel (" Years ")
plt.ylabel (" prices ")

plt.subplot(222)
plt.scatter( years , Ticket)
plt.scatter( years , Win_up_prize)
plt.title (" World Cup Prizes Scatter")
plt.xlabel (" Years ")
plt.ylabel (" prices ")

plt.subplot(223)
plt.bar( years , Ticket)
plt.bar( years , Win_up_prize)
plt.title (" World Cup Prizes bar")
plt.xlabel (" Years ")
plt.ylabel (" prices ")

plt.subplot(224)
plt.hist( years)
plt.hist(  Win_up_prize)
plt.title (" World Cup Prizes hostogram")
plt.xlabel (" prices ")
plt.ylabel (" Frequancy ")

plt.show()