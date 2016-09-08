# -*- coding: utf-8 -*-
print ("Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ!\nР’С‹Р±РµСЂРёС‚Рµ РїСѓРЅРєС‚:\n1. РџСЂРѕРґР°Р¶Р° С‚РѕРІР°СЂР°\n2. РџРѕСЃС‚Р°РІРєР° С‚РѕРІР°СЂР° \n3. Р”Р°РЅРЅС‹Рµ РїРѕ РїСЂРѕРґР°Р¶Р°Рј")
a = int(input())
if a == 1 : 
    import xlrd
    book = xlrd.open_workbook('СЃРєР»Р°Рґ.xlsx')
    print ("The number of worksheets is", book.nsheets)
    print ("Worksheet name(s):", book.sheet_names())
    sh = book.sheet_by_index(0)
    print (sh.name, sh.nrows, sh.ncols)
    print ("Cell B4 is", sh.cell_value(rowx=3, colx=1))
    for rx in range(sh.nrows):
            print (sh.row(rx))
    print("da 123")
    answer = input()
    while answer == 'Р”':    
        print("12")
        N = int(input())
        Q = int(input())
        if 0 <= Q <= sh.cell_value(rowx = N, colx = 3):
            import xlwt
            workbook = xlwt.Workbook()
            workbook.save('СЃРєР»Р°Рґ.xlsx')
            sheet = workbook.add_sheet('Р›РёСЃС‚ 1')
            sheet.write(0,0,N)
            sheet.write(0,1,Q)  
        else : 
            print("net zdachi") 
        
    
 
elif a == 2 :
    print( spasiba)
elif a == 3 :
    print(spasiba)
