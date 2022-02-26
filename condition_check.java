package com.company;
import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
        String a="1a2b3c4de5";
        ArrayList<String> c = new ArrayList<>();
        ArrayList<Integer> d= new ArrayList<>();
        for(int i=0;i<a.length();i++){
            char ch=a.charAt(i);
            if(Character.isAlphabetic(ch)){
                String s=String.valueOf(ch);
                c.add(s);
            }
            else if(Character.isDigit(ch)){
                int e=Character.getNumericValue(ch);
                d.add(e);
            }
        }
        for(int j=0;j<c.size();j++){
            System.out.print(c.get(j)+" ");
        }
        System.out.println();
        for(int k=0;k<c.size();k++){
            System.out.print(d.get(k)+" ");
        }

	// write your code here
    }
}

