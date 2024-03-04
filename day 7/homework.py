score1 = int(input("პირველი რიცხვი: "))#ვწერთ "int"ს რადგან სისტემამ არ აღიქვას ციფრო როგორც ასო/სიტყვა
score2 = int(input("მეორე რიცხვი: "))
score3 = int(input("მესამე რიცხვი: "))
score4 = int(input("მეოთხე რიცხვი: "))
score5 = int(input("მეხუთე რიცხვი: "))
#ზემოთ მოცემული თითოეული "score" აღნიშნავს მონაცემს ანუ რიცხვს.

sum = score1 + score2 + score3 + score4 + score5 #sum, იგივე ჯამი უდრის თითოეული მონაცემის ჯამს
aretmatic_average = sum / 5 #საშუალო არითმეტიკული.
print(aretmatic_average)