import csv
with open("csv_list.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    writer.writerow(["Rank", "Country", "Population"]) 
    writer.writerow(["1","China","1.40 Billion"])  
    writer.writerow(["2","India","1.39 Billion"]) 
    writer.writerow(["3","USA","329 Million"])
    writer.writerow(["4","Indonesia","268 Million"])
    writer.writerow(["5","Pakistan","216 Million"])
    writer.writerow(["6","Brazil","209 Million"])
    writer.writerow(["7","Nigeria","200 Million"])
    writer.writerow(["8","Bangladesh","163 Million"])
    writer.writerow(["9","Russia","146 Million"])
    writer.writerow(["10","Mexico","126 Million"])

     

