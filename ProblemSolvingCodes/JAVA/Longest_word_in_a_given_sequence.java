package com.company;

import java.util.Scanner;

public class Main {
    public static String add(String a){
        String[] c=a.split("\\s");
        int d=c.length;
        int[] arr=new int[d];
        int max=0;
        int output=1;
        for(int i=0;i<c.length;i++){
            char[] ch=c[i].toCharArray();
            arr[i]=ch.length;
            if(arr[i]>max){
                max=arr[i];
                output=i;
            }
        }
        String s=c[output];
        return s;

    }
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        String a=scan.nextLine();
        String b=add(a);
        System.out.print(b);
    }
}

