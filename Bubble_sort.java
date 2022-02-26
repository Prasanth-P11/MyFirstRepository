package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("enter the value:");
        int a = scan.nextInt();
        int[] arr = new int[a];
        int temp=0;
        System.out.println("enter the value:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = scan.nextInt();

        }
        for (int i = 0; i < arr.length; i++){
            for (int j= i+1; j < arr.length; j++){
                if(arr[i]>arr[j]){
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }


            }
        }
        for (int k = 0; k < arr.length; k++){
            System.out.print(arr[k]+" ");
        }
	// write your code here
    }
}

