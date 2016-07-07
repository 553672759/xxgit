package test6;

import java.util.Scanner;

public class MainUtils {
	public static void main(String[] args){
		System.out.println("ÇëÊäÈëÒ»ĞĞ×Ö·û´®");
		Scanner in= new Scanner(System.in);
		System.out.println(storage(in.nextLine()));		
	}
	public static int storage(String s){
		return s.length()*2;
	}
}
