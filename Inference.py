#RHSDict(RHS,String[]LHS) - Traitor, LHS[0]-
#TermDict(Term,String[] Params) getParams, setParams
#FindTerms(Query) - True or False

class ParseInference:

    RHSDict=dict()
    TermDict=dict()
    OperatorDict=dict()
    OperatorDict[0]="&&"
    OperatorDict[1]="=>"
    def AddtoKB(self,fact):
        Term=""
        Facts=fact.split("&&")
        for eachfact in Facts:
            term=eachfact.replace(" ","").split("(")[0]
            params=eachfact.replace(" ","").split("(",1)[1]
            paramsArray= params.replace(")","").split(",")
            self.TermDict[term]=paramsArray


Obj=ParseInference()
Obj.AddtoKB("ViterbiSquirrel(x) && Secret(y) && Tells(x,y,z) && Hostile(z)")
print Obj.TermDict["Tells"]



