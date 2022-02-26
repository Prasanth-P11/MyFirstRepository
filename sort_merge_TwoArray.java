package com.company;
import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> n=new ArrayList<>();
        Scanner scan = new Scanner(System.in);
        System.out.println("enter the value:");
        int a = scan.nextInt();
        int[] arr1 = new int[a];
        System.out.println("enter the value:");
        for (int i = 0; i < arr1.length; i++) {
            arr1[i] = scan.nextInt();
        }
        System.out.println("enter the value:");
        int b = scan.nextInt();
        int[] arr2 = new int[b];
        System.out.println("enter the value:");
        for (int j = 0; j < arr2.length; j++) {
            arr2[j] = scan.nextInt();
        }
        for (int k = 0; k < arr1.length; k++){
            n.add(arr1[k]);
        }
        for (int l = 0; l < arr2.length; l++){
            n.add(arr2[l]);
        }
        Collections.sort(n);
        Collections.reverse(n);
        for (int m = 0; m < n.size(); m++){
            System.out.print(n.get(m)+" ");
        }

        // write your code here
    }
}

