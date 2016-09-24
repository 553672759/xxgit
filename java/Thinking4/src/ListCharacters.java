
public class ListCharacters {
	
	public static void main(String[] args) {
		for(char c=0;c<128;c++){
			if(Character.isLowerCase(c))//isLowerCase()检查是否是小写字母
				System.out.println("value:"+(int)c+" character:"+c);
		}
	}

}
