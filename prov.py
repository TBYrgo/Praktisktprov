#Author: Tobias Blom
#Date: 2023-10-13

print("Ei22 - Praktiskt prov")

resistorer = input("Ange resistorer: ")

my_list = []
my_list = resistorer.split(" ")
serie = 0
para = 0
rtot = 0

for res in my_list:
    serie += int(res)

    if res == "0":
        para + 0
    else:
        para += 1/int(res)

if para == 0:
    print("Serieresistans: 0")
    print("Parallellresistans: 0")
else:
    rtot = 1 / para
    print(f"Serieresistans: {serie}")
    print(f"Parallellresistans: {rtot}")




