package com.company;

import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        int [] arr = new int [] {1,2,2,4,3,5,6,7,6,8,8,9,9,9,5,3};
        for (int i = 0; i < arr.length; i++) {
            int count=0;
            for (int j = i+1; j < arr.length; j++) {
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

    }
}

