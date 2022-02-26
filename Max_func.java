package com.company;
import java.util.Collections;
import java.util.Arrays;
public class Main {

    public static void main(String[] args) {
        int [] a= {86,94,67,34,89};
        int min=a[0];
        for(int i=0;i<a.length;i++){
            if(a[i]<min){
                min=a[i];
            }
        }
        System.out.println(min);
        int[] b={1,2,3,4,5};
        int max=0;
        for(int j=0;j<b.length;j++){
            if(b[j]>max){
                max=b[j];
            }
        }
        System.out.println(max);

    }
}

