package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        int b=0;
        int c=0;
        Scanner scan=new Scanner(System.in);
        System.out.println("Enter the value:");
        int a= scan.nextInt();
        int[] arr=new int[a];
        System.out.println("Enter the value:");
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        for(int i=0;i<arr.length;i++){
            if(arr[i]%2==0){
                b=b+arr[i];
            }
            else if(arr[i]%2!=0){
                c=c+arr[i];
            }
        }
        System.out.println(b);
        System.out.println(c);

	// write your code here
    }
}

