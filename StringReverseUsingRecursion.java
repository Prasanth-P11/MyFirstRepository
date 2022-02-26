package com.company;

public class Main {

    public static void main(String[] args) {
        String a="prasanth";
        String b="";
        char[] ch=a.toCharArray();
        for(int i=(ch.length)-1;i>=0;i--){
            b=b+ch[i];
        }
        System.out.print(b);
	// write your code here
    }
}

