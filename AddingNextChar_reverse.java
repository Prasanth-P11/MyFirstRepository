package com.company;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        ArrayList<String> b=new ArrayList<>();
        ArrayList<String> c=new ArrayList<>();
        ArrayList<String> m=new ArrayList<>();
        ArrayList<String> u=new ArrayList<>();
        ArrayList<StringBuilder> n=new ArrayList<>();
        String a="Goa is beautiful place";
        String[] d=a.split("\\s");
        int x=0;
        int y=0;
        for(int i=0;i<d.length;i++){
            if(i%2==0){
                b.add(d[i]);
            }
            else{
                c.add(d[i]);
            }
        }
        String e=String.join(" ",b);
        String f="";
        boolean g;
        char[] h=e.toCharArray();
        for(int j=0;j<h.length;j++) {
            if (g = Character.isUpperCase(h[j])) {
                f += (char) (((int) h[j] - 65 + 1) % 26 + 65);
            } else if (g = Character.isLowerCase(h[j])) {
                f += (char) (((int) h[j] - 97 + 1) % 26 + 97);
            } else {
                f += h[j];
            }
        }
        for(int k=0;k<c.size();k++){
            String l=c.get(k).toUpperCase();
            m.add(l);
        }
        for(int o=0;o<m.size();o++){
            StringBuilder p=new StringBuilder();
            p.append(m.get(o));
            p.reverse();
            n.add(p);
        }
        String[] q=f.split("\\s");
        String z=String.join(" ",n);
        String[] r=z.split("\\s");
        int n1=q.length;
        int n2=r.length;
        while(n1>x && n2>y){
            u.add(q[x]);
            x+=1;
            u.add(r[y]);
            y+=1;
        }
        while(n1>x){
            u.add(q[x]);
            x+=1;
        }
        while(n2>y){
            u.add(r[y]);
            y+=1;
        }
        String q1=String.join(" ",u);
        System.out.print(q1);
    }
}

