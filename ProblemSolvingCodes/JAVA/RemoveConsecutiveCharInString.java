package com.company;

public class Main {

    public static void main(String[] args) {
        String a="greeks for geeks";
        String b="";
        char c=' ';
        char[] ch=a.toCharArray();
        for(int i=0;i<ch.length;i++){
            if(c!=ch[i]){
                b=b+ch[i];
                c=ch[i];
            }
        }
        System.out.print(b);

	// write your code here
    }
}

