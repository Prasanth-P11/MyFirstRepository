package com.company;
import java.util.ArrayList;
import java.util.Collections;
public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> c=new ArrayList<>();
        ArrayList<Integer> e=new ArrayList<>();
        int[] a={1,1,2,3,4,5,5};
        int[] b={1,5};
        for(int j=0;j<a.length;j++){
            c.add(a[j]);
        }
        for(int i=0;i<b.length;i++){
            int d=Collections.frequency(c,b[i]);
            e.add(d);
        }
        for(int k=0;k<e.size();k++){
            System.out.println("count of " + b[k] + " is " + e.get(k));
        }

    }
}

