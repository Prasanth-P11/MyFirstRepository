package com.company;
import java.util.Scanner;
import java.util.ArrayList;
public class Main{
    public static void add(String a){
        ArrayList<Integer> d=new ArrayList<>();
        int vowels=0;
        int consonant=0;
        String e=a.toLowerCase();
        char[] c=e.toCharArray();
        for(int i=0;i<c.length;i++){
            if(c[i]=='a' || c[i]== 'e' || c[i]=='i' || c[i]=='o' || c[i]=='u'){
                vowels+=1;
            }
            else{
                if(c[i]!=' '){
                    consonant+=1;
                }
            }
        }
        d.add(vowels);
        d.add(consonant);
        for(int j=0;j<d.size();j++){
            System.out.print(d.get(j)+" ");
        }
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String a=sc.nextLine();
        add(a);
    }
}
