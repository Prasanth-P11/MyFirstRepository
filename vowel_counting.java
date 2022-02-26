package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("enter the value:");
        String b = scan.nextLine();
        char[] ch=b.toCharArray();
        String[] x={"a","e","i","o","u"};
        int a=0;
        int e=0;
        int i=0;
        int o=0;
        int u=0;
        for(int j=0;j<b.length();j++) {
            if (ch[j] == 'a') {
                a += 1;
            } else if (ch[j] == 'e') {
                e += 1;
            } else if (ch[j] == 'i') {
                i += 1;
            } else if (ch[j] == 'o') {
                o += 1;
            } else if (ch[j] == 'u') {
                u += 1;
            }
        }
        System.out.println("a:"+a);
        System.out.println("e:"+e);
        System.out.println("i:"+i);
        System.out.println("o:"+o);
        System.out.println("u:"+u);
        for(int k=0;k<x.length;k++){
            b=b.replace(x[k],"");
        }
        System.out.print(b);
    }
}

