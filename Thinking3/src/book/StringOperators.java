package book;

public class StringOperators {
	public static void main(String[] args){
		int x=0,y=1,z=2;
		String s="x,y,z";
		System.out.println(s+x+y+z);//该行x+yxz被当成了与S类型一样的字符串，并没有没计算。
		System.out.println(x+" "+s);
		s+="(summed)=";
		System.out.println(s+(x+y+z));
		System.out.println(""+x);
	}

}
