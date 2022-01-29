package com.company;
public class Main
{
    public static void add(int a)
    {
        int e=0;
        String g=String.valueOf(a);
        char[] ch=g.toCharArray();
        int b=ch.length;
        for(int i=0;i<ch.length;i++)
        {
            int d=Character.getNumericValue(ch[i]);
            double f=Math.pow(d,b);
            e+=f;
        }
        if(e==a)
        {
            System.out.print(a + ":is an Armstrong number");
        }
        else
        {
            System.out.print(a + ":is not an Armstrong number");
        }
    }

    public static void main(String[] args)
    {
        int a=153;
        add(a);
    }
}
