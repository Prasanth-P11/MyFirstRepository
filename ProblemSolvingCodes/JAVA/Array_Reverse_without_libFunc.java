package com.company;
public class Main
{
    public static void add(int[] a)
    {
        int temp=0;
        int i=0;
        int j=a.length-1;
        while(i<j)
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
            i++;
            j--;
        }
        for(int k=0;k<a.length;k++)
        {
            System.out.print(a[k]+" ");
        }
    }
    public static void main(String[] args)
    {
        int a[] = { 1, 2, 6, 3, 4, 5 };
        add(a);
    }
}

