package javamiti1;

public class jishuxing{
	public static void main(String[] args) {
		System.out.println(new jishuxing().isOdd(-5));
		
	}
	
	public static boolean isOdd(int i){//����Ǹ�������᷵�ش�����
		return i%2==1;
	}
	public static	boolean isOdd2(int i){//����˸����������⡣
		return i%2!=0;
	}
	public static boolean isOdd3(int i){//�ʺ��ٽ����ܻ�����ʹ�á�
		return (i&1)!=0;
	}
	

}
