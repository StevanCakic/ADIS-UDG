import csv
with open("musical_instruments_reviews.csv", newline="") as fajl:

    reader=csv.reader(fajl)
    header=next(reader)
    data=[]

    for row in reader:
        reviewerID=row[0]
        asin=(row[1])
        reviewerName=row[2]
        helpful=row[3]
        reviewText=row[4]
        overall=float(row[5])
        summary=row[6]
        unixReviewTime=row[7]
        reviewTime=row[8]
        data.append([reviewerID,asin,reviewerName,helpful,reviewText,overall,summary,unixReviewTime,reviewTime])

    n=int(input("Unesite broj proizvoda:"))
    god=int(input("Unesite godinu:"))
    data2=[]

    # Izdvajanje prvih n recenzija nakon unesene godine cija je ocjena bar 4
    # (iako pise u postavci proizvoda, mada se i mislilo na recenzije)
    for elem in data:
        if len(data2)<=n:
            m=int(elem[8].split(",")[1])

            if int(elem[5])>=4 and m>god:
                data2.append(elem)

    fajl2=open("novi.csv", 'w')
    writer=csv.writer(fajl2)
    writer.writerow(["reviewerID","asin","reviewerName","helpful","reviewText","overall","summary","unixReviewTime","reviewTime"])

    for elem in data2:
        writer.writerow([elem[0],elem[1],elem[2],elem[3],elem[4],elem[5],elem[6],elem[7], elem[8]])

    ocjene=[]
    asin=[]
    for elem in data:
        asin.append(elem[1])

    for elem in asin:
        ocjena=0
        br = 0
        for elem2 in data:
            if elem==elem2[1]:
                br += 1
                ocjena+=int(elem2[5])
        
        ocjene.append(ocjena / br)
    lista=[]
    
    for i in range(len(asin)):
        lista.append({asin[i]:ocjene[i]})
    
    # da uklonim duplikate
    final_list = [i for n, i in enumerate(lista) if i not in lista[n + 1:]]
    
    print(final_list)