package com.company;
public class Main
{
    public static int add(int a)
    {
        int e=0;
        String c=String.valueOf(a);
        char[] d=c.toCharArray();
        for(int i=0;i<d.length;i++)
        {
            int f=Character.getNumericValue(d[i]);
            e+=f;
        }
        return e;
    }

    public static void main(String[] args)
    {
        int a=153;
        int b=add(a);
        System.out.print(b);
    }
}

