package javamiti1;

public class JoyOfHex {
	public static void main(String[] args) {
		System.out.println(Long.toHexString(0x100000000L+0xcafebabe));
		/*
		 * �����ӣ���Ӧ����1cafebabe��
		 * �������ӡcafebabe
		 * 
		 * �����ֻ�����͵ļ��㣬����������long���Ҳ�������int
		 * �Ȱ�int����ת��Ϊһ����ֵ��ȵ�long���ͣ��ٽ�����long������ӡ�
		 */
		//����취��
		System.out.println(Long.toHexString(0x100000000L+0xcafebabeL));
	}
}
