
public class Classifier {
	public static void main(String[] args) {
		System.out.println(classify('n')+classify('+')+classify('2'));
		if(false){
			//里面填写必须是代码形式的注释
		}
	}
	static String classify(char ch){
		if("0123456789".indexOf(ch)>=0)
			return "NUMERAL";
		if("abcdefghijklmnopqrstuvwxyz".indexOf(ch)>=0)
			return "LETTER";
		/*(Operators not supported yet)
		 	if("+-*/    /*&|！=">=0)
		 	return "OPERATOR";
		 */
		return "UNKNOWN";
	}
	
}
