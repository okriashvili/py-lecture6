# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # 3. დააგენერირეთ 20 ელემენტიანი რიცხვების სია,
# # რომელიც შევსებული იქნება -50 დან 50-მდე შემთხვევითი რიცხვებით და შექმენით მეორე
# # სია, რომელიც პირველი სიიდან იქნება შევსებული მხოლოდ ლუწი რიცხვებით და დაბეჭდეთ ორივე სია,
# # გამოიყენეთ აუცილებლად ლისტის გენერატორი!
# numbers_lst = []
# for i in range(20):
#     import random
#     numbers_lst.append(random.randint(-50, 50))
# print(numbers_lst)
# new_numbers_list = [j for j in numbers_lst if j % 2 == 0]
# print(new_numbers_list)
# # გრძელი გზა სიების შესაქმნელად
#
#
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # 3. დააგენერირეთ 20 ელემენტიანი რიცხვების სია,
# # რომელიც შევსებული იქნება -50 დან 50-მდე შემთხვევითი რიცხვებით და შექმენით მეორე
# # სია, რომელიც პირველი სიიდან იქნება შევსებული მხოლოდ ლუწი რიცხვებით და დაბეჭდეთ ორივე სია,
# # გამოიყენეთ აუცილებლად ლისტის გენერატორი!
#
# # სიების გენერატორით შექმნილი მოკლე კოდი
# import random
# number = [random.randint(-50, 50) for i in range(20)]
# new_number = [i for i in number if i % 2 == 0]
# print(number)
# print(new_number)
#
#
#
#
# # 4th python 3rd task: anagram task!!!!!!!!!!!!!!!!!!!
# text1 = input("Enter text: ").lower()
# text2 = input("Enter text: ").lower()
# # შემოგვყსვს ოდრი სიტყვა რომელსაც შემდგომ შევადარებთ ერთმანეთს
#
# # გავუტოლეთ ორი სიტყვა ერთამენთს, რათა ვნახოთ მათი სიგრძე(სიგრძე - ასოების რაოდენობა თითოეულ სიტყვაში)
# if len(text1) != len(text2):
#     print("არაა ანაგრამა")
# # თუკი სიტყვის ასოების რაოდენეობა ერთამნეთს არ დაემთხვა, ესეიგი ისინი არ არიან ანაგრამები
#
#
# for char in text1:
# # for()ციკლს ვატარებთ text1 ზე, რათა დავშალოთ და მივიღოთ სათითაო ასოები თითოეულ იტერაციაზე
#     if char in text2:
# # ვამოწმებთ თუკი, text2 შეიცვს text1 დან მიღებული ასოებს
#         text2 = text2.replace(char, "", 1)
# # თუკი შეიცავს, მაშინ ყოველ text1 ის თითეულ ასოს, ვაკლებთ text2ს
# # სინამდვილეში არ ვაკლებთ, text2ში აღმოჩენილ ყოველ text1 ის ალფაბეტს, რომლებიც ერთმანეთს ემთხვევა ვანაცვლებთ ცარიელი სტრინგით
# # ბოლოში დაწერილი 1იანი არნიშნავს რომ ვანაცვლებთ 1ის ბიჯით -->
# # --> მაგ: თუკი text1 ის h ასო, 2ჯერ გვხვდება text2ში, ჩაანაცვლოს მხოლოდ ერთი და არა ორივე ასო
#
#         print(text2)
#     else:
# # თუკი ამოკლების შემდეგ რაიმე ასო დაგვრჩება text2 ში, ეს ავტომატურად ნიშნავს რომ სიტყვები ანაგრამ არაა
#         print("არაა ანაგრამა")
#         break
#
# else:
# #საბოლოოდ კი თუკი ასოები არ დაგვრჩება არც text1 ში და არც text2 ში, ეს ნიშნავს რო ყველა ასო დაემთხვა ერთმანეთს
# # და ისინი ანაგრამებია
#     print("ანაგრამაა")
#
#
#
# numbers = [5, -2, 3, 0, -7, 8, 8, 12, 13]
# result = 0
# # Your code should output: 5+ 3 + 8 = 16
# for num in numbers:
#     if num > 0:
#         result += num
#
# print(result)
#
#
# data = [19, 21, 12, 7, 45, 3, 22, 1]
# # Your code should print:
# # Smallest: 1
# # Largest: 45
# max = 0
# for i in data:
#     if i > max:
#         max = i
# print(f"ყველაზე მეტია{max}")
#
#
#
# items = ['a', 'b', 'a', 'c', 'b', 'd']
# # Your code should produce: ['a', 'b', 'c', 'd']
# dup = []
# for i in items:
#     if i not in dup:
#         dup.append(i)
# print(dup)
#
#
#
# # სიაში სიის ამოკლება
# nested = [1, [2, 3], 4, [5, 6], 7]
# # Your code should produce: [1, 2, 3, 4, 5, 6, 7]
# new_nested = []
# for i in nested:
#     if isinstance(i, list):
#         for j in i:
#             new_nested.append(j)
#
#
#     else:
#         new_nested.append(i)
#         # handle single item
#
#         # nested.remove(i)
# # print(nested)
# print(new_nested)
#
#
#
#
#
#
# # palindrome
# # seq1 = [1, 11, 2, 3, 2, 11, 1]    # Palindrome
# seq1 = ['a', 'b', 'c', 'c', 'b', 'b', 'a']     # Not a palindrome
# rev = seq1[::-1]
#
# if seq1 == rev:
#     print("they are palindrome")
# else:
#     print("they are not palindrome")
# # print(type(reverse_seq1))
# # for i in seq1:
# #     print(i)
# #     reverse_seq1 = rev
# #     for j in i:
# #         print(j)
# #         if i == j:
# #             print("they are palindrome")
# #             break
# #         else:
# #             print("they are not palindrome")
#





