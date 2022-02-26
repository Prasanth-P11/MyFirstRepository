package com.company;
public class Main
{
    public static void add(int a)
    {
        int c=a;
        int rev=0;
        while(a>0)
        {
            int b=a%10;
            rev=rev*10+b;
            a=a/10;
        }
        if(rev==c)
        {
            System.out.print("Palindrome");
        }
        else
        {
            System.out.print("Not Palindrome");
        }
    }

    public static void main(String[] args)
    {
        int a=121;
        add(a);
    }
}

