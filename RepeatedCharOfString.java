package com.company;
import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
        ArrayList<String> c=new ArrayList<>();
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
        for(int k=0;k<c.size();k++){
            System.out.print(c.get(k)+" ");
        }
        System.out.println();
        String[] l=new String[c.size()];
        for(int y=0;y<l.length;y++){
            l[y]=c.get(y);
        }
        for(int g=0;g<l.length;g++){
            str = str.replace(l[g], "");
        }
        System.out.print(str);



	// write your code here
    }
}
