
public class CommaOperator {
	public static void main(String[] args) {
		for(int i=1,j=i+10;i<5;i++,j=i*2){//for(初始化部分;控制表达式;步进部分)
			System.out.println("i="+i+" j="+j);
		}		
	}

}
