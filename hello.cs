using System;

class MainApp
{
    public static void Main()
    {
        string s="Hello World using C#!";
        string ss=s + "!!!!";
        ss=ss+"hello";
        Integer i=50;
        Float f=5.00;
        Double d=5.00;
        Int32 i32=5;
        i=i+50;
        i=i-1;
        i=i+i;
        i=i*2;
        i=i/4;
        i=i%5;
        Long ii=50;
        ii=ii+50;
        ii=ii-1;
        ii=ii+ii;
        ii=ii*2;
        ii=ii/4;
        ii=ii%5;

        Console.Write(ss);
        Console.WriteLine();
        Console.Write(i);
        Console.WriteLine();
        Console.Write(ii);
        Console.WriteLine();
        Console.WriteLine(f);
        Console.WriteLine(d);
        Console.WriteLine(i32);
        Console.WriteLine(f.value);
        Console.WriteLine(d.value);
        Console.WriteLine(i32.value);

        ss=Console.ReadLine("press key? ");
        Console.WriteLine(ss);
    }
}