import os
tttt="""
#include "System.hpp"

"""

yyyy="""

int main(){
    MainApp m;
    m.Main();
    frees();
    return 0;
}"""
files=input("file c# or java to convert? ")

pfiles=files
ill=files.find(".")
if ill>-1:
    pfiles=files[:ill]

f1=open(files,"r")
txts=f1.read()
f1.close()
if files.find(".cs")>-1:
    txts=txts.replace("using System;",tttt)
    txts=txts.replace("public ","public :")
    txts=txts.replace("}","};")
    list1=txts.split("\n")
    txts=""
    onon=False
    counter=0
    counter2=0
    for n in list1:
        spacess=n.strip()!=""
        txts=txts+n+"\n"
        counter+=1
    txts=txts+yyyy
    f1=open(pfiles+".c","w")
    f1.write(txts)
    f1.close()
if files.find(".java")>-1:    
    yyyy="""

int main(){
    $MainApp$ m;
    m.main();
    frees();
    return 0;
}
    """


    yyyy=yyyy.replace("$MainApp$",pfiles)
    txts=txts.replace("public static","public :static")
    txts=txts.replace("public class","class")
    txts=txts.replace("main(String[] args)","main()")
    
    txts=txts.replace("}","};")
    list1=txts.split("\n")
    txts=tttt
    onon=False
    counter=0
    counter2=0
    for n in list1:
        spacess=n.strip()!=""
        txts=txts+n+"\n"
        counter+=1
    txts=txts+yyyy
    f1=open(pfiles+".c","w")
    f1.write(txts)
    f1.close()
if files.find(".js")>-1:
    yyyy="""

int main(){
    Variantes v("");
    v=Main();
    frees();
    return 0;
}   """

    f1=open(files,"r")
    txts=f1.read()
    f1.close()
    txts=txts.replace("var ","Variantes ")
    txts=txts.replace("const ","Variantes ")
    txts=txts.replace("function ","Variantes ")
    txts=txts.replace("VAR ","Variantes ")
    txts=txts.replace("public static","public :static")
    txts=txts.replace("public class","class")
    txts=txts.replace("main(String[] args)","main()")
    
    txts=txts.replace("}","};")
    list1=txts.split("\n")
    txts=tttt
    onon=False
    counter=0
    counter2=0
    for n in list1:
        spacess=n.strip()!=""
        txts=txts+n+"\n"
        counter+=1
    txts=txts+yyyy
    f1=open(pfiles+".c","w")
    f1.write(txts)
    f1.close()
    
