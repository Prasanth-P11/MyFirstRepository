package com.company;

import java.util.ArrayList;
import java.util.Collections;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> c=new ArrayList<>();
        ArrayList<String> d=new ArrayList<>();
        ArrayList<Integer> n=new ArrayList<>();
        String str = "beautiful place is goa";
        char[] a=str.toCharArray();
        for (int i = 0; i < a.length; i++) {
            int count=0;
            for (int j = i+1; j < a.length; j++) {
                if (a[i]==a[j]) {
                    count++;
                }
            }
            if(count==1){
                String b=String.valueOf(a[i]);
                if(!b.equals(" ")){
                    c.add(b);
                }
            }
        }
        for(int k=0;k<a.length;k++){
            String g=String.valueOf(a[k]);
            d.add(g);
        }
        for(int l=0;l<c.size();l++){
            int h= Collections.frequency(d,c.get(l));
            n.add(h);
        }
        for(int m=0;m<n.size();m++){
            System.out.println("Count of "+c.get(m)+" is "+n.get(m));
        }

	// write your code here
    }
}

