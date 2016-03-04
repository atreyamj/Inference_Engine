#RHSDict(RHS,String[][]LHS)
#TermDict(With_Sign_Term,String[] Params) getParams, setParams
#FindTerms(Query) - True or False

class ParseInference:

    RHSDict=dict()
    TermDict=dict()
    OperatorDict=dict()
    OperatorDict[0]="||"
    OperatorDict[1]="&&"
    OperatorDict[2]="=>"
    def AddtoKB(self,fact):
        Term=""
        Facts=fact.split("&&")
        for eachfact in Facts:
           # print eachfact.replace(" ","")
            print eachfact.replace(" ","").split("(",1)[0]




Obj=ParseInference()
Obj.AddtoKB("ViterbiSquirrel(x) && Secret(y)&&Tells(x,y,z)&&Hostile(z)")


