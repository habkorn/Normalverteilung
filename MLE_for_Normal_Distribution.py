
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.stats
import csv



# def normal_mu_MLE(X):
#     # Get the number of observations
#     T = len(X)
#     # Sum the observations
#     s = np.sum(X)
#     return 1.0/T * s

# def normal_sigma_MLE(X):
#     T = len(X)
#     # Get the mu MLE
#     mu = normal_mu_MLE(X)
#     # Sum the square of the differences
#     s = np.sum( np.power((X - mu), 2) )
#     # Compute sigma^2
#     sigma_squared = 1.0/T * s
#     return math.sqrt(sigma_squared)

pdffilenames=[]
csv_files = ["1.csv", "2.csv", "3.csv", "4.csv"]
for csv_file in csv_files:

    data=[]
    i=0
    header=""

    with open(csv_file) as file:

        csvreader = csv.reader(file)
        for row in csvreader:
            if i==0: 
                header=str(row[0])
                i=i+1
            else:
                data = np.append(data, row)

    print("" )
    print("=====================================" )
    print("BEGIN - " +  header)
    lwz=len(data)
    print("len(data) with zeros: " + str(lwz))
    data=data.astype(float)
    data=np.delete(data,(np.argwhere(data==0)).flatten())  # remove all zeros
    lwoz=len(data) 
    print("len(data) without zeros: " + str(lwoz))
    print("# data entries with 0: " + str(lwz-lwoz))


    mu, std = scipy.stats.norm.fit(data)
    print("mu estimate:",  str(mu))
    print("std estimate:", str(std))


    # We would like to plot our data along an x-axis ranging from 0-80 with 80 intervals
    # (increments of 1)
    x =np.arange(min(data), max(data), (max(data)- min(data))/100)
    bin_def=np.arange(min(data), max(data), (max(data)- min(data))/50)

    fig, ax1 = plt.subplots(figsize=(8, 8))
    ax2 = ax1.twinx()

    ax1.hist(data, bins=bin_def,color = "lightblue", ec="white")
    ax2.plot(x,scipy.stats.norm.pdf(x, mu, std))





    plt.axvline(mu,ymax=2*scipy.stats.norm.pdf(mu, mu, std),color="k",linestyle="dashed",linewidth="1.25")

    plt.axvline(mu-std,ymax=2*scipy.stats.norm.pdf(mu-std, mu, std),color="g",linestyle="dashed",linewidth="1.25")
    plt.axvline(mu+std,ymax=2*scipy.stats.norm.pdf(mu-std, mu, std),color="g",linestyle="dashed",linewidth="1.25")
    plt.axvline(mu-2*std,ymax=2*scipy.stats.norm.pdf(mu-2*std, mu, std),color="g",linestyle="dashed",linewidth="1.25")
    plt.axvline(mu+2*std,ymax=2*scipy.stats.norm.pdf(mu-2*std, mu, std),color="g",linestyle="dashed",linewidth="1.25")


    # plt.text(mu-0.06,0.02,'$\mu$', fontsize=12)
    # plt.text(mu-std-0.1,0.02,'-$\sigma$', fontsize=12)
    # plt.text(mu+std-0.1,0.02,'$\sigma$', fontsize=12)
    # plt.text(mu-2*std-0.14,0.02,'-2$\sigma$', fontsize=12)
    # plt.text(mu+2*std-0.14,0.02,'2$\sigma$', fontsize=12)


    # plt.xticks(ticks=np.append(np.arange(14,25,2),[mu,mu-std,mu+std,mu-2*std,mu+2*std]), labels=np.append(np.arange(14,25,2),["$\mu$","$\mu$","$\mu$","$\mu$","$\mu$"]))
    # plt.tick_params(axis='x', which='minor', bottom=False)
    plt.minorticks_on()
    ax1.minorticks_on()
    plt.xlabel('Value')
    ax1.set_ylabel('Observed Frequency')
    ax2.set_ylabel("Normal Distribution Probability Density")


    # for e in bin_def: print(e)

    plt.title(header)


    plt.ylim(bottom=0)
    plt.ylim((0,0.5))

    ax1.set_ylim((0,2500))

    # legend_pos=""

    if "max.Durchfluss" in header:
        plt.xlim((20,40)) 
    #     legend_pos="right"

    if "MD60sec" in header:
        plt.xlim((14,26)) 
    #     legend_pos="right"


    ax1.legend(['Observed Data,\n in total '+str(lwz)+' measurements'+ "\n failed: " + str(lwz-lwoz)+ " (" + str(round((lwz-lwoz)/lwz*100,1)) + "%)"+ "\n N = " + str(len(data)) + "\n Bin Count=" + str(len(bin_def))+ "\n Bin Width=" + str(round((max(bin_def)-min(bin_def))/(len(bin_def)-1),3)) ], loc='upper ' + 'left')
    ax2.legend(['Fitted Normal Distribution,\n'+'$\mu$=' + str(round(mu,3))+ "," + "\n$\sigma$=" + str(round(std,3)) , "$\mu$ (Average)","$\pm$1*$\sigma$ (68.27%), $\pm$2*$\sigma$ (95.45%)"], loc='upper ' + 'right')


    plt.grid()

  
    f = plt.gcf()  # f = figure(n) if you know the figure number
    fig.set_size_inches(11.69,8.27) #DIN A4

    plt.savefig(header + ".pdf", format="pdf")
    

    pdffilenames.append(header + ".pdf")
    # plt.show()
    


    print("END - " +  header)



