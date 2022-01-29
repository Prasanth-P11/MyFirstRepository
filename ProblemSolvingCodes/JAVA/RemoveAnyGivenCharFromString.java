package com.company;

import java.util.Scanner;

public class Main {
    public static String add(String a, char b){
        String d=String.valueOf(b);
        a=a.replace(d,"");
        return a;
    }

    public static void main(String[] args) {
        Scanner scan =new Scanner(System.in);
        String a=scan.nextLine();
        char b=scan.next().charAt(0);
        String c=add(a,b);
        System.out.print(c);

    }
}

