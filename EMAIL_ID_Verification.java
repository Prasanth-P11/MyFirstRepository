package com.company;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
    public static void main(String[] args) {
        String a = "prasanthprasanth916@gmail.com";
        Pattern p = Pattern.compile("[a-zA-z]");
        Pattern q = Pattern.compile("[0-9]");
        Pattern r = Pattern.compile("[@.]");
        Matcher s = p.matcher(a);
        Matcher t = q.matcher(a);
        Matcher u = r.matcher(a);
        if (s.find() && t.find() && u.find()) {
            System.out.print("Valid");
        }
        else{
            System.out.print("Not valid");
        }

    }
}

