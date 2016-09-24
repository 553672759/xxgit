interface fire{
	String fire();
	int getfiretime();
}
interface canfire{
	fire fireme();
}

class xiangmu implements fire{
	private static int firetime=10;
	public String fire(){			//实现接口时，方法名前加修饰符public	
		return "xiangmu's frietime:"+--firetime;
	}
	@Override
	public int getfiretime() {
		return firetime;
	}	
}

class baihua implements fire{
	private static int firetime=8;
	public String fire(){
		return "baihua'sfiretime:"+(--firetime);
	}
	@Override
	public int getfiretime() {
		return firetime;
	}
}
//工厂类
class xiangmuFactory implements canfire{
	public fire fireme() {
		return new xiangmu();
	}	
}
class baihuaFactory implements canfire{
	public fire fireme(){
		return new baihua();
	}
}
public class game {
	public static void letfire(canfire f){
		fire s=f.fireme();
		while(s.getfiretime()>0)
		System.out.println(s.fire());
		
	}
	public static void main(String[] args) {
		letfire(new xiangmuFactory());
		letfire(new baihuaFactory());
	}

}
