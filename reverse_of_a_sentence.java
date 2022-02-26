package com.company;
import java.util.Scanner;
public class Main{
    public static String add(String a){
        String[] c=a.split("\\s");
        String d="";
        for(int i=(c.length)-1;i>=0;i--){
            d=d+(c[i]+" ");
        }
        return d;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String a=sc.nextLine();
        String b=add(a);
        System.out.print(b);
    }
}

