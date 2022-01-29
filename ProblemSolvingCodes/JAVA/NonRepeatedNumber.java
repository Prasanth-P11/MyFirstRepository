package com.company;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        int [] arr = new int [] {1, 2, 3, 4, 2, 7, 8, 8, 3};
        for (int i = 0; i < arr.length; i++) {
            int count=0;
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    count++;
                }
            }
            if(count==1){
                a.add(arr[i]);// write your code here
            }
        }
        for(int j=0;j<a.size();j++){
            System.out.print(a.get(j)+" ");
        }
	// write your code here
    }
}

