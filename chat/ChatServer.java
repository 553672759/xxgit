import java.io.IOException;
import java.net.*;
import java.io.*;
import java.util.*;

public class ChatServer {
	
	boolean started=false;
	ServerSocket ss=null;
	List<Client> clients=new ArrayList<Client>();//用于存放连接的集合
	
	Client c=null;
	public static void main(String[] args) {
		new ChatServer().start();	
	}
	
	//
	public void start(){
		try {
			 ss = new ServerSocket(8888);
			 started=true;
		}catch(BindException e){
			System.out.println("端口被占用。。。");
			System.out.println("请关掉相关程序并重新运行服务器！");
			System.exit(0);
		}catch(IOException e){
			e.printStackTrace();
		}
		
		try{
			started=true;
			while (started) {
				boolean bConnected=false;
				Socket s = ss.accept();
				 c=new Client(s);
System.out.println("a client connected");// 这是一行注释，调试用
				new Thread(c).start();
				clients.add(c);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}finally{
			try {
				ss.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
			
		}
	}
	
	//多线程连接客户端
	class Client implements Runnable{
		private Socket s;
		private DataInputStream dis=null;
		private DataOutputStream dos=null;
		
		private boolean bConnected=false;
		
		public Client(Socket s){
			try {
				dis=new DataInputStream(s.getInputStream());
				dos=new DataOutputStream(s.getOutputStream());
				bConnected=true;
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		public void send(String str){
			try {
				dos.writeUTF(str);
			} catch (IOException e) {
 				e.printStackTrace();
			}
		}
		
		public void run() {
			try{
				while(bConnected){
					String str=dis.readUTF();
System.out.println(str);
					for(int i=0;i<clients.size();i++){
						Client c=clients.get(i);
						c.send(str); 
					}
					/*for(Iterator<Client> it =clients.iterator();it.hasNext();){
						Client c=it.next();
						c.send(str);
					}*/
					/*Iterator<Client> it =clients.iterator();
					while(it.hasNext()){
						Client c=it.next();
						c.send(str);
					}*/
				}
			}catch(SocketException e){
				if(c!=null){
					clients.remove(this);
				}
				System.out.println("一个客户端断开");
			}catch(EOFException e){
				System.out.println("连接关闭！");
			}catch(IOException e){
				e.printStackTrace();
			}finally{
				try{
					if(dis!=null){
						dis.close();
						dis=null;
					}
					if(dos!=null){
						dos.close();
						dos=null;
					}
					if(s!=null){
						s.close();
						s=null;//关闭后将对象设置为空。
					}
					
				}catch(IOException e){
					e.printStackTrace();
				}
				
				
			}
		}
		
	}
}



