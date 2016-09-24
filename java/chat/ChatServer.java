import java.io.IOException;
import java.net.*;
import java.io.*;
import java.util.*;

public class ChatServer {
	
	boolean started=false;
	ServerSocket ss=null;
	List<Client> clients=new ArrayList<Client>();//���ڴ�����ӵļ���
	
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
			System.out.println("�˿ڱ�ռ�á�����");
			System.out.println("��ص���س����������з�������");
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
System.out.println("a client connected");// ����һ��ע�ͣ�������
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
	
	//���߳����ӿͻ���
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
				System.out.println("һ���ͻ��˶Ͽ�");
			}catch(EOFException e){
				System.out.println("���ӹرգ�");
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
						s=null;//�رպ󽫶�������Ϊ�ա�
					}
					
				}catch(IOException e){
					e.printStackTrace();
				}
				
				
			}
		}
		
	}
}



