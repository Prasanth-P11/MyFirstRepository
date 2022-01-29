package com.company;

public class Main {

    public static void main(String[] args) {
        String s="prasanth";
        StringBuilder s1 = new StringBuilder();
        s1.append(s);
        int a=1234;
        int rev=0;
        while(a>0){
            int b=a%10;
            rev=rev*10+b;
            a=a/10;
        }
        s1.reverse();
        System.out.println(rev);
        System.out.println(s1);
	// write your code here
    }
}

