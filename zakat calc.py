from tkinter import *
from tkinter import ttk



def extract_silver_price():#====>mohamed
    import requests
    from bs4 import BeautifulSoup
    respond = requests.get("https://www.kitco.com/charts/livesilver.html")
    src = respond.content
    soup = BeautifulSoup(src, "lxml")
    silver_price = soup.find("span", {"id": "sp-bid"}).text.strip()
    convert_to_float1 = silver_price
    convert_to_float2 = convert_to_float1.strip("$")
    convert_to_float2 = convert_to_float2.replace(",", "")
    silver_price_gram = float(convert_to_float2)/28.3495

    return silver_price_gram
#------------------------------------------------------------------------------------------------------------------------
def extract_gold_price():#======>mohamed
    import requests
    from bs4 import BeautifulSoup
    import csv

    respond = requests.get("https://pricegold.net/us-united-states/")
    src = respond.content
    soup = BeautifulSoup(src, "lxml")
    gold_price = soup.find("strong", {"class": "exMoney"}).text.strip()
    convert_to_float = gold_price
    convert_to_float1= convert_to_float.strip("$")
    convert_to_float2 = convert_to_float1.replace(",", "")
    gold_price_gram = float(convert_to_float2)/28.3495

    return gold_price_gram
#==----===================================================================================================================

def exchange_rate():#=====>rahma
    import requests
    from bs4 import BeautifulSoup
    respond = requests.get("https://www.forbes.com/advisor/money-transfer/currency-converter/usd-egp/?amount=1")
    src=respond.content
    soup = BeautifulSoup(src, "lxml")
    EGP_str = soup.find("span", {"class": "amount"}).text.strip()
    EGP=float(EGP_str)
    return EGP




# busniss zakat calculater===========================================================================================================================

def bussnis_zakat(current_liabilities,assests):#=====>mohamed

    nesab = extract_gold_price() * 85
    working_capital = (current_liabilities) - (assests)

    if working_capital >= nesab:
        zakat1 = 2.5 / 100 * working_capital
    elif working_capital <= (-1) * (nesab):
        new = working_capital / -1
        zakat1 = 2.5 / 100 * new

    else:
        zakat1=0
    return zakat1
# gold zakat calculater=======================================================================================================================
def gold_zakat(gold_value):#=====rahma elsayed
    if (gold_value*extract_gold_price()) >= extract_gold_price()*85:
        zakat_of_gold=(2.5/100)*gold_value*extract_gold_price()
    else:
        zakat_of_gold=0
    return zakat_of_gold
# silver zakat calculater========================================================================================================================
def silver_zakat(silver_value):#======omar kassem
    if(silver_value*extract_silver_price()) >= extract_gold_price()*85:
        zakat_on_silver =(2.5/100)*silver_value*extract_silver_price()
    else:
        zakat_on_silver=0
    return zakat_on_silver

# Livestock Zakat Calculator=============================================================================================

def calculate_zakat_of_livestock(num_camels,num_cows,num_sheep):#======rahma elsayed

    # Define the Nisab (minimum threshold) in grams for each type of animal
     nisab_camel = 12000
     nisab_cow = 30
     nisab_sheep = 40

    # Calculate the total value of the animals in grams of silver
     total_value = (num_camels * 750) + (num_cows * 1200) + (num_sheep * 120)

    # Check if the total value is above the Nisab for camels
     if total_value >= (nisab_camel * 3):
        zakat_camel = (total_value * 2.5) / 100

     else:
        zakat_camel = 0


    # Check if the total value is above the Nisab for cows and buffaloes
     if total_value >= (nisab_cow * 30):
        zakat_cow = (total_value * 2.5) / 100

     else:
        zakat_cow = 0


    # Check if the total value is above the Nisab for sheep and goats
     if total_value >= (nisab_sheep * 40):
        zakat_sheep = (total_value * 2.5) / 100

     else:
        zakat_sheep = 0


    # Calculate the total Zakat due
     total_zakat = zakat_camel + zakat_cow + zakat_sheep
     return total_zakat




#========================================================================================================================

def zakat_on_cash(total_cash_value):  #====> Omar Kassem
    nisab=extract_gold_price()*85



    if total_cash_value >= nisab:
        zakat_payable = (total_cash_value * 0.025)

    else:
        zakat_payable=0
    return zakat_payable

