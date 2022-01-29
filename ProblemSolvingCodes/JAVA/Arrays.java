package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        // write your code here
        Scanner scan = new Scanner(System.in);
        System.out.println("enter the value:");
        int a = scan.nextInt();
        int[] arr = new int[a];
        int sum=0;
        System.out.println("enter the value:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = scan.nextInt();

        }
        for(int i=0;i<arr.length;i++){
            sum=sum+arr[i];

        }
        System.out.println(sum);
    }
}

