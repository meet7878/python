stu = {'course':'python', 'fees':15000,1:{'course':'javascript','fees':10000}}

for i in stu:
    if type(stu[i]) is dict:
        for k in stu[i]:
            print(k,'=',stu[i][k])
            

    else:
      print(i,'=',stu[i])