def agriculturalcaluclator(agricultural_land_area,agricultural_land_location):#=====>omar kassem
    agricultural_land_value = agricultural_land_values = {
    "Cairo": 20000,
    "Alexandria": 15000,
    "Aswan": 5000,
    "Luxor": 7000,
    "Giza": 18000,
    "Asyut": 4000,
    "Suez": 12000,
    "Ismailia": 10000,
    "Port Said": 9000,
    "Qena": 6000,
    "Damietta": 8000,
    "Beni Suef": 3000,
    "Minya": 3500,
    "Fayoum": 2000,
    "Red Sea": 10000,
    "New Valley": 4000,
    "Beheira": 5000,
    "Dakahlia": 5500,
    "Sharqia": 6000,
    "Kafr El-Sheikh": 4500,
    "Gharbia": 4000,
    "Qalyubia": 3500,
    "Menofia": 3000,
    "Sohag": 5000,
    "Monufia": 2500,
    "Matruh": 1500,
    "None":0
}
    if agricultural_land_location in agricultural_land_values:
        agricultural_land_value = agricultural_land_area * agricultural_land_values[agricultural_land_location]

    else:
        agricultural_land_value=0
    return agricultural_land_value




#+======================================================================================================================
def final():#======mohamed ayoub
    current_liabilities = float(entry1.get())
    assests = float(entry2.get())
    gold_value = float(entry3.get())
    silver_value = float(entry4.get())
    num_camels = float(entry5.get())
    num_cows = float(entry6.get())
    num_sheep = float(entry7.get())
    total_cash_value = float(entry8.get())
    agricultural_land_area = float(entry9.get())
    agricultural_land_location = entry10.get()

    zakat_in_total = (agriculturalcaluclator(agricultural_land_area,agricultural_land_location) / exchange_rate()) + zakat_on_cash(total_cash_value) + (
                calculate_zakat_of_livestock(num_camels,num_cows,num_sheep) * extract_silver_price()) + silver_zakat(silver_value) + gold_zakat(gold_value) + bussnis_zakat(current_liabilities,assests)
    final_lable.config(text=str(zakat_in_total),font=30)

    return zakat_in_total





#=======================================================================================================================

#=======>omar,rahma,mohamed
root=Tk()
root.geometry("500x700")
root.title("zakat calculater")

# current liabilites lable
lable1=ttk.Label(text="current liabilities($)==>",font=30)
lable1.place(x=20,y=20)
#current liabiltis entry field
entry1=ttk.Entry(root,width=30)
entry1.place(x=200,y=20)
#assits lable
lable2=ttk.Label(text="Assets($)========>",font=30)
lable2.place(x=20,y=80)
#assits entry field
entry2=ttk.Entry(root,width=30)
entry2.place(x=200,y=80)
#gold value lable
lable3=ttk.Label(text="Gold amount (g)======>",font=30)
lable3.place(x=20,y=140)
#gold value entry field
entry3=ttk.Entry(root,width=30)
entry3.place(x=200,y=140)
#silver value lable
lable4=ttk.Label(text="Silver amount (g)======>",font=30)
lable4.place(x=20,y=200)
#silver value entry field
entry4=ttk.Entry(root,width=30)
entry4.place(x=200,y=200)
#num of camals lable
lable5=ttk.Label(text="Num of camels===>",font=30)
lable5.place(x=20,y=260)
#num of camals entry field
entry5=ttk.Entry(root,width=30)
entry5.place(x=200,y=260)
#num of cows lable
lable6=ttk.Label(text="Num of cows====>",font=30)
lable6.place(x=20,y=320)
#num of cows entry field
entry6=ttk.Entry(root,width=30)
entry6.place(x=200,y=320)
#num of sheeps lable
lable7=ttk.Label(text="Num of sheep===>",font=30)
lable7.place(x=20,y=380)
#num of sheeps entry field
entry7=ttk.Entry(root,width=30)
entry7.place(x=200,y=380)
#total cash value lable
lable8=ttk.Label(text="Total cash value($)==>",font=30)
lable8.place(x=20,y=440)
#total cash value entry field
entry8=ttk.Entry(root,width=30)
entry8.place(x=200,y=440)
#agricultural land area lable
lable9=ttk.Label(text="Agricultural land area(m**2)=>",font=30)
lable9.place(x=20,y=500)
#agricultural land area entry field
entry9=ttk.Entry(root,width=30)
entry9.place(x=240,y=500)
#agricultural land location lable
lable10=ttk.Label(text="Agricultural land location=>",font=30)
lable10.place(x=20,y=560)
#agricultural land location entry field
entry10=ttk.Entry(root,width=30)
entry10.place(x=260,y=560)

#calculate button
button=ttk.Button(root,text="Calculate",width=15,command=final)
button.place(x=40,y=620)
#final zakat lable
end_lable=ttk.Label(root,text="Your total zakat:",font=30)
end_lable.place(x=200,y=620)

final_lable=ttk.Label(root,text="")
final_lable.place(x=350,y=620)



root.mainloop()



