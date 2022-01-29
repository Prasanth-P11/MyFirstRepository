package com.company;
import java.util.Locale;
import java.util.Scanner;
import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
        ArrayList<String> b=new ArrayList<>();
        ArrayList<StringBuilder> p=new ArrayList<>();
        System.out.println("enter the value:");
        Scanner scan=new Scanner(System.in);
        int s=scan.nextInt();
        String[] str=new String[s];
        System.out.println("enter the string:");
        for(int i=0;i<str.length;i++){
            str[i]=scan.next();
        }
        for(int j=0;j<str.length;j++){
            String d=str[j].toUpperCase();
            b.add(d);
        }
        for(int k=0;k<b.size();k++){
            StringBuilder g=new StringBuilder();
            g.append(b.get(k));
            g.reverse();
            p.add(g);
        }
        for(int l=0;l<p.size();l++){
            System.out.print(p.get(l)+" ");
        }


	// write your code here
    }
}

