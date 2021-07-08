q_1 = input("How will the promo be applied ?\n1. Auto\n2. BOH3\n3. MOEM\n4. Base Plus\n")
list_1_q_1 = ["AUT_", "BOH_", "MEM_", "BP"]
if q_1=='1':
    piece_1 = list_1_q_1[0]
    print(piece_1)
elif q_1=='2':
    piece_1 = list_1_q_1[1]
    print(piece_1)
elif q_1=='3':
    piece_1 = list_1_q_1[2]
    print(piece_1)
elif q_1=='4':
    piece_1 = list_1_q_1[3]
    print(piece_1)
else:
    print("Error, Invalid option")

q_2 = input("What type of promo is it?\n1. Coded_BTL\n2. Included_ATL\n3. Included_BTL\n")
list_2_q_2 = ["COD_B_", "INC_A_", "INC_B_"]
if q_2=='1':
    piece_2 = list_2_q_2[0]
    print(piece_2)
elif q_2=='2':
    piece_2 = list_2_q_2[1]
    print(piece_2)
elif q_2=='3':
    piece_2 = list_2_q_2[2]
    print(piece_2)
else:
    print("Error, Invalid option")

q_3 = input("What is the Sales Channel?\n1. ADSL/CABLE\n2. NBN\n3. Foxtel\n4. 5G\n5. Home Phone\n6. ADSL/CABLE Small Business\n7. NBN Small Business\n")
list_3_q_3 = ["AD_CBL_", "NBN_", "FOX_", "5G_", "H_PHONE_", "SMB_AD_CBL_", "SMB_NBN_" ]
if q_3=='1':
    piece_3 = list_3_q_3[0]
    print(piece_3)
elif q_3=='2':
    piece_3 = list_3_q_3[1]
    print(piece_3)
elif q_3=='3':
    piece_3 = list_3_q_3[2]
    print(piece_3)
elif q_3=='4':
    piece_3 = list_3_q_3[3]
    print(piece_3)
elif q_3=='5':
    piece_3 = list_3_q_3[4]
    print(piece_3)
elif q_3=='6':
    piece_3 = list_3_q_3[5]
    print(piece_3)
elif q_3=='7':
    piece_3 = list_3_q_3[6]
    print(piece_3)
else:
    print("Error, Invalid option")

q_4 = input("What is the Credit Amount ?\n1. $10\n2. $20\n. $30\n")
list_4_q_4 = ["10_", "20_", "30_"]
if q_4=='1':
    piece_4 = list_4_q_4[0]
    print(piece_4)
elif q_4=='2':
    piece_4 = list_4_q_4[1]
    print(piece_4)
elif q_4=='3':
    piece_4 = list_4_q_4[2]
    print(piece_4)
else:
    print("Error, Invalid option")
    
q_5 = input("What is the Recurring Discount Period? \n1. 3 months\n2. 6 months\n3. 9months\n4. 12 months\n")
list_5_q_5 = ["3months_", "6months_", "9months_", "12months_"]
if q_5=='1':
    piece_5 = list_5_q_5[0]
    print(piece_5)
elif q_5=='2':
    piece_5 = list_5_q_5[1]
    print(piece_5)
elif q_5=='3':
    piece_5 = list_5_q_5[2]
    print(piece_5)
elif q_5=='4':
    piece_5 = list_5_q_5[3]
    print(piece_5)
else:
    print("Error, Invalid option")

q_6 = input("What are the Plans ?\n1. Core Internet\n2. Unlimited Internet\n3. Premium Internet\n4. Foxtel packages\n5. Soft bundle Packages\n")
list_6_q_6 = ["core-plans_", "unlimited-plans_", "premium-plans_", "Foxtel_", "soft_bundle_"]
if q_6=='1':
    piece_6 = list_6_q_6[0]
    print(piece_6)
elif q_6=='2':
    piece_6 = list_6_q_6[1]
    print(piece_6)
elif q_6=='3':
    piece_6 = list_6_q_6[2]
    print(piece_6)
elif q_6=='4':
    piece_6 = list_6_q_6[3]
    print(piece_6)
elif q_6=='5':
    piece_6 = list_6_q_6[4]
    print(piece_6)
else:
    print("Error, Invalid option")

q_7 = input("Is the prmotion attached to a Product card ? \n1. Yes\n2. No")
if q_7== '1':
    piece_7 = ""
else:
    piece_7 = "PC"

promo_code = piece_1 + piece_2 + piece_3 + piece_4 + piece_5 + piece_6 + piece_7
print(promo_code)

