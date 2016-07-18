/*
 * 每次提前检查字符集
 */

public class StringCheese {

	public static void main(String[] args) {
		System.out.println(java.nio.charset.Charset.defaultCharset());
		//显示默认字符集
		byte bytes[]=new byte[256];
		for(int i=0;i<256;i++){
			bytes[i]=(byte)i;
		}
		String str=new String(bytes);
		for(int i=0,n=str.length();i<n;i++)
			System.out.println((int)str.charAt(i)+" ");
	}

}
