package cn.xx;
import java.io.PrintStream;

public class Print {
	//print with a newline
	public static void print(Object obj){
		System.out.println(obj);
	}
	//print a newline by itself
	public static void print(){
		System.out.println();
	}
	//print with no line break 
	public static void printnb(Object obj){
		System.out.print(obj);
	}
	//The new java SE5 printf()(from C)
	public static PrintStream print(String format,Object...args){
		return System.out.printf(format, args);
	}
}
