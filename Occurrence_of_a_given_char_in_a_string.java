package com.company;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static int add(String a, char b){
        char[] ch=a.toCharArray();
        ArrayList<String> e = new ArrayList<>();
        for(int i=0;i<ch.length;i++){
            String f=String.valueOf(ch[i]);
            e.add(f);
        }
        String g=String.valueOf(b);
        int d= Collections.frequency(e,g);
        return d;
    }

    public static void main(String[] args) {
	// write your code here
        Scanner scan =new Scanner(System.in);
        String a=scan.nextLine();
        char b=scan.next().charAt(0);
        int c=add(a,b);
        System.out.print(c);
    }
}

