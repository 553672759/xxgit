package javamiti1;

public class fuhefuzhibiaodashi {
	public static void main(String[] args) {
		char c='c';
		System.out.println((int)c);
		
		c+=1;
		System.out.println(c);
		
		c='c';
		int i=10;
		i+=c;
		System.out.println(i);
		
		//i=10,c='c'; �����﷨���ԡ�
		
		i=10;
		c='c';
		i=i+c;
		System.out.println(i);
		
		short x=0;
		int n=123456;
		x+=n;//������ת�ͣ�
		System.out.println(x);
		x=0;
		n=123456;
		//x=x+n;//����ʧ�ܣ���Ҫ��ʾת��
		System.out.println(x+n);//д�����������������ʾ
		
		/*
		 * �����
		 * 99
		 * d
		 * 109
		 * 109
		 *-7616
		 *123456
		*/
		
		
		
		
	}

}
