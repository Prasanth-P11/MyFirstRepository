package com.company;
public class Main {
    public static void main(String[] args) {
        String a="All-the-Best";
        String b="";
        boolean d;
        char[] c=a.toCharArray();
        for(int i=0;i<c.length;i++){
            if(d=Character.isUpperCase(c[i])){
                b+=(char)(((int)c[i]-65+2) % 26 + 65);
            }
            else if(d=Character.isLowerCase(c[i])){
                b+=(char)(((int)c[i]-97+2) % 26 + 97);
            }
            else{
                b+=c[i];
            }
        }
        System.out.print(b);
    }
}

