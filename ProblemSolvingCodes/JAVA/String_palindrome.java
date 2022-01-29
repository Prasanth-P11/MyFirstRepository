package com.company;

import java.util.Scanner;

public class Main {
    public static void palindrome(String a){
        String b="";
        char[] ch=a.toCharArray();
        for(int i=(ch.length)-1;i>=0;i--)
        {
            b+=ch[i];
        }
        if(a.equals(b)){
            System.out.print("IS PALINDROME");
        }
        else{
            System.out.print("IS NOT PALINDROME");
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String a= scan.nextLine();
        palindrome(a);

    }
}

