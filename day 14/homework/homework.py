#2) დაწერე პროგრამა, რომელიც ამოწმებს არის თუ არა შეყვანილი რიცხვი 5-სა და 15-ს შორის, მაგრამ ის არ უნდა იყოს 10-ის ტოლი.
num = int(input("enter number?:  "))
if 5 > num > 15 and num != 10:
    print("you got it")