# ლექსიკონი ან (ობიექტები JSში)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print("dictionary(objects in JS)")

myDict = {
    1 : 1**2,
    "name" : "malkhaz"
}
print(myDict[1])
print(myDict["name"])


# dictioary{ლექსიკონი} : სინტაქსი:
# {} ორმაგ ფიგურულ ფრჩხილებში key და value პრინციპით
# key : value - key არის ლექსიკონში დასახელება,
# name : malkhaz - keys შეგვიძლია სახელის დასაქრმევლად გამოვიყენოთ რიცხვებიც და სტრინგბიც, ასევე booleaნიც
# სტრინგები უნდა მოვაქციოთ ფრჩხილებში " "
dict = {
    "name" : "malkhaz",
    "age" : 21,
    "lastname" : "okriashvili",
    "nationality" : "georigain"
}
# ისინი ერთმანეთისგან გამოიყოფა მძიმით,

# მათი გამოძახება კი ხდება key ის სახელის გამოძახებით,
# print(dict[1])
# ინდექსაციით ვერ გამოვიძახებთ რადგანაც არ აქვთ ინდექსაცია / ამიტომ უნდა გამოვიძახოთ keyების დახმარებით

# შეგვიძლია keyში ახალი ობიექტი ჩავსვათ და ა შ...
# ამისათვის ვქმნით ცვლადს და ცვლადში ვქმნით გასაღებს - key
# keyი კი : {} ისევ ვქმნით ახალ ლექსიკონს / ორი წერტილის შემდგომ ვხსნით {} ფიგურულ ფრჩხილებს და შიგ ვწერთ valueს
dictInDict = {
    "states" : {
        "west" : {
            "samegrelo" : "megrelebi",
            "imereti" : "imerlebi",
            "svaneti" : "svanebi",
        },
        "east" : {
            "qartli",
            "tusheti",
            "kakheti",
        }
    }
}
for i in dictInDict["states"]["west"]:
    print(dictInDict["states"]["west"][i])
# მათ გამოსაძახებლად კი ვიყენებთ ისევ keyზე წვდომის მეთოდს
print(dictInDict["states"]["west"])
# თუკი ჩაშენებული ლექსიკონები გვაქვს [key] -ს გვერდზე ვუწერთ იმ keys რომელზეც გვინდა წვდომა განვახორციელოთ
# ობიეტის სახელი და [] კვადრატულ ფრჩხილის შიგნით ვწერთ keyსახელს


# რამდენიმე ინფორმაცია keyში
familyTree = {
    "motherland" : {
        "ფირცხალავები",
        "წულაიები",
        "მეგრელები"
    },
    "fatherland" : {
        "ოქრიაშვილები",
        "ბერძნები"
        "დმანისი"
    }
}
print(familyTree["motherland"])

# შეგვიძლია listიც ჩავსვათ valueში
listInDict = {
    "car" : [
        "volvo",
        "BMW",
        "mercedes",
        "jeep"
    ],
    "motorcycles" : [
        "kawasaki",
        "hraley"
        "honda"
    ]
}
print(listInDict["car"][1])
# ლექსიკონებს არ გააჩნიათ ინდექსააცია, მაგრამ, თუკი სეიბს გამოვიყენებთ ლექსიკონში, სიებზე ინდექსაცით შევძლებთ წვდომის განხორციელებას





emptyDict = {}
for i in range(1,11):
    emptyDict[i] = i ** 2
print(emptyDict)



# მოცემულია პროდუქტების ლისტი:
products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]
total = 0
for i in products:
    for j in i:
        name = i[j]
        print(f"products names are:{j}")
        price = name["price"]
        quantity = name["quantity"]
        total += price * quantity
print(f"total is: {total}")




# დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი, მაგალითად:
fruits = {}
while True:
    fruit = input("Enter your favoriute fruit: ")
    if fruit in fruits:
        fruits[fruit] += 1
    elif fruit == "stop":
        break
    else:
        fruits[fruit] = 1
print(fruits)
   # Enter your favorite fruit: banana
   # Enter your favorite fruit: apple
   # Enter your favorite fruit: banana
   # Enter your favorite fruit: stop

# შედეგი:

{'banana': 2, 'apple': 1}







# დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი, მაგალითად:
fruits = {}
fruit_name = input("Enter your fruit name: ")

while True:
    if fruit_name == "stop":
        break
    elif fruit_name in fruits:
        fruits[fruit_name] += 1
    else:
        fruits[fruit_name] = 1
print(fruits)































