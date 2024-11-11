using System;

class MainApp
{
    static void ddebugs(int a){
        string s="";
        Console.WriteLine(a);
        s=Console.ReadLine("\nwait a key enter.");
        s=s+"";
     }

    public static void Main()
    {
        int i=0;
        for(i=0;i<10;i++)ddebugs(i);

    }
